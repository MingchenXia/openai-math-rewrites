# Adding a manuscript

Put each manuscript in `papers/<family>/<short-title>/`. Use the three-digit identifier from the upstream catalogue for `<family>` and a lowercase, hyphenated short title for `<short-title>`. Give each manuscript its own folder, even if the family already has one.

1. Add `main.tex`, the local `cgeometry.sty` and `ComplexGeometry.bib`, and the section and figure files needed to build the manuscript from its folder. Keep document-relative paths and leave the author field blank until authorship is supplied.
2. Add `PROVENANCE.md` with the original title, a link to the upstream source pinned to a commit, and a short account of the adaptation. Add any source notices that accompany the files.
3. Build with `latexmk -pdf -outdir=.build main.tex`. Add the reviewed PDF to the manuscript folder using `<family>-<short-title>.pdf` for new entries.
4. Add the manuscript and its PDF and LaTeX links to the root catalogue. Record mathematical review and outstanding dependencies in `docs/proof-audit.md`.
5. Put checks specific to one paper in its own `verification/` directory. Put checks shared by a family in `papers/<family>/verification/`. In either case, document how to reproduce the result and what the checks cover.

LaTeX packages and bibliographies are kept with each manuscript so that a single folder can be downloaded and built on its own.
