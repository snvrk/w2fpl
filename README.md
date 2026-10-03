<p align="center">
  <img src="logo/w2fpl-445x160.gif" width="445" alt="W2FPL">
</p>

<h1 align="center">W2FPL</h1>
<p align="center"><b>DO WHAT THE FUCK YOU WANT TO, WHEN YOU WANT TO PUBLIC LICENSE</b><br>Version 1, October 2026</p>

A public license for anything: software, data, writing, music, images. It keeps the
[WTFPL](http://www.wtfpl.net/)'s whole idea, total freedom in one line, and adds what
the WTFPL leaves unsaid:

- **Clause 1** states the grant as free, worldwide, permanent and irrevocable, in the
  terms CC0's fallback license uses.
- **Clause 4** is a no-warranty, no-liability disclaimer, which the WTFPL lacks.
- **Clauses 2 and 3** are jokes, and clause 3 cancels clause 2, so nothing past
  clause 1 is a condition.

No attribution, no notice, no share-alike. The full text is in [`LICENSE`](LICENSE).
What it is and why: **https://snvrkotics.com/w2fpl**. Permanent text:
https://snvrkotics.com/licenses/w2fpl ([plain text](https://snvrkotics.com/licenses/w2fpl.txt)).

## Use it

1. Save [`LICENSE`](LICENSE), unchanged, in your project. Its copyright line is the
   license's own; put yours in a notice of your own:

   ```
   Copyright (C) 2026 Your Name. Released under the W2FPL, version 1:
   https://snvrkotics.com/licenses/w2fpl
   ```

2. Until it has an SPDX identifier, tag files with:

   ```
   SPDX-License-Identifier: LicenseRef-W2FPL-1.0
   ```

3. Badge, if you like. It comes in several sizes, like Creative Commons' buttons; all of them, with their embed codes, are in [`logo/`](logo/):

   ```html
   <a href="https://snvrkotics.com/licenses/w2fpl" rel="license"><img src="https://snvrkotics.com/brand/licenses/w2fpl/w2fpl-88x31.png" srcset="https://snvrkotics.com/brand/licenses/w2fpl/w2fpl-88x31@2x.png 2x" alt="W2FPL" width="88" height="31"></a>
   ```

### One line

```sh
curl -o LICENSE https://snvrkotics.com/licenses/w2fpl.txt
```

### Package managers

Until SPDX lists it, use the `LicenseRef-` form, which every SPDX-aware tool accepts:

| Ecosystem | Field |
| --- | --- |
| npm (`package.json`) | `"license": "LicenseRef-W2FPL-1.0"` |
| Python (`pyproject.toml`) | `license = { file = "LICENSE" }` |
| Rust (`Cargo.toml`) | `license-file = "LICENSE"` |
| Hugging Face (dataset card) | `license: other`, `license_name: w2fpl-1.0`, `license_link: https://snvrkotics.com/licenses/w2fpl` |

## Propose a fucking idea

The W2FPL is written in public. **Anyone can propose what goes into the next version,
and if your proposal lands, you're a coauthor**: named in [`AUTHORS.md`](AUTHORS.md)
and on https://snvrkotics.com/w2fpl, and covered by the license's own credit line,
"and the W2FPL coauthors". See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Paper

Gottfried, C. (2026). *Do What You Want, Permanently: The W2FPL, a WTFPL Derivative
with an Explicit Irrevocable Grant and a Warranty Disclaimer.* Zenodo.
https://doi.org/10.5281/zenodo.23121447

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23121447.svg)](https://doi.org/10.5281/zenodo.23121447)

The clause-by-clause analysis, a comparison with six other licenses, and the
limitations. Source in [`paper/`](paper/).

## Versions

| Version | Date | Text |
| --- | --- | --- |
| 1 | October 2026 | [`versions/1.0.txt`](versions/1.0.txt) |

A published version never changes. Accepted proposals go into the next one.

## Status

Not yet on the SPDX License List; not reviewed by the FSF or OSI. Based on the
WTFPL, version 2 (SPDX: `WTFPL`), renamed as its terms require.

This README explains the license; it isn't legal advice.
