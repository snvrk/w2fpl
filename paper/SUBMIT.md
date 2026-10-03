# Submitting the paper

**Published on Zenodo:** https://doi.org/10.5281/zenodo.23121447

File: `w2fpl-paper.pdf` (8 pages). Source: `w2fpl-paper.html`. Rebuild with:

```sh
chromium --headless --no-pdf-header-footer --print-to-pdf=w2fpl-paper.pdf w2fpl-paper.html
```

Before submitting: read it through, check that every URL in the references loads
(snvrkotics.com pages need the site deployed), and add your ORCID if you have one
(orcid.org, free).

## Zenodo (zenodo.org → New upload)

| Field | Value |
| --- | --- |
| Resource type | Publication → Preprint |
| Title | Do What You Want, Permanently: The W2FPL, a WTFPL Derivative with an Explicit Irrevocable Grant and a Warranty Disclaimer |
| Creator | Gottfried, Caleb · Affiliation: SNVRKOTICS LLC · ORCID if you have one |
| Description | The abstract (below) |
| Version | 1.0 |
| Language | English |
| Keywords | open source licensing; permissive licenses; WTFPL; public domain dedication; CC0; warranty disclaimer; open data; SPDX; license proliferation |
| License | Custom: title `W2FPL-1.0`, link `https://snvrkotics.com/licenses/w2fpl` (if the form only offers a list, pick the closest open option and say "Released under the W2FPL, version 1" in the description) |
| Related works | "Is supplemented by" → `https://github.com/snvrk/w2fpl` (URL); "References" → `https://github.com/spdx/license-list-XML/issues/3091` (URL) |
| Publication date | The day you upload |

Zenodo issues a DOI on publish. Put that DOI in the repo README and on
snvrkotics.com/w2fpl, and post it on the SPDX issue as another reference.

Alternatively, connect the GitHub repo in Zenodo's GitHub settings: every GitHub
release of snvrk/w2fpl is then archived with its own DOI automatically.

## SSRN (ssrn.com → Submit a paper)

| Field | Value |
| --- | --- |
| Title | Do What You Want, Permanently: The W2FPL, a WTFPL Derivative with an Explicit Irrevocable Grant and a Warranty Disclaimer |
| Author | Caleb Gottfried, SNVRKOTICS LLC, snvrk@snvrkotics.com |
| Abstract | The abstract (below) |
| Keywords | open source licensing, permissive licenses, WTFPL, CC0, public domain dedication, warranty disclaimer, open data, SPDX |
| JEL codes | K11 (Property Law), O34 (Intellectual Property and Intellectual Capital), L17 (Open Source Products and Markets), L86 (Information and Internet Services; Computer Software) |
| Paper type | Working paper |
| Classification | Choose from the eJournals SSRN offers under its Legal Scholarship Network, in the intellectual property, copyright and technology law areas |

SSRN screens submissions before posting, which can take a few days. If you
publish on Zenodo first, add the DOI to the SSRN record.

## Abstract (both)

The WTFPL ("Do What The Fuck You Want To Public License") is among the shortest
free licenses in use: a single operative sentence granting unlimited permission.
The Free Software Foundation lists it as free and GPL-compatible, and it carries
an SPDX identifier. Two practical gaps limit its use. It never states the scope,
duration or revocability of the permission it grants, and it contains no
disclaimer of warranty or liability, an omission that some institutions cite
when restricting contributions to projects under it. This paper presents the
W2FPL ("Do What The Fuck You Want To, When You Want To Public License"), version
1, a renamed derivative of the WTFPL, version 2, that closes both gaps while
keeping the original's one-sentence grant and its voice. Clause 1 states the
grant as free, worldwide, permanent and irrevocable, the same terms used by the
fallback license of CC0 1.0. Clause 4 disclaims warranty and liability. Two
humorous clauses are drafted so that neither binds the licensee: the second
cancels the first, a structure chosen to avoid the interpretive problem created
by the JSON License's "Good, not Evil" clause. The paper analyzes each clause,
compares the license with six permissive alternatives, describes its governance
(frozen versions, public development and a coauthorship model), reports its
first deployment as the data license of two public datasets, and sets out its
limitations. The license has not yet been reviewed by the FSF, the OSI or SPDX;
a request for SPDX listing is pending.
