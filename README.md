# OpenAI Math rewrites

An independent rewrite of twelve manuscripts from families 038, 039, 058, 087, 091, and 166 in the [OpenAI Math catalogue](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/CONTENTS.md). The rewrites use Mingchen’s LaTeX template and leave the manuscript author fields blank. Each manuscript folder has a provenance note linking to its original source.

| Family | Manuscript | Files |
| --- | --- | --- |
| 038 | Fujita’s freeness conjecture | [PDF (19 pp.)](papers/038/fujita-freeness/038-Fujita-freeness.pdf) · [LaTeX](papers/038/fujita-freeness/main.tex) |
| 039 | Nagata’s conjecture for plane curves | [PDF (18 pp.)](papers/039/nagata-plane-curves/039-Nagata-plane-curves.pdf) · [LaTeX](papers/039/nagata-plane-curves/main.tex) |
| 039 | Maximal Seshadri constants on arbitrary polarized surfaces | [PDF (14 pp.)](papers/039/seshadri-surfaces/039-Seshadri-surfaces.pdf) · [LaTeX](papers/039/seshadri-surfaces/main.tex) |
| 039 | Maximal multipoint Seshadri constants in higher dimensions | [PDF (14 pp.)](papers/039/seshadri-higher-dimensions/039-Seshadri-higher-dimensions.pdf) · [LaTeX](papers/039/seshadri-higher-dimensions/main.tex) |
| 039 | Maximal multipoint Seshadri constants in positive characteristic | [PDF (12 pp.)](papers/039/seshadri-positive-characteristic/039-Seshadri-positive-characteristic.pdf) · [LaTeX](papers/039/seshadri-positive-characteristic/main.tex) |
| 058 | Semialgebraic universal covers of normal projective varieties | [PDF (52 pp.)](papers/058/semialgebraic-universal-covers/058-Semialgebraic-universal-covers.pdf) · [LaTeX](papers/058/semialgebraic-universal-covers/main.tex) |
| 058 | Symmetry of semialgebraic bounded domains with compact quotient | [PDF (16 pp.)](papers/058/symmetry-bounded-domains/058-Symmetry-bounded-domains.pdf) · [LaTeX](papers/058/symmetry-bounded-domains/main.tex) |
| 087 | The symmetric Mahler conjecture and its equality cases | [PDF (17 pp.)](papers/087/symmetric-mahler/087-Symmetric-Mahler.pdf) · [LaTeX](papers/087/symmetric-mahler/main.tex) |
| 087 | The Mahler conjecture for general convex bodies | [PDF (58 pp.)](papers/087/general-mahler/087-General-Mahler.pdf) · [LaTeX](papers/087/general-mahler/main.tex) |
| 087 | Symplectic balls in symmetric polar products | [PDF (13 pp.)](papers/087/symmetric-polar-products/087-Symmetric-polar-products.pdf) · [LaTeX](papers/087/symmetric-polar-products/main.tex) |
| 091 | The logarithmic Brunn–Minkowski conjecture | [PDF (13 pp.)](papers/091/logarithmic-brunn-minkowski/091-Logarithmic-Brunn-Minkowski.pdf) · [LaTeX](papers/091/logarithmic-brunn-minkowski/main.tex) |
| 166 | The higher-dimensional Erdős distinct-distances conjecture | [PDF (74 pp.)](papers/166/erdos-distinct-distances/166-Erdos-distinct-distances.pdf) · [LaTeX](papers/166/erdos-distinct-distances/main.tex) |

## Build a manuscript

The projects are self-contained LaTeX directories. Use TeX Live with `latexmk`, pdfLaTeX, and Biber. The reviewed edition was built with TeX Live 2026 and Biber 2.22. This command builds the Fujita manuscript from the repository root.

```sh
cd papers/038/fujita-freeness
latexmk -pdf -outdir=.build main.tex
```

The regenerated PDF is `.build/main.pdf`. The named PDF in the manuscript folder is the reviewed copy.

## Review and verification

- The [proof audit](docs/proof-audit.md) records the mathematical checks, revisions, and remaining dependencies for each manuscript.
- The [general Mahler verification](papers/087/general-mahler/verification/README.md) reproduces the ten finite arithmetic checks.
- The [family 039 interpolation checks](papers/039/verification/README.md) reproduce the finite-field examples for the jet and horizontal-row matrices.

See [how to add a manuscript](docs/adding-a-manuscript.md) for the directory and catalogue conventions. The [provenance notice](NOTICE.md) describes the scope of the included [upstream license](LICENSE-OpenAI.txt).
