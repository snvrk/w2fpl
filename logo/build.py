"""
Builds the W2FPL logo kit from logo/source.svg, the master artwork.

Like Creative Commons' buttons, the mark comes in a family of sizes:
  w2fpl.svg / w2fpl-{890x320,445x160,222x80}.png   the full logo
  w2fpl-88x31.{svg,png} (+ @2x)                    the classic web button
  w2fpl-80x15.{svg,png} (+ @2x)                    the compact button
  w2fpl-icon.svg / w2fpl-icon-{32..256}.png        the clock alone, square
  w2fpl-mark{,-white}.svg / .png                   the clock mark alone, black or white
  w2fpl-mark-{black,white}{,@2x}.gif               the mark animated, transparent ground
  w2fpl-{445x160,890x320,88x31}.gif                animated: the clock whirls
                                                   through twelve hours and
                                                   lands back on two o'clock

The master embeds three images (a white ground, the pixel wordmark, the clock)
and one vector path (the black band, notched around the clock). For the
animation and the compact/icon layouts, the clock's hands are separated from
its rings and redrawn as vector strokes that can rotate.

Run:  python3 logo/build.py      (needs cairosvg, pillow, numpy, scipy)
"""
import base64, io, math, re
from pathlib import Path
import numpy as np
import cairosvg
from PIL import Image
from scipy import ndimage

HERE = Path(__file__).resolve().parent
OUT = HERE
SRC = (HERE / "source.svg").read_text()

imgs = {m.group(1): m.group(2) for m in re.finditer(r'id="(img\d)" href="data:image/png;base64,([^"]+)"', SRC)}
WORD = imgs["img2"]                       # 566 x 163, placed at (310, 75)
CLOCK_FULL = imgs["img3"]                 # 355 x 257, placed at (-70, 31)
BAND = re.search(r'<path class="s0" d="([^"]+)"', SRC).group(1)

# ---- split the clock into rings and hands -------------------------------------------
clk = Image.open(io.BytesIO(base64.b64decode(CLOCK_FULL))).convert("RGBA")
alpha = np.array(clk)[:, :, 3]
lab, n = ndimage.label(alpha > 40)
sizes = ndimage.sum(np.ones_like(alpha), lab, range(1, n + 1))
hands_id = int(np.argsort(sizes)[0]) + 1
grow = ndimage.binary_dilation(lab == hands_id, iterations=3)
rings = np.array(clk)
rings[grow, 3] = 0
buf = io.BytesIO(); Image.fromarray(rings).save(buf, "PNG")
CLOCK_RINGS = base64.b64encode(buf.getvalue()).decode()
# the face (inside the rings) filled white, for the icon on any background
ring_mask = alpha > 128
filled = ndimage.binary_fill_holes(ndimage.binary_closing(ring_mask, iterations=2))
face = np.zeros((*alpha.shape, 4), np.uint8); face[filled & ~ring_mask] = (255, 255, 255, 255)
buf = io.BytesIO(); Image.fromarray(face).save(buf, "PNG")
FACE = base64.b64encode(buf.getvalue()).decode()

# hand geometry, measured from the master (clock-image pixels)
PIVOT = (177.0, 145.0)
HUB_R = 29.0
MIN_LEN, MIN_W = 57.0, 42.0
HOUR_LEN, HOUR_W = 58.0, 37.0

def hands_svg(minutes_after_twelve=120.0, ox=0.0, oy=0.0):
    """Vector hands at a time given in minutes after 12:00; the logo shows 2:00."""
    m_ang = (minutes_after_twelve % 60) / 60 * 360
    h_ang = (minutes_after_twelve % 720) / 720 * 360
    px, py = PIVOT[0] + ox, PIVOT[1] + oy
    def tip(a, L):
        r = math.radians(a)
        return px + L * math.sin(r), py - L * math.cos(r)
    mx, my = tip(m_ang, MIN_LEN); hx, hy = tip(h_ang, HOUR_LEN)
    return (f'<g stroke="#000" stroke-linecap="round">'
            f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{mx:.2f}" y2="{my:.2f}" stroke-width="{MIN_W}"/>'
            f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{hx:.2f}" y2="{hy:.2f}" stroke-width="{HOUR_W}"/></g>'
            f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{HUB_R}" fill="#000"/>')

def img(data, x, y, w, h):
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{data}"/>'

def full_logo(t=None):
    """The master layout (890 x 320). t = None keeps the original raster hands."""
    clock = img(CLOCK_FULL, -70, 31, 355, 257) if t is None else img(CLOCK_RINGS, -70, 31, 355, 257) + hands_svg(t, -70, 31)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 890 320" width="890" height="320">'
            f'<rect width="890" height="320" fill="#fff"/><path d="{BAND}" fill="#000"/>'
            f'{img(WORD, 310, 75, 566, 163)}{clock}</svg>')

def button(w, h, t=None):
    """A web button in the master's own layout: the clock cropped at the left edge, the band
    notched around it, the wordmark on the band. 88x31 is the master itself, trimmed; wider
    buttons (80x15) stretch the band to the full height and centre a larger wordmark."""
    clock = img(CLOCK_FULL, -70, 31, 355, 257) if t is None else img(CLOCK_RINGS, -70, 31, 355, 257) + hands_svg(t, -70, 31)
    if w / h < 4:
        y0, Ht = 3.25, 313.5
        W = Ht * w / h
        x0 = (890 - W) / 2
        body = f'<path d="{BAND}" fill="#000"/>{img(WORD, 310, 75, 566, 163)}'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.2f} {y0} {W:.2f} {Ht}" width="{w}" height="{h}">'
                f'<rect x="{x0:.2f}" y="{y0}" width="{W:.2f}" height="{Ht}" fill="#fff"/>{body}{clock}</svg>')
    y0, Ht = 31.0, 257.0
    W = Ht * w / h
    cx, cy, r_gap = 156.5, 159.5, 145.7          # the clock's right ring centre; the band's notch
    word_h = 0.80 * Ht
    word_w = word_h * 566 / 163
    left = cx + r_gap
    word_x = left + (W - left - word_w) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {y0} {W:.2f} {Ht}" width="{w}" height="{h}">'
            f'<rect x="0" y="{y0}" width="{W:.2f}" height="{Ht}" fill="#fff"/>'
            f'<rect x="{cx}" y="{y0}" width="{W - cx:.2f}" height="{Ht}" fill="#000"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r_gap}" fill="#fff"/>'
            f'{img(WORD, round(word_x, 2), round(y0 + (Ht - word_h) / 2, 2), round(word_w, 2), round(word_h, 2))}{clock}</svg>')

def icon():
    S = 355.0
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 {-(S - 257) / 2 - 10:.1f} {S + 20} {S + 20}" width="256" height="256">'
            f'{img(FACE, 0, 0, 355, 257)}{img(CLOCK_FULL, 0, 0, 355, 257)}</svg>')

def png(svg, w, h, path):
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(path), output_width=w, output_height=h)

def write(name, text):
    (OUT / name).write_text(text)

# ---- static kit ----------------------------------------------------------------------
# The master's white ground is 887 px on an 890 px canvas; the rebuild fills it to the edge.
write("w2fpl.svg", full_logo())
for w, h in [(890, 320), (445, 160), (222, 80)]:
    png(full_logo(), w, h, OUT / f"w2fpl-{w}x{h}.png")
for w, h in [(88, 31), (80, 15)]:
    s = button(w, h)
    write(f"w2fpl-{w}x{h}.svg", s)
    png(s, w, h, OUT / f"w2fpl-{w}x{h}.png")
    png(s, 2 * w, 2 * h, OUT / f"w2fpl-{w}x{h}@2x.png")
write("w2fpl-icon.svg", icon())
for s in (32, 64, 128, 256):
    png(icon(), s, s, OUT / f"w2fpl-icon-{s}.png")

# ---- animation: hold at 2:00, whirl through twelve hours, land on 2:00 -----------------
def ease(u):
    return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2

def gif(make_svg, w, h, path, frames=44, hold_ms=1600, step_ms=34):
    seq, dur = [], []
    for i in range(frames):
        t = 120 + 720 * ease(i / frames)
        buf = io.BytesIO()
        cairosvg.svg2png(bytestring=make_svg(t).encode(), write_to=buf, output_width=w, output_height=h)
        seq.append(Image.open(buf).convert("RGB"))
        dur.append(hold_ms if i == 0 else step_ms)
    pal = seq[0].quantize(colors=32, method=Image.Quantize.MEDIANCUT)
    frames_p = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in seq]
    frames_p[0].save(path, save_all=True, append_images=frames_p[1:], duration=dur, loop=0, optimize=True, disposal=1)

gif(full_logo, 445, 160, OUT / "w2fpl-445x160.gif")
gif(full_logo, 890, 320, OUT / "w2fpl-890x320.gif")
gif(lambda t: button(88, 31, t), 88, 31, OUT / "w2fpl-88x31.gif")
# ---- the mark alone (logo/mark-source.svg): the double ring and a vector clock ----------
MARK = (HERE / "mark-source.svg").read_text()
RING = re.search(r'<path fill="#000" d="([^"]+)"', MARK).group(1)
MP, MHUB, MW = (147.47, 122.00), 22, 32
MMIN, MHOUR = 47.0, math.hypot(187.31 - 147.47, 99.00 - 122.00)

def mark(t=120.0, colour="#000"):
    m_ang = (t % 60) / 60 * 360; h_ang = (t % 720) / 720 * 360
    def tip(a, L):
        r = math.radians(a); return MP[0] + L * math.sin(r), MP[1] - L * math.cos(r)
    (mx, my), (hx, hy) = tip(m_ang, MMIN), tip(h_ang, MHOUR)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 297 215" width="297" height="215" role="img" aria-label="W2FPL">'
            f'<path fill="{colour}" d="{RING}"/>'
            f'<g stroke="{colour}" stroke-width="{MW}" stroke-linecap="round" fill="none">'
            f'<line x1="{MP[0]}" y1="{MP[1]}" x2="{hx:.2f}" y2="{hy:.2f}"/><line x1="{MP[0]}" y1="{MP[1]}" x2="{mx:.2f}" y2="{my:.2f}"/></g>'
            f'<circle cx="{MP[0]}" cy="{MP[1]}" r="{MHUB}" fill="{colour}"/></svg>')

def gif_transparent(make_svg, w, h, path, colour, matte, frames=44, hold_ms=1600, step_ms=34):
    """A one-colour mark on a transparent ground. GIF transparency is all-or-nothing, so edge
    pixels are blended against the background the mark is meant for (`matte`)."""
    rgb = tuple(int(colour[i:i + 2], 16) for i in (1, 3, 5)); mrgb = tuple(int(matte[i:i + 2], 16) for i in (1, 3, 5))
    out, dur = [], []
    for i in range(frames):
        t = 120 + 720 * ease(i / frames)
        buf = io.BytesIO()
        cairosvg.svg2png(bytestring=make_svg(t).encode(), write_to=buf, output_width=w, output_height=h)
        a = np.array(Image.open(buf).convert("RGBA"))[:, :, 3].astype(float) / 255
        levels = np.clip(np.round(a * 15), 0, 15).astype(np.uint8)          # 0 = transparent, 1..15 = coverage
        pal = [mrgb]                                                         # index 0 is the transparent colour
        for k in range(1, 16):
            f = k / 15; pal.append(tuple(round(rgb[c] * f + mrgb[c] * (1 - f)) for c in range(3)))
        im = Image.fromarray(levels, "P"); im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
        out.append(im); dur.append(hold_ms if i == 0 else step_ms)
    out[0].save(path, save_all=True, append_images=out[1:], duration=dur, loop=0, transparency=0, disposal=2, optimize=False)

write("w2fpl-mark.svg", mark())
write("w2fpl-mark-white.svg", mark(colour="#fff"))
png(mark(), 594, 430, OUT / "w2fpl-mark.png")
png(mark(colour="#fff"), 594, 430, OUT / "w2fpl-mark-white.png")
for name, colour, matte in (("black", "#000000", "#ffffff"), ("white", "#ffffff", "#000000")):
    gif_transparent(lambda t, c=colour: mark(t, c), 297, 215, OUT / f"w2fpl-mark-{name}.gif", colour, matte)
    gif_transparent(lambda t, c=colour: mark(t, c), 594, 430, OUT / f"w2fpl-mark-{name}@2x.gif", colour, matte)
print("built", len(list(OUT.glob("w2fpl*"))), "files in", OUT)
