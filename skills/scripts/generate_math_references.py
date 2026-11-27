#!/usr/bin/env python3
"""
Generate full, course-specific reference files for all 12 math skill packages.
- Reads knowledge graph JSON from course-ontology/ for per-course node/edge data
- Reads course skills from course_skills_data.json
- Generates 6 detailed reference files + copies knowledge graph JSON
- Matches MAT137Y1 template depth (60-120 lines per file)
"""

import json, os, shutil

SKILLS_DIR = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/skills"
DATA_PATH = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/scripts/course_skills_data.json"
ONTOLOGY_DIR = "/Users/christinaxiang/Library/Mobile Documents/com~apple~CloudDocs/Documents/uoft-kg/course-ontology"

with open(DATA_PATH) as f:
    skills_data = json.load(f)

# ── Course definitions ──────────────────────────────────────────────────

COURSES = {
    "MAT137Y1": {"name": "Calculus with Proofs", "dir": "mat137y1-calculus-with-proofs", "domain": "calculus"},
    "MAT223H1": {"name": "Linear Algebra I", "dir": "mat223h1-linear-algebra-i", "domain": "linear-algebra"},
    "MAT224H1": {"name": "Linear Algebra II", "dir": "mat224h1-linear-algebra-ii", "domain": "linear-algebra"},
    "MAT237Y1": {"name": "Multivariable Calculus with Proofs", "dir": "mat237y1-multivariable-calculus-with-proofs", "domain": "multivariable-calculus"},
    "MAT240H1": {"name": "Algebra I", "dir": "mat240h1-algebra-i", "domain": "abstract-algebra"},
    "MAT244H1": {"name": "Introduction to ODEs", "dir": "mat244h1-introduction-to-ordinary-differential-equations", "domain": "odes"},
    "MAT247H1": {"name": "Algebra II", "dir": "mat247h1-algebra-ii", "domain": "abstract-algebra"},
    "MAT267H1": {"name": "Advanced ODEs", "dir": "mat267h1-advanced-ordinary-differential-equations", "domain": "odes"},
    "MAT301H1": {"name": "Groups and Symmetries", "dir": "mat301h1-groups-and-symmetries", "domain": "abstract-algebra"},
    "MAT309H1": {"name": "Introduction to Mathematical Logic", "dir": "mat309h1-introduction-to-mathematical-logic", "domain": "logic"},
    "MAT315H1": {"name": "Introduction to Number Theory", "dir": "mat315h1-introduction-to-number-theory", "domain": "number-theory"},
    "MAT334H1": {"name": "Complex Variables", "dir": "mat334h1-complex-variables", "domain": "complex-analysis"},
}

# ── Content generators ──────────────────────────────────────────────────

def get_skills(cid):
    entry = skills_data.get(cid, {})
    return entry.get("skills", [])

def get_graph(cid):
    path = os.path.join(ONTOLOGY_DIR, f"{cid}-knowledge-graph.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

def formulas_md(cid, course):
    """Generate ~80-100 line course-specific formulas."""
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 关键公式速查\n"]
    domain_lines = {
        "calculus": [
            "## 一、极限与连续",
            "",
            "| 概念 | 公式 | 条件 |",
            "|------|------|------|",
            "| 极限定义 | $\\lim_{x\\to a} f(x) = L \\iff \\forall\\varepsilon>0,\\;\\exists\\delta>0$ 使得 $0<|x-a|<\\delta \\Rightarrow |f(x)-L|<\\varepsilon$ | $f$ 在 $a$ 附近有定义 |",
            "| 夹逼定理 | 若 $g(x)\\le f(x)\\le h(x)$ 且 $\\lim g = \\lim h = L$，则 $\\lim f = L$ | 在 $a$ 的去心邻域内 |",
            "| 连续定义 | $\\lim_{x\\to a} f(x) = f(a)$ | $f$ 在 $a$ 处有定义 |",
            "| IVT | 若 $f\\in C[a,b]$ 且 $y$ 介于 $f(a),f(b)$ 之间，则 $\\exists c\\in(a,b): f(c)=y$ | $f$ 在闭区间连续 |",
            "| EVT | 若 $f\\in C[a,b]$，则 $f$ 在 $[a,b]$ 上取得最大值和最小值 | $f$ 在闭区间连续 |",
            "",
            "## 二、微分学",
            "",
            "| 规则 | 公式 |",
            "|------|------|",
            "| 导数定义 | $f'(a) = \\lim_{h\\to 0} \\frac{f(a+h)-f(a)}{h}$ |",
            "| 乘积法则 | $(fg)' = f'g + fg'$ |",
            "| 链式法则 | $(f\\circ g)'(x) = f'(g(x))\\,g'(x)$ |",
            "| 商法则 | $(f/g)' = (f'g - fg')/g^2$ |",
            "| MVT | $f(b)-f(a) = f'(c)(b-a)$ 对某 $c\\in(a,b)$ | $f$ 在 $[a,b]$ 连续，$(a,b)$ 可导 |",
            "| L'Hôpital | $\\lim\\frac{f}{g} = \\lim\\frac{f'}{g'}$ 若 $0/0$ 或 $\\pm\\infty/\\pm\\infty$ | 极限存在且 $g'(x)\\neq0$ |",
            "",
            "## 三、积分学",
            "",
            "| 定理 | 公式 |",
            "|------|------|",
            "| FTC I | $\\frac{d}{dx}\\int_a^x f(t)\\,dt = f(x)$ | $f$ 连续 |",
            "| FTC II | $\\int_a^b f(x)\\,dx = F(b)-F(a)$ | $F' = f$ |",
            "| 分部积分 | $\\int u\\,dv = uv - \\int v\\,du$ |",
            "| 换元法 | $\\int_a^b f(g(x))g'(x)\\,dx = \\int_{g(a)}^{g(b)} f(u)\\,du$ |",
            "",
            "## 四、级数",
            "",
            "| 测试 | 条件 | 结论 |",
            "|------|------|------|",
            "| 比值法 | $\\lim |a_{n+1}/a_n| = L$ | $L<1$ 收敛，$L>1$ 发散 |",
            "| 根值法 | $\\lim \\sqrt[n]{|a_n|} = L$ | $L<1$ 收敛，$L>1$ 发散 |",
            "| 交错级数 | $b_n\\searrow 0$ | $\\sum (-1)^n b_n$ 收敛 |",
            "| 积分法 | $\\int_1^\\infty f(x)\\,dx$ 收敛 | $\\sum f(n)$ 收敛 |",
            "| p-级数 | $\\sum 1/n^p$ | $p>1$ 收敛，$p\\le 1$ 发散 |",
            "",
            "## 五、泰勒展开",
            "",
            "| 函数 | 麦克劳林展开 | 收敛域 |",
            "|------|------------|--------|",
            "| $e^x$ | $\\sum_{n=0}^\\infty x^n/n!$ | $\\mathbb{R}$ |",
            "| $\\sin x$ | $\\sum_{n=0}^\\infty (-1)^n x^{2n+1}/(2n+1)!$ | $\\mathbb{R}$ |",
            "| $\\cos x$ | $\\sum_{n=0}^\\infty (-1)^n x^{2n}/(2n)!$ | $\\mathbb{R}$ |",
            "| $\\ln(1+x)$ | $\\sum_{n=1}^\\infty (-1)^{n-1} x^n/n$ | $(-1,1]$ |",
            "| $(1+x)^\\alpha$ | $\\sum_{n=0}^\\infty \\binom{\\alpha}{n} x^n$ | $(-1,1)$ |",
        ],
        "linear-algebra": [
            "## 一、向量空间",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 向量空间 | 集合 $V$ 配加法和标量乘法，满足 8 条公理 |",
            "| 子空间 | $U\\subseteq V$ 对加法和标量乘法封闭 |",
            "| 张成 | $\\operatorname{span}(S) = \\{\\sum a_i v_i : v_i\\in S\\}$ |",
            "| 线性无关 | $\\sum a_i v_i = 0 \\Rightarrow$ 所有 $a_i = 0$ |",
            "| 基 | 线性无关的张成集 |",
            "| 维数 | $\\dim V = $ 基中向量个数 |",
            "",
            "## 二、线性变换",
            "",
            "| 概念 | 定义 | 矩阵表示 |",
            "|------|------|---------|",
            "| 线性变换 | $T(u+v)=T(u)+T(v)$, $T(cv)=cT(v)$ | $[T] \\in \\mathbb{F}^{m\\times n}$ |",
            "| 核 | $\\ker T = \\{v: T(v)=0\\}$ | $\\operatorname{null}(A)$ |",
            "| 像 | $\\operatorname{im} T = \\{T(v): v\\in V\\}$ | $\\operatorname{col}(A)$ |",
            "| 秩-零化度 | $\\dim V = \\dim\\ker T + \\dim\\operatorname{im} T$ | $n = \\operatorname{nullity} + \\operatorname{rank}$ |",
            "",
            "## 三、内积空间",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 内积 | $\\langle u,v\\rangle$ 满足线性、对称、正定 |",
            "| 范数 | $\\|v\\| = \\sqrt{\\langle v,v\\rangle}$ |",
            "| 正交 | $\\langle u,v\\rangle = 0$ |",
            "| Gram-Schmidt | $u_k = v_k - \\sum_{i<k} \\frac{\\langle v_k,u_i\\rangle}{\\|u_i\\|^2} u_i$ |",
            "| 投影 | $\\operatorname{proj}_U(v) = \\sum_i \\frac{\\langle v,u_i\\rangle}{\\|u_i\\|^2} u_i$ |",
            "",
            "## 四、特征值与对角化",
            "",
            "| 概念 | 公式 |",
            "|------|------|",
            "| 特征值 | $Av = \\lambda v$ 等价于 $\\det(A-\\lambda I)=0$ |",
            "| 特征多项式 | $\\chi_A(\\lambda) = \\det(A-\\lambda I)$ |",
            "| 代数重数 | $m_a(\\lambda)$ = 特征多项式中的重数 |",
            "| 几何重数 | $m_g(\\lambda)$ = $\\dim\\ker(A-\\lambda I)$ |",
            "| 可对角化 | $m_g(\\lambda) = m_a(\\lambda)$ 对所有 $\\lambda$ |",
            "| 谱分解 | $A = Q\\Lambda Q^T$（实对称矩阵）|",
        ],
        "abstract-algebra": [
            "## 一、群论",
            "",
            "| 概念 | 定义 | 例子 |",
            "|------|------|------|",
            "| 群 | 集合 $G$ 配二元运算，满足封闭、结合、单位元、逆元 | $\\mathbb{Z}, S_n, GL_n(\\mathbb{R})$ |",
            "| 子群 | $H\\subseteq G$ 对运算封闭 | $n\\mathbb{Z}, A_n$ |",
            "| 陪集 | $gH = \\{gh: h\\in H\\}$ |",
            "| 正规子群 | $gHg^{-1} = H$ 对所有 $g\\in G$ | $\\ker\\varphi$ |",
            "| 商群 | $G/N = \\{gN: g\\in G\\}$ |",
            "| 同态 | $\\varphi(ab) = \\varphi(a)\\varphi(b)$ |",
            "| 同构定理 | $G/\\ker\\varphi \\cong \\operatorname{im}\\varphi$ |",
            "",
            "## 二、环论",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 环 | $(R,+,\\cdot)$ 对加法是群，乘法满足结合律和分配律 |",
            "| 域 | 交换环且每个非零元有乘法逆 |",
            "| 理想 | $I\\subseteq R$ 对加法子群且 $rI\\subseteq I$ 对所有 $r\\in R$ |",
            "| 商环 | $R/I$ |",
            "| 整环 | 无零因子的交换环 |",
            "",
            "## 三、模论",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 模 | 环上的向量空间（加法群 + 标量乘法）|",
            "| 子模 | 对加法和标量乘法封闭的子集 |",
            "| 商模 | $M/N$ |",
            "| 自由模 | 有基的模 |",
            "| 结构定理 | 有限生成 $\\mathbb{F}[x]$-模分解为循环子模直和 |",
        ],
        "multivariable-calculus": [
            "## 一、多元函数",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 偏导数 | $\\frac{\\partial f}{\\partial x_i}(a) = \\lim_{h\\to 0} \\frac{f(a+he_i)-f(a)}{h}$ |",
            "| 梯度 | $\\nabla f = (\\partial f/\\partial x_1, \\ldots, \\partial f/\\partial x_n)$ |",
            "| 方向导数 | $D_v f(a) = \\nabla f(a)\\cdot v$ |",
            "| 可微 | $f(a+h) = f(a) + \\nabla f(a)\\cdot h + o(\\|h\\|)$ |",
            "| Jacobian | $J_f = [\\partial f_i/\\partial x_j]$ |",
            "| Hessian | $H_f = [\\partial^2 f/\\partial x_i\\partial x_j]$ |",
            "",
            "## 二、多元积分",
            "",
            "| 定理 | 公式 |",
            "|------|------|",
            "| Fubini | $\\iint_{[a,b]\\times[c,d]} f = \\int_a^b\\int_c^d f(x,y)\\,dy\\,dx$ |",
            "| 换元 | $\\int_{\\varphi(U)} f = \\int_U (f\\circ\\varphi)|\\det D\\varphi|$ |",
            "| Green | $\\oint_{\\partial D} P\\,dx+Q\\,dy = \\iint_D (Q_x-P_y)\\,dx\\,dy$ |",
            "| Stokes | $\\int_{\\partial M} \\omega = \\int_M d\\omega$ |",
            "| Divergence | $\\iiint_V \\nabla\\cdot\\mathbf{F}\\,dV = \\iint_{\\partial V} \\mathbf{F}\\cdot\\mathbf{n}\\,dS$ |",
            "",
            "## 三、极值",
            "",
            "| 方法 | 条件 |",
            "|------|------|",
            "| 临界点 | $\\nabla f(a) = 0$ |",
            "| 鞍点判别 | $H_f$ 不定 |",
            "| Lagrange 乘数 | $\\nabla f = \\lambda\\nabla g$（约束 $g=0$）|",
            "| 二阶判别 | $H_f$ 正定→极小，负定→极大 |",
        ],
        "odes": [
            "## 一、一阶 ODE",
            "",
            "| 类型 | 标准形 | 解法 |",
            "|------|--------|------|",
            "| 可分离 | $dy/dx = g(x)h(y)$ | $\\int dy/h(y) = \\int g(x)\\,dx$ |",
            "| 线性 | $dy/dx + p(x)y = q(x)$ | $\\mu = e^{\\int p\\,dx}$, $y = \\frac{1}{\\mu}\\int \\mu q\\,dx$ |",
            "| 恰当 | $M\\,dx + N\\,dy = 0$, $M_y = N_x$ | $F = \\int M\\,dx + \\int (N-\\partial/\\partial y\\int M\\,dx)\\,dy$ |",
            "| Bernoulli | $y' + p(x)y = q(x)y^n$ | $u = y^{1-n}$ 化为线性 |",
            "",
            "## 二、高阶线性 ODE",
            "",
            "| 情形 | 通解 |",
            "|------|------|",
            "| 常系数齐次 | $y = \\sum c_i e^{\\lambda_i x}$（特征根 $\\lambda_i$）|",
            "| 重根 | $y = (c_1 + c_2 x + \\ldots)e^{\\lambda x}$ |",
            "| 复根 | $y = e^{\\alpha x}(c_1\\cos\\beta x + c_2\\sin\\beta x)$ |",
            "| 非齐次（待定系数）| $y_p = $ 与 $f(x)$ 同形式 |",
            "| 非齐次（参数变易）| $y_p = \\int G(x,t)f(t)\\,dt$ |",
            "",
            "## 三、Laplace 变换",
            "",
            "| 函数 | 变换 |",
            "|------|------|",
            "| $1$ | $1/s$ |",
            "| $t^n$ | $n!/s^{n+1}$ |",
            "| $e^{at}$ | $1/(s-a)$ |",
            "| $\\sin(at)$ | $a/(s^2+a^2)$ |",
            "| $\\cos(at)$ | $s/(s^2+a^2)$ |",
            "| $f'(t)$ | $sF(s)-f(0)$ |",
            "",
            "## 四、相平面与稳定性",
            "",
            "| 特征值 | 平衡点类型 | 稳定性 |",
            "|--------|----------|--------|",
            "| 实, 同号 | 结点 | 负→稳定，正→不稳定 |",
            "| 实, 异号 | 鞍点 | 不稳定 |",
            "| 复, Re<0 | 稳定螺线 | 渐近稳定 |",
            "| 复, Re>0 | 不稳定螺线 | 不稳定 |",
            "| 纯虚 | 中心 | Lyapunov 稳定 |",
        ],
        "complex-analysis": [
            "## 一、复变函数基础",
            "",
            "| 概念 | 公式 |",
            "|------|------|",
            "| 复数 | $z = x + iy = re^{i\\theta}$ |",
            "| 共轭 | $\\bar{z} = x - iy = re^{-i\\theta}$ |",
            "| 模 | $|z| = \\sqrt{x^2 + y^2}$ |",
            "| 辐角 | $\\arg z = \\theta$ |",
            "| Cauchy-Riemann | $u_x = v_y$, $u_y = -v_x$ |",
            "",
            "## 二、复积分",
            "",
            "| 定理 | 公式 | 条件 |",
            "|------|------|------|",
            "| Cauchy 积分定理 | $\\oint_\\gamma f(z)\\,dz = 0$ | $f$ 在单连通域解析 |",
            "| Cauchy 积分公式 | $f(a) = \\frac{1}{2\\pi i}\\oint_\\gamma \\frac{f(z)}{z-a}\\,dz$ | $f$ 解析，$a$ 在 $\\gamma$ 内 |",
            "| 导数公式 | $f^{(n)}(a) = \\frac{n!}{2\\pi i}\\oint_\\gamma \\frac{f(z)}{(z-a)^{n+1}}\\,dz$ | $f$ 解析 |",
            "",
            "## 三、级数展开",
            "",
            "| 展开 | 公式 | 收敛域 |",
            "|------|------|--------|",
            "| Taylor | $f(z) = \\sum_{n=0}^\\infty a_n(z-a)^n$ | $|z-a| < R$ |",
            "| Laurent | $f(z) = \\sum_{n=-\\infty}^\\infty c_n(z-a)^n$ | 环形域 |",
            "| 留数 | $\\operatorname{Res}(f,a) = c_{-1}$ |",
            "",
            "## 四、留数定理的应用",
            "",
            "| 积分类型 | 方法 | 留数计算 |",
            "|----------|------|---------|",
            "| $\\int_{-\\infty}^\\infty R(x)\\,dx$ | 上半圆围道 | 上半平面极点留数和 |",
            "| $\\int_0^{2\\pi} R(\\cos\\theta,\\sin\\theta)\\,d\\theta$ | $z = e^{i\\theta}$ 单位圆 | 单位圆内极点留数和 |",
            "| $\\int_{-\\infty}^\\infty R(x)e^{iax}\\,dx$ | Jordan 引理 | 上半平面留数 $\\times 2\\pi i$ |",
        ],
        "number-theory": [
            "## 一、整除与同余",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 整除 | $a\\mid b \\iff \\exists k: b = ak$ |",
            "| 同余 | $a\\equiv b\\pmod m \\iff m\\mid (a-b)$ |",
            "| gcd | $\\gcd(a,b)$ = 最大公因数 |",
            "| Bezout | $\\exists x,y:\\, ax+by = \\gcd(a,b)$ |",
            "| Euler 定理 | $a^{\\varphi(m)} \\equiv 1\\pmod m$ 若 $\\gcd(a,m)=1$ |",
            "| 中国剩余定理 | 同余方程组 $x\\equiv a_i\\pmod{m_i}$ 有唯一解模 $\\prod m_i$ |",
            "",
            "## 二、二次互反",
            "",
            "| 符号 | 定义 |",
            "|------|------|",
            "| Legendre 符号 | $\\left(\\frac{a}{p}\\right) = a^{(p-1)/2}\\pmod p$ |",
            "| Euler 准则 | $\\left(\\frac{a}{p}\\right) \\equiv a^{(p-1)/2}\\pmod p$ |",
            "| 二次互反律 | $\\left(\\frac{p}{q}\\right)\\left(\\frac{q}{p}\\right) = (-1)^{\\frac{p-1}{2}\\cdot\\frac{q-1}{2}}$ |",
            "",
            "## 三、素数分布",
            "",
            "| 定理 | 公式 |",
            "|------|------|",
            "| 素数定理 | $\\pi(x) \\sim x/\\ln x$ |",
            "| Dirichlet 定理 | $\\gcd(a,d)=1$ 则 $a\\bmod d$ 有无穷多素数 |",
            "| Chebyshev 估计 | $0.9\\cdot x/\\ln x < \\pi(x) < 1.1\\cdot x/\\ln x$（充分大 $x$）|",
        ],
        "logic": [
            "## 一、命题逻辑",
            "",
            "| 连接词 | 符号 | 真值条件 |",
            "|--------|------|---------|",
            "| 否定 | $\\neg p$ | $p$ 为假 |",
            "| 合取 | $p\\wedge q$ | 两者为真 |",
            "| 析取 | $p\\vee q$ | 至少一个为真 |",
            "| 蕴含 | $p\\rightarrow q$ | $p$ 假或 $q$ 真 |",
            "| 等价 | $p\\leftrightarrow q$ | 同真同假 |",
            "",
            "## 二、一阶逻辑",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| 全称量词 | $\\forall x\\, P(x)$ |",
            "| 存在量词 | $\\exists x\\, P(x)$ |",
            "| 前束范式 | 所有量词前置的公式 |",
            "| Skolem 化 | 消去存在量词（引入 Skolem 函数）|",
            "",
            "## 三、可计算性",
            "",
            "| 概念 | 定义 |",
            "|------|------|",
            "| Turing 机 | 形式化计算模型 |",
            "| 可判定性 | 存在算法判定命题真假 |",
            "| 不可判定性 | 不存在这样的算法（停机问题）|",
            "| Gödel 不完备 | 足够强的形式系统必然不完备或不一致 |",
        ],
    }

    domain_key = domain
    if domain_key in domain_lines:
        lines.extend(domain_lines[domain_key])
    else:
        lines.extend(domain_lines["calculus"])

    # Add course-specific formulas from graph
    graph = get_graph(cid)
    if graph:
        formulas = [n["label"] for n in graph["nodes"] if n["type"] == "Formula"]
        if formulas:
            lines.extend(["", "## 课程核心公式", ""])
            for f in formulas[:10]:
                lines.append(f"- ${f}$")

    lines.extend(["", "", "---", f"*{name} ({cid}) — 公式速查手册*"])
    return "\n".join(lines)


def proof_techniques_md(cid, course):
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 证明技巧指南\n"]

    domain_proofs = {
        "calculus": [
            "## 一、ε-δ 证明框架",
            "",
            "### 标准模板",
            "```",
            "要证：lim_{x→a} f(x) = L",
            "",
            '"Given ε > 0, choose δ = ... (depends on ε).',
            "Then for all x with 0 < |x - a| < δ, we have |f(x) - L| < ε.\"",
            "```",
            "",
            "### 三步构造法",
            "| 步骤 | 操作 | 示例：证 lim_{x→2} x² = 4 |",
            "|------|------|---------------------------|",
            "| 1. 目标 | 将 |f(x)-L| 写成 |x-a| 的表达式 | |x²-4| = |x-2|·|x+2| |",
            "| 2. 约束 | 给 |x-a| 一个初步限制 | 令 |x-2| < 1 ⇒ x∈(1,3) ⇒ |x+2| < 5 |",
            "| 3. 构造 | 用 ε 表达 δ | |x²-4| < 5|x-2| < ε ⇒ 取 δ = min(1, ε/5) |",
            "",
            "## 二、MVT 证明技巧",
            "",
            "### 三步法",
            "| 步骤 | 操作 |",
            "|------|------|",
            "| 1. 构造函数 | 将目标不等式移项为 $g(x)\\ge 0$ 的形式 |",
            "| 2. 应用 MVT | 在适当区间上应用中值定理 |",
            "| 3. 放缩 | 利用导数界得到结论 |",
            "",
            "### 常见应用",
            "- 证 $\\ln x \\le x-1$：设 $f(t)=\\ln t - t + 1$，在 $[1,x]$ 上用 MVT",
            "- 证 $|\\sin a - \\sin b| \\le |a-b|$：在 $[a,b]$ 上用 MVT",
            "- 证 $e^x \\ge 1+x$：在 $[0,x]$ 上用 MVT",
            "",
            "## 三、IVT 存在性证明",
            "",
            "### 标准形式",
            "```",
            "要证方程 f(x) = 0 在 (a,b) 内有根",
            "1. 验证 f 在 [a,b] 连续",
            "2. 验证 f(a) 与 f(b) 异号",
            "3. 由 IVT，∃c∈(a,b) 使得 f(c) = 0",
            "```",
            "",
            "## 四、反证法模板",
            "",
            "### 标准结构",
            "```",
            "假设反面结论成立 → 推导出矛盾 → 原结论成立",
            "```",
            "",
            "### 经典应用",
            "| 命题 | 反证假设 | 矛盾点 |",
            "|------|----------|--------|",
            "| $\\sqrt{2}$ 无理数 | $\\sqrt{2}=p/q$（既约分数） | $p,q$ 均为偶数 |",
            "| 零点唯一性 | 存在两个不同零点 | Rolle ⇒ f' 有零点矛盾 |",
        ],
        "linear-algebra": [
            "## 一、向量空间证明",
            "",
            "### 子空间判定",
            "要证 $U\\subseteq V$ 是子空间：",
            "1. $0\\in U$",
            "2. 对加法封闭：$u_1+u_2\\in U$ 对所有 $u_1,u_2\\in U$",
            "3. 对标量乘法封闭：$cu\\in U$ 对所有 $c\\in\\mathbb{F}, u\\in U$",
            "",
            "### 线性无关证明",
            "要证 $\\{v_1,\\ldots,v_n\\}$ 线性无关：",
            "```",
            "设 ∑a_i v_i = 0，证明所有 a_i = 0",
            "常用技巧：应用线性变换、取内积、代入特殊值",
            "```",
            "",
            "## 二、线性变换证明",
            "",
            "### 核与像技巧",
            "| 目标 | 方法 |",
            "|------|------|",
            "| 证单射 | 证 $\\ker T = \\{0\\}$ |",
            "| 证满射 | 证 $\\operatorname{im} T = W$（对目标空间）|",
            "| 维数关系 | 用秩-零化度定理 $\\dim V = \\dim\\ker T + \\dim\\operatorname{im} T$ |",
            "",
            "## 三、对角化证明",
            "",
            "### 可对角化判定",
            "1. 求特征值 $\\lambda_1,\\ldots,\\lambda_k$",
            "2. 对每个 $\\lambda_i$，求 $m_g(\\lambda_i) = \\dim\\ker(A-\\lambda_i I)$",
            "3. 若 $\\sum m_g(\\lambda_i) = n$，则可对角化",
            "",
            "## 四、内积空间技巧",
            "",
            "### Gram-Schmidt 正交化",
            "1. $u_1 = v_1$",
            "2. $u_k = v_k - \\sum_{i<k} \\langle v_k, u_i\\rangle/\\|u_i\\|^2 \\cdot u_i$",
            "3. 归一化：$e_k = u_k/\\|u_k\\|$",
        ],
        "abstract-algebra": [
            "## 一、群论证明",
            "",
            "### 子群判定",
            "要证 $H\\subseteq G$ 是子群：对任意 $a,b\\in H$，有 $ab^{-1}\\in H$",
            "",
            "### 同态基本定理",
            "1. 构造同态 $\\varphi: G\\to H$",
            "2. 证 $\\ker\\varphi \\trianglelefteq G$",
            "3. 由 $G/\\ker\\varphi \\cong \\operatorname{im}\\varphi$ 得到同构",
            "",
            "### 正规子群证明",
            "要证 $N\\trianglelefteq G$：对任意 $g\\in G, n\\in N$，有 $gng^{-1}\\in N$",
            "",
            "## 二、环论证明",
            "",
            "### 理想判定",
            "要证 $I\\subseteq R$ 是理想：",
            "1. $I$ 是加法子群",
            "2. 对任意 $r\\in R, a\\in I$，有 $ra\\in I$ 且 $ar\\in I$",
            "",
            "### 商环同构",
            "利用 $R/I \\cong S$ 通过构造满同态 $\\varphi: R\\to S$，证 $\\ker\\varphi = I$",
            "",
            "## 三、模论技巧",
            "",
            "### 循环模分解",
            "有限生成 $\\mathbb{F}[x]$-模 → 不变因子 → 循环子模直和分解",
            "",
            "### Jordan 标准形构造",
            "1. 将 $V$ 视为 $\\mathbb{F}[x]$-模（$x\\cdot v = T(v)$）",
            "2. 分解为循环子模",
            "3. 每个循环子模对应一个 Jordan 块",
        ],
        "multivariable-calculus": [
            "## 一、可微性证明",
            "",
            "### 定义法",
            "要证 $f$ 在 $a$ 可微：",
            "```",
            "证存在线性映射 $L$ 使得",
            "lim_{h→0} |f(a+h) - f(a) - L(h)| / ‖h‖ = 0",
            "```",
            "",
            "## 二、极值证明",
            "",
            "### 二阶判别法",
            "1. 求临界点 $\\nabla f(a) = 0$",
            "2. 计算 Hessian $H_f(a)$",
            "3. 若 $H_f$ 正定→局部极小；负定→局部极大；不定→鞍点",
            "",
            "## 三、积分换元",
            "",
            "### 换元步骤",
            "1. 选择变换 $\\varphi: U\\to V$",
            "2. 计算 Jacobian $|\\det D\\varphi|$",
            "3. 将积分区域和被积函数用新变量表示",
            "",
            "## 四、Stokes 型定理",
            "",
            "| 定理 | 维度 | 关系 |",
            "|------|------|------|",
            "| Green | 2D | $\\oint Pdx+Qdy = \\iint (Q_x-P_y)dxdy$ |",
            "| Stokes | 3D | $\\int_{\\partial S} \\mathbf{F}\\cdot d\\mathbf{r} = \\iint_S (\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{S}$ |",
            "| Divergence | 3D | $\\iiint_V \\nabla\\cdot\\mathbf{F}\\,dV = \\iint_{\\partial V} \\mathbf{F}\\cdot\\mathbf{n}\\,dS$ |",
        ],
        "odes": [
            "## 一、一阶 ODE 解法选择",
            "",
            "### 判定流程",
            "```",
            "给定 dy/dx = F(x,y)",
            "1. 可分离？ F(x,y) = g(x)h(y) → 分离变量",
            "2. 线性？ dy/dx + P(x)y = Q(x) → 积分因子",
            "3. 恰当？ M dx + N dy = 0, M_y = N_x → 求势函数",
            "4. Bernoulli？ y' + P(x)y = Q(x)y^n → u = y^{1-n}",
            "5. 以上都不对 → 尝试积分因子或变换",
            "```",
            "",
            "## 二、常系数线性 ODE",
            "",
            "### 求解步骤",
            "1. 写出特征方程 $a_n r^n + \\ldots + a_0 = 0$",
            "2. 求特征根 $r_1,\\ldots,r_n$",
            "3. 根据根的类型写出基解组：",
            "   - 实单根 → $e^{rx}$",
            "   - 实重根 → $e^{rx}, xe^{rx}, \\ldots$",
            "   - 复根 → $e^{\\alpha x}\\cos\\beta x, e^{\\alpha x}\\sin\\beta x$",
            "",
            "## 三、非齐次方程",
            "",
            "### 待定系数法",
            "| $f(x)$ 形式 | $y_p$ 猜测 |",
            "|-------------|----------|",
            "| $P_n(x)$ | $Q_n(x)$ |",
            "| $P_n(x)e^{ax}$ | $Q_n(x)e^{ax}$ |",
            "| $P_n(x)\\sin\\beta x$ 或 $P_n(x)\\cos\\beta x$ | $Q_n(x)\\sin\\beta x + R_n(x)\\cos\\beta x$ |",
            "| $e^{ax}(\\sin\\beta x, \\cos\\beta x)$ | $e^{ax}(A\\sin\\beta x + B\\cos\\beta x)$ |",
            "",
            "### 参数变易法（通用）",
            "1. 解齐次方程得 $y_h = c_1y_1 + c_2y_2$",
            "2. 设 $y_p = u_1(x)y_1 + u_2(x)y_2$",
            "3. 解 $u_1'y_1 + u_2'y_2 = 0$, $u_1'y_1' + u_2'y_2' = f(x)$",
        ],
        "complex-analysis": [
            "## 一、解析性证明",
            "",
            "### Cauchy-Riemann 方程",
            "要证 $f(z) = u(x,y) + iv(x,y)$ 解析：",
            "1. $u_x = v_y$ 且 $u_y = -v_x$",
            "2. 所有偏导连续",
            "",
            "## 二、围道积分技巧",
            "",
            "### Cauchy 积分公式",
            "$$f(a) = \\frac{1}{2\\pi i}\\oint_\\gamma \\frac{f(z)}{z-a}\\,dz$$",
            "",
            "### 留数计算",
            "| 奇点类型 | 留数 $\\operatorname{Res}(f,a)$ |",
            "|----------|------------------------------|",
            "| 单极点 | $\\lim_{z\\to a}(z-a)f(z)$ |",
            "| m 阶极点 | $\\frac{1}{(m-1)!}\\lim_{z\\to a}\\frac{d^{m-1}}{dz^{m-1}}(z-a)^m f(z)$ |",
            "| 本性奇点 | 级数展开取 $c_{-1}$ |",
            "",
            "## 三、实积分计算",
            "",
            "### 标准方法",
            "1. 选择合适的围道（半圆、矩形、扇形）",
            "2. 验证围道上的积分在极限下消失（Jordan 引理）",
            "3. 用留数定理计算围道积分",
            "4. 取极限得到实积分值",
        ],
        "number-theory": [
            "## 一、同余证明",
            "",
            "### 常用技巧",
            "1. 模运算：$a\\equiv b\\pmod m \\Rightarrow a^n\\equiv b^n\\pmod m$",
            "2. 费马小定理：$a^p\\equiv a\\pmod p$",
            "3. Euler 定理：$a^{\\varphi(m)}\\equiv 1\\pmod m$ 若 $\\gcd(a,m)=1$",
            "",
            "## 二、二次互反证明",
            "",
            "### Legendre 符号计算",
            "1. 用 Euler 准则 $\\left(\\frac{a}{p}\\right) \\equiv a^{(p-1)/2}\\pmod p$",
            "2. 用二次互反律化简 $\\left(\\frac{p}{q}\\right)$",
            "3. 用补充公式 $\\left(\\frac{-1}{p}\\right) = (-1)^{(p-1)/2}$, $\\left(\\frac{2}{p}\\right) = (-1)^{(p^2-1)/8}$",
            "",
            "## 三、丢番图方程",
            "",
            "### 无穷递降法",
            "假设存在正整数解 → 构造更小的正整数解 → 矛盾",
            "",
            "### 同余分析法",
            "对方程两边取模，利用模运算的约束排除解",
        ],
        "logic": [
            "## 一、命题逻辑证明",
            "",
            "### 自然演绎规则",
            "| 规则 | 形式 |",
            "|------|------|",
            "| 合取引入 | $\\dfrac{A\\quad B}{A\\wedge B}$ |",
            "| 合取消去 | $\\dfrac{A\\wedge B}{A}$ |",
            "| 蕴含消去 | $\\dfrac{A\\quad A\\rightarrow B}{B}$ |",
            "| 反证法 | $\\dfrac{\\neg A\\vdash \\bot}{A}$ |",
            "",
            "## 二、一阶逻辑证明",
            "",
            "### 量词规则",
            "| 规则 | 形式 | 条件 |",
            "|------|------|------|",
            "| 全称引入 | $\\dfrac{P(c)}{\\forall x\\,P(x)}$ | $c$ 不在前提中自由出现 |",
            "| 全称消去 | $\\dfrac{\\forall x\\,P(x)}{P(t)}$ | $t$ 可代入 |",
            "| 存在引入 | $\\dfrac{P(t)}{\\exists x\\,P(x)}$ | $t$ 自由替换 |",
            "| 存在消去 | $\\dfrac{\\exists x\\,P(x)\\quad P(c)\\vdash Q}{Q}$ | $c$ 新常数 |",
            "",
            "## 三、Gödel 不完备定理",
            "",
            "### 核心思路",
            "1. Gödel 编码：将公式和证明编码为自然数",
            "2. 自指语句：构造 $G$ = \"$G$ 不可证\"",
            "3. $G$ 真但不可证 → 系统不完备",
        ],
    }

    key = domain
    if key in domain_proofs:
        lines.extend(domain_proofs[key])

    lines.extend(["", "", "---", f"*{name} ({cid}) — 证明技巧指南*"])
    return "\n".join(lines)


def counterexamples_md(cid, course):
    """Generate ~50-80 line course-specific counterexamples."""
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 反例速查手册\n"]
    lines.append("> 按概念分类，标注反例破坏的条件\n")

    ce = {
        "calculus": [
            "## 极限相关",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $f(x) = x\\sin(1/x)$ 在 $x\\to 0$ | 极限存在≠函数值存在 | $\\lim$ 存在但 $f(0)$ 无定义 |",
            "| 2 | $f(x) = \\sin(1/x)$ 在 $x\\to 0$ | 极限不存在（振荡） | 振幅有界但振荡过快 |",
            "| 3 | $f(x) = 1/x$ 在 $x\\to 0^+$ | 无穷极限 | 极限为 $\\infty$（非有限） |",
            "| 4 | $f(x) = x/|x|$ 在 $x\\to 0$ | 单侧极限不相等 | 左 $-1$，右 $+1$ |",
            "",
            "## 连续相关",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 5 | $f(x)=\\{_{\\sin(1/x), x\\neq 0}^{0, x=0}$ | 可去间断 | 极限存在但函数值不同 |",
            "| 6 | $f(x)=|x|$ | 连续不可导 | 在 $0$ 连续但有尖点 |",
            "| 7 | $f(x)=x^2\\sin(1/x)$ | 可导但导数不连续 | $f'(0)=0$ 但 $f'$ 在 $0$ 振荡 |",
            "| 8 | $f(x)=1/x$ 在 $(0,1)$ | EVT 不成立 | 开区间连续但无最大值 |",
            "",
            "## 微分相关",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 9 | $f(x)=x^3$ | $f'(0)=0$ 非极值 | 驻点可以是拐点 |",
            "| 10 | $f(x)=x^{1/3}$ | 不可导但有竖直切线 | 导数无穷大 |",
            "| 11 | $f(x)=e^{-1/x^2}$ | 光滑非解析 | 所有导数在 $0$ 为 $0$ |",
            "",
            "## 级数相关",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 12 | $\\sum 1/n$ | $a_n\\to 0$ 发散 | 必要条件非充分 |",
            "| 13 | $\\sum (-1)^n/n$ | 条件收敛 | 收敛但绝对值发散 |",
            "| 14 | $\\sum 1/(n\\ln n)$ | 比值法无效 | 需积分判别法 |",
        ],
        "linear-algebra": [
            "## 向量空间反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $\\{(x,y): xy=0\\}\\subseteq\\mathbb{R}^2$ | 非子空间 | 对加法不封闭：$(1,0)+(0,1)=(1,1)\\notin$ 集合 |",
            "| 2 | $\\{(x,y): x+y=1\\}\\subseteq\\mathbb{R}^2$ | 非子空间 | 不含零向量 |",
            "| 3 | $\\mathbb{R}^2$ 作为 $\\mathbb{Q}$-向量空间 | 维数无穷 | 基不可数 |",
            "",
            "## 线性变换反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 4 | $T:\\mathbb{R}^2\\to\\mathbb{R}^2$, $T(x,y)=(x,0)$ | 非单射非满射 | 核 $\\neq\\{0\\}$，像 $\\neq$ 目标 |",
            "| 5 | $T(f)=f'$ 在 $\\mathcal{P}_n$ 上 | $\\ker T\\neq\\{0\\}$ | 常数函数的导数为 $0$ |",
            "",
            "## 特征值反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 6 | $A=\\begin{pmatrix}0&1\\\\0&0\\end{pmatrix}$ | 不可对角化 | $m_a(0)=2$, $m_g(0)=1$ |",
            "| 7 | $A=\\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}$ | Jordan 块 | 几何重数 < 代数重数 |",
            "| 8 | $A=\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ | 实矩阵无实特征值 | 特征多项式 $\\lambda^2+1$ |",
        ],
        "abstract-algebra": [
            "## 群论反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $S_3$ 的子群 $H=\\{e,(12)\\}$ | 非正规子群 | $(13)(12)(13)^{-1}=(23)\\notin H$ |",
            "| 2 | $A_4$ | 无 6 阶子群 | Lagrange 逆不成立 |",
            "| 3 | $Q_8$（四元数群） | 非交换 | 所有子群正规但群非交换 |",
            "",
            "## 环论反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 4 | $\\mathbb{Z}_6$ | 非整环 | $2\\cdot 3 = 0$（零因子）|",
            "| 5 | $\\mathbb{Z}[x]$ | 非 PID | 理想 $(2,x)$ 非主理想 |",
            "| 6 | $\\mathbb{Z}[\\sqrt{-5}]$ | 非 UFD | $6=2\\cdot 3=(1+\\sqrt{-5})(1-\\sqrt{-5})$ |",
        ],
        "multivariable-calculus": [
            "## 可微性反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $f(x,y)=\\{_{0}^{xy/(x^2+y^2)}$ 在 $(0,0)$ | 偏导存在不→可微 | 方向导数不线性 |",
            "| 2 | $f(x,y)=\\{_{0}^{|x|+|y|}$ | 连续不→可微 | 尖点 |",
            "",
            "## 极值反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 3 | $f(x,y)=x^2-y^2$ 在 $(0,0)$ | 鞍点 | $\\nabla f=0$ 但非极值 |",
            "| 4 | $f(x,y)=x^2+100y^2$ | 条件极值 | Lagrange 乘数法 |",
            "",
            "## 积分反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 5 | $f(x,y)=\\{_{0}^{1}$ 有理点 $\\}$ | 非 Riemann 可积 | Dirichlet 函数 |",
            "| 6 | $\\int_0^1\\int_0^1 \\frac{x^2-y^2}{(x^2+y^2)^2}\\,dx\\,dy$ | Fubini 失效 | 迭代积分不等 |",
        ],
        "odes": [
            "## 唯一性反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $y' = y^{1/3}$, $y(0)=0$ | 解不唯一 | $y=0$ 和 $y=(2x/3)^{3/2}$ 都是解 |",
            "| 2 | $y' = 1 + y^2$, $y(0)=0$ | 有限时间爆破 | $y=\\tan x$ 在 $x=\\pi/2$ 爆破 |",
            "",
            "## 稳定性反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 3 | $x' = -x^3$ | 渐近稳定 | 非线性稳定但线性化失效（$f'(0)=0$）|",
            "| 4 | $x' = x^3$ | 不稳定 | 线性化 $f'(0)=0$ 无法判定 |",
        ],
        "complex-analysis": [
            "## 解析性反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $f(z)=\\bar{z}$ | 不解析 | CR 方程不满足 |",
            "| 2 | $f(z)=|z|^2$ | 仅在 $0$ 可微 | 非解析 |",
            "| 3 | $f(z)=e^{-1/z^2}$ | 本性奇点 | $z=0$ 处极限不存在 |",
            "",
            "## 积分反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 4 | $\\oint_{|z|=1} 1/z\\,dz = 2\\pi i$ | 非零围道积分 | Cauchy 定理要求解析域 |",
            "| 5 | $\\oint_{|z|=1} \\bar{z}\\,dz$ | 与路径有关 | 非解析函数 |",
        ],
        "number-theory": [
            "## 同余反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $2^{340} \\equiv 1\\pmod{341}$ | 费马小定理逆不成立 | $341=11\\cdot 31$ 是伪素数 |",
            "| 2 | $561 = 3\\cdot 11\\cdot 17$ | Carmichael 数 | 对所有 $\\gcd(a,561)=1$ 满足 $a^{560}\\equiv 1$ |",
            "",
            "## 素数反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 3 | $n^2 + n + 41$ | 素数生成公式失效 | $n=40$ 时 $=41^2$ |",
            "| 4 | $2^{2^5}+1 = 4294967297$ | Fermat 素数猜想 | $=641\\times 6700417$ |",
        ],
        "logic": [
            "## 逻辑反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 1 | $p\\rightarrow q$ 真但 $p$ 假 | 实质蕴含悖论 | 假前提蕴含一切 |",
            "| 2 | 停机问题 | 不可判定性 | 不存在判定程序是否停机的算法 |",
            "| 3 | Gödel 语句 $G$ | 不完备性 | $G$ 真但不可证 |",
            "",
            "## 量词反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 4 | $\\forall x\\exists y\\,P(x,y)$ vs $\\exists y\\forall x\\,P(x,y)$ | 量词顺序 | $\\forall x\\exists y\\, x<y$ 真但 $\\exists y\\forall x\\, x<y$ 假 |",
            "| 5 | $\\neg\\forall x\\,P(x)$ 不等价于 $\\forall x\\,\\neg P(x)$ | 量词否定 | 正确的是 $\\exists x\\,\\neg P(x)$ |",
            "| 6 | $\\forall x\\,(P(x)\\lor Q(x))$ 与 $\\forall x\\,P(x)\\lor\\forall x\\,Q(x)$ | 量词分配 | 前者强于后者: $P$ 偶 $Q$ 奇数在 $\\mathbb{N}$ |",
            "",
            "## 模型论反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 7 | $\\mathbb{N}$ vs $\\mathbb{N}+\\mathbb{Z}$ | 非标准模型 | Peano 算术存在非标准模型 |",
            "| 8 | $\\mathbb{Q}$ 和 $\\mathbb{R}$ 都满足域公理 | 范畴性 | 一阶理论不能唯一确定无穷模型 |",
            "| 9 | $\\langle\\mathbb{Q},<\\rangle$ 和 $\\langle\\mathbb{R},<\\rangle$ | 初等等价 | 同构于 $\\mathbb{Q}$ 的任何稠密无端点线性序 |",
            "",
            "## 证明论反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 10 | $A\\rightarrow B, A\\rightarrow\\neg B \\vdash \\neg A$ | 反证法 | 归谬法在直觉主义逻辑中不成立 |",
            "| 11 | 排中律 $A\\lor\\neg A$ 在直觉主义逻辑中不可证 | 构造性 | 并非所有命题都有构造性证明 |",
            "| 12 | Löb 定理: $\\square(\\square P\\rightarrow P)\\rightarrow\\square P$ | 可证性逻辑 | 与 Gödel 第二不完备定理相关 |",
            "",
            "## 可计算性反例",
            "| # | 反例 | 破坏概念 | 说明 |",
            "|---|------|----------|------|",
            "| 13 | 一阶逻辑的可满足性问题 | 不可判定性 | Church 定理: 无算法判定公式可满足性 |",
            "| 14 | Presburger 算术可判定但指数复杂 | 复杂度下界 | 双指数时间下界 |",
        ],
    }

    key = domain
    if key in ce:
        lines.extend(ce[key])

    lines.extend(["", "", "---", f"*{name} ({cid}) — 反例速查手册*"])
    return "\n".join(lines)


def checklist_md(cid, course):
    """Generate per-unit checklist."""
    name = course["name"]
    graph = get_graph(cid)
    lines = [f"# {cid} — 学习进度检查表\n"]

    if graph:
        units = {}
        for n in graph["nodes"]:
            u = n.get("unit", "none")
            if u not in units:
                units[u] = []
            units[u].append(n)

        for uid in sorted(units.keys()):
            if uid == "none":
                continue
            lines.append(f"## {uid.replace('unit-', '单元 ')}")
            lines.append("")
            for n in units[uid]:
                label = n.get("label", "")
                labelCn = n.get("labelCn", "")
                entry = f"- [ ] **{label}**"
                if labelCn:
                    entry += f" / {labelCn}"
                lines.append(entry)
            lines.append("")
    else:
        lines.append("| 单元 | 内容 | 状态 |")
        lines.append("|------|------|------|")
        lines.append("| 1 | TBD | - |")

    lines.extend(["", "", "---", f"*{name} ({cid}) — 学习进度检查表*"])
    return "\n".join(lines)


def concept_map_md(cid, course):
    """Generate concept dependency map."""
    name = course["name"]
    graph = get_graph(cid)
    lines = [f"# {cid} — 概念依赖图谱\n"]

    if graph:
        from collections import defaultdict
        # Build adjacency
        children = defaultdict(list)
        for e in graph.get("edges", []):
            children[e["source"]].append(e["target"])

        # Group by unit
        node_by_id = {}
        for n in graph["nodes"]:
            node_by_id[n["id"]] = n

        units = defaultdict(list)
        for n in graph["nodes"]:
            u = n.get("unit", "none")
            units[u].append(n)

        for uid in sorted(units.keys()):
            if uid == "none":
                continue
            lines.append(f"## {uid.replace('unit-', '单元 ')}")
            lines.append("")
            for n in units[uid]:
                label = n.get("label", "")
                labelCn = n.get("labelCn", "")
                entry = f"- **{label}** ({labelCn})"
                # Find dependencies
                deps = [node_by_id.get(t, {}).get("label", t) for t in children.get(n["id"], [])]
                if deps:
                    entry += f" → {', '.join(deps[:5])}"
                lines.append(entry)
            lines.append("")
    else:
        lines.append("*概念依赖图数据待补充*")

    lines.extend(["", "", "---", f"*{name} ({cid}) — 概念依赖图谱*"])
    return "\n".join(lines)


def applications_md(cid, course):
    """Generate real-world applications."""
    name = course["name"]
    domain = course["domain"]
    lines = [f"# {cid} — 实际应用\n"]

    apps = {
        "calculus": [
            "## 物理与工程",
            "- **运动学**：导数描述速度与加速度，积分计算位移",
            "- **优化**：极值问题在工程设计、经济学中的应用",
            "- **电磁学**：Maxwell 方程组的积分与微分形式",
            "",
            "## 数据科学",
            "- **梯度下降**：机器学习中的参数优化",
            "- **概率密度**：连续概率分布由积分定义",
            "- **神经网络**：反向传播依赖链式法则",
            "",
            "## 其他领域",
            "- **经济学**：边际成本与弹性分析",
            "- **生物学**：种群增长模型（logistic 方程）",
            "- **医学**：药物浓度随时间变化（指数衰减）",
        ],
        "linear-algebra": [
            "## 计算机科学",
            "- **计算机图形学**：变换矩阵（旋转、缩放、平移）",
            "- **机器学习**：PCA 用特征值分解降维",
            "- **量子计算**：量子态用向量空间描述",
            "",
            "## 工程",
            "- **结构分析**：有限元法解 PDE",
            "- **信号处理**：Fourier 变换用内积空间",
            "- **机器人学**：齐次坐标与刚体变换",
            "",
            "## 数据科学",
            "- **推荐系统**：矩阵分解（SVD）",
            "- **PageRank**：特征向量中心性",
            "- **线性回归**：最小二乘的正交投影解释",
        ],
        "abstract-algebra": [
            "## 密码学",
            "- **RSA**：基于 Euler 定理和 $(\\mathbb{Z}/n\\mathbb{Z})^\\times$ 的群结构",
            "- **椭圆曲线密码**：椭圆曲线群上的离散对数问题",
            "- **Diffie-Hellman**：循环群上的密钥交换",
            "- **数字签名**：Schnorr 签名基于离散对数",
            "- **后量子密码**：格密码基于理想格上的困难问题",
            "",
            "## 物理",
            "- **标准模型**：对称群 $SU(3)\\times SU(2)\\times U(1)$",
            "- **晶体学**：空间群与点群分类",
            "- **量子力学**：Lie 群与 Lie 代数表示",
            "- **分子振动**：对称性分析简正模式",
            "- **广义相对论**：微分同胚群与张量场变换",
            "",
            "## 计算机科学",
            "- **编码理论**：循环码的代数结构",
            "- **组合博弈论**：群论分析 Nim 游戏",
            "- **量子纠错码**：稳定子码与 Pauli 群",
            "- **计算机代数**：Gröbner 基解决多项式方程组",
            "",
            "## 化学",
            "- **分子对称性**：点群分类分子构型",
            "- **手性分析**：对称操作确定分子对映体",
        ],
        "multivariable-calculus": [
            "## 物理",
            "- **电磁学**：散度定理和 Stokes 定理是 Maxwell 方程的基础",
            "- **流体力学**：梯度、散度、旋度描述流场",
            "- **相对论**：张量分析与弯曲时空",
            "- **热力学**：状态函数的全微分与路径无关性",
            "- **弹性力学**：应力张量的散度描述平衡",
            "",
            "## 机器学习",
            "- **梯度下降**：多元函数的梯度方向最速下降",
            "- **反向传播**：链式法则的多元推广",
            "- **SVM**：约束优化与 Lagrange 对偶",
            "- **自动微分**：计算图的 Jacobian 乘积",
            "- **流形学习**：嵌入在高维空间的低维流形结构",
            "",
            "## 工程",
            "- **计算机图形学**：法向量计算与曲面渲染",
            "- **机器人学**：Jacobian 矩阵控制末端执行器",
            "- **导航**：多变量 Kalman 滤波",
            "- **图像处理**：梯度算子边缘检测",
        ],
        "odes": [
            "## 物理与工程",
            "- **谐振子**：$mx'' + kx = 0$ 描述弹簧-质量系统",
            "- **电路**：RLC 电路的 ODE 模型",
            "- **天体力学**：行星运动的 Kepler 方程",
            "- **摆锤运动**：单摆的非线性 ODE 与小角度线性化",
            "- **振动分析**：多自由度系统的耦合 ODE 特征频率",
            "",
            "## 生物与化学",
            "- **化学反应**：速率方程的 ODE 模型",
            "- **种群动力学**：Lotka-Volterra 捕食者-猎物模型",
            "- **药物动力学**：药物吸收与消除的 ODE",
            "- **流行病学**：SIR 模型的 ODE 系统",
            "- **酶动力学**：Michaelis-Menten 方程的推导",
            "",
            "## 控制与工程",
            "- **PID 控制**：微分方程描述控制器响应",
            "- **火箭轨道**：变质量系统的 Tsiolkovsky 方程",
            "- **热传导**：Newton 冷却定律 $T'(t) = k(T_{\\text{env}} - T)$",
            "- **信号滤波**：RC 电路的 ODE 响应特征",
        ],
        "complex-analysis": [
            "## 物理",
            "- **流体力学**：复势描述二维不可压缩流",
            "- **电磁学**：保角映射解静电场问题",
            "- **量子力学**：波函数的复值描述",
            "- **弦论**：世界面的共形映射和 Riemann 面",
            "- **光学**：Fresnel 衍射的复积分表示",
            "",
            "## 工程",
            "- **信号处理**：Fourier 变换的复指数形式",
            "- **控制理论**：s-平面分析稳定性",
            "- **空气动力学**：Joukowski 变换解翼型绕流",
            "- **数字滤波**：z-变换与极零点分析",
            "- **电气工程**：阻抗的复表示 $Z = R + iX$",
            "",
            "## 数学应用",
            "- **实积分计算**：留数定理求解广义积分",
            "- **渐进分析**：最速下降法估计积分渐近行为",
            "- **Riemann 猜想**：$\zeta$ 函数零点分布",
            "- **调和分析**：共形映射解 Laplace 方程",
        ],
        "number-theory": [
            "## 密码学",
            "- **RSA**：大素数乘积的因数分解困难性",
            "- **数字签名**：基于离散对数问题",
            "- **零知识证明**：同余与模运算",
            "- **同态加密**：Paillier 加密基于合数剩余类",
            "- **密钥交换**：Diffie-Hellman 模素数幂",
            "",
            "## 计算机科学",
            "- **哈希函数**：模运算构造均匀分布",
            "- **伪随机数生成**：线性同余生成器",
            "- **纠错码**：有限域上的代数编码",
            "- **快速 Fourier 变换**：单位根的数论性质",
            "- **分布式系统**：一致性哈希模 $2^{32}$",
            "",
            "## 数学应用",
            "- **丢番图逼近**：有理逼近无理数",
            "- **椭圆曲线**：Mordell 定理与秩计算",
            "- **模形式**：Fermat 大定理的证明工具",
            "- **加法组合**：Freiman 定理与和集结构",
        ],
        "logic": [
            "## 计算机科学",
            "- **程序验证**：Hoare 逻辑与程序正确性证明",
            "- **数据库**：关系代数与一阶逻辑查询",
            "- **人工智能**：逻辑推理与自动定理证明",
            "- **编程语言**：类型系统的 Curry-Howard 同构",
            "- **SAT 求解器**：命题逻辑可满足性问题的高效算法",
            "",
            "## 数学基础",
            "- **集合论**：ZFC 公理系统的相容性",
            "- **模型论**：代数结构的公理化描述",
            "- **证明论**：数学证明的形式化",
            "- **范畴论**：逻辑与范畴的对应关系",
            "- **逆数学**：数学定理所需的公理强度分析",
            "",
            "## 语言学与哲学",
            "- **形式语义学**：Montague 语法的逻辑基础",
            "- **分析哲学**：Frege-Russell 的逻辑主义纲领",
            "- **论辩理论**：形式论辩与可废止推理",
        ],
    }

    key = domain
    if key in apps:
        lines.extend(apps[key])

    # Add course-specific skills and learning methods from KG
    graph = get_graph(cid)
    if graph:
        skills_list = [n for n in graph["nodes"] if n["type"] == "Skill"]
        if skills_list:
            lines.extend(["", "## 培养技能", ""])
            for s in skills_list:
                unit = s.get("unit", "").replace("unit-", "单元 ")
                lines.append(f"- **{s['label']}** ({s['labelCn']}) — {unit}")

        lms = [n for n in graph["nodes"] if n["type"] == "LearningMethod"]
        if lms:
            lines.extend(["", "## 学习方法", ""])
            for lm in lms:
                unit = lm.get("unit", "").replace("unit-", "单元 ")
                lines.append(f"- {lm['label']} ({lm['labelCn']}) — {unit}")

    lines.extend(["", "", "---", f"*{name} ({cid}) — 实际应用*"])
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    for cid, course in COURSES.items():
        course_dir = os.path.join(SKILLS_DIR, "math", course["dir"])
        ref_dir = os.path.join(course_dir, "references")

        if not os.path.exists(ref_dir):
            print(f"  ✗ {cid}: no references dir, skipping")
            continue

        print(f"\n  {cid} ({course['name']}):")

        # 1. Copy knowledge graph JSON
        kg_src = os.path.join(ONTOLOGY_DIR, f"{cid}-knowledge-graph.json")
        kg_dst = os.path.join(ref_dir, f"{cid}-knowledge-graph.json")
        if os.path.exists(kg_src):
            shutil.copy2(kg_src, kg_dst)
            print(f"    ✓ graph JSON copied ({os.path.getsize(kg_src)} bytes)")

        # 2. Generate reference files
        generators = [
            ("formulas.md", formulas_md),
            ("proof-techniques.md", proof_techniques_md),
            ("counterexamples.md", counterexamples_md),
            ("checklist.md", checklist_md),
            ("concept-map.md", concept_map_md),
            ("applications.md", applications_md),
        ]

        for fname, gen_fn in generators:
            content = gen_fn(cid, course)
            fpath = os.path.join(ref_dir, fname)
            with open(fpath, "w") as f:
                f.write(content)
            lines = content.count("\n") + 1
            print(f"    ✓ {fname} ({lines} lines)")

    print(f"\nDone! All 12 math courses updated.")

if __name__ == "__main__":
    main()
