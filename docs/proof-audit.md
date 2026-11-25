# Proof review

The audit compares the revised manuscripts with the second edition and with the pinned OpenAI Math sources. Each entry records which arguments were traced, what changed, and any dependencies that remain.

## 038 Fujita

All four argument files read. Reconstructed the lattice equality and exceptional-restriction case, normalized minimizer compactness on a fixed SNC resolution, threshold specialization, tangent variation and slice-growth inequalities with the order m → ∞ followed by l → ∞, rational polytope support, ideal-order minimum and strictness, and the two adjoint lifts.

Gave the threshold-ideal localization proof using the truncated monomial basis in the completed local ring, and verified explicitly why the adapted basis preserves the minimum. Uses log-resolution, threshold semicontinuity, and Kawamata–Viehweg as external results.

## 039 Nagata

All proof sections read. Checked the common incidence exceptional set and cyclic product, rational family of plane equations and frame transitions in the normal limit, square-case torsion and displacement argument, coefficient spaces and degree, theta multipliers and normalized convergence, collision ideal, irrational endpoint parameters, exact polygon slices and rounding, and final substitutions.

The earlier migration had corrupted the array subscript in the displayed limiting matrix. Restored the exact row and column indices; the surrounding proof had the correct sets. Checked the same delimiter pattern across the twelve pinned sources.

## 039 Seshadri higher dimensions

All argument sections read. Checked lexicographic flag and division, finite positive exposing weights, row-product inclusion, compression, nodal branch degree via parametrization, lattice interval and order of three heights, fixed smaller interior, CRT jets, singular curve lengths, and upper volume bound.

Explained why the blow-up of the embedded curve is the strict transform via the Rees algebra map.

## 039 Seshadri positive characteristic

All argument sections read. Checked the jet matrix over the truncated power-series ring, including distinctness of formal centers and passage from the nonempty rank locus to rational points. Checked the Hensel node also in characteristic two, the nonconsecutive compressed rows, all interpolation/positivity steps, and the geometric generic point.

Spelled out field base change of global sections and completed the nef boundary claim in the introduction.

## 039 Seshadri surfaces

All argument sections read. Checked nodal divisor from the very ample square on the blow-up, intersection on the transverse branches, finite weighted transfer, diagonal slice compression, triangle width and order, subgroup averaging, exact determinant range, principal parts, effective perturbation, and field descent.

Restored the pushforward explanation with the local exceptional order and normality. Standard algebraic geometry is used at the stated references.

## 058 bounded domains

All argument sections read. Checked finite-sheet root polynomial and the maximum argument, proper intrinsic metric, generic joint offset limits, independent supporting covectors, analytic-disc contraction and radial derivative, noncollapse, both directions of rescaled set convergence, normal families and bounded realization.

Made the line restriction in the zero-free Jacobian limit explicit. Verified the three actions, divisibility convention and zero-block convention against Vey, pp. 479–481. [Vey’s paper](https://www.numdam.org/item/10.24033/asens.1200.pdf)

## 058 semialgebraic universal covers

Read the preparation, localization, window induction, quotient, group and compact-factor sections and the applications. Traced the box/accuracy order, full projective fibres versus a parametrizing open subset, actual incidence and local psh trace, compact inverse charts, deck stabilizers, fibrewise Albanese and polarization.

Made uniform seed membership at a moving center explicit before the matrix square root in the recentering ratio. The compact special abelianity and log abundance theorems are independent research inputs; their proofs are not part of this paper. Several cited analytic preparations remain a dependency audit rather than a reproof.

## 087 general Mahler

Reconstructed the projection normalization, Gaussian covariance and entropy bounds, the spectral threshold identity, the weighted commutator estimates and the strictness argument. Traced the quantitative inputs to the analytic interpolation, tail bounds, and width cases in the two scalar sections. Checked the distinction between a positive-length segment and a coincident endpoint in the equality argument.

Corrected three instances where earlier typesetting treated a variable or a defect functional as the exponential constant. Added the moment integrability step to the entropy–transport corollary. All ten finite arithmetic programs passed when run from fresh inputs. The programs verify the specified finite inequalities. The analytic estimates and the geometric-to-functional and entropy–transport implications have separate proofs or cited theorem inputs.

## 087 symmetric Mahler

All argument sections read. Checked the lens convexity and boundary distribution, homogeneous flux and d! normalization, minor mass and radial Fatou bounds, boundary ties, simplex maximizers and approximation, product-neighborhood deficit passage, common supporting witness, uniform endpoint comparison, three-ball criterion and Hanner recursion.

Wrote the support-function normalization and separation explicitly in the median step. The proof uses the finite-dimensional classification in Hansen and Lima, Corollary 7.4. [Hansen and Lima](https://doi.org/10.1007/BF02392457)

## 087 symmetric polar products

All proof sections read. Verified radial and angular derivatives, uniform endpoint bound and constants, fixed order of Moser choices, flow direction, radial pullback, strict monotonicity on common horizontal intervals, symplectic rescalings, nonsqueezing cylinder and volume consequences.

Fixed mismatched embedding symbol, stale step reference and broken capacity sentence. Compared the exact strict hypotheses and the closed-source convention of the optional packing corollary with the pinned upstream packing theorem. Its independent proof is outside these twelve manuscripts.

## 091 logarithmic Brunn–Minkowski

All proof sections read. Compact moment construction, uniform coercivity and local ellipticity, adjoints and parity, cutoff powers and L² splitting, tensor trace invariance and symmetrization, joint Hilbert-space estimate, slab limits, Wulff and Lₚ deductions.

Clarified cutoff estimates. Replaced the density classification argument by convolution with uniform measure on a ball and outer dilations, valid for singular measures. Berman–Berndtsson Theorem 1.1, Klartag Proposition 2/Remark 1, Wang Corollary 2.3, Saroglou Theorem 3.1, and local elliptic regularity checked at source. The published books and papers are used as theorem inputs.

## 166 Erdős distinct distances

Checked the least-dimension reduction, the endpoint selection, the global and local evaluation parameters, and the sampling rank inequality. Read through the isolated-component interpolation, positive-characteristic multiplicity compression, common regular equations, degree and tangent constraints for evaluation flats, the two rich-motion counts, terminal-curve deletion, and rank propagation at common and separated scales. In particular, traced where strict exponent margins are required and where the proof instead uses regularity and curve lifting.

Made explicit why distinct retained neighbors supply distinct local flats. Checked the Guth–Katz incidence statement with its plane cap and k ≥ 3 threshold against the published theorem. Our review of the long scale and incidence arguments was a check of the manuscript’s proof. [Guth–Katz, Theorem 4.5](https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p02-p.pdf)

## Reproducible checks

- All twelve LaTeX projects were built with pdfLaTeX and Biber, with resolved references and citations and zero errors from the house TeX checker.
- The ten general Mahler programs were run in a fresh directory with Python assertions enabled and SymPy 1.14.0. The archive contains the programs, their input hashes, and instructions.
- The interpolation implementation was checked on 132 finite-field jet examples and 90 horizontal-row examples. These are spot checks of the interpolation formulas.
- Where upstream Lean entries were available, the review compared the theorem statements and solution entry points. This review did not execute the upstream Lean checks.

The mathematical review follows the implications in the revised manuscripts and checks selected source statements where hypotheses matter. The cited results remain inputs. In particular, the abelianity and log abundance papers used by the semialgebraic universal-cover theorem and the separate packing theorem used by the optional symplectic corollary were not re-proved in this review. [Pinned OpenAI Math catalogue](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/CONTENTS.md)
