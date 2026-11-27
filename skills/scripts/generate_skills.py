#!/usr/bin/env python3
"""
Batch-generate skill packages for 33 remaining courses.
Reads course data from course_skills_data.json, outputs skills/<domain>/<course-dir>/.
"""

import json, os, shutil, textwrap, re

SKILLS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON = os.path.join(os.path.dirname(SKILLS_ROOT), "scripts", "course_skills_data.json")

LICENSE_TEXT = """MIT License

Copyright (c) 2025 UofT KG Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Course metadata extracted from original ontology (not present in data JSON)
COURSE_META = {
    "MAT224H1": {
        "name": "Linear Algebra II",
        "domain": "math",
        "difficulty": 4, "units": 7,
        "description": "Abstract vector spaces, linear transformations, inner products, spectral theorem, Jordan canonical form.",
        "socratic_topic": "abstract vector space axioms",
        "socratic_concept": "generalising from $\\mathbb{R}^n$ to arbitrary fields",
        "deductive_theorem": "Spectral Theorem for real symmetric matrices: $A = Q\\Lambda Q^T$",
        "deductive_concept": "diagonalisation of symmetric matrices via orthogonal eigenvectors",
        "correction_error": "confusing algebraic multiplicity with geometric multiplicity",
        "correction_concept": "Jordan blocks and why $A$ might not be diagonalisable even when $\\det(A-\\lambda I)=0$ has $n$ roots",
        "formulas": [
            "$\\langle u, v \\rangle = u^T v$ — standard inner product on $\\mathbb{R}^n$",
            "$\\|v\\| = \\sqrt{\\langle v, v \\rangle}$ — norm induced by inner product",
            "$A = Q\\Lambda Q^T$ — spectral decomposition (real symmetric)",
            "$\\dim(V) = \\dim(\\ker(T)) + \\dim(\\operatorname{im}(T))$ — rank-nullity",
            "$\\chi_A(\\lambda) = \\det(A - \\lambda I)$ — characteristic polynomial",
            "$m_g(\\lambda) \\leq m_a(\\lambda)$ — geometric vs algebraic multiplicity",
        ],
        "proofs": [
            "Gram-Schmidt orthogonalisation: $u_k = v_k - \\sum_{i=1}^{k-1} \\operatorname{proj}_{u_i}(v_k)$",
            "Cauchy-Schwarz: $|\\langle u, v \\rangle| \\leq \\|u\\|\\|v\\|$",
            "Spectral Theorem: every real symmetric matrix has an orthonormal eigenbasis",
        ],
        "counterexamples": [
            "$A = [[1,1],[0,1]]$ is not diagonalisable ($m_g(1)=1 < m_a(1)=2$)",
            "$\\langle u, v \\rangle = u_1 v_1 - u_2 v_2$ is not an inner product (fails positivity)",
            "non-symmetric matrix can have real eigenvalues but not be orthogonally diagonalisable",
        ],
        "applications": [
            "PCA: spectral decomposition of covariance matrix $\\Sigma = Q\\Lambda Q^T$",
            "Google PageRank: eigenvector of stochastic matrix for $\\lambda=1$",
            "Image compression via SVD: $A = U\\Sigma V^T$",
        ],
        "skills_count": 8,
    },
    "MAT237Y1": {
        "name": "Multivariable Calculus with Proofs",
        "domain": "math",
        "difficulty": 5, "units": 8,
        "description": "Proof-based multivariable calculus: topology of $\\mathbb{R}^n$, differential calculus, implicit function theorem, optimisation, multiple integrals, vector calculus.",
        "socratic_topic": "topology of $\\mathbb{R}^n$",
        "socratic_concept": "open/closed/compact/connected sets in higher dimensions",
        "deductive_theorem": "Implicit Function Theorem",
        "deductive_concept": "when $F(x,y)=0$ defines $y$ locally as a function of $x$",
        "correction_error": "confusing path-connected with connected",
        "correction_concept": "topological connectedness vs path-connectedness",
        "formulas": [
            "$Df(a) = \\begin{bmatrix} \\partial f_i/\\partial x_j \\end{bmatrix}$ — Jacobian matrix at $a$",
            "$\\int_B f = \\int_a^b \\int_c^d f(x,y)\\,dy\\,dx$ — iterated integral (Fubini)",
            "$\\int_{\\partial \\Omega} \\omega = \\int_\\Omega d\\omega$ — generalised Stokes' theorem",
            "$\\nabla \\times (\\nabla f) = 0$ — curl of gradient is zero",
            "$\\nabla \\cdot (\\nabla \\times F) = 0$ — div of curl is zero",
            "$\\iiint_V \\nabla \\cdot F\\,dV = \\iint_{\\partial V} F \\cdot \\hat{n}\\,dS$ — divergence theorem",
        ],
        "proofs": [
            "Heine-Borel: $K \\subset \\mathbb{R}^n$ is compact $\\iff$ $K$ is closed and bounded",
            "Implicit Function Theorem: if $D_yF(a,b)$ is invertible, then $y=g(x)$ locally",
            "Change of variables: $\\int_{\\phi(U)} f = \\int_U (f\\circ\\phi)|\\det D\\phi|$",
        ],
        "counterexamples": [
            "$f(x,y) = \\frac{xy}{x^2+y^2}$ has no limit at $(0,0)$ — directional limits agree, but limit does not exist",
            "$f(x) = x^2 \\sin(1/x)$ is differentiable but $f'$ is not continuous at $0$",
            "topologist's sine curve is connected but not path-connected",
        ],
        "applications": [
            "Lagrange multipliers: $\\nabla f = \\lambda \\nabla g$ for constrained optimisation",
            "Divergence theorem: flux through closed surface = integral of divergence",
            "Stokes' theorem: circulation = flux of curl",
        ],
        "skills_count": 14,
    },
    "MAT240H1": {
        "name": "Algebra I",
        "domain": "math",
        "difficulty": 5, "units": 6,
        "description": "Theoretical approach to vector spaces over arbitrary fields, linear transformations, determinants, eigenvalues.",
        "socratic_topic": "vector spaces over arbitrary fields",
        "socratic_concept": "what changes when the field is $\\mathbb{Q}$, $\\mathbb{C}$, or $\\mathbb{F}_p$ instead of $\\mathbb{R}$",
        "deductive_theorem": "Cayley-Hamilton Theorem: $p_A(A)=0$",
        "deductive_concept": "every matrix satisfies its own characteristic polynomial",
        "correction_error": "assuming every linear operator has an eigenvalue",
        "correction_concept": "eigenvalues require the field to be algebraically closed (or at least contain the roots)",
        "formulas": [
            "$\\dim(V) = \\dim(U) + \\dim(V/U)$ — dimension of quotient space",
            "$p_A(\\lambda) = \\det(A-\\lambda I)$ — characteristic polynomial",
            "$p_A(A) = 0$ — Cayley-Hamilton theorem",
            "$T$ is diagonalisable $\\iff$ its minimal polynomial splits into distinct linear factors",
            "$\\operatorname{Hom}(V,W) \\cong M_{m\\times n}(F)$ — linear maps as matrices",
            "$\\det(T) = \\prod_i \\lambda_i$ — determinant as product of eigenvalues (over algebraically closed field)",
        ],
        "proofs": [
            "Cayley-Hamilton via the adjugate matrix: $\\det(A-\\lambda I)I = (A-\\lambda I)\\operatorname{adj}(A-\\lambda I)$",
            "Primary Decomposition Theorem: $V = \\bigoplus_i \\ker(p_i(T)^{m_i})$",
            "Rational Canonical Form via invariant factors",
        ],
        "counterexamples": [
            "$T: \\mathbb{R}^2 \\to \\mathbb{R}^2$ rotation by $90^\\circ$ has no real eigenvalues",
            "$A = [[0,1],[0,0]]$ is nilpotent ($A^2=0$) but not diagonalisable",
            "infinite-dimensional vector spaces have bases (requires Axiom of Choice)",
        ],
        "applications": [
            "Markov chains: transition matrix eigenvector for stationary distribution",
            "Differential equations: $x' = Ax$ solved by $x(t)=e^{At}x_0$",
            "Quantum mechanics: observables as Hermitian operators on Hilbert space",
        ],
        "skills_count": 8,
    },
    "MAT244H1": {
        "name": "Introduction to Ordinary Differential Equations",
        "domain": "math",
        "difficulty": 3, "units": 5,
        "description": "Applied ODEs: first-order equations, higher-order linear equations, systems, phase plane analysis, stability.",
        "socratic_topic": "direction fields and geometric intuition for ODEs",
        "socratic_concept": "reading slope fields to predict solution behaviour without solving",
        "deductive_theorem": "variation of parameters for $y''+p(t)y'+q(t)y = g(t)$",
        "deductive_concept": "particular solution via Wronskian and integration",
        "correction_error": "assuming $e^{\\int p}$ is always the correct integrating factor",
        "correction_concept": "the integrating factor method $\\mu(x) = e^{\\int P(x)\\,dx}$ for $y'+P(x)y=Q(x)$",
        "formulas": [
            "$y' + P(x)y = Q(x)$ — first-order linear, integrating factor $\\mu = e^{\\int P\\,dx}$",
            "$y'' + p(t)y' + q(t)y = g(t)$ — second-order linear",
            "$y_h = c_1 y_1 + c_2 y_2$ — homogeneous solution (superposition)",
            "$y_p = -y_1\\int \\frac{y_2 g}{W}\\,dt + y_2\\int \\frac{y_1 g}{W}\\,dt$ — variation of parameters",
            "$W(y_1,y_2) = y_1 y_2' - y_2 y_1'$ — Wronskian",
            "$\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = A \\begin{bmatrix} x \\\\ y \\end{bmatrix}$ — linear system, solutions via eigenvalues of $A$",
        ],
        "proofs": [
            "Existence and Uniqueness Theorem (Picard-Lindelöf): $|f(t,y)-f(t,z)| \\leq L|y-z|$ implies unique solution",
            "Wronskian test for linear independence of solutions: $W(t) \\neq 0$",
            "Stability via eigenvalues: $\\operatorname{Re}(\\lambda) < 0$ for all $\\lambda \\implies$ asymptotically stable",
        ],
        "counterexamples": [
            "$y' = y^{2/3}, y(0)=0$ has multiple solutions (fails uniqueness — not Lipschitz at $0$)",
            "$y' = 1 + y^2$ blows up in finite time even though $f$ is smooth",
            "a centre ($\\lambda = \\pm i$) is Lyapunov stable but not asymptotically stable",
        ],
        "applications": [
            "Population dynamics: logistic equation $P' = rP(1-P/K)$",
            "Spring-mass system: $mx'' + bx' + kx = 0$",
            "Predator-prey: Lotka-Volterra equations",
        ],
        "skills_count": 6,
    },
    "MAT247H1": {
        "name": "Algebra II",
        "domain": "math",
        "difficulty": 5, "units": 6,
        "description": "Advanced linear algebra: modules, canonical forms, bilinear forms.",
        "socratic_topic": "modules over a PID and their structure",
        "socratic_concept": "generalising vector spaces to modules — what breaks when the scalar set is not a field",
        "deductive_theorem": "Rational Canonical Form via invariant factors",
        "deductive_concept": "cyclic decomposition of $F[x]$-module $V_T$",
        "correction_error": "confusing Jordan canonical form with rational canonical form",
        "correction_concept": "JCF requires eigenvalues in the field; RCF works over any field",
        "formulas": [
            "$V_T \\cong F[x]/(p_1(x)) \\oplus \\cdots \\oplus F[x]/(p_k(x))$ — cyclic decomposition",
            "$\\chi_A(x) = \\prod_i p_i(x)^{e_i}$ — characteristic polynomial as product of invariant factors",
            "$m_A(x) = p_k(x)$ — minimal polynomial = largest invariant factor",
            "$J = \\operatorname{diag}(J_{n_1}(\\lambda_1), \\dots, J_{n_k}(\\lambda_k))$ — Jordan canonical form",
            "$B: V \\times V \\to F$ — bilinear form, matrix $[B]_{ij} = B(v_i, v_j)$",
            "$\\operatorname{Sym}_n(F) = \\{A = A^T\\}$ — space of symmetric bilinear forms",
        ],
        "proofs": [
            "Structure Theorem for finitely generated modules over a PID",
            "Rational Canonical Form via companion matrices of invariant factors",
            "Sylvester's Law of Inertia for real symmetric bilinear forms",
        ],
        "counterexamples": [
            "$\\mathbb{Z}$ as a $\\mathbb{Z}$-module is not a vector space (torsion-free but not over a field)",
            "a module over a non-PID may not decompose into cyclic submodules",
            "a real symmetric matrix can be diagonalised over $\\mathbb{R}$ but not every bilinear form can be diagonalised",
        ],
        "applications": [
            "Special relativity: Minkowski metric as indefinite bilinear form of signature $(3,1)$",
            "Crystallography: point groups as automorphisms of lattices",
            "Control theory: reachability via Krylov subspaces and companion matrices",
        ],
        "skills_count": 6,
    },
    "MAT267H1": {
        "name": "Advanced Ordinary Differential Equations",
        "domain": "math",
        "difficulty": 4, "units": 5,
        "description": "Advanced ODE topics building on MAT244: nonlinear systems, bifurcations, perturbation methods, boundary value problems.",
        "socratic_topic": "phase portraits of nonlinear systems",
        "socratic_concept": "linearising near fixed points and interpreting eigenvalues of the Jacobian",
        "deductive_theorem": "Poincaré–Bendixson Theorem",
        "deductive_concept": "bounded orbits in 2D must approach a fixed point or a limit cycle",
        "correction_error": "assuming linear stability guarantees nonlinear stability",
        "correction_concept": "Hartman-Grobman: linearisation determines local dynamics only when eigenvalues have non-zero real part",
        "formulas": [
            "$x' = f(x)$ — autonomous system, fixed point $f(x^*) = 0$",
            "$\\delta x' = Df(x^*)\\delta x$ — linearisation near fixed point",
            "$\\dot{r} = r(\\mu - r^2),\\; \\dot{\\theta} = 1$ — supercritical Hopf bifurcation normal form",
            "$\\epsilon y'' + y' + f(y) = 0$ — singular perturbation (boundary layer)",
            "$y'' + \\lambda y = 0,\\; y(0)=y(L)=0$ — Sturm-Liouville eigenvalue problem",
            "$\\lambda_n = \\left(\\frac{n\\pi}{L}\\right)^2$ — eigenvalues for Dirichlet BC",
        ],
        "proofs": [
            "Hartman-Grobman: if $Df(x^*)$ has no eigenvalue with $\\operatorname{Re}(\\lambda)=0$, then the nonlinear flow is topologically conjugate to the linearisation",
            "Poincaré–Bendixson: a non-empty compact $\\omega$-limit set in $\\mathbb{R}^2$ with no fixed points is a periodic orbit",
            "Sturm-Liouville: eigenvalues are real and simple, eigenfunctions form orthogonal basis",
        ],
        "counterexamples": [
            "$\\dot{x} = -x^3$ is asymptotically stable but linearisation gives $\\dot{x}=0$ (centre, not hyperbolic)",
            "Lorenz system $\\dot{x}=\\sigma(y-x), \\dot{y}=x(\\rho-z)-y, \\dot{z}=xy-\\beta z$ has chaotic attractor (3D, not constrained by Poincaré–Bendixson)",
            "a centre in the linearisation ($\\lambda = \\pm i\\omega$) can become a stable or unstable spiral when nonlinear terms are added",
        ],
        "applications": [
            "Hodgkin-Huxley model: action potential propagation via coupled ODEs",
            "Chemical oscillations: Belousov-Zhabotinsky reaction as limit cycle",
            "Predator-prey with Holling type II functional response: bifurcation analysis",
        ],
        "skills_count": 5,
    },
    "MAT301H1": {
        "name": "Groups and Symmetries",
        "domain": "math",
        "difficulty": 4, "units": 6,
        "description": "Group theory: permutations, symmetry groups, group actions, cosets, quotient groups, classification of finitely generated abelian groups.",
        "socratic_topic": "symmetry as a group",
        "socratic_concept": "the set of symmetries of a square has structure — closure, identity, inverse, associativity",
        "deductive_theorem": "Lagrange's Theorem: $|H|$ divides $|G|$",
        "deductive_concept": "cosets partition the group, each of size $|H|$",
        "correction_error": "assuming all groups are abelian",
        "correction_concept": "non-abelian groups: $S_n$, $D_{2n}$, $GL_n(F)$ — composition is not commutative",
        "formulas": [
            "$|G| = |H| \\cdot [G:H]$ — Lagrange's theorem",
            "$G/H = \\{gH : g \\in G\\}$ — quotient group when $H \\trianglelefteq G$",
            "$\\phi: G \\to H$ — homomorphism, $\\ker\\phi \\trianglelefteq G$, $\\operatorname{im}\\phi \\leq H$",
            "$G/\\ker\\phi \\cong \\operatorname{im}\\phi$ — First Isomorphism Theorem",
            "$|G| = |Z(G)| + \\sum [G:C_G(g_i)]$ — class equation",
            "$\\mathbb{Z}_{m} \\times \\mathbb{Z}_{n} \\cong \\mathbb{Z}_{mn}$ $\\iff$ $\\gcd(m,n)=1$",
        ],
        "proofs": [
            "Lagrange: left cosets $gH$ partition $G$, each bijects to $H$",
            "Cauchy's Theorem: if prime $p$ divides $|G|$, then $G$ has an element of order $p$",
            "Class equation: $|G| = |Z(G)| + \\sum_{i=1}^k [G:C_G(g_i)]$",
        ],
        "counterexamples": [
            "$A_4$ has order $12$ but no subgroup of order $6$ (converse of Lagrange fails)",
            "$S_3$ is non-abelian of order $6$ — smallest non-abelian group",
            "$Q_8 = \\{\\pm 1, \\pm i, \\pm j, \\pm k\\}$ — quaternion group, every subgroup is normal but $Q_8$ is not abelian",
        ],
        "applications": [
            "Crystallography: space groups describe crystal symmetries",
            "Rubik's cube: $\\approx 4.3 \\times 10^{19}$ configurations form a group",
            "Chemistry: molecular symmetry groups determine vibrational modes",
        ],
        "skills_count": 7,
    },
    "MAT309H1": {
        "name": "Introduction to Mathematical Logic",
        "domain": "math",
        "difficulty": 4, "units": 5,
        "description": "Predicate calculus, Gödel completeness and incompleteness theorems, recursive functions.",
        "socratic_topic": "formal languages and truth",
        "socratic_concept": "syntax vs semantics — what does it mean for a formula to be 'true' in a structure",
        "deductive_theorem": "Gödel's Completeness Theorem: $\\Gamma \\vdash \\varphi \\iff \\Gamma \\models \\varphi$",
        "deductive_concept": "semantic entailment coincides with syntactic provability for first-order logic",
        "correction_error": "confusing completeness of a logic with completeness of a theory",
        "correction_concept": "a logic is complete (every valid formula is provable); a theory (like PA) is incomplete (there are true but unprovable statements)",
        "formulas": [
            "$\\Gamma \\vdash \\varphi$ — syntactic consequence (provability)",
            "$\\Gamma \\models \\varphi$ — semantic consequence (all models of $\\Gamma$ satisfy $\\varphi$)",
            "$\\forall x (P(x) \\to \\exists y Q(x,y))$ — first-order formula",
            "$\\ulcorner \\varphi \\urcorner$ — Gödel number of formula $\\varphi$",
            "$\\operatorname{Con}(T) \\equiv \\neg \\exists x \\, \\operatorname{Proof}_T(x, \\ulcorner \\bot \\urcorner)$ — consistency statement",
            "$T \\not\\vdash \\operatorname{Con}(T)$ — Second Incompleteness Theorem (for consistent $T$ containing PA)",
        ],
        "proofs": [
            "Completeness via Henkin construction: extend $\\Gamma$ to a maximally consistent, witness-rich set, then build the canonical model",
            "Incompleteness via diagonal lemma: $\\exists \\varphi$ such that $PA \\vdash \\varphi \\leftrightarrow \\neg \\operatorname{Prov}_{PA}(\\ulcorner\\varphi\\urcorner)$",
            "Undecidability of first-order logic: reduction from halting problem",
        ],
        "counterexamples": [
            "Second-order logic is semantically complete but not deductively complete (no complete proof system)",
            "$PA$ is consistent but $PA \\not\\vdash \\operatorname{Con}(PA)$ (Gödel's Second)",
            "$ZFC$ cannot prove its own consistency (if consistent)",
        ],
        "applications": [
            "Automated theorem proving: resolution principle for first-order logic",
            "Database theory: relational algebra = first-order logic without quantifiers",
            "Programming languages: Curry-Howard correspondence (proofs = programs)",
        ],
        "skills_count": 5,
    },
    "MAT315H1": {
        "name": "Introduction to Number Theory",
        "domain": "math",
        "difficulty": 4, "units": 5,
        "description": "Elementary number theory: arithmetic functions, congruences, quadratic reciprocity, sums of squares.",
        "socratic_topic": "prime numbers",
        "socratic_concept": "there are infinitely many primes — but can we find a formula for them",
        "deductive_theorem": "Law of Quadratic Reciprocity",
        "deductive_concept": "determining solvability of $x^2 \\equiv p \\pmod{q}$ via $\\left(\\frac{p}{q}\\right)\\left(\\frac{q}{p}\\right) = (-1)^{\\frac{p-1}{2}\\frac{q-1}{2}}$",
        "correction_error": "$\\mathbb{Z}/n\\mathbb{Z}$ is a field $\\iff$ $n$ is prime — ignoring non-prime modulus structures",
        "correction_concept": "Chinese Remainder Theorem: $\\mathbb{Z}/mn\\mathbb{Z} \\cong \\mathbb{Z}/m\\mathbb{Z} \\times \\mathbb{Z}/n\\mathbb{Z}$ for $\\gcd(m,n)=1$",
        "formulas": [
            "$a \\equiv b \\pmod{n} \\iff n \\mid (a-b)$",
            "$\\gcd(a,b) = \\min\\{ax+by : x,y \\in \\mathbb{Z}, ax+by > 0\\}$",
            "$\\left(\\frac{a}{p}\\right) \\equiv a^{\\frac{p-1}{2}} \\pmod{p}$ — Euler's criterion",
            "$\\left(\\frac{p}{q}\\right)\\left(\\frac{q}{p}\\right) = (-1)^{\\frac{p-1}{2}\\frac{q-1}{2}}$ — Quadratic Reciprocity",
            "$\\varphi(n) = n\\prod_{p\\mid n} \\left(1-\\frac{1}{p}\\right)$ — Euler's totient",
            "$n = p_1^{e_1}\\cdots p_k^{e_k}$ — fundamental theorem of arithmetic",
        ],
        "proofs": [
            "Euclid: if $p_1,\\dots,p_k$ are all primes, then $p_1\\cdots p_k+1$ has a new prime factor",
            "Quadratic Reciprocity via Gauss's Lemma and Eisenstein's Lemma",
            "Fermat's Two-Square Theorem: $p = a^2 + b^2$ $\\iff$ $p \\equiv 1 \\pmod{4}$",
        ],
        "counterexamples": [
            "$2^{2^5}+1 = 4294967297 = 641 \\times 6700417$ — Fermat number $F_5$ is composite",
            "$n^2 + n + 41$ is prime for $n=0,\\dots,39$ but composite for $n=40$",
            "$\\mathbb{Z}/6\\mathbb{Z}$ has zero divisors: $2 \\cdot 3 \\equiv 0$ but neither factor is $0$",
        ],
        "applications": [
            "RSA encryption: $c \\equiv m^e \\pmod{n}$, $m \\equiv c^d \\pmod{n}$ where $n=pq$",
            "Elliptic curve cryptography (ECC)",
            "Hash functions and digital signatures",
        ],
        "skills_count": 5,
    },
    "MAT334H1": {
        "name": "Complex Variables",
        "domain": "math",
        "difficulty": 4, "units": 6,
        "description": "Functions of one complex variable: analytic functions, Cauchy's theorem, residue calculus, conformal mappings.",
        "socratic_topic": "complex differentiability",
        "socratic_concept": "Cauchy-Riemann equations: $f(z)=u+iv$ is analytic $\\iff$ $u_x=v_y$ and $u_y=-v_x$",
        "deductive_theorem": "Cauchy's Integral Formula: $f(a) = \\frac{1}{2\\pi i}\\oint_\\gamma \\frac{f(z)}{z-a}\\,dz$",
        "deductive_concept": "analytic functions are completely determined by their values on a closed curve",
        "correction_error": "$\\log(z)$ is multi-valued — forgetting branch cuts",
        "correction_concept": "$\\operatorname{Log}(z) = \\ln|z| + i\\operatorname{Arg}(z)$ with $\\operatorname{Arg}(z) \\in (-\\pi, \\pi]$",
        "formulas": [
            "$f'(z_0) = \\lim_{h\\to 0} \\frac{f(z_0+h)-f(z_0)}{h}$ — complex derivative",
            "$f(a) = \\frac{1}{2\\pi i}\\oint_\\gamma \\frac{f(z)}{z-a}\\,dz$ — Cauchy Integral Formula",
            "$\\oint_\\gamma f(z)\\,dz = 2\\pi i \\sum \\operatorname{Res}(f, a_k)$ — Residue Theorem",
            "$f(z) = \\sum_{n=0}^{\\infty} a_n (z-a)^n$ — power series expansion (radius of convergence)",
            "$\\sin(z) = \\frac{e^{iz} - e^{-iz}}{2i}$ — complex trigonometric functions",
            "$z \\mapsto \\frac{z-a}{1-\\bar{a}z}$ — Möbius transformation mapping unit disk to itself",
        ],
        "proofs": [
            "Cauchy's Theorem: $\\oint_\\gamma f = 0$ for analytic $f$ on simply connected domain (Goursat's proof)",
            "Cauchy Integral Formula from Cauchy's Theorem via deformation of contour",
            "Liouville: bounded entire functions are constant",
        ],
        "counterexamples": [
            "$f(z) = \\bar{z}$ is not complex differentiable anywhere (fails Cauchy-Riemann)",
            "$f(z) = e^{1/z}$ has an essential singularity at $z=0$ (Picard: every value except possibly one attained infinitely often)",
            "$f(z) = \\sqrt{z}$ cannot be defined continuously on all of $\\mathbb{C}$ — need branch cut",
        ],
        "applications": [
            "Evaluating real integrals via residue calculus: $\\int_{-\\infty}^{\\infty} \\frac{\\cos x}{x^2+1}\\,dx = \\frac{\\pi}{e}$",
            "Potential flow in fluid dynamics: complex potential $\\Phi(z) = \\phi + i\\psi$",
            "Conformal mapping for solving Laplace's equation on irregular domains",
        ],
        "skills_count": 6,
    },
    "STA130H1": {
        "name": "An Introduction to Statistical Reasoning and Data Science",
        "domain": "stats",
        "difficulty": 2, "units": 4,
        "description": "Introduction to statistical reasoning using R: EDA, hypothesis testing, confidence intervals, regression, simulation.",
        "socratic_topic": "what is a p-value",
        "socratic_concept": "the probability of observing data at least as extreme as what was observed, assuming $H_0$ is true",
        "deductive_theorem": "Central Limit Theorem: $\\bar{X}_n \\xrightarrow{d} N(\\mu, \\sigma^2/n)$",
        "deductive_concept": "the sampling distribution of the sample mean becomes normal as $n$ increases",
        "correction_error": "p-value is the probability that $H_0$ is true",
        "correction_concept": "the p-value is $P(\\text{data} \\mid H_0)$, not $P(H_0 \\mid \\text{data})$",
        "formulas": [
            "$\\bar{x} = \\frac{1}{n}\\sum_{i=1}^n x_i$ — sample mean",
            "$s^2 = \\frac{1}{n-1}\\sum_{i=1}^n (x_i - \\bar{x})^2$ — sample variance",
            "$\\text{SE}(\\bar{x}) = s/\\sqrt{n}$ — standard error of the mean",
            "$\\bar{x} \\pm t_{\\alpha/2, n-1} \\cdot \\text{SE}(\\bar{x})$ — confidence interval for $\\mu$",
            "$\\hat{y} = \\hat{\\beta}_0 + \\hat{\\beta}_1 x$ — simple linear regression",
            "$\\text{cor}(x,y) = \\frac{\\sum(x_i-\\bar{x})(y_i-\\bar{y})}{(n-1)s_x s_y}$ — Pearson correlation",
        ],
        "proofs": [
            "CLT via moment generating functions (conceptual): $M_{\\bar{X}_n}(t) \\to e^{\\mu t + \\sigma^2 t^2/2}$",
            "Unbiasedness of $s^2$: $E[s^2] = \\sigma^2$",
            "$t$-distribution as ratio of normal to chi-squared: $t = \\frac{Z}{\\sqrt{\\chi^2/\\nu}}$",
        ],
        "counterexamples": [
            "Anscombe's quartet: four datasets with identical $\\bar{x}, \\bar{y}, s_x, s_y, r$ but very different scatterplots",
            "Simpson's paradox: trend reverses when groups are combined",
            "p-hacking: running 20 tests at $\\alpha=0.05$ gives $1-0.95^{20} \\approx 64\\%$ chance of at least one false positive",
        ],
        "applications": [
            "A/B testing: two-sample $t$-test for comparing conversion rates",
            "Linear regression for predicting housing prices",
            "Bootstrap confidence intervals: resample $B=1000$ times, compute $\\bar{x}^*$, find 2.5th and 97.5th percentiles",
        ],
        "skills_count": 4,
    },
    "STA237H1": {
        "name": "Probability, Statistics and Data Analysis I",
        "domain": "stats",
        "difficulty": 3, "units": 5,
        "description": "Probability with simulation: probability spaces, random variables, distributions, LLN, CLT, sampling distributions.",
        "socratic_topic": "probability spaces and axioms",
        "socratic_concept": "Kolmogorov's axioms: $P(\\Omega)=1$, $P(A)\\geq 0$, $P(\\bigcup_i A_i)=\\sum_i P(A_i)$ for disjoint events",
        "deductive_theorem": "Law of Large Numbers: $\\bar{X}_n \\xrightarrow{p} \\mu$",
        "deductive_concept": "the sample average converges in probability to the population mean",
        "correction_error": "confusing $P(A \\cap B)$ with $P(A)P(B)$ — assuming independence without justification",
        "correction_concept": "$P(A \\cap B) = P(A)P(B|A) = P(B)P(A|B)$ — the product rule with conditioning",
        "formulas": [
            "$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$ — inclusion-exclusion",
            "$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ — conditional probability",
            "$E[X] = \\sum_x x \\cdot P(X=x)$ — discrete expectation",
            "$\\operatorname{Var}(X) = E[X^2] - (E[X])^2$ — variance",
            "$M_X(t) = E[e^{tX}]$ — moment generating function",
            "$\\bar{X}_n \\xrightarrow{d} N(\\mu, \\sigma^2/n)$ — Central Limit Theorem",
        ],
        "proofs": [
            "Weak Law of Large Numbers via Chebyshev's inequality: $P(|\\bar{X}_n-\\mu| > \\epsilon) \\leq \\sigma^2/(n\\epsilon^2)$",
            "Central Limit Theorem via MGFs (sketch): $M_{Z_n}(t) \\to e^{t^2/2}$",
            "Borel-Cantelli Lemma: if $\\sum P(A_n) < \\infty$, then $P(\\limsup A_n) = 0$",
        ],
        "counterexamples": [
            "Cauchy distribution has no mean — LLN does not apply",
            "St Petersburg paradox: $E[X] = \\infty$ but no rational person would pay infinite entry fee",
            "pairwise independence $\\nRightarrow$ mutual independence",
        ],
        "applications": [
            "Insurance risk modelling: Poisson distribution for claim counts",
            "Quality control: CLT justifies $\\bar{x}$ control charts with $\\pm 3\\sigma$ limits",
            "Monte Carlo integration: $E[g(X)] \\approx \\frac{1}{n}\\sum g(X_i)$",
        ],
        "skills_count": 4,
    },
    "STA238H1": {
        "name": "Probability, Statistics and Data Analysis II",
        "domain": "stats",
        "difficulty": 3, "units": 5,
        "description": "Statistical inference with computation: estimation, confidence intervals, hypothesis testing, linear models.",
        "socratic_topic": "maximum likelihood estimation",
        "socratic_concept": "finding $\\theta$ that maximises $L(\\theta; x) = \\prod_{i=1}^n f(x_i; \\theta)$",
        "deductive_theorem": "Neyman-Pearson Lemma",
        "deductive_concept": "the most powerful test for simple hypotheses is the likelihood ratio test",
        "correction_error": "confidence interval $(L,U)$ means $P(\\mu \\in (L,U))$ — but $\\mu$ is fixed, not random",
        "correction_concept": "the interval is random: $P(\\text{interval covers }\\mu) = 1-\\alpha$, not $P(\\mu \\in \\text{interval})$",
        "formulas": [
            "$L(\\theta; x) = \\prod_{i=1}^n f(x_i; \\theta)$ — likelihood function",
            "$\\hat{\\theta}_{MLE} = \\arg\\max_\\theta L(\\theta; x)$ — MLE",
            "$\\Lambda(x) = \\frac{L(\\theta_0; x)}{L(\\theta_1; x)}$ — likelihood ratio test statistic",
            "$\\text{SE}(\\hat{\\theta}) \\approx 1/\\sqrt{I(\\hat{\\theta})}$ — asymptotic standard error via Fisher information",
            "$\\hat{y} = X\\hat{\\beta}$ where $\\hat{\\beta} = (X^TX)^{-1}X^Ty$ — OLS estimator",
            "$F = \\frac{(\\text{RSS}_0 - \\text{RSS}_1)/(p_1-p_0)}{\\text{RSS}_1/(n-p_1)}$ — $F$-test for nested models",
        ],
        "proofs": [
            "Neyman-Pearson: any test with $\\phi(x) = I(\\Lambda(x) \\leq k)$ is most powerful at level $\\alpha = E_{\\theta_0}[\\phi(X)]$",
            "Asymptotic normality of MLE: $\\sqrt{n}(\\hat{\\theta} - \\theta_0) \\xrightarrow{d} N(0, I(\\theta_0)^{-1})$",
            "Gauss-Markov Theorem: OLS is BLUE (best linear unbiased estimator)",
        ],
        "counterexamples": [
            "MLE can be biased: $\\hat{\\sigma}^2_{MLE} = \\frac{1}{n}\\sum (x_i-\\bar{x})^2$ is biased for $\\sigma^2$",
            "Huber's example: MLE breaks down under heavy-tailed distributions (use robust M-estimation)",
            "likelihood can have multiple local maxima — especially in mixture models",
        ],
        "applications": [
            "Logistic regression: $\\hat{\\beta} = \\arg\\max \\sum [y_i \\log p_i + (1-y_i)\\log(1-p_i)]$",
            "AIC model selection: $AIC = 2k - 2\\log \\hat{L}$",
            "Wald test for $H_0: \\beta_j = 0$: $z = \\hat{\\beta}_j / \\text{SE}(\\hat{\\beta}_j)$",
        ],
        "skills_count": 4,
    },
    "STA257H1": {
        "name": "Probability and Statistics I",
        "domain": "stats",
        "difficulty": 4, "units": 5,
        "description": "Mathematically rigorous probability: probability spaces, random variables, distributions, LLN, CLT.",
        "socratic_topic": "probability as measure",
        "socratic_concept": "a probability space $(\\Omega, \\mathcal{F}, P)$ where $\\mathcal{F}$ is a $\\sigma$-algebra and $P$ is a measure",
        "deductive_theorem": "Strong Law of Large Numbers: $\\bar{X}_n \\xrightarrow{\\text{a.s.}} \\mu$",
        "deductive_concept": "almost sure convergence via the Borel-Cantelli lemma",
        "correction_error": "confusing convergence in probability with almost sure convergence",
        "correction_concept": "$X_n \\xrightarrow{p} X$ vs $X_n \\xrightarrow{\\text{a.s.}} X$ — the latter is stronger, requiring $P(\\lim X_n = X) = 1$",
        "formulas": [
            "$P(\\bigcup_{i=1}^\\infty A_i) \\leq \\sum_{i=1}^\\infty P(A_i)$ — countable subadditivity",
            "$F_X(x) = P(X \\leq x)$ — cumulative distribution function",
            "$f_X(x) = F_X'(x)$ — probability density function (if absolutely continuous)",
            "$\\varphi_X(t) = E[e^{itX}]$ — characteristic function",
            "$\\bar{X}_n \\xrightarrow{\\text{a.s.}} \\mu$ — SLLN (Kolmogorov)",
            "$\\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} N(0,1)$ — CLT",
        ],
        "proofs": [
            "SLLN via Kolmogorov's inequality and Borel-Cantelli",
            "Continuous Mapping Theorem: $X_n \\xrightarrow{d} X \\implies g(X_n) \\xrightarrow{d} g(X)$ for continuous $g$",
            "Cramér-Wold device: $X_n \\xrightarrow{d} X$ $\\iff$ $a^T X_n \\xrightarrow{d} a^T X$ for all $a$",
        ],
        "counterexamples": [
            "Slutsky's theorem requires convergence in distribution of one sequence and in probability of the other",
            "convergence in distribution $\\nRightarrow$ convergence in probability (e.g., $X_n = X$ for all $n$ vs $X$)",
            "characteristic function of Cauchy: $\\varphi(t) = e^{-|t|}$ is not differentiable at $0$",
        ],
        "applications": [
            "Portfolio theory: $E[R_p] = w^T \\mu$, $\\operatorname{Var}(R_p) = w^T \\Sigma w$",
            "Risk management: Value at Risk (VaR) as quantile of loss distribution",
            "Option pricing: $C = E[e^{-rT}(S_T - K)^+]$ under risk-neutral measure",
        ],
        "skills_count": 4,
    },
    "STA261H1": {
        "name": "Probability and Statistics II",
        "domain": "stats",
        "difficulty": 4, "units": 5,
        "description": "Rigorous statistical inference: estimation, MLE, hypothesis testing, likelihood ratio tests, confidence regions.",
        "socratic_topic": "sufficiency and the Rao-Blackwell Theorem",
        "socratic_concept": "a statistic $T(X)$ is sufficient if $P(X=x \\mid T(X)=t)$ does not depend on $\\theta$",
        "deductive_theorem": "Rao-Blackwell Theorem: $E[\\delta(X) \\mid T(X)]$ has variance no larger than $\\delta(X)$",
        "deductive_concept": "conditioning on a sufficient statistic improves any estimator",
        "correction_error": "UMVUE always exists and is unique",
        "correction_concept": "UMVUE may not exist, or may not be unique — depends on completeness of the sufficient statistic",
        "formulas": [
            "$f(x;\\theta) = g(T(x);\\theta)h(x)$ — factorisation theorem (Neyman-Fisher)",
            "$\\operatorname{Var}(E[\\delta|T]) \\leq \\operatorname{Var}(\\delta)$ — Rao-Blackwell",
            "$E[\\delta(X)] = g(\\theta)$ — bias of estimator $\\delta$",
            "$\\operatorname{MSE}(\\delta) = \\operatorname{Var}(\\delta) + \\text{Bias}(\\delta)^2$ — mean squared error",
            "$\\Lambda(x) = \\frac{\\sup_{\\theta \\in \\Theta_0} L(\\theta; x)}{\\sup_{\\theta \\in \\Theta} L(\\theta; x)}$ — likelihood ratio test",
            "$-2\\log\\Lambda(x) \\xrightarrow{d} \\chi^2_{\\nu}$ — Wilks' theorem",
        ],
        "proofs": [
            "Rao-Blackwell: law of total variance $\\operatorname{Var}(\\delta) = \\operatorname{Var}(E[\\delta|T]) + E[\\operatorname{Var}(\\delta|T)]$",
            "Lehmann-Scheffé: if $T$ is complete sufficient, then $E[\\delta|T]$ is UMVUE",
            "Neyman-Pearson Lemma for most powerful tests",
        ],
        "counterexamples": [
            "the MLE of $\\theta$ for $U(0,\\theta)$ is $\\hat{\\theta}=X_{(n)}$, which is biased — the UMVUE is $\\frac{n+1}{n}X_{(n)}$",
            "the sample median is a consistent estimator of the mean but is not UMVUE (not a function of a complete sufficient statistic)",
            "for the Cauchy distribution, no UMVUE exists — no complete sufficient statistic",
        ],
        "applications": [
            "Hypothesis testing in clinical trials: $H_0: \\mu_\\text{trt} = \\mu_\\text{ctrl}$ vs $H_1: \\mu_\\text{trt} \\neq \\mu_\\text{ctrl}$",
            "Likelihood ratio tests for model selection in GLMs",
            "Confidence intervals via likelihood profiling: $\\{ \\theta : -2\\log\\Lambda(\\theta) \\leq \\chi^2_{1,\\alpha} \\}$",
        ],
        "skills_count": 4,
    },
    "STA302H1": {
        "name": "Methods of Data Analysis I",
        "domain": "stats",
        "difficulty": 3, "units": 5,
        "description": "Regression-focused data analysis: simple/multiple regression, diagnostics, variable selection, model validation.",
        "socratic_topic": "the geometry of least squares",
        "socratic_concept": "$\\hat{y} = X\\hat{\\beta}$ is the orthogonal projection of $y$ onto $\\operatorname{col}(X)$",
        "deductive_theorem": "Gauss-Markov Theorem",
        "deductive_concept": "OLS is BLUE under the Gauss-Markov assumptions",
        "correction_error": "$R^2$ alone determines model quality",
        "correction_concept": "$R^2$ always increases with more predictors — use adjusted $R^2$ or $C_p$",
        "formulas": [
            "$\\hat{\\beta} = (X^TX)^{-1}X^Ty$ — OLS solution",
            "$\\hat{y} = X\\hat{\\beta} = Hy$ where $H = X(X^TX)^{-1}X^T$ — hat matrix",
            "$\\operatorname{Var}(\\hat{\\beta}) = \\sigma^2 (X^TX)^{-1}$",
            "$\\text{SSR} = \\sum (\\hat{y}_i - \\bar{y})^2$, $\\text{SSE} = \\sum (y_i - \\hat{y}_i)^2$",
            "$R^2 = 1 - \\text{SSE}/\\text{SST}$ — coefficient of determination",
            "$R^2_{\\text{adj}} = 1 - \\frac{\\text{SSE}/(n-p-1)}{\\text{SST}/(n-1)}$ — adjusted $R^2$",
        ],
        "proofs": [
            "Gauss-Markov: any linear estimator $\\tilde{\\beta} = Cy$ has $\\operatorname{Var}(\\tilde{\\beta}) \\geq \\operatorname{Var}(\\hat{\\beta})$ under $E[\\tilde{\\beta}]=\\beta$",
            "ANOVA decomposition: $\\text{SST} = \\text{SSR} + \\text{SSE}$",
            "$F$-test: $\\frac{(\\text{RSS}_0-\\text{RSS}_1)/(p_1-p_0)}{\\text{RSS}_1/(n-p_1-1)} \\sim F_{p_1-p_0, n-p_1-1}$ under $H_0$",
        ],
        "counterexamples": [
            "Anscombe's quartet shows $R^2$ can be identical for very different data",
            "multicollinearity: $\\hat{\\beta}$ has high variance when predictors are correlated",
            "extrapolation beyond observed predictor range is dangerous (model may not hold)",
        ],
        "applications": [
            "Predicting house prices: $\\log(\\text{price}) = \\beta_0 + \\beta_1\\text{sqft} + \\beta_2\\text{bedrooms} + \\epsilon$",
            "Residual diagnostics: Q-Q plot for normality, fitted vs residuals for homoscedasticity",
            "Variable selection via stepwise regression and $C_p$",
        ],
        "skills_count": 4,
    },
    "STA303H1": {
        "name": "Methods of Data Analysis II",
        "domain": "stats",
        "difficulty": 4, "units": 5,
        "description": "Advanced data analysis: ANOVA, mixed effects models, generalized linear models, experimental design.",
        "socratic_topic": "hierarchical structure in data",
        "socratic_concept": "students within classrooms within schools — correlation within groups violates independence",
        "deductive_theorem": "the EM algorithm for mixed models",
        "deductive_concept": "iteratively estimate fixed effects (M-step) and predict random effects (E-step)",
        "correction_error": "ignoring random effects and treating all observations as independent",
        "correction_concept": "mixed models: $y = X\\beta + Zu + \\epsilon$ where $u \\sim N(0, G)$ and $\\epsilon \\sim N(0, R)$",
        "formulas": [
            "$y_{ij} = \\mu + \\alpha_i + \\epsilon_{ij}$ — one-way ANOVA",
            "$\\text{SS}_{\\text{total}} = \\text{SS}_{\\text{treatment}} + \\text{SS}_{\\text{error}}$ — ANOVA decomposition",
            "$\\log\\left(\\frac{p}{1-p}\\right) = X\\beta$ — logistic regression (GLM with logit link)",
            "$\\log(E[Y]) = X\\beta$ — Poisson regression (log link for count data)",
            "$y = X\\beta + Zu + \\epsilon$ — linear mixed model",
            "$\\text{AIC} = 2k - 2\\log L$, $\\text{BIC} = k\\log n - 2\\log L$ — model selection",
        ],
        "proofs": [
            "ANOVA $F$-test: $F = \\frac{\\text{MS}_{\\text{treat}}}{\\text{MS}_{\\text{error}}} \\sim F_{k-1, n-k}$ under $H_0: \\alpha_i = 0$",
            "EM algorithm increases likelihood at each iteration: $Q(\\theta|\\theta^{(t)}) \\leq \\log L(\\theta^{(t+1)}|x)$",
            "REML: restricted maximum likelihood estimates variance components unbiasedly",
        ],
        "counterexamples": [
            "ignoring clustering inflates Type I error (standard errors too small)",
            "GLM with wrong link function can give biased estimates",
            "ANOVA is robust to moderate non-normality but not to unequal variances (use Welch's test)",
        ],
        "applications": [
            "Longitudinal data analysis: repeated measures across time within subjects",
            "Logistic regression for credit default prediction",
            "Split-plot designs in agricultural experiments",
        ],
        "skills_count": 4,
    },
    "STA304H1": {
        "name": "Surveys, Sampling and Observational Data",
        "domain": "stats",
        "difficulty": 3, "units": 5,
        "description": "Survey design, sampling methods, observational studies, confounding, propensity scores.",
        "socratic_topic": "bias in surveys",
        "socratic_concept": "selection bias, non-response bias, and measurement error — the three fundamental survey errors",
        "deductive_theorem": "Horvitz-Thompson estimator",
        "deductive_concept": "$\\hat{\\tau} = \\sum_{i \\in S} y_i / \\pi_i$ where $\\pi_i$ is inclusion probability — unbiased for population total",
        "correction_error": "correlation implies causation in observational studies",
        "correction_concept": "confounding: $X$ and $Y$ may both be caused by $Z$ — randomisation is the gold standard",
        "formulas": [
            "$\\hat{\\tau} = \\sum_{i \\in S} \\frac{y_i}{\\pi_i}$ — Horvitz-Thompson estimator of population total",
            "$\\operatorname{Var}(\\hat{\\tau}) = \\sum_{i \\in S} \\sum_{j \\in S} \\frac{\\pi_{ij} - \\pi_i\\pi_j}{\\pi_i\\pi_j} \\frac{y_i}{\\pi_i} \\frac{y_j}{\\pi_j}$",
            "$\\hat{\\mu}_{\\text{strat}} = \\sum_{h=1}^H \\frac{N_h}{N} \\bar{y}_h$ — stratified sampling mean",
            "$\\hat{\\mu}_{\\text{clust}} = \\frac{\\sum_{i \\in S} y_i}{\\sum_{i \\in S} m_i}$ — cluster sampling ratio estimator",
            "$e(x) = P(Z=1 | X=x)$ — propensity score",
            "$\\hat{\\tau}_{\\text{IPTW}} = \\frac{1}{n}\\sum \\frac{Z_i Y_i}{e(X_i)} - \\frac{1}{n}\\sum \\frac{(1-Z_i)Y_i}{1-e(X_i)}$ — inverse probability weighting",
        ],
        "proofs": [
            "Horvitz-Thompson: $E[\\hat{\\tau}] = \\sum_{i=1}^N y_i$ by design-unbiasedness",
            "Rosenbaum-Rubin: conditioning on $e(X)$ yields balanced covariate distributions between treated and control",
            "Neyman allocation: $n_h \\propto N_h \\sigma_h$ minimises variance for fixed cost",
        ],
        "counterexamples": [
            "Literary Digest poll (1936): $n=2.4$ million but biased by selection (non-response and convenience sampling)",
            "Simpson's paradox in Berkeley admissions — gender bias disappears when conditioning on department",
            "confounding in observational studies: ice cream sales and drowning are correlated (confounded by temperature)",
        ],
        "applications": [
            "Canadian census: stratified sampling by province and urban/rural",
            "A/B testing: blocked randomisation by user segment",
            "Causal inference from electronic health records: propensity score matching",
        ],
        "skills_count": 4,
    },
    "STA314H1": {
        "name": "Statistical Methods for Machine Learning I",
        "domain": "stats",
        "difficulty": 4, "units": 5,
        "description": "Statistical ML: supervised learning, regularization, classification, clustering, cross-validation, decision trees.",
        "socratic_topic": "the bias-variance tradeoff",
        "socratic_concept": "$E[(\\hat{f}(x) - f(x))^2] = \\text{Bias}^2 + \\text{Variance} + \\sigma^2$",
        "deductive_theorem": "representer theorem for kernel methods",
        "deductive_concept": "the optimal solution in a reproducing kernel Hilbert space has the form $f(x) = \\sum \\alpha_i K(x_i, x)$",
        "correction_error": "cross-validation leaks information when feature selection is done before the split",
        "correction_concept": "all feature selection and preprocessing must be embedded inside the cross-validation loop",
        "formulas": [
            "$E[(y - \\hat{f}(x))^2] = \\text{Bias}^2 + \\text{Variance} + \\sigma^2$ — bias-variance decomposition",
            "$\\hat{\\beta}_{\\text{ridge}} = (X^TX + \\lambda I)^{-1}X^Ty$ — ridge regression",
            "$\\hat{\\beta}_{\\text{lasso}} = \\arg\\min_\\beta \\|y - X\\beta\\|^2 + \\lambda\\|\\beta\\|_1$ — LASSO",
            "$K(x_i, x_j) = \\exp(-\\gamma\\|x_i - x_j\\|^2)$ — RBF kernel",
            "$\\text{CV}_{(k)} = \\frac{1}{k}\\sum_{v=1}^k \\frac{1}{n_v}\\sum_{i \\in \\text{fold}_v} (y_i - \\hat{f}_{-v}(x_i))^2$ — $k$-fold CV",
            "$Gini(D) = 1 - \\sum_{k=1}^K p_k^2$ — Gini impurity for decision trees",
        ],
        "proofs": [
            "Bias-variance decomposition: expand $E[(y-\\hat{f})^2]$ and add/subtract $E[\\hat{f}]$",
            "Representer theorem: any minimiser in RKHS lies in the span of the kernel evaluated at training points",
            "LASSO: $\\ell_1$ penalty induces sparsity via geometry of $\\ell_1$ ball (diamond) touching contours of $\\|y-X\\beta\\|^2$",
        ],
        "counterexamples": [
            "overfitting: a polynomial of degree $n-1$ fits $n$ points perfectly ($R^2=1$) but generalises poorly",
            "no free lunch theorem: no algorithm dominates all others across all problems",
            "correlation $\\neq$ causation: feature importance from trees does not imply causal relationship",
        ],
        "applications": [
            "Regularised regression for high-dimensional genomics data ($p \\gg n$)",
            "Support vector machines with RBF kernel for image classification",
            "Random forests for feature importance ranking in customer churn prediction",
        ],
        "skills_count": 4,
    },
    "STA347H1": {
        "name": "Probability",
        "domain": "stats",
        "difficulty": 5, "units": 5,
        "description": "Advanced probability theory: measure-theoretic foundations, modes of convergence, characteristic functions, conditional expectation.",
        "socratic_topic": "what is a probability measure",
        "socratic_concept": "a measure $P: \\mathcal{F} \\to [0,1]$ with $P(\\Omega)=1$ — extending from intervals to all measurable sets",
        "deductive_theorem": "Kolmogorov's Three Series Theorem for almost sure convergence of sums",
        "deductive_concept": "$\\sum X_n$ converges a.s. $\\iff$ three series converge (means, variances, truncated tails)",
        "correction_error": "confusing $\\sigma$-algebras with partitions of $\\Omega$",
        "correction_concept": "$\\sigma$-algebras are closed under countable operations, not just finite — the Borel $\\sigma$-algebra on $\\mathbb{R}$ is uncountably rich",
        "formulas": [
            "$E[X|\\mathcal{G}]$ — conditional expectation = $\\mathcal{G}$-measurable r.v. with $\\int_A E[X|\\mathcal{G}]\\,dP = \\int_A X\\,dP$ for all $A \\in \\mathcal{G}$",
            "$\\varphi_X(t) = E[e^{itX}]$ — characteristic function, always exists",
            "$\\mu_n \\xrightarrow{w} \\mu$ $\\iff$ $\\int f\\,d\\mu_n \\to \\int f\\,d\\mu$ for all bounded continuous $f$ (weak convergence)",
            "$\\frac{X_n}{b_n} \\xrightarrow{d} G_{\\alpha, \\beta, \\gamma}$ — generalised central limit theorem for stable laws",
            "$\\limsup_{n\\to\\infty} A_n = \\bigcap_{n=1}^\\infty \\bigcup_{k=n}^\\infty A_k$ — events occur infinitely often",
            "$P(\\limsup A_n) = 0$ $\\iff$ $\\sum P(A_n) < \\infty$ — Borel-Cantelli",
        ],
        "proofs": [
            "Kolmogorov's Three Series Theorem via Lévy's equivalence and Borel-Cantelli",
            "Radon-Nikodym Theorem: $\\nu \\ll \\mu$ $\\implies$ $d\\nu = f\\,d\\mu$ for some measurable $f$",
            "Lévy Continuity Theorem: $X_n \\xrightarrow{d} X$ $\\iff$ $\\varphi_{X_n}(t) \\to \\varphi_X(t)$ pointwise and the limit is continuous at $0$",
        ],
        "counterexamples": [
            "a random variable can be $L^1$ but not $L^2$, so $E[X]$ exists but $\\operatorname{Var}(X)=\\infty$ (e.g., Cauchy)",
            "convergence in probability $\\nRightarrow$ almost sure convergence (e.g., sliding hump example)",
            "the conditional expectation $E[X|\\mathcal{G}]$ is defined $P$-almost surely, not pointwise — modifications exist",
        ],
        "applications": [
            "Financial mathematics: change of measure via Girsanov's theorem for option pricing",
            "MCMC convergence diagnostics: $E[g(X_t)] \\to \\int g\\,d\\pi$ for the stationary distribution",
            "Empirical process theory: Donsker's theorem for bootstrapped confidence bands",
        ],
        "skills_count": 4,
    },
    "STA410H1": {
        "name": "Statistical Computation",
        "domain": "stats",
        "difficulty": 4, "units": 5,
        "description": "Statistical algorithms: random variate generation, Monte Carlo, EM algorithm, MCMC, bootstrap.",
        "socratic_topic": "generating random variables from a uniform source",
        "socratic_concept": "inversion sampling: if $U \\sim U(0,1)$, then $X = F^{-1}(U)$ has distribution $F$",
        "deductive_theorem": "Metropolis-Hastings Algorithm",
        "deductive_concept": "accept-reject sampling: $\\alpha(x\\to y) = \\min\\left(1, \\frac{\\pi(y)q(x|y)}{\\pi(x)q(y|x)}\\right)$ gives reversible Markov chain with stationary distribution $\\pi$",
        "correction_error": "burn-in removes the need for MCMC convergence diagnostics",
        "correction_concept": "burn-in reduces initialisation bias but does not guarantee convergence — use Gelman-Rubin $\\hat{R}$ and effective sample size",
        "formulas": [
            "$X = F^{-1}(U)$ — inverse transform sampling",
            "$\\hat{I} = \\frac{1}{n}\\sum_{i=1}^n g(X_i)$ — Monte Carlo estimator, $\\operatorname{Var}(\\hat{I}) = \\sigma_g^2/n$",
            "$\\pi(x|y) = \\frac{\\pi(y|x)\\pi(x)}{\\int \\pi(y|x)\\pi(x)\\,dx}$ — posterior (Bayes' theorem)",
            "$\\theta^{(t+1)} = \\arg\\max_\\theta Q(\\theta|\\theta^{(t)})$, $Q(\\theta|\\theta^{(t)}) = E[\\log L(\\theta; X, Z) | X, \\theta^{(t)}]$ — EM algorithm",
            "$\\hat{R} = \\sqrt{\\frac{\\hat{\\sigma}^2_+}{W}}$ — Gelman-Rubin convergence diagnostic ($\\hat{R} < 1.01$ suggests convergence)",
            "$\\text{ESS} = \\frac{n}{1+2\\sum_{k=1}^\\infty \\rho_k}$ — effective sample size for MCMC",
        ],
        "proofs": [
            "Inversion theorem: $P(F^{-1}(U) \\leq x) = P(U \\leq F(x)) = F(x)$",
            "Metropolis-Hastings satisfies detailed balance: $\\pi(x)P(x\\to y) = \\pi(y)P(y\\to x)$",
            "EM monotonicity: $\\log L(\\theta^{(t+1)}|x) \\geq \\log L(\\theta^{(t)}|x)$",
        ],
        "counterexamples": [
            "rejection sampling can be extremely inefficient when the proposal is far from the target (acceptance rate $\\to 0$)",
            "MCMC on multi-modal distributions can miss modes if chains are not well-mixed",
            "bootstrap fails for extremes (max of sample) — use subsampling instead",
        ],
        "applications": [
            "Bayesian inference via MCMC: posterior sampling for hierarchical models",
            "Importance sampling for rare event estimation in insurance",
            "EM algorithm for Gaussian mixture models (clustering with soft assignments)",
        ],
        "skills_count": 4,
    },
    "STA414H1": {
        "name": "Statistical Methods for Machine Learning II",
        "domain": "stats",
        "difficulty": 5, "units": 5,
        "description": "Advanced ML: deep learning, kernel methods, Gaussian processes, graphical models.",
        "socratic_topic": "the representational power of depth",
        "socratic_concept": "a single hidden layer can approximate any continuous function (universal approximation), but depth allows exponentially more efficient representation",
        "deductive_theorem": "backpropagation as the chain rule",
        "deductive_concept": "$\\frac{\\partial L}{\\partial w_{ij}^{(l)}} = \\frac{\\partial L}{\\partial a_j^{(l)}} \\cdot \\frac{\\partial a_j^{(l)}}{\\partial w_{ij}^{(l)}}$ — the gradient flows backward through the computation graph",
        "correction_error": "Gaussian processes always use the RBF kernel",
        "correction_concept": "the kernel encodes prior assumptions about function smoothness — Matérn kernels allow flexible smoothness control via $\\nu$",
        "formulas": [
            "$a^{(l+1)} = \\sigma(W^{(l)}a^{(l)} + b^{(l)})$ — forward pass of a neural network",
            "$\\frac{\\partial L}{\\partial W^{(l)}} = \\delta^{(l+1)}(a^{(l)})^T$ — backpropagation",
            "$f(x) \\sim GP(m(x), k(x,x'))$ — Gaussian process prior",
            "$p(f_* | X_*, X, y) = N(\\mu_*, \\Sigma_*)$ — GP posterior prediction",
            "$\\text{ELBO} = E_{q_\\phi(z|x)}[\\log p_\\theta(x|z)] - KL(q_\\phi(z|x)\\|p(z))$ — variational autoencoder",
            "$\\theta^{(t+1)} = \\theta^{(t)} - \\eta \\nabla_{\\theta} L$ — gradient descent",
        ],
        "proofs": [
            "Universal approximation theorem: feedforward networks with one hidden layer can approximate any continuous function on compact sets",
            "Backpropagation via multivariate chain rule",
            "Reparameterisation trick: $z = \\mu + \\sigma \\odot \\epsilon$ where $\\epsilon \\sim N(0,I)$ — enables gradient-based VI",
        ],
        "counterexamples": [
            "deep networks can memorise random labels (overparameterisation)",
            "GP with RBF kernel assumes $f$ is infinitely differentiable — inappropriate for discontinuous functions",
            "variational inference underestimates posterior variance (overconfidence)",
        ],
        "applications": [
            "Variational autoencoders for anomaly detection in high-dimensional data",
            "Gaussian process regression for Bayesian optimisation (hyperparameter tuning)",
            "Deep kernel learning: combining neural feature extractors with GP prediction",
        ],
        "skills_count": 4,
    },
    "CSC108H1": {
        "name": "Introduction to Computer Programming",
        "domain": "cs",
        "difficulty": 1, "units": 4,
        "description": "Python programming: data types, control flow, functions, OOP basics, searching, sorting, testing.",
        "socratic_topic": "what is a variable",
        "socratic_concept": "a name that refers to a value — not a box, but a label on a value (Python's object model)",
        "deductive_theorem": "binary search correctness",
        "deductive_concept": "loop invariant: if $x$ is in $A$, then $x \\in A[lo:hi]$ — the search space halves each iteration",
        "correction_error": "$==$ vs $=$ for assignment vs comparison",
        "correction_concept": "$=$ is assignment (binds a name), $==$ is comparison (returns a boolean)",
        "formulas": [
            "$T(n) = O(n)$ — linear search",
            "$T(n) = O(\\log n)$ — binary search (requires sorted input)",
            "$\\text{time} = c \\cdot n$ — linear scaling with input size",
            "$\\text{selection sort: } T(n) = O(n^2)$",
            "$\\text{merge sort: } T(n) = O(n \\log n)$",
        ],
        "proofs": [],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC148H1": {
        "name": "Introduction to Computer Science",
        "domain": "cs",
        "difficulty": 2, "units": 5,
        "description": "ADTs, data structures, recursion, OOP, specifications, algorithm analysis.",
        "socratic_topic": "recursion",
        "socratic_concept": "a function that calls itself on a smaller instance of the same problem — base case + recursive step",
        "deductive_theorem": "induction for recursion correctness",
        "deductive_concept": "prove base case, assume correctness for $n-1$, prove for $n$ — exactly matches recursive structure",
        "correction_error": "infinite recursion — no base case or base case never reached",
        "correction_concept": "every recursive call must move closer to a base case on each invocation",
        "formulas": [
            "$T(n) = T(n-1) + O(1) \\implies T(n) = O(n)$ — linear recursion depth",
            "$T(n) = 2T(n/2) + O(n) \\implies T(n) = O(n \\log n)$ — divide-and-conquer (merge sort)",
            "$T(n) = T(n-1) + T(n-2) + O(1) \\implies T(n) = O(2^n)$ — naive Fibonacci",
        ],
        "proofs": [],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC165H1": {
        "name": "Mathematical Expression and Reasoning for Computer Science",
        "domain": "cs",
        "difficulty": 3, "units": 5,
        "description": "Logic, proof techniques, running time analysis, Big-O, diagonalization, halting problem.",
        "socratic_topic": "the halting problem",
        "socratic_concept": "no program can decide whether another program halts — a diagonalisation proof",
        "deductive_theorem": "Master Theorem for divide-and-conquer recurrences",
        "deductive_concept": "$T(n) = aT(n/b) + f(n)$ — compare $f(n)$ with $n^{\\log_b a}$",
        "correction_error": "confusing $O$ (upper bound) with $\\Theta$ (tight bound)",
        "correction_concept": "$f(n) = O(g(n))$ means $f$ grows no faster than $g$; $f(n) = \\Theta(g(n))$ means $f$ and $g$ grow at the same rate",
        "formulas": [
            "$\\exists c > 0, n_0 > 0: \\forall n \\geq n_0, f(n) \\leq c \\cdot g(n)$ — definition of $f(n) = O(g(n))$",
            "$T(n) = aT(n/b) + f(n)$ — master theorem recurrence",
            "$\\log(n!) = \\Theta(n \\log n)$ — Stirling's approximation",
            "$\\sum_{i=1}^n i = n(n+1)/2 = \\Theta(n^2)$",
            "$\\sum_{i=1}^n i^k = \\Theta(n^{k+1})$ for $k \\geq 0$",
        ],
        "proofs": [
            "Master Theorem: three cases based on whether $f(n)$ is polynomially smaller, equal, or larger than $n^{\\log_b a}$",
            "Halting Problem is undecidable: assume $H(P,I)$ exists, construct $D(P)$ that halts $\\iff$ $P$ does not halt on itself",
        ],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC207H1": {
        "name": "Software Design",
        "domain": "cs",
        "difficulty": 2, "units": 4,
        "description": "OOP design, design patterns, refactoring, software architecture, API design.",
        "socratic_topic": "encapsulation",
        "socratic_concept": "hiding internal state and requiring all interaction through public methods — why information hiding reduces coupling",
        "deductive_theorem": "Liskov Substitution Principle",
        "deductive_concept": "if $S \\leq T$, then objects of type $T$ can be replaced with objects of type $S$ without altering correctness",
        "correction_error": "inheritance overuse — the 'fragile base class' problem",
        "correction_concept": "prefer composition over inheritance: $Has{-}a$ is more flexible than $Is{-}a$",
        "formulas": [],
        "proofs": [],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC209H1": {
        "name": "Software Tools and Systems Programming",
        "domain": "cs",
        "difficulty": 3, "units": 4,
        "description": "C programming, UNIX tools, processes, threads, socket programming.",
        "socratic_topic": "pointers and memory",
        "socratic_concept": "a pointer is a variable that holds a memory address — $*$ dereferences, $\\&$ takes address",
        "deductive_theorem": "producer-consumer with bounded buffer",
        "deductive_concept": "mutex protects the buffer; two semaphores track empty and full slots — $P(\\text{empty})$, $V(\\text{full})$",
        "correction_error": "buffer overflow: assuming input will fit without checking size",
        "correction_concept": "C does not bounds-check arrays — the programmer must ensure $\\text{size} \\leq \\text{capacity}$",
        "formulas": [],
        "proofs": [],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC236H1": {
        "name": "Introduction to the Theory of Computation",
        "domain": "cs",
        "difficulty": 4, "units": 5,
        "description": "Regular languages, context-free languages, Turing machines, decidability, NP-completeness.",
        "socratic_topic": "finite automata and regular languages",
        "socratic_concept": "a DFA has finite memory — $L = \\{0^n1^n : n \\geq 0\\}$ is not regular (pumping lemma)",
        "deductive_theorem": "Pumping Lemma for regular languages",
        "deductive_concept": "if $L$ is regular, then long strings have a repeatable substring: $\\forall w \\in L, |w| \\geq p$, $\\exists xyz = w$ with $y$ pumpable",
        "correction_error": "confusing decidability with recognisability",
        "correction_concept": "decidable: halts on all inputs; recognisable: halts on 'yes', may loop on 'no'; co-recognisable: halts on 'no', may loop on 'yes'",
        "formulas": [
            "$L$ is regular $\\iff$ $\\exists$ DFA $M$ such that $L(M) = L$",
            "$L = \\{a^n b^n : n \\geq 0\\}$ is context-free but not regular",
            "$A_{TM} = \\{\\langle M, w \\rangle : M \\text{ accepts } w\\}$ is undecidable (recognisable but not co-recognisable)",
            "$P = \\{L : L \\text{ can be decided in } O(n^k) \\text{ time for some } k\\}$",
            "$NP = \\{L : L \\text{ has a polynomial-time verifier}\\}$",
        ],
        "proofs": [
            "Pumping Lemma: if DFA has $p$ states, a string of length $\\geq p$ must visit some state twice — the loop can be pumped",
            "Diagonalisation: $A_{TM}$ is undecidable — assume $H$ decides it, construct $D$ that uses $H$ against itself",
            "Cook-Levin Theorem: SAT is NP-complete — encode any NP computation as a CNF formula",
        ],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC263H1": {
        "name": "Data Structures and Analysis",
        "domain": "cs",
        "difficulty": 3, "units": 5,
        "description": "Advanced data structures: balanced trees, hash tables, union-find, graph algorithms, amortized analysis.",
        "socratic_topic": "amortised analysis",
        "socratic_concept": "some operations are expensive but rare — spread the cost across all operations",
        "deductive_theorem": "union-find has amortised $O(\\alpha(n))$ per operation",
        "deductive_concept": "path compression + union by rank give near-constant amortised time — $\\alpha(n)$ is the inverse Ackermann function",
        "correction_error": "hash tables are $O(1)$ worst-case",
        "correction_concept": "$O(1)$ is average-case with good hash and load factor — worst-case is $O(n)$ if many keys collide",
        "formulas": [
            "$T(n) = 2T(n/2) + O(n) \\implies T(n) = O(n \\log n)$ — mergesort",
            "$T(n) = T(n/2) + O(1) \\implies T(n) = O(\\log n)$ — binary search",
            "$\\text{load factor } \\alpha = n/m$ for hash table with $n$ keys, $m$ slots",
            "$\\text{Dijkstra: } O((V+E)\\log V)$ with binary heap",
            "$\\text{Union-Find: } m \\text{ ops } = O(m\\alpha(n))$ amortised",
        ],
        "proofs": [
            "Amortised analysis of dynamic array: doubling strategy gives $O(1)$ amortised per insertion",
            "Potential method for union-find: $\\Phi = \\sum \\log(\\text{size})$",
        ],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC301H1": {
        "name": "Introduction to Software Engineering",
        "domain": "cs",
        "difficulty": 2, "units": 4,
        "description": "Software lifecycle, agile methods, requirements, team project management, CI/CD.",
        "socratic_topic": "requirements engineering",
        "socratic_concept": "what does the client actually need — functional vs non-functional requirements",
        "deductive_theorem": "COCOMO cost estimation model",
        "deductive_concept": "$\\text{effort} = a \\cdot (KLOC)^b$ — empirical model calibrated from historical projects",
        "correction_error": "agile means no planning",
        "correction_concept": "agile is iterative planning — each sprint has a plan, but plans adapt to feedback",
        "formulas": [
            "$\\text{effort} = a \\cdot (KLOC)^b$ — COCOMO basic model",
            "$\\text{schedule} = c \\cdot (\\text{effort})^d$ — COCOMO schedule estimation",
        ],
        "proofs": [],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC311H1": {
        "name": "Introduction to Machine Learning",
        "domain": "cs",
        "difficulty": 4, "units": 5,
        "description": "Supervised/unsupervised learning, neural networks, model selection, optimization, learning theory.",
        "socratic_topic": "the fundamental problem of ML",
        "socratic_concept": "we want $f: X \\to Y$ that minimises expected loss $E[L(f(x), y)]$, but we only have empirical samples",
        "deductive_theorem": "VC-dimension and generalisation",
        "deductive_concept": "with probability $1-\\delta$, the generalisation error is bounded by empirical risk plus $O(\\sqrt{d \\log(n/d)/n})$ where $d$ is VC-dimension",
        "correction_error": "training accuracy measures real-world performance",
        "correction_concept": "training accuracy can be arbitrarily higher than test accuracy (overfitting) — the gap increases with model capacity",
        "formulas": [
            "$R(f) = E[L(f(X), Y)]$ — expected risk",
            "$\\hat{R}(f) = \\frac{1}{n}\\sum L(f(x_i), y_i)$ — empirical risk",
            "$f^* = \\arg\\min_{f \\in \\mathcal{H}} \\hat{R}(f) + \\lambda \\Omega(f)$ — regularised empirical risk minimisation",
            "$\\text{Pr}\\left(|\\hat{R}(f) - R(f)| \\leq \\sqrt{\\frac{d \\log(2n/d)}{n} + \\frac{\\log(1/\\delta)}{2n}}\\right) \\geq 1-\\delta$ — VC-generalisation bound",
            "$\\text{SGD: } \\theta^{(t+1)} = \\theta^{(t)} - \\eta_t \\nabla L(\\theta^{(t)}; x_i, y_i)$",
        ],
        "proofs": [
            "VC-dimension bound via Sauer-Shelah Lemma and symmetrisation",
            "Convergence of SGD for convex $L$: $E[L(\\bar{\\theta}_T)] - L(\\theta^*) \\leq O(1/\\sqrt{T})$",
        ],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC369H1": {
        "name": "Operating Systems",
        "domain": "cs",
        "difficulty": 4, "units": 5,
        "description": "Processes, threads, synchronization, memory management, file systems, I/O.",
        "socratic_topic": "the operating system as resource manager",
        "socratic_concept": "the OS virtualises hardware — each process thinks it has its own CPU, memory, and files",
        "deductive_theorem": "Banker's Algorithm for deadlock avoidance",
        "deductive_concept": "a state is safe if there exists a sequence where all processes can finish with available resources",
        "correction_error": "locking always prevents race conditions",
        "correction_concept": "locks prevent concurrent access but can cause deadlock, livelock, or priority inversion — lock ordering and $\\texttt{lock}()/\\texttt{unlock}()$ pairing matter",
        "formulas": [
            "$\\text{response time} = \\text{wait time} + \\text{service time}$",
            "$\\text{throughput} = \\text{processes completed} / \\text{time}$",
            "$\\text{CPU utilisation} = \\frac{E[\\text{busy}]}{E[\\text{busy}] + E[\\text{idle}]}$",
            "$\\text{page fault rate} = \\frac{\\#\\text{ page faults}}{\\#\\text{ memory accesses}}$",
            "$\\text{effective access time} = (1-p)\\cdot t_{mem} + p\\cdot t_{disk}$",
        ],
        "proofs": [],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
    "CSC373H1": {
        "name": "Algorithm Design and Analysis",
        "domain": "cs",
        "difficulty": 5, "units": 6,
        "description": "Algorithm design paradigms: divide-and-conquer, DP, greedy, network flow, NP-completeness, approximation.",
        "socratic_topic": "optimal substructure",
        "socratic_concept": "the optimal solution to a problem contains optimal solutions to its subproblems — DP or greedy depending on overlap",
        "deductive_theorem": "Max-Flow Min-Cut Theorem",
        "deductive_concept": "the maximum flow value equals the minimum cut capacity — $\\max_{f} |f| = \\min_{S \\subseteq V, s \\in S, t \\notin S} c(S, \\bar{S})$",
        "correction_error": "greedy works whenever the problem has optimal substructure",
        "correction_concept": "optimal substructure is necessary but not sufficient — the greedy choice property (local optimality leads to global optimality) must also hold",
        "formulas": [
            "$\\max_{f} |f| = \\min_{S} c(S, \\bar{S})$ — Max-Flow Min-Cut",
            "$f^* = \\arg\\max \\sum_e f_e$ subject to $0 \\leq f_e \\leq c_e$ and flow conservation",
            "$\\text{OPT}(i, w) = \\max(\\text{OPT}(i-1, w), v_i + \\text{OPT}(i-1, w-w_i))$ — 0/1 knapsack DP",
            "$T(n) = aT(n/b) + f(n)$ — Master Theorem",
            "$\\text{OPT} \\leq \\text{ALG} \\leq \\rho \\cdot \\text{OPT}$ — $\\rho$-approximation algorithm",
        ],
        "proofs": [
            "Max-Flow Min-Cut: augmenting path algorithm terminates at max flow; residual graph's reachable set $S$ from $s$ gives the min cut",
            "Correctness of Dijkstra via induction on distance estimates",
            "NP-completeness of 3-SAT via reduction from CIRCUIT-SAT",
        ],
        "counterexamples": [],
        "applications": [],
        "skills_count": 4,
    },
}

# The 35 program courses (2 already manually done: MAT137Y1, MAT223H1)
COURSES_TO_GENERATE = [
    "MAT224H1", "MAT237Y1", "MAT240H1", "MAT244H1", "MAT247H1",
    "MAT267H1", "MAT301H1", "MAT309H1", "MAT315H1", "MAT334H1",
    "STA130H1", "STA237H1", "STA238H1", "STA257H1", "STA261H1",
    "STA302H1", "STA303H1", "STA304H1", "STA314H1", "STA347H1",
    "STA410H1", "STA414H1",
    "CSC108H1", "CSC148H1", "CSC165H1", "CSC207H1", "CSC209H1",
    "CSC236H1", "CSC263H1", "CSC301H1", "CSC311H1", "CSC369H1",
    "CSC373H1",
]

RICH_COURSES = {"MAT224H1", "MAT237Y1", "MAT244H1", "MAT301H1", "MAT315H1", "MAT334H1"}


def load_data():
    with open(DATA_JSON) as f:
        return json.load(f)


def dir_name(cid, cmeta):
    name_slug = re.sub(r"[^a-z0-9]+", "-", cmeta["name"].lower()).strip("-")
    return cid.lower() + "-" + name_slug


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  \u2713 {os.path.relpath(path, SKILLS_ROOT)}")


def escape_json(s):
    return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\t", "\\t")

def js(s):
    """JSON-encode a string: strip surrounding quotes so result can be embedded in JSON f-strings."""
    return json.dumps(str(s))[1:-1]


# ─── generator functions ──────────────────────────────────────────────────────


def make_skill_md(cid, cmeta, data_entry):
    d = dir_name(cid, cmeta)
    did = cid
    name = cmeta["name"]
    desc = cmeta["description"]
    diff = cmeta["difficulty"]
    sk = len(data_entry["skills"]) if data_entry.get("skills") else cmeta["skills_count"]

    t = f"""---
name: {d}
description: Socratic/deductive/correction teaching modes for UofT {name} ({did}). Use when a student needs help with {desc.lower().rstrip('.')}, or any related topic.
license: MIT
metadata:
  course: {did}
  domain: {cmeta['domain']}
  skill-count: "{sk}"
  difficulty: "{diff}"
  version: "1.0"
---

Socratic discovery · Deductive derivation · Correction attribution · Units: 1–{cmeta['units']}

## Instructions

You are a {did} {name} instructor. When a student invokes this skill, identify the mode they need and follow the corresponding protocol.

### Mode 1 — Socratic Discovery ({cmeta['socratic_topic']})

**Goal:** Guide the student to discover {cmeta['socratic_concept']} through questioning, never by telling the answer directly.

1. Ask: "{cmeta['socratic_topic']} — what do you already understand about this concept? Describe it in your own words."
2. If they give a surface-level answer: "That's a start. Now consider the edge case: what happens when we push this idea to its limit?"
3. Guide them through a concrete example: lead with a simple case, then generalise step by step.
4. Resolution: "You've rediscovered the key insight: {cmeta['socratic_concept']}. The definition captures something you already knew intuitively — it just makes it precise."

Key insight to reinforce: **The definition is a precision tool, not a replacement for intuition.**

### Mode 2 — Deductive Derivation ({cmeta['deductive_theorem']})

**Goal:** Derive {cmeta['deductive_theorem']} logically, never by memorising the formula.

1. Start: "We want to prove {cmeta['deductive_concept']}. Where should we begin?"
2. Ask: "What assumptions are we allowed to make? Write them down."
3. Hint: "Break the problem into pieces. What's the first logical step from the definition?"
4. Lead through: step-by-step from definitions to the theorem, checking each inference for validity.
5. At each step, ask "Why is this step logically valid?" before revealing.
6. Conclusion: Emphasise the **meta-pattern** — the reasoning structure applies to other theorems too.

### Mode 3 — Correction Attribution ({cmeta['correction_error']})

**Goal:** Fix the common error: {cmeta['correction_error']}.

1. Present the error: a typical student makes this mistake.
2. Say: "This is NOT a silly mistake. It reveals a conceptual gap. Let's find it."
3. Ask: "What assumption is this student making that isn't justified?"
4. Let them work through the correct reasoning: {cmeta['correction_concept']}.
5. When they see the gap: "Now you see why the correct understanding matters."
6. Insight: The error comes from over-generalising a pattern that works in simple cases but fails in general.

## Context

This skill covers UofT's {did} — {desc}

## Mode Data Files

Each teaching mode has a companion JSON file with structured step-by-step content (bilingual EN/ZH templates) for programmatic use:

| File | Mode | Content |
|------|------|---------|
| `socratic.json` | Socratic Discovery ({cmeta['socratic_topic']}) | Guided questioning sequence leading to conceptual insight |
| `deductive.json` | Deductive Derivation ({cmeta['deductive_theorem']}) | Step-by-step logical derivation |
| `correction.json` | Correction ({cmeta['correction_error']}) | Pitfall → question → insight → practice cycle |

To load a mode's full structured data: `Read socratic.json` (or deductive.json / correction.json) and follow its `steps` array sequentially, using `template_en` or `template_zh` based on the student's language preference.

## References

All supporting documents are in the `references/` directory:

| File | Purpose | Use When |
|------|---------|----------|
| `formulas.md` | Key formulas, definitions, and computational recipes | Student needs formula lookup |
| `proof-techniques.md` | Common proof patterns and strategies | Student stuck on proof |
| `counterexamples.md` | Classic non-examples organised by concept | Student asks "what if we drop this condition?" |
| `concept-map.md` | Concept dependencies and course overview | Student wants the big picture |
| `checklist.md` | Per-unit progress tracking | Student wants to self-assess |
| `applications.md` | Real-world applications | Student wants motivation beyond theory |

To reference a file during instruction: `See references/formulas.md for the relevant formulas.`

## Skill Taxonomy

The complete {did} skill system has {sk} skills. For detailed level descriptors (L1–L5) and practice strategies, consult `references/checklist.md`.
"""
    return t


def make_socratic_json(cid, cmeta, data_entry):
    flow = data_entry.get("socratic", {}).get("flow", [])
    flow_cn = data_entry.get("socratic", {}).get("flowCn", [])
    entry = data_entry.get("socratic", {}).get("entry", "")

    if flow:
        steps = []
        for i, step in enumerate(flow):
            step_en = step.get("question", "")
            step_hint = step.get("hint", "")
            step_res = step.get("resolution", "")
            step_zh = flow_cn[i].get("question", "") if i < len(flow_cn) else ""
            step_hint_zh = flow_cn[i].get("hint", "") if i < len(flow_cn) else ""
            step_res_zh = flow_cn[i].get("resolution", "") if i < len(flow_cn) else ""

            steps.append(f"""    {{
      "type": "question",
      "template_en": "{escape_json(step_en)}",
      "template_zh": "{escape_json(step_zh)}"
    }},
    {{
      "type": "hint",
      "template_en": "{escape_json(step_hint)}",
      "template_zh": "{escape_json(step_hint_zh)}"
    }},
    {{
      "type": "resolution",
      "template_en": "{escape_json(step_res)}",
      "template_zh": "{escape_json(step_res_zh)}"
    }}""")

        steps_str = ",\n".join(steps)
    else:
        first_skill = (data_entry.get("skills") or [{}])[0]
        s_label = first_skill.get("label", cmeta["socratic_topic"])
        s_desc = first_skill.get("description", cmeta["socratic_concept"])
        s_levels = first_skill.get("levels", [])

        steps_str = f"""    {{
      "type": "question",
      "template_en": "We're exploring {escape_json(s_label)}. Start with what you know: describe it in plain language — as if explaining to someone who has never heard of it.",
      "template_zh": "我们来探索 {escape_json(s_label)}。从你知道的开始：用通俗语言描述它——就像在向从未听说过的人解释。"
    }},
    {{
      "type": "hint",
      "template_en": "Think about a concrete example. What does this concept look like in the simplest possible case?",
      "template_zh": "想一个具体的例子。在最简单的情况下，这个概念是什么样的？"
    }},
    {{
      "type": "resolution",
      "template_en": "Here is the key insight: {escape_json(s_desc)}. The formality generalises what you just described intuitively.",
      "template_zh": "关键洞察是：{escape_json(s_desc)}。形式化定义只是将你刚才直观描述的内容一般化。"
    }},
    {{
      "type": "practice",
      "template_en": "Now apply this understanding: (1) construct an example that illustrates this concept. (2) Construct a non-example that violates it. (3) Explain why the non-example fails.",
      "template_zh": "现在运用这个理解：(1) 构造一个例证来说明这个概念。(2) 构造一个反例来违反它。(3) 解释反例为什么失败。"
    }}"""

    return f"""{{
  "name": "{js(cid)} — Socratic Discovery ({js(cmeta['socratic_topic'])})",
  "description": "Guide the student to discover {js(cmeta['socratic_concept'])} through scaffolded Socratic questioning.",
  "parameters": {{
    "type": "object",
    "properties": {{
      "courseId": {{ "type": "string", "enum": ["{cid}"] }},
      "skillId":  {{ "type": "string", "const": "{cid}-SKILL-S1" }},
      "lang":     {{ "type": "string", "enum": ["en","zh"] }}
    }},
    "required": ["courseId", "skillId", "lang"]
  }},
  "steps": [
{steps_str}
  ],
  "references": [
    "references/formulas.md",
    "references/concept-map.md",
    "references/counterexamples.md",
    "references/checklist.md"
  ],
  "metadata": {{
    "domain": "{cmeta['domain']}",
    "course": "{cid}",
    "skillType": "socratic",
    "difficulty": {cmeta['difficulty']},
    "version": "1.0"
  }}
}}"""


def make_deductive_json(cid, cmeta, data_entry):
    chain = data_entry.get("deductive", {}).get("chain", {})
    chain_cn = data_entry.get("deductive", {}).get("chainCn", {})

    if chain and chain.get("steps"):
        from_en = chain.get("from", "")
        principle_en = chain.get("principle", "")
        steps_en = chain.get("steps", [])
        conclusion_en = chain.get("conclusion", "")

        from_cn = chain_cn.get("from", "") if chain_cn else ""
        principle_cn = chain_cn.get("principle", "") if chain_cn else ""
        steps_cn = chain_cn.get("steps", []) if chain_cn else []
        conclusion_cn = chain_cn.get("conclusion", "") if chain_cn else ""

        # Build steps with Q/H/I/R from chain data
        chain_steps = []
        chain_steps.append(f"""    {{
      "type": "question",
      "template_en": "We start from: {escape_json(from_en)}. {escape_json(principle_en)} What is the first logical step?",
      "template_zh": "我们从 {escape_json(from_cn if from_cn else from_en)} 出发。{escape_json(principle_cn if principle_cn else principle_en)} 第一步逻辑推理是什么？"
    }}""")
        chain_steps.append(f"""    {{
      "type": "hint",
      "template_en": "Begin from the definitions. What is the first logical consequence we can derive?",
      "template_zh": "从定义出发。我们能推导出的第一个逻辑结果是什么？"
    }}""")

        steps_text_en = " ".join(steps_en)
        steps_text_cn = " ".join(steps_cn) if steps_cn else steps_text_en
        chain_steps.append(f"""    {{
      "type": "insight",
      "template_en": "Step by step: {escape_json(steps_text_en)}",
      "template_zh": "逐步推导：{escape_json(steps_text_cn)}"
    }}""")
        chain_steps.append(f"""    {{
      "type": "resolution",
      "template_en": "Therefore, {escape_json(conclusion_en)} Every step followed logically from definitions — no leaps of faith.",
      "template_zh": "因此，{escape_json(conclusion_cn if conclusion_cn else conclusion_en)} 每一步都逻辑地跟随定义——没有跳跃。"
    }}""")
        chain_steps.append(f"""    {{
      "type": "practice",
      "template_en": "Variant: what changes if we modify one of the assumptions? Does the theorem still hold? Construct a counterexample to test the boundary.",
      "template_zh": "变体：如果我们修改其中一个假设，会改变什么？定理是否仍然成立？构造一个反例来测试边界。"
    }}""")
        steps_str = ",\n".join(chain_steps)
    else:
        first_skill = (data_entry.get("skills") or [{}])[0]
        d_label = first_skill.get("label", cmeta["deductive_theorem"])
        d_desc = first_skill.get("description", cmeta["deductive_concept"])

        steps_str = f"""    {{
      "type": "question",
      "template_en": "We want to show that {escape_json(cmeta['deductive_theorem'])}. What are the definitions we need? Write them down.",
      "template_zh": "我们要证明 {escape_json(cmeta['deductive_theorem'])}。需要哪些定义？写下来。"
    }},
    {{
      "type": "hint",
      "template_en": "Begin from the definitions. What is the first logical consequence we can derive?",
      "template_zh": "从定义出发。我们能推导出的第一个逻辑结果是什么？"
    }},
    {{
      "type": "insight",
      "template_en": "The key move is: {escape_json(cmeta['deductive_concept'])}. This connects what we assumed to what we want to prove.",
      "template_zh": "关键步骤是：{escape_json(cmeta['deductive_concept'])}。这连接了我们的假设和目标证明。"
    }},
    {{
      "type": "resolution",
      "template_en": "Therefore, {escape_json(cmeta['deductive_theorem'])}. Every step followed logically from definitions — no leaps of faith. The structure of this proof is a pattern you can apply in other contexts.",
      "template_zh": "因此，{escape_json(cmeta['deductive_theorem'])}。每一步都逻辑地跟随定义——没有跳跃。这个证明的结构是一种可以在其他情境中应用的模式。"
    }},
    {{
      "type": "practice",
      "template_en": "Variant: what changes if we modify one of the assumptions? Does the theorem still hold? Construct a counterexample to test the boundary.",
      "template_zh": "变体：如果我们修改其中一个假设，会改变什么？定理是否仍然成立？构造一个反例来测试边界。"
    }}"""

    return f"""{{
  "name": "{js(cid)} — Deductive Derivation ({js(cmeta['deductive_theorem'])})",
  "description": "Derive {js(cmeta['deductive_theorem'])} step by logical step.",
  "parameters": {{
    "type": "object",
    "properties": {{
      "courseId": {{ "type": "string", "enum": ["{cid}"] }},
      "skillId":  {{ "type": "string", "const": "{cid}-SKILL-D1" }},
      "lang":     {{ "type": "string", "enum": ["en","zh"] }}
    }},
    "required": ["courseId", "skillId", "lang"]
  }},
  "steps": [
{steps_str}
  ],
  "references": [
    "references/formulas.md",
    "references/proof-techniques.md",
    "references/concept-map.md"
  ],
  "metadata": {{
    "domain": "{cmeta['domain']}",
    "course": "{cid}",
    "skillType": "deductive",
    "difficulty": {cmeta['difficulty']},
    "version": "1.0"
  }}
}}"""


def make_correction_json(cid, cmeta, data_entry):
    pair = data_entry.get("correction", {}).get("pair", {})
    pair_cn = data_entry.get("correction", {}).get("pairCn", {})

    if pair and pair.get("pitfall"):
        pitfall_en = pair.get("pitfall", "")
        socratic_q_en = pair.get("socraticQuestion", "")
        insight_en = pair.get("insight", "")

        pitfall_cn = pair_cn.get("pitfall", "") if pair_cn else ""
        socratic_q_cn = pair_cn.get("socraticQuestion", "") if pair_cn else ""
        insight_cn = pair_cn.get("insight", "") if pair_cn else ""

        steps_str = f"""    {{
      "type": "pitfall",
      "template_en": "Common error: {escape_json(pitfall_en)} This mistake is natural — it comes from over-generalising a pattern that works in simpler cases.",
      "template_zh": "常见错误：{escape_json(pitfall_cn if pitfall_cn else pitfall_en)}。这个错误很自然——它来自于过度泛化一个在简单情况下有效的模式。"
    }},
    {{
      "type": "question",
      "template_en": "Let's test your understanding. {escape_json(socratic_q_en)} Work through the problem carefully. What assumption did you just make? Is it justified?",
      "template_zh": "让我们测试你的理解。{escape_json(socratic_q_cn if socratic_q_cn else socratic_q_en)} 仔细解题。你刚才做了什么假设？这个假设合理吗？"
    }},
    {{
      "type": "insight",
      "template_en": "The correct reasoning: {escape_json(insight_en)} The subtlety is that intuition from elementary cases doesn't always carry over.",
      "template_zh": "正确的推理是：{escape_json(insight_cn if insight_cn else insight_en)}。微妙之处在于，从初等情况得到的直觉并不总是能推广。"
    }},
    {{
      "type": "practice",
      "template_en": "Find where this error appears in the wild: (1) search your work for this pattern. (2) Correct it. (3) Explain to a peer why the correction matters.",
      "template_zh": "找出这个错误出现在你之前作业中的位置：(1) 在你的作业中搜索这个模式。(2) 修正它。(3) 向同学解释为什么这个修正很重要。"
    }}"""
    else:
        first_skill = (data_entry.get("skills") or [{}])[0]
        c_desc = first_skill.get("description", cmeta["correction_concept"])
        c_error = cmeta["correction_error"]

        steps_str = f"""    {{
      "type": "pitfall",
      "template_en": "Common error: {escape_json(c_error)}. This mistake is natural — it comes from over-generalising a pattern that works in simpler cases.",
      "template_zh": "常见错误：{escape_json(c_error)}。这个错误很自然——它来自于过度泛化一个在简单情况下有效的模式。"
    }},
    {{
      "type": "question",
      "template_en": "Let's test your understanding with a concrete example. Work through the problem carefully. What assumption did you just make? Is it justified?",
      "template_zh": "让我们用一个具体的例子测试你的理解。仔细解题。你刚才做了什么假设？这个假设合理吗？"
    }},
    {{
      "type": "insight",
      "template_en": "The correct reasoning: {escape_json(cmeta['correction_concept'])}. The subtlety is that intuition from elementary cases doesn't always carry over.",
      "template_zh": "正确的推理是：{escape_json(cmeta['correction_concept'])}。微妙之处在于，从初等情况得到的直觉并不总是能推广。"
    }},
    {{
      "type": "practice",
      "template_en": "Find where this error appears in the wild: (1) search your work for this pattern. (2) Correct it. (3) Explain to a peer why the correction matters.",
      "template_zh": "找出这个错误出现在你之前作业中的位置：(1) 在你的作业中搜索这个模式。(2) 修正它。(3) 向同学解释为什么这个修正很重要。"
    }}"""

    return f"""{{
  "name": "{js(cid)} — Correction ({js(cmeta['correction_error'])})",
  "description": "Fix the common conceptual error: {js(cmeta['correction_error'])}.",
  "parameters": {{
    "type": "object",
    "properties": {{
      "courseId": {{ "type": "string", "enum": ["{cid}"] }},
      "skillId":  {{ "type": "string", "const": "{cid}-SKILL-C1" }},
      "lang":     {{ "type": "string", "enum": ["en","zh"] }}
    }},
    "required": ["courseId", "skillId", "lang"]
  }},
  "steps": [
{steps_str}
  ],
  "references": [
    "references/formulas.md",
    "references/counterexamples.md",
    "references/checklist.md"
  ],
  "metadata": {{
    "domain": "{cmeta['domain']}",
    "course": "{cid}",
    "skillType": "correction",
    "difficulty": {cmeta['difficulty']},
    "version": "1.0"
  }}
}}"""


# ─── references ─────────────────────────────────────────────────────────────


def make_formulas_md(cid, cmeta):
    lines = [f"# {cid} — 关键公式速查\n"]
    for f in cmeta.get("formulas", []):
        lines.append(f"- {f}")
    return "\n".join(lines) + "\n"


def make_proofs_md(cid, cmeta):
    lines = [f"# {cid} — 证明技巧指南\n"]
    for p in cmeta.get("proofs", []):
        lines.append(f"- {p}")
    if not cmeta.get("proofs"):
        lines.append("  *（本课程以应用和编程为主，形式化和推演较少）*")
    return "\n".join(lines) + "\n"


def make_counterexamples_md(cid, cmeta):
    lines = [f"# {cid} — 反例速查手册\n"]
    for ex in cmeta.get("counterexamples", []):
        lines.append(f"- ${ex}$")
    if not cmeta.get("counterexamples"):
        lines.append("  *（反例取决于具体的解题上下文）*")
    return "\n".join(lines) + "\n"


def make_concept_map_md(cid, cmeta):
    return f"""# {cid} — 概念联通图

## 核心主题

{cmeta['description']}

## 循序渐进

1. **概念理解** — 掌握定义和术语
2. **计算能力** — 熟练运用公式
3. **理论洞察** — 理解定理之间的关联
4. **综合应用** — 跨章节解决问题

> 详细的概念依赖图请参考主项目的 knowledge graph。
"""


def make_checklist_md(cid, cmeta, data_entry):
    skills = data_entry.get("skills", [])
    t = f"""# {cid} 学习检查清单

> 逐步勾选，追踪学习进度

## 基础理解
- [ ] 理解课程的核心概念和术语
- [ ] 能用自己的语言解释关键定义
- [ ] 能识别概念在不同上下文中的表现形式

## 计算与应用
- [ ] 能正确应用公式进行计算
- [ ] 能选择合适的工具解决具体问题
- [ ] 能解释计算结果的含义

## 理论层面
- [ ] 理解重要定理的陈述和条件
- [ ] 能复述定理证明的关键步骤
- [ ] 能将定理应用于新情境

## 技能自评

在对应单元格打 ✓：

| 核心概念 | L1 理解 | L2 识别 | L3 应用 | L4 掌握 | L5 精通 |
|----------|---------|---------|---------|---------|---------|
"""
    topics = []
    for skill in skills[:5]:
        label = skill.get("label", "")
        topics.append(f"  {label} | ☐ | ☐ | ☐ | ☐ | ☐ |")
    if not topics and cmeta.get("formulas"):
        for formula in cmeta["formulas"][:5]:
            label = formula.split("—")[-1].strip(" $") if "—" in formula else formula[:40]
            topics.append(f"  {label} | ☐ | ☐ | ☐ | ☐ | ☐ |")
    return t + "\n".join(topics) + "\n"


def make_applications_md(cid, cmeta):
    lines = [f"# {cid} — 实际应用\n"]
    for a in cmeta.get("applications", []):
        lines.append(f"- ${a}$")
    if not cmeta.get("applications"):
        lines.append("  *（具体应用取决于课程内容和学生兴趣）*")
    return "\n".join(lines) + "\n"


def make_readme_md(cid, cmeta):
    d = dir_name(cid, cmeta)
    domain_label = {"math": "Math", "stats": "Stats", "cs": "CS"}.get(cmeta["domain"], "")
    credit = "Full Year" if "Y" in cid else "Half"
    return f"""# {cid} — {cmeta['name']}

UofT · {domain_label} · {credit} Credit

## About

This skill package provides three teaching modes for mastering {cid}:

| Mode | File | Description |
|------|------|-------------|
| Socratic | `socratic.json` | Guided discovery of {cmeta['socratic_topic']} |
| Deductive | `deductive.json` | Step-by-step derivation of {cmeta['deductive_theorem']} |
| Correction | `correction.json` | Fixing the error: {cmeta['correction_error']} |

Each mode is also documented in `SKILL.md` as the Anthropic Skills entry point.

## Installation

**Claude Code / OpenCode:**
```
cp -r skills/{cmeta['domain']}/{d} ~/.claude/skills/
```
or for OpenCode:
```
cp -r skills/{cmeta['domain']}/{d} ~/.opencode/agent/skills/
```

Restart your agent, then invoke:
```
agent run skills/{cmeta['domain']}/{d}/SKILL.md
```

## References

All supporting documents are in `references/`.

## License

See `LICENSE` file.
"""


# ─── main ────────────────────────────────────────────────────────────────────


def main():
    data = load_data()

    for cid in COURSES_TO_GENERATE:
        cmeta = COURSE_META[cid]
        data_entry = data.get(cid, {})
        d = dir_name(cid, cmeta)
        dom = cmeta["domain"]
        base = os.path.join(SKILLS_ROOT, dom, d)
        ref_dir = os.path.join(base, "references")

        print(f"\n{'=' * 60}")
        print(f"Generating {cid} — {cmeta['name']}")
        print(f"  → {os.path.relpath(base, SKILLS_ROOT)}/")

        write_file(os.path.join(base, "SKILL.md"), make_skill_md(cid, cmeta, data_entry))
        write_file(os.path.join(base, "socratic.json"), make_socratic_json(cid, cmeta, data_entry))
        write_file(os.path.join(base, "deductive.json"), make_deductive_json(cid, cmeta, data_entry))
        write_file(os.path.join(base, "correction.json"), make_correction_json(cid, cmeta, data_entry))
        write_file(os.path.join(base, "README.md"), make_readme_md(cid, cmeta))
        write_file(os.path.join(base, "LICENSE"), LICENSE_TEXT)

        write_file(os.path.join(ref_dir, "formulas.md"), make_formulas_md(cid, cmeta))
        write_file(os.path.join(ref_dir, "proof-techniques.md"), make_proofs_md(cid, cmeta))
        write_file(os.path.join(ref_dir, "counterexamples.md"), make_counterexamples_md(cid, cmeta))
        write_file(os.path.join(ref_dir, "concept-map.md"), make_concept_map_md(cid, cmeta))
        write_file(os.path.join(ref_dir, "checklist.md"), make_checklist_md(cid, cmeta, data_entry))
        write_file(os.path.join(ref_dir, "applications.md"), make_applications_md(cid, cmeta))

    update_skill_json(data)

    print(f"\n{'=' * 60}")
    print(f"Done! {len(COURSES_TO_GENERATE)} skill packages generated.")
    print("Locations: skills/math/, skills/stats/, skills/cs/")


def update_skill_json(data):
    path = os.path.join(SKILLS_ROOT, "skill.json")
    with open(path) as f:
        sj = json.load(f)

    existing = [s for s in sj["skills"] if s["courseId"] not in COURSE_META]

    for cid in COURSES_TO_GENERATE:
        cmeta = COURSE_META[cid]
        d = dir_name(cid, cmeta)
        dom = cmeta["domain"]
        prefix = f"{dom}/{d}/"
        existing.append({
            "id": f"{cid}-SKILL-S1",
            "courseId": cid,
            "mode": "socratic",
            "file": f"{prefix}socratic.json"
        })
        existing.append({
            "id": f"{cid}-SKILL-D1",
            "courseId": cid,
            "mode": "deductive",
            "file": f"{prefix}deductive.json"
        })
        existing.append({
            "id": f"{cid}-SKILL-C1",
            "courseId": cid,
            "mode": "correction",
            "file": f"{prefix}correction.json"
        })

    sj["skills"] = sorted(existing, key=lambda x: x["courseId"])
    with open(path, "w") as f:
        json.dump(sj, f, indent=2)
    print(f"\n  ✓ skill.json updated ({len(sj['skills'])} total skill entries)")


if __name__ == "__main__":
    main()
