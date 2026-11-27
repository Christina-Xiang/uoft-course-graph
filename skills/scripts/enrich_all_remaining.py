#!/usr/bin/env python3
"""Enrich all remaining thin mode JSON files."""
import json, os
SKILLS_DIR = "skills"

def kg_nodes(cid):
    for d in ['math','stats','cs']:
        p = os.path.join(SKILLS_DIR, d)
        if not os.path.isdir(p): continue
        for s in os.listdir(p):
            if s.startswith(cid[:6].lower()):
                kp = os.path.join(p, s, 'references', f'{cid[:8]}-knowledge-graph.json')
                if os.path.exists(kp):
                    try:
                        with open(kp) as f: kg = json.load(f)
                        return [n['id'] for n in kg.get('nodes', [])[:6]]
                    except: pass
    return []

def write_mode(cp, mode, cid, topic, steps):
    ml = {'socratic':'Socratic Discovery','deductive':'Deductive Derivation','correction':'Correction Attribution'}
    si = {'socratic':'S','deductive':'D','correction':'C'}
    di = {'socratic':2,'deductive':3,'correction':2}
    st = [{"type":t,"template_en":e,"template_zh":z} for t,e,z in steps]
    if not st: return 0
    kn = kg_nodes(cid)
    dm = 'cs' if cid.startswith('CSC') else 'stats' if cid.startswith('STA') else 'math'
    data = {"name":f"{cid[:8]} — {ml[mode]} ({topic})","description":st[0]['template_en'][:150],
        "parameters":{"type":"object","properties":{"courseId":{"type":"string","enum":[cid[:8]]},"skillId":{"type":"string","const":f"{cid[:8]}-SKILL-{si[mode]}1"},"lang":{"type":"string","enum":["en","zh"]}},"required":["courseId","skillId","lang"]},
        "steps":st,"references":["references/formulas.md","references/proof-techniques.md","references/counterexamples.md","references/concept-map.md"],
        "metadata":{"domain":dm,"course":cid[:8],"skillType":mode,"difficulty":di[mode],"relatedUnits":["unit-1"],"version":"1.0","knowledgeGraphNodes":kn[:5]}}
    with open(os.path.join(cp,f'{mode}.json'),'w') as f: json.dump(data,f,indent=2,ensure_ascii=False)
    return os.path.getsize(os.path.join(cp,f'{mode}.json'))

def find(cid):
    dm = 'cs' if cid.startswith('CSC') else 'stats' if cid.startswith('STA') else 'math'
    for s in os.listdir(os.path.join(SKILLS_DIR, dm)):
        if s.startswith(cid[:6].lower()): return os.path.join(SKILLS_DIR, dm, s)
    return None

def P(cid, s=None, d=None, c=None):
    cp = find(cid)
    if not cp: print(f"X {cid}: not found"); return 0
    n = 0
    if s: sz = write_mode(cp,'socratic',cid,s['topic'],s['steps']); n+=1; print(f"OK {cid} socratic: {sz:,}b ({len(s['steps'])} steps)")
    if d: sz = write_mode(cp,'deductive',cid,d['topic'],d['steps']); n+=1; print(f"OK {cid} deductive: {sz:,}b ({len(d['steps'])} steps)")
    if c: sz = write_mode(cp,'correction',cid,c['topic'],c['steps']); n+=1; print(f"OK {cid} correction: {sz:,}b ({len(c['steps'])} steps)")
    return n

# ===== REMAINING CS =====

# CSC236 — Theory of Computation
P("CSC236H1",
  {"topic":"DFA Design and Regular Languages","steps":[
  ("setup","Let's design a DFA for L = {w∈{0,1}* | w ends with 01}. A DFA has finite memory — it can only remember a BOUNDED amount of information. For this language, we need to remember the last 1 or 2 bits.","让我们为 L = {w∈{0,1}* | w 以 01 结尾} 设计一个DFA。DFA有有限记忆——只能记住有界量的信息。对这个语言，我们需要记住最后1或2位。"),
  ("question","What states do we need? We need to track: (1) no relevant suffix seen yet (start), (2) last bit was 0 (potentially starting '01'), (3) last bit was 01 (accepting). How many states total? Three! Now draw the transitions between them for inputs 0 and 1.","我们需要什么状态？需要跟踪：(1)尚未看到相关后缀（开始），(2)最后一位是0（可能开始'01'），(3)最后一位是01（接受）。总共几个状态？三个！现在画出0和1输入在它们之间的转移。"),
  ("explore","From start state q₀: on 0 → q₁ (seen 0), on 1 → q₀ (stays start). From q₁: on 0 → q₁ (still just a 0), on 1 → q₂ (saw 01! Accept). From q₂: on 0 → q₁ (01 followed by 0 = last bit 0), on 1 → q₀ (01 followed by 1 = no relevant suffix). The DFA is complete!","从开始状态q₀：输入0→q₁（看到0），输入1→q₀（保持开始）。从q₁：输入0→q₁（仍然只有一个0），输入1→q₂（看到01！接受）。从q₂：输入0→q₁（01后跟0=最后一位是0），输入1→q₀（01后跟1=没有相关后缀）。DFA完成！"),
  ("formalize","DFA = (Q,Σ,δ,q₀,F). Q = {q₀,q₁,q₂}, Σ={0,1}, δ defined by transition table, q₀ start, F={q₂}. This DFA accepts strings ending with 01. Check: '101' → q₀→q₀→q₁→q₂ (accept). '010' → q₀→q₁→q₂→q₁ (reject). The finite memory is the 3 states.","DFA = (Q,Σ,δ,q₀,F)。Q={q₀,q₁,q₂}，Σ={0,1}，δ由转移表定义，q₀开始，F={q₂}。这个DFA接受以01结尾的串。验证：'101'→q₀→q₀→q₁→q₂（接受）。'010'→q₀→q₁→q₂→q₁（拒绝）。有限记忆就是3个状态。"),
  ("practice","Design DFAs for: (1) L = strings containing '010' as substring. (2) L = strings with even number of 0s. (3) L = strings where every 1 is followed by a 0. For each, state the number of states needed and explain what each state 'remembers.'","为以下设计DFA：(1)包含'010'作为子串的串。(2)有偶数个0的串。(3)每个1后跟一个0的串。对每个，说明所需状态数并解释每个状态'记住'了什么。"),
  ("insight","DFAs capture REGULAR languages — the simplest class in the Chomsky hierarchy. They can't count beyond a fixed bound (needs a stack for aⁿbⁿ). The state = finite memory. More states = more memory. But infinite memory requires a Turing machine.","DFA捕获正则语言——Chomsky层次中最简单的类别。它们不能计数超过有界（aⁿbⁿ需要栈）。状态 = 有限记忆。更多状态 = 更多记忆。但无限记忆需要图灵机。")
  ]},
  {"topic":"Pumping Lemma for Regular Languages","steps":[
  ("principle","The Pumping Lemma: For any regular language L, there exists p (pumping length) such that ∀w∈L with |w|≥p, w = xyz where |xy|≤p, |y|≥1, and ∀k≥0: xyᵏz∈L. This property must hold for ALL regular languages — so if a language VIOLATES it, it's NOT regular.","泵引理：对任何正则语言L，存在p（泵长度）使得对所有|w|≥p的w∈L，w=xyz其中|xy|≤p、|y|≥1，且对所有k≥0：xyᵏz∈L。该性质对所有正则语言必须成立——所以如果某个语言违反它，它就不是正则的。"),
  ("step1","We'll prove L = {aⁿbⁿ | n≥0} is NOT regular. Assume it IS regular with pumping length p. Choose w = aᵖbᵖ (p a's followed by p b's). Since |w|=2p≥p, the pumping lemma applies.","我们将证明 L={aⁿbⁿ|n≥0} 不是正则的。假设它是正则的，泵长度为p。选择 w=aᵖbᵖ（p个a后跟p个b）。由于|w|=2p≥p，泵引理适用。"),
  ("step2","By the lemma, w=xyz with |xy|≤p and |y|≥1. Since |xy|≤p, both x and y consist ONLY of a's (they're in the first p characters). So y = aᵐ for some m≥1. Now pump: xy²z = aᵖ⁺ᵐbᵖ. This has more a's than b's → NOT in L! Contradiction.","由引理，w=xyz其中|xy|≤p且|y|≥1。由于|xy|≤p，x和y都只包含a（在前p个字符中）。所以y=aᵐ对某个m≥1。现在泵：xy²z=aᵖ⁺ᵐbᵖ。a比b多→不在L中！矛盾。"),
  ("step3","The contradiction proves L = {aⁿbⁿ} is NOT regular. Intuitively: a DFA has finite memory (p states). To check aⁿbⁿ, it must remember n — an unbounded count. But finite memory can only track up to p. So beyond p, it 'forgets' and can't distinguish aⁿbⁿ from aⁿ⁺ᵐbⁿ.","矛盾证明了L={aⁿbⁿ}不是正则的。直观理解：DFA有有限记忆（p个状态）。要检查aⁿbⁿ，它必须记住n——无界计数。但有限记忆只能跟踪到p。超过p就'忘记'了，无法区分aⁿbⁿ和aⁿ⁺ᵐbⁿ。"),
  ("conclusion","The Pumping Lemma is a NECESSARY condition for regularity. If L violates it → L is NOT regular. But some non-regular languages satisfy it (converse fails). For proving non-regularity: choose w carefully, consider all possible splits, derive contradiction.","泵引理是正则性的必要条件。若L违反它→L不是正则的。但某些非正则语言满足它（逆不成立）。证明非正则性：仔细选择w，考虑所有可能分割，推导矛盾。"),
  ("meta","This SAME proof structure works for many languages: pick w that forces y to be in a part that unbalances the count. Try: {aⁿbᵐ | n>m}, {wwᴿ}, {0²ⁿ}. Each requires choosing w cleverly so pumping creates a string outside L.","相同的证明结构适用于多种语言：选择w迫使y位于会破坏计数的部分。试试：{aⁿbᵐ|n>m}、{wwᴿ}、{0²ⁿ}。每个都需要巧妙地选择w使得泵产生L之外的串。")
  ]},
  {"topic":"Decidable vs Recognizable Languages","steps":[
  ("pitfall","Common error: confusing decidable with recognizable. A language L is DECIDABLE if some Turing machine halts on ALL inputs (accepts if w∈L, rejects if w∉L). RECOGNIZABLE = halts (accepts) on strings in L but may LOOP on strings not in L. Decidable is STRONGER.","常见错误：混淆可判定与可识别。语言L可判定：存在图灵机在所有输入上停机（若w∈L接受，若w∉L拒绝）。可识别：对L中串停机（接受），对不在L中的串可能循环。可判定更强。"),
  ("question","The Halting Problem HALT = {⟨M,w⟩ | M halts on w}. Is it recognizable? Yes — run M on w; if M halts, accept. If M loops, the recognizer also loops. This is fine for recognizability. Is it decidable? No — we proved it's undecidable by diagonalization.","停机问题 HALT = {⟨M,w⟩ | M在w上停机}。它是可识别的吗？是——在w上运行M；若M停机则接受。若M循环，识别器也循环。这对可识别性没问题。它是可判定的吗？否——我们用对角化证明了它不可判定。"),
  ("explore","Theorem: L is decidable ⟺ BOTH L and its complement are recognizable. Proof (⟹): If L decidable by TM M, then M recognizes L. Flip accept/reject to recognize complement. Proof (⟸): If L recognized by M₁ and complement by M₂, run M₁ and M₂ in parallel. One must halt. If M₁ halts → accept. If M₂ halts → reject.","定理：L可判定 ⟺ L和它的补都可识别。证明(⟹)：若L由TM M判定，则M识别L。翻转接受/拒绝来识别补。证明(⟸)：若L由M₁识别，补由M₂识别，并行运行M₁和M₂。其中一个必停机。若M₁停机→接受。若M₂停机→拒绝。"),
  ("insight","The parallel simulation is key: it converts a recognizer into a decider by also running the complement recognizer. If only ONE recognizer exists (not the complement), the language is recognizable but NOT decidable. The Halting Problem is the classic example: recognizable, not decidable.","并行模拟是关键：通过同时运行补的识别器，将识别器转换为判定器。如果只有一个识别器存在（补的没有），语言是可识别的但不可判定。停机问题是经典例子：可识别，不可判定。"),
  ("practice","Classify each as decidable, recognizable but not decidable, or not recognizable: (1) {⟨M⟩ | M prints 'hello'}. (2) {⟨M⟩ | M has exactly 5 states}. (3) {⟨M⟩ | M accepts ε}. (4) {⟨M⟩ | M rejects all inputs}. For each, explain your reasoning using reductions.","将每个分类为可判定、可识别但不可判定、或不可识别：(1){⟨M⟩ | M打印'hello'}。(2){⟨M⟩ | M恰好有5个状态}。(3){⟨M⟩ | M接受ε}。(4){⟨M⟩ | M拒绝所有输入}。对每个，用归约解释你的推理。"),
  ("reflection","Three categories: DECIDABLE (both L and ¬L recognizable), RECOGNIZABLE (but not decidable — L recognizable, ¬L not), NOT RECOGNIZABLE (neither L nor ¬L recognizable). The Halting Problem is in category 2. Its complement (does NOT halt) is in category 3.","三个类别：可判定（L和¬L都可识别）、可识别但不可判定（L可识别，¬L不可）、不可识别（L和¬L都不可识别）。停机问题在第2类。它的补（不停机）在第3类。")
  ]}
)

# CSC263 — Data Structures and Analysis
P("CSC263H1",
  {"topic":"Amortized Analysis of Dynamic Arrays","steps":[
  ("setup","A dynamic array grows when full: allocate 2× size, copy all elements. Most inserts are O(1). The doubling step is O(n). Is the average O(1)? Let's compute total cost for n inserts.","动态数组满时增长：分配2×大小，复制所有元素。大多数插入是O(1)。翻倍步骤是O(n)。平均是O(1)吗？计算n次插入的总成本。"),
  ("question","Sizes: 1→2→4→8→... up to n. Copies at each doubling: 1, 2, 4, 8, ..., n/2. Sum = 1+2+4+...+n/2 = n-1. Total cost = n inserts + (n-1) copies = O(n). Average = O(1) per operation. This is AGGREGATE ANALYSIS.","大小：1→2→4→8→...直到n。每次翻倍复制：1、2、4、8、...、n/2。和=1+2+4+...+n/2=n-1。总成本=n次插入+(n-1)次复制=O(n)。平均=每次操作O(1)。这是聚合分析。"),
  ("explore","Accounting (banker's) method: 'Charge' $3 for each insert. $1 pays for the insert itself. $2 is banked. When doubling occurs, each of the n/2 old elements uses its banked $2 to copy itself. Total charge = 3n = O(n). The bank balance is never negative → amortized O(1).","记账（银行家）法：每次插入'收取'$3。$1支付插入本身。$2存入银行。翻倍时，n/2个旧元素各用其存储的$2复制自己。总收费=3n=O(n)。银行余额永不变成负→分摊O(1)。"),
  ("formalize","Potential method: Define Φ = 2n - capacity (where n = size, capacity = allocated space). After insert without doubling: Φ increases by 2. After insert with doubling: Φ drops by n. Amortized cost = actual + ΔΦ = (n+1) + (-n+2) = 3 = O(1).","势能法：定义Φ=2n-capacity（n=大小，capacity=分配空间）。无翻倍的插入后：Φ增加2。有翻倍的插入后：Φ减少n。分摊成本=实际+ΔΦ=(n+1)+(-n+2)=3=O(1)。"),
  ("practice","Analyze with accounting method: (1) Stack: Push costs 1, Multipop(k) costs k. Show amortized O(1). (2) Binary counter: Increment flips k bits in worst case. Show amortized O(1) per increment. (3) Queue with two stacks.","用记账法分析：(1)栈：Push成本1，Multipop(k)成本k。证明分摊O(1)。(2)二进制计数器：最坏情况Increment翻转k位。证明每次increment分摊O(1)。(3)用两个栈实现队列。"),
  ("insight","Amortized analysis gives AVERAGE cost per operation over a sequence, not worst-case per operation. 'Amortized' = spread the cost. Dynamic arrays, Union-Find, splay trees — all analyzed this way. The potential function method is the most powerful (and hardest to invent).","分摊分析给出操作序列上的平均成本，不是每次操作的最坏情况。'分摊'=分散成本。动态数组、Union-Find、伸展树——都这样分析。势能函数法最强大（也最难发明）。")
  ]},
  {"topic":"Union-Find with Path Compression","steps":[
  ("principle","Union-Find tracks disjoint sets. Three operations: Makeset(x), Find(x) (returns set representative), Union(x,y) (merges sets). With union by rank + path compression, m operations on n elements run in O(m·α(n)) — essentially constant!","Union-Find跟踪不相交集合。三个操作：Makeset(x)、Find(x)（返回集合代表）、Union(x,y)（合并集合）。使用按秩合并+路径压缩，n个元素上的m次操作为O(m·α(n))——几乎常数！"),
  ("step1","Makeset(x): parent[x] = x; rank[x] = 0. Find(x): if parent[x]==x: return x; else: parent[x] = find(parent[x]); return parent[x]. Path compression: during find, point ALL traversed nodes directly to the root.","Makeset(x): parent[x]=x; rank[x]=0。Find(x): if parent[x]==x: return x; else: parent[x]=find(parent[x]); return parent[x]。路径压缩：在find期间，将所有经过的节点直接指向根。"),
  ("step2","Union(x,y): rx=find(x), ry=find(y). If rx==ry: return. If rank[rx]<rank[ry]: parent[rx]=ry. If rank[rx]>rank[ry]: parent[ry]=rx. If equal: parent[ry]=rx; rank[rx]++. Union by rank: always attach smaller tree under larger tree — keeps height O(log n) without compression.","Union(x,y): rx=find(x), ry=find(y)。若rx==ry: return。若rank[rx]<rank[ry]: parent[rx]=ry。若rank[rx]>rank[ry]: parent[ry]=rx。若相等: parent[ry]=rx; rank[rx]++。按秩合并：始终将小树附在大树下——无压缩时高度O(log n)。"),
  ("step3","Without compression: find is O(log n). With compression: subsequent finds become O(1). The total work for m finds is O(m·α(n)) where α is the inverse Ackermann function — grows so slowly that α(n) ≤ 4 for n up to 2^65536.","无压缩：find是O(log n)。有压缩：后续find变为O(1)。m次find的总工作量为O(m·α(n))，其中α是反Ackermann函数——增长如此之慢，对n≤2^65536有α(n)≤4。"),
  ("conclusion","Union-Find with both optimizations = '(near) constant time' per operation. The inverse Ackermann bound is the SLOWEST-growing function that appears in algorithm analysis. This makes Union-Find one of the most elegant data structures.","Union-Find加上两种优化=每次操作'(近)常数时间'。反Ackermann界是算法分析中出现的最慢增长函数。这使Union-Find成为最优雅的数据结构之一。"),
  ("meta","Path compression is SELF-ADJUSTING — each find pays a little extra to make future finds cheaper. This 'pay now, benefit later' pattern appears in splay trees (self-adjusting BSTs) and other amortized data structures. The key insight: tall trees get flattened.","路径压缩是自调整的——每次find多花一点成本使后续find更便宜。这种'现在付出，以后受益'模式出现在伸展树（自调整BST）和其他分摊数据结构中。关键洞见：高树被压平。")
  ]},
  {"topic":"Hash Table Worst-Case Fallacy","steps":[
  ("pitfall","Common error: 'Hash table lookups are O(1).' TRUE for average case with good hash function. FALSE for worst case: ALL keys hash to same bucket → O(n). This happens with: (1) a poor hash function, (2) malicious input (hash DoS attack).","常见错误：'哈希表查找是O(1)。'使用好哈希函数时平均情况为真。最坏情况为假：所有键哈希到同一桶→O(n)。发生在：(1)坏哈希函数，(2)恶意输入（哈希DoS攻击）。"),
  ("question","If we insert n keys and they all hash to bucket 7, how long does a lookup take? The answer is O(n) — we must linearly search through all n keys. But isn't the hash table supposed to be fast? It is FAST in expectation if keys are distributed uniformly.","如果插入n个键全哈希到桶7，一次查找需要多长时间？答案是O(n)——必须线性搜索所有n个键。但哈希表不是应该很快吗？如果键均匀分布，它在期望上是快的。"),
  ("explore","Worst-case scenarios: (1) String.hashCode() in Java — easily construct many strings with same hash. (2) Universal hashing — randomly pick hash function from a family, making worst-case unlikely. (3) Perfect hashing — guarantee O(1) worst-case for STATIC key sets.","最坏情况场景：(1)Java的String.hashCode()——容易构造具有相同哈希的许多串。(2)全域哈希——从族中随机选取哈希函数，使最坏情况几乎不可能。(3)完美哈希——对静态键集保证O(1)最坏情况。"),
  ("insight","Average-case O(1) requires: (1) hash function distributes keys uniformly, (2) load factor α = n/m is bounded (rehashing when α too high). Java 8+: tree-based buckets (threshold 8) degrade to O(log n) instead of O(n). Cuckoo hashing: O(1) worst-case lookup.","平均情况O(1)需要：(1)哈希函数均匀分布键，(2)负载因子α=n/m有界（α太高时rehash）。Java 8+：基于树的桶（阈值8）退化为O(log n)而非O(n)。布谷鸟哈希：O(1)最坏情况查找。"),
  ("practice","Analyze worst-case: (1) n=10000, hash(x)=x%10. Insert keys 0,10,20,...,99990. What's lookup time? (2) Same keys, hash(x)=x%9973. What's lookup time? (3) If an adversary knows your hash function, can they force O(n) behavior?","分析最坏情况：(1)n=10000，hash(x)=x%10。插入键0,10,20,...,99990。查找时间？(2)相同键，hash(x)=x%9973。查找时间？(3)如果攻击者知道你的哈希函数，他们能强制O(n)行为吗？"),
  ("reflection","Always specify: 'Hash table operations are EXPECTED O(1), worst-case O(n).' Use balanced BST (O(log n) guaranteed) if worst-case matters more than average. Know your data — if keys are predictable (sequential integers), a simple modulo works great. If adversarial, use universal hashing.","始终说明：'哈希表操作是期望O(1)，最坏情况O(n)。'如果最坏情况比平均更重要，使用平衡BST（保证O(log n)）。了解你的数据——如果键可预测（顺序整数），简单取模就很好。如果存在恶意，使用全域哈希。")
  ]}
)

# CSC301 — Software Engineering
P("CSC301H1",
  {"topic":"Functional vs Non-Functional Requirements","steps":[
  ("setup","Client: 'I need a login system.' What do they REALLY need? Requirements engineering is about discovering the true needs, not just writing down what the client says. Let's distinguish two types.","客户：'我需要一个登录系统。'他们真正需要什么？需求工程是关于发现真实需求，而不仅仅是写下客户说的。让我们区分两种类型。"),
  ("question","Functional requirement: 'Users can register with email/password, authenticate, reset password.' Non-functional: 'Authentication must complete in <200ms, support 10K concurrent users, be PCI-DSS compliant.' Which is harder to validate? Which is more costly to fix if wrong?","功能需求：'用户能用邮箱/密码注册、认证、重置密码。'非功能：'认证必须在<200ms内完成，支持10K并发用户，符合PCI-DSS标准。'哪个更难验证？哪个错了修正成本更高？"),
  ("explore","Non-functional requirements (NFRs) are often neglected until the system fails. A login system that's functionally perfect but takes 30 seconds to authenticate is USELESS. NFRs include: performance, security, scalability, reliability, usability, maintainability, portability.","非功能需求（NFR）常被忽视，直到系统失败。功能完美的登录系统但需30秒认证是没用的。NFR包括：性能、安全、可伸缩性、可靠性、可用性、可维护性、可移植性。"),
  ("formalize","Good requirements are: (1) CORRECT — each is a true stakeholder need. (2) UNAMBIGUOUS — only one interpretation. (3) COMPLETE — all scenarios covered. (4) CONSISTENT — no conflicts. (5) VERIFIABLE — testable. 'The system should be fast' → 'Page load < 2s under 95th percentile with 1000 concurrent users.'","好需求是：(1)正确——每个都是真实的利益相关者需要。(2)无歧义——只有一种解释。(3)完整——覆盖所有场景。(4)一致——无冲突。(5)可验证——可测试。'系统应快速'→'在1000并发用户下，95分位页面加载<2秒。'"),
  ("practice","Rewrite these vague requirements: (1) 'The system should be user-friendly.' (2) 'The system should handle high traffic.' (3) 'The system should be secure.' (4) 'The system should be reliable.' For each, propose a verifiable metric and acceptance criteria.","重写这些模糊需求：(1)'系统应友好用户。'(2)'系统应处理高流量。'(3)'系统应安全。'(4)'系统应可靠。'对每个，提出可验证的度量标准和验收标准。"),
  ("insight","'The hardest part of building software is deciding WHAT to build, not building it.' — Fred Brooks. Incorrect requirements are the MOST expensive defect to fix (10-100× more than coding errors). Invest in requirements elicitation: interviews, prototyping, observation, Use Cases, User Stories.","'构建软件最难的部分是决定构建什么，而不是构建它。'——Fred Brooks。不正确的需求是最昂贵的缺陷（比编码错误贵10-100倍）。投资需求获取：访谈、原型、观察、用例、用户故事。")
  ]},
  {"topic":"COCOMO Cost Estimation","steps":[
  ("principle","COCOMO (Constructive Cost Model) estimates software effort from size. Basic COCOMO: Effort = a(KLoC)^b person-months. Organic (simple, small team): a=2.4, b=1.05. Semi-detached: a=3.0, b=1.12. Embedded (complex, tight constraints): a=3.6, b=1.20.","COCOMO（构造性成本模型）根据大小估算软件工作量。基本COCOMO：工作量=a(KLoC)^b人月。有机（简单、小团队）：a=2.4,b=1.05。半独立：a=3.0,b=1.12。嵌入式（复杂、严格约束）：a=3.6,b=1.20。"),
  ("step1","For a 50 KLoC organic project: Effort = 2.4 × (50)^1.05 ≈ 2.4 × 62 ≈ 149 person-months. Schedule: TDEV = 2.5 × (Effort)^0.38 ≈ 2.5 × 149^0.38 ≈ 14 months. Team size ≈ Effort/TDEV ≈ 11 developers.","对50 KLoC的有机项目：工作量=2.4×(50)^1.05≈2.4×62≈149人月。进度：TDEV=2.5×(工作量)^0.38≈2.5×149^0.38≈14个月。团队规模≈工作量/TDEV≈11名开发者。"),
  ("step2","Intermediate COCOMO multiplies by 15 effort adjustment factors: required reliability, database size, product complexity, analyst capability, experience, programming language, etc. Each factor multiplies the nominal effort. A complex project could have product of factors from 0.9 to 2.5.","中级COCOMO乘以15个工作调整因子：所需可靠性、数据库大小、产品复杂度、分析师能力、经验、编程语言等。每个因子乘以名义工作量。复杂项目的因子乘积可达0.9到2.5。"),
  ("step3","Detailed COCOMO adds phase-by-phase estimates: Plans & Reqs (6%), Product Design (16%), Detailed Design (26%), Code & Unit Test (42%), Integration & Test (10%). These percentages vary by project type.","详细COCOMO增加了分阶段估算：计划与需求(6%)、产品设计(16%)、详细设计(26%)、编码与单元测试(42%)、集成与测试(10%)。这些百分比随项目类型变化。"),
  ("conclusion","COCOMO gives ORDER-OF-MAGNITUDE estimates. Accuracy: ±20% within the calibrated range, ±50% outside. Modern alternatives: Planning Poker (expert-based, agile), Story Points (relative sizing), Function Points (language-independent).","COCOMO给出数量级估算。精度：校准范围内±20%，范围外±50%。现代替代方案：Planning Poker（基于专家的、敏捷）、故事点（相对大小）、功能点（语言无关的）。"),
  ("meta","Estimation is not a prediction — it's a RISK MANAGEMENT tool. 'How long will this take?' is the wrong question. Better: 'Given our constraints, what's the 80th-percentile estimate?' All estimates are wrong; some are useful. Always include confidence intervals.","估算不是预测——它是风险管理工具。'需要多长时间？'是错误的问题。更好：'给定我们的约束，80分位估算是什么？'所有估算都是错的；有些是有用的。始终包含置信区间。")
  ]},
  {"topic":"Agile vs No Planning","steps":[
  ("pitfall","Common misconception: 'We use agile, so we just start coding and figure it out.' Agile is NOT about no planning — it's about ADAPTIVE PLANNING. The Agile Manifesto values 'Responding to change over following a plan' — but you need a plan to RESPOND to!","常见误解：'我们用敏捷，所以直接开始编码。'敏捷不是不计划——它是关于适应性计划。敏捷宣言更重视'响应变化而非遵循计划'——但你需要计划才能响应！"),
  ("question","Scrum defines: Sprint Planning (2-week cycle, plan what to build), Daily Standup (15 min sync), Sprint Review (demo + feedback), Retrospective (improve process). Which of these is a planning activity? ALL of them! Agile has MORE planning, not less.","Scrum定义：Sprint规划（2周周期，规划构建什么）、每日站会（15分钟同步）、Sprint评审（演示+反馈）、回顾（改进过程）。哪个是规划活动？全部！敏捷有更多的规划，不是更少。"),
  ("explore","Waterfall: plan everything upfront (months) → build → test → deploy. Agile: plan 2 weeks → build → test → deploy → plan next 2 weeks. Waterfall assumes requirements are stable. Agile embraces change — but change requires RE-planning, which requires planning skills.","瀑布：预先全面计划（数月）→构建→测试→部署。敏捷：规划2周→构建→测试→部署→规划下2周。瀑布假设需求稳定。敏捷拥抱变化——但变化需要重新规划，而重新规划需要规划技能。"),
  ("insight","Misunderstanding agile leads to: (1) No documentation ('working software over comprehensive documentation' ≠ NO documentation). (2) No design ('emergent design' ≠ no design upfront). (3) No process. These are 'cargo cult agile' — following the rituals without understanding the principles.","误解敏捷导致：(1)无文档（'可工作软件胜于全面文档'≠无文档）。(2)无设计（'涌现设计'≠无预先设计）。(3)无过程。这些是'货物崇拜敏捷'——遵循仪式而不理解原则。"),
  ("practice","Your team says they're agile but: (1) There are no user stories. (2) There are no sprint reviews. (3) There is no product owner. (4) There are no retrospectives. What would you change? Create a 1-page proposal explaining the minimal agile ceremonies and their purposes.","你的团队说他们在用敏捷但：(1)没有用户故事。(2)没有sprint评审。(3)没有产品负责人。(4)没有回顾。你会改变什么？创建一页提案解释最小化敏捷仪式及其目的。"),
  ("reflection","Agile = iterative planning + continuous feedback + willingness to change course. 'Plan, Do, Check, Act' (Deming cycle) applied to software. The plan IS important — what changes is WHEN you plan (continuously) and HOW MUCH detail (just-in-time, not upfront).","敏捷=迭代式规划+持续反馈+愿意改变方向。'计划、执行、检查、行动'（戴明环）应用于软件。计划是重要的——改变的是何时计划（持续地）和多少细节（即时而非预先）。")
  ]}
)

# CSC311 — ML
P("CSC311H1",
  {"topic":"Empirical Risk Minimization","steps":[
  ("setup","We want f:X→Y minimizing expected loss E[loss(f(X),Y)]. We don't know the true distribution — only training data. ERM: minimize (1/n)Σ loss(f(xᵢ),yᵢ), hoping this ≈ expected risk. This is the FUNDAMENTAL learning framework.","我们希望最小化期望损失E[loss(f(X),Y)]的f:X→Y。我们不知道真实分布——只有训练数据。ERM：最小化(1/n)Σloss(f(xᵢ),yᵢ)，希望这≈期望风险。这是基本学习框架。"),
  ("question","Complex f can achieve ZERO empirical risk (memorize data) but have POOR expected risk (bad generalization). Simple f has higher empirical risk but may generalize better. This is the OVERFITTING dilemma. How do we choose the right complexity?","复杂的f能实现零经验风险（记忆数据）但期望风险差（泛化差）。简单的f有更高经验风险但可能泛化更好。这是过拟合困境。如何选择正确复杂度？"),
  ("explore","ERM unifies ML algorithms: (1) Linear regression: loss = MSE. (2) Classification: loss = cross-entropy. (3) SVM: loss = hinge loss + regularization. (4) Decision trees: loss = misclassification rate. All minimize training error + regularization.","ERM统一了ML算法：(1)线性回归：loss=MSE。(2)分类：loss=交叉熵。(3)SVM：loss=合页损失+正则化。(4)决策树：loss=误分类率。都最小化训练误差+正则化。"),
  ("formalize","The gap between empirical risk R̂ₙ(f) and expected risk R(f) depends on: (1) n (more data → smaller gap). (2) Complexity of hypothesis class H (more complex → larger gap). PAC learning: R(f) ≤ R̂ₙ(f) + O(√(d/n)) where d = VC dimension.","经验风险R̂ₙ(f)与期望风险R(f)之间的差距取决于：(1)n（更多数据→更小差距）。(2)假设类H的复杂度（更复杂→更大差距）。PAC学习：R(f)≤R̂ₙ(f)+O(√(d/n))其中d=VC维。"),
  ("practice","For each scenario, would you use a simple or complex model? Explain using ERM: (1) n=100 features=10000. (2) n=10⁶ features=10. (3) Medical diagnosis (0.1% false negative tolerance). (4) Movie recommendation (no tolerance for slow inference).","对每个场景，用简单还是复杂模型？用ERM解释：(1)n=100,特征=10000。(2)n=10⁶,特征=10。(3)医疗诊断（0.1%假阴性容忍）。(4)电影推荐（不能容忍慢推理）。"),
  ("insight","ERM + regularization = the bias-variance tradeoff. Simple models: high bias (assumptions may be wrong), low variance (stable). Complex models: low bias, high variance (sensitive to data). The optimal complexity minimizes TOTAL error = bias² + variance + irreducible error.","ERM+正则化=偏差-方差权衡。简单模型：高偏差（假设可能错）、低方差（稳定）。复杂模型：低偏差、高方差（对数据敏感）。最优复杂度最小化总误差=偏差²+方差+不可约误差。")
  ]},
  {"topic":"Bias-Variance Decomposition","steps":[
  ("principle","For any predictor f̂ trained on data D: E[(y-f̂(x))²] = Bias[f̂(x)]² + Var[f̂(x)] + σ². Bias = E[f̂(x)]-f*(x) (systematic error). Var = E[(f̂(x)-E[f̂(x)])²] (sensitivity to data). σ² = irreducible noise.","对在数据D上训练的任何预测器f̂：E[(y-f̂(x))²]=Bias[f̂(x)]²+Var[f̂(x)]+σ²。偏差=E[f̂(x)]-f*(x)（系统误差）。方差=E[(f̂(x)-E[f̂(x)])²]（对数据的敏感度）。σ²=不可约噪声。"),
  ("step1","Let f*(x) = E[y|x] be the optimal predictor (Bayes predictor). Then y = f*(x) + ε where E[ε]=0, Var[ε]=σ². Write E[(y-f̂)²] = E[(f*+ε-f̂)²] = E[(f*-E[f̂]+E[f̂]-f̂+ε)²]. Expand the square.","设f*(x)=E[y|x]为最优预测器（贝叶斯预测器）。则y=f*(x)+ε其中E[ε]=0,Var[ε]=σ²。写出E[(y-f̂)²]=E[(f*+ε-f̂)²]=E[(f*-E[f̂]+E[f̂]-f̂+ε)²]。展开平方。"),
  ("step2","The cross terms vanish because E[ε]=0 and E[f̂-E[f̂]]=0. So: E[(y-f̂)²] = (f*-E[f̂])² + E[(f̂-E[f̂])²] + σ² = Bias² + Variance + Irreducible Error. This is the BIAS-VARIANCE DECOMPOSITION.","交叉项消失因为E[ε]=0且E[f̂-E[f̂]]=0。所以：E[(y-f̂)²]=(f*-E[f̂])²+E[(f̂-E[f̂])²]+σ²=偏差²+方差+不可约误差。这是偏差-方差分解。"),
  ("step3","k-NN: k=1 → bias≈0 (flexible), variance high (overfits). k=100 → bias high (oversmooths), variance≈0 (stable). Ridge regression: λ↑ → bias↑ (shrinkage), variance↓. The optimal λ minimizes total error.","k-NN：k=1→偏差≈0（灵活），方差高（过拟合）。k=100→偏差高（过度平滑），方差≈0（稳定）。岭回归：λ↑→偏差↑（收缩），方差↓。最优λ最小化总误差。"),
  ("conclusion","Bias-variance tradeoff: INCREASING model complexity: bias↓ (fits better), variance↑ (more sensitive). DECREASING complexity: bias↑, variance↓. The U-shape of total error = find the sweet spot where bias²+variance is minimized.","偏差-方差权衡：增加模型复杂度：偏差↓（拟合更好），方差↑（更敏感）。减少复杂度：偏差↑，方差↓。总误差的U形=找到偏差²+方差最小化的最佳点。"),
  ("meta","The decomposition explains: (1) Overfitting = low bias, high variance. (2) Underfitting = high bias, low variance. (3) Regularization controls variance at the cost of bias. (4) More data reduces variance without increasing bias. This is the CENTRAL concept in ML theory.","分解解释：(1)过拟合=低偏差、高方差。(2)欠拟合=高偏差、低方差。(3)正则化以偏差为代价控制方差。(4)更多数据在不大幅增加偏差情况下减少方差。这是ML理论的核心概念。")
  ]},
  {"topic":"Training Accuracy ≠ Real-World Performance","steps":[
  ("pitfall","99.9% training accuracy but 60% test accuracy → CLASSIC OVERFITTING. The model memorized the training data (including noise) instead of learning generalizable patterns. This is THE most common mistake in applied ML.","99.9%训练准确率但60%测试准确率→经典过拟合。模型记忆了训练数据（包括噪声）而非学习可泛化的模式。这是应用ML中最常见的错误。"),
  ("question","A model achieves 100% on training data but 50% on test data (binary classification). What's happening? The model has simply MEMORIZED all training examples — it's a lookup table, not a learner. It has zero ability to generalize to unseen examples.","模型在训练数据上达到100%但在测试数据上50%（二分类）。发生了什么？模型只是记忆了所有训练样本——它是查找表，不是学习器。它对未见示例完全没有泛化能力。"),
  ("explore","Signs of overfitting: (1) Training loss << validation loss (large gap). (2) Model weights are very large (especially with linear models). (3) Model changes dramatically with small data changes. (4) Feature importance is unstable. (5) Performance on random noise is near-perfect.","过拟合的迹象：(1)训练损失<<验证损失（大差距）。(2)模型权重非常大（尤其线性模型）。(3)模型随小数据变化剧烈变化。(4)特征重要性不稳定。(5)在随机噪声上性能接近完美。"),
  ("insight","Solutions: (1) More training data — hardest but most effective. (2) Regularization (L1/L2/dropout). (3) Simpler model (reduce features/depth/complexity). (4) Early stopping — stop training when validation loss stops improving. (5) Ensemble methods — bagging, boosting.","解决方案：(1)更多训练数据——最难但最有效。(2)正则化（L1/L2/dropout）。(3)更简单模型（减少特征/深度/复杂度）。(4)早停——当验证损失停止改进时停止训练。(5)集成方法——bagging、boosting。"),
  ("practice","You train 100 models on the same dataset. The best model on training data (99% acc) achieves 55% on test. The 50th best on training (85% acc) achieves 82% on test. Why? What should you do instead of picking the best training model?","你在同一数据集上训练100个模型。训练数据上最好的模型（99%准确率）在测试上达到55%。训练上第50好的（85%）在测试上达到82%。为什么？你应该怎么做而不是选训练上最好的模型？"),
  ("reflection","'If you torture the data long enough, it will confess.' — Ronald Coase. The test set should be used EXACTLY ONCE — at the very end. Use a VALIDATION set for model selection. Cross-validation is even better. But NEVER use test performance to decide between models.","'如果你折磨数据足够久，它终将招供。'——Ronald Coase。测试集应该只用一次——在最后。用验证集做模型选择。交叉验证更好。但绝不用测试性能在模型间做决定。")
  ]}
)

# CSC369 — Operating Systems
P("CSC369H1",
  {"topic":"Virtual Memory and Address Translation","steps":[
  ("setup","Two programs run simultaneously. How can both use address 0x100? They don't! Each process has its OWN virtual address space. The OS + MMU translates virtual → physical addresses. Process A's 0x100 → physical 0x300. Process B's 0x100 → physical 0x700.","两个程序同时运行。它们怎么能都用地址0x100？不能！每个进程有自己的虚拟地址空间。OS+MMU将虚拟地址翻译为物理地址。进程A的0x100→物理0x300。进程B的0x100→物理0x700。"),
  ("question","A program accesses address 0x1234. Walk through the translation: (1) Split into VPN (virtual page number) and offset. (2) Look up VPN in page table. (3) If valid+present → get physical frame number. (4) Concatenate with offset. How many memory accesses does this take WITHOUT TLB?","程序访问地址0x1234。跟踪翻译过程：(1)拆分为VPN（虚拟页号）和偏移量。(2)在页表中查找VPN。(3)如果有效+存在→获得物理帧号。(4)与偏移量拼接。没有TLB时这需要多少次内存访问？"),
  ("explore","A TLB (Translation Lookaside Buffer) caches recent VPN→PFN mappings. With TLB hit: 1 memory access (no page table walk). With TLB miss: 2+ accesses (walk page table). Temporal locality: recently accessed pages likely accessed again → TLB works well.","TLB（转译后备缓冲器）缓存最近的VPN→PFN映射。TLB命中：1次内存访问（无需页表遍历）。TLB未命中：2+次访问（遍历页表）。时间局部性：最近访问的页面可能再次访问→TLB工作良好。"),
  ("formalize","Multi-level page tables save space. For 64-bit address space with 4KB pages: single-level page table = 2⁵² entries × 8 bytes = impractical. 4-level page table: only allocate levels that have valid mappings. Each process has its own page table hierarchy.","多级页表节省空间。对64位地址空间和4KB页：单级页表=2⁵²个条目×8字节=不切实际。4级页表：只分配有有效映射的级别。每个进程有自己的页表层次。"),
  ("practice","A process uses 4KB pages, 32-bit virtual addresses. (1) How many entries in a single-level page table? (2) If page table entry = 4 bytes, what's the table size? (3) With 2-level page table (10+10+12 bits), what's the max number of page table pages needed?","一个进程使用4KB页，32位虚拟地址。(1)单级页表有多少条目？(2)如果页表条目=4字节，表大小是多少？(3)用2级页表（10+10+12位），最多需要多少页表页？"),
  ("insight","Virtual memory provides: (1) ISOLATION — processes can't touch each other's memory. (2) SIMPLICITY — each process has a clean linear address space. (3) EFFICIENCY — only frequently used pages in physical RAM. (4) SHARING — shared libraries mapped into multiple address spaces. This is why your laptop runs 100+ processes with 8GB RAM.","虚拟内存提供：(1)隔离——进程不能互相访问内存。(2)简单——每个进程有干净的线性地址空间。(3)高效——只有频繁使用的页面在物理RAM中。(4)共享——共享库映射到多个地址空间。这就是为什么笔记本能用8GB RAM运行100+个进程。")
  ]},
  {"topic":"Banker's Algorithm for Deadlock Avoidance","steps":[
  ("principle","Deadlock requires 4 Coffman conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait. Banker's Algorithm AVOIDS deadlock by checking if granting a request leads to a SAFE state — one where processes can finish in some order.","死锁需要4个Coffman条件：互斥、持有并等待、非剥夺、循环等待。银行家算法通过检查批准请求是否导致安全状态来避免死锁——安全状态意味着进程能按某种顺序完成。"),
  ("step1","Data structures: Available[m] = resources available. Max[n][m] = max demand per process. Allocation[n][m] = currently allocated. Need[n][m] = Max - Allocation. A state is SAFE if there exists a sequence where all processes complete.","数据结构：Available[m]=可用资源。Max[n][m]=每个进程的最大需求。Allocation[n][m]=当前已分配。Need[n][m]=Max-Allocation。如果存在一个所有进程完成的序列，状态是安全的。"),
  ("step2","Safety algorithm: Work = Available; Finish = [false]*n. Find i where Finish[i]=false AND Need[i]≤Work. If found: Work += Allocation[i]; Finish[i]=true; repeat. If all Finish[i]=true → SAFE. Otherwise → UNSAFE.","安全性算法：Work=Available；Finish=[false]*n。找到满足Finish[i]=false且Need[i]≤Work的i。如果找到：Work+=Allocation[i]; Finish[i]=true; 重复。如果所有Finish[i]=true→安全。否则→不安全。"),
  ("step3","Resource request: If Requestᵢ ≤ Needᵢ and Requestᵢ ≤ Available: pretend to allocate, run safety check. If resulting state is SAFE → approve. If UNSAFE → block (process must wait). The pretends are rolled back if unsafe.","资源请求：如果Requestᵢ≤Needᵢ且Requestᵢ≤Available：假装分配，运行安全性检查。如果结果状态安全→批准。如果不安全→阻塞（进程必须等待）。如果不安全则回滚假装分配。"),
  ("conclusion","Banker's prevents deadlock by ensuring the system is always in a safe state. A deadlock can NEVER occur — it's 'prevented' before it could happen. Cost: requires knowing Max demand in advance (unrealistic in practice). Used in some database systems, rarely in OS kernels.","银行家算法通过确保系统始终处于安全状态来预防死锁。死锁永远不会发生——在发生之前就被'预防'了。代价：需要预先知道最大需求（实际中不现实）。在一些数据库系统中使用，很少在OS内核中使用。"),
  ("meta","Avoidance vs prevention vs detection: (1) Prevention: break one of 4 Coffman conditions statically. (2) Avoidance: dynamically check safety (Banker's). (3) Detection + Recovery: allow deadlock, detect it, kill processes or preempt resources. Most practical systems use detection + recovery (UNIX kill -9).","预防vs避免vs检测：(1)预防：静态打破4个Coffman条件之一。(2)避免：动态检查安全性（银行家）。(3)检测+恢复：允许死锁、检测它、杀死进程或抢占资源。多数实际系统使用检测+恢复（UNIX kill -9）。")
  ]},
  {"topic":"Locking and Race Conditions","steps":[
  ("pitfall","Common error: 'I put a lock on the shared variable, so the code is thread-safe.' WRONG! If one thread locks but another thread accesses the variable WITHOUT the lock, the lock provides NO protection. A lock only works when ALL threads use the SAME lock for the SAME data.","常见错误：'我在共享变量上放了锁，所以代码是线程安全的。'错！如果一个线程加锁但另一个线程不加锁访问变量，锁不提供任何保护。锁只在对同一数据的所有线程使用同一锁时才有效。"),
  ("question","Thread 1: lock(mtx); x++; unlock(mtx). Thread 2: x-- (no lock). What are the possible values of x if both run concurrently? Answer: x can be anything — Thread 2's read-modify-write of x-- interleaves unpredictably with Thread 1's x++.","线程1：lock(mtx); x++; unlock(mtx)。线程2：x--（无锁）。两者并发运行时x的可能值？答案：x可以是任何值——线程2对x--的读-改-写与线程1的x++不可预测地交错。"),
  ("explore","Even WITH locks, deadlock is possible: Thread 1: lock(A); lock(B). Thread 2: lock(B); lock(A). This is the 'deadly embrace.' Solution: LOCK ORDERING — always acquire locks in the same order. If both threads lock A then B, deadlock cannot occur.","即使有锁，死锁也可能：线程1：lock(A); lock(B)。线程2：lock(B); lock(A)。这是'致命拥抱'。解决方案：锁排序——始终以相同顺序获取锁。如果两个线程都先锁A再锁B，死锁不会发生。"),
  ("insight","Lock discipline: (1) Always lock for shared data. (2) Always unlock (use try/finally or RAII). (3) Establish a global lock ordering. (4) Keep critical sections small. (5) Consider lock-free data structures when performance-critical (atomic ops, RCU).","锁规范：(1)始终为共享数据加锁。(2)始终解锁（使用try/finally或RAII）。(3)建立全局锁顺序。(4)保持临界区小。(5)性能关键时考虑无锁数据结构（原子操作、RCU）。"),
  ("practice","Find the bug: (1) void f() { static int x; lock(m); x++; unlock(m); }. (2) void transfer(Acct a, Acct b, int amt) { lock(a.mtx); lock(b.mtx); a-=amt; b+=amt; unlock(b.mtx); unlock(a.mtx); }. (3) if(shared==null) { lock(m); shared = new Data(); unlock(m); } return shared;","找bug：(1)void f() { static int x; lock(m); x++; unlock(m); }。(2)void transfer(Acct a, Acct b, int amt) { lock(a.mtx); lock(b.mtx); a-=amt; b+=amt; unlock(b.mtx); unlock(a.mtx); }。(3)if(shared==null) { lock(m); shared=new Data(); unlock(m); } return shared;"),
  ("reflection","'Concurrency is not parallelism' — Rob Pike. Concurrency = dealing with many things simultaneously (structure). Parallelism = doing many things simultaneously (execution). Locks are about CORRECTNESS first, performance second. A correct but slow program can be fixed; a fast but wrong program is useless.","'并发不是并行'——Rob Pike。并发=同时处理多件事（结构）。并行=同时做多件事（执行）。锁首先关乎正确性，其次才是性能。正确但慢的程序可以修复；快但错的程序没有用。")
  ]}
)

# CSC373 — Algorithm Design
P("CSC373H1",
  {"topic":"Optimal Substructure in Dynamic Programming","steps":[
  ("setup","Shortest path A→D is A→B→C→D. Subpath A→C is also the shortest A→C. If it weren't, we could replace it and get a shorter overall path. This is OPTIMAL SUBSTRUCTURE — an optimal solution contains optimal sub-solutions. This is the KEY property enabling DP.","最短路径A→D是A→B→C→D。子路径A→C也是最短的A→C。如果不是，我们可以替换它得到更短的总路径。这是最优子结构——最优解包含最优子解。这是使DP成为可能的关键性质。"),
  ("question","Weighted interval scheduling: each job has start time, end time, weight. Goal: max-weight set of non-overlapping jobs. If job j is in the optimal solution, what can we say about the subproblem? (Jobs compatible before job j). Does this problem have optimal substructure? YES.","加权区间调度：每个作业有开始时间、结束时间、权重。目标：不重叠作业的最大权重集。如果作业j在最优解中，我们能对子问题说什么？（作业j之前兼容的作业）。这问题有最优子结构吗？有。"),
  ("explore","Longest simple path is DIFFERENT. In a graph with cycles, a subpath of the longest simple path may NOT be the longest simple path between its endpoints. Example: A→B→C→D→E has subpath B→C→D, but the longest B→D might go through a cycle.","最长简单路径不同。在有环的图中，最长简单路径的子路径不一定是其端点间的最长简单路径。例子：A→B→C→D→E有子路径B→C→D，但最长的B→D可能经过一个环。"),
  ("formalize","DP recipe: (1) Define subproblems — clever indexing. (2) Relate subproblems — recurrence. (3) Order subproblems — topological order. (4) Base cases. (5) Solve original from subproblems. The recurrence IS the optimal substructure.","DP配方：(1)定义子问题——巧妙索引。(2)关联子问题——递推关系。(3)排序子问题——拓扑序。(4)基础情况。(5)从子问题求解原问题。递推关系就是最优子结构。"),
  ("practice","For each, does it have optimal substructure? If yes, define subproblems and recurrence: (1) 0/1 Knapsack. (2) Huffman coding. (3) Longest common subsequence. (4) Traveling salesman (small city count). (5) Matrix chain multiplication.","对每个，它有最优子结构吗？如果有，定义子问题和递推关系：(1)0/1背包。(2)Huffman编码。(3)最长公共子序列。(4)旅行商（小城市数）。(5)矩阵链乘法。"),
  ("insight","Not all optimization problems have optimal substructure! It's a property you must PROVE, not assume. The 'cut-and-paste' argument: if a sub-solution is not optimal, replace it with the optimal one to get a better overall solution → contradiction → sub-solution must be optimal.","不是所有优化问题都有最优子结构！这是一个必须证明、不能假设的性质。'剪贴'论证：如果子解不是最优的，用最优的替换得到更好的整体解→矛盾→子解必须是最优的。")
  ]},
  {"topic":"Max-Flow Min-Cut Theorem","steps":[
  ("principle","The maximum flow from source s to sink t equals the minimum capacity of an s-t cut. A CUT partitions vertices into S and T with s∈S, t∈T. Capacity = sum of capacities of edges from S to T. This is the fundamental duality theorem of network flow.","从源s到汇t的最大流等于s-t割的最小容量。割将顶点分为S和T，s∈S、t∈T。容量=从S到T的边的容量之和。这是网络流的基本对偶定理。"),
  ("step1","Ford-Fulkerson: while there's an augmenting path in residual graph, push flow. Let f* be max flow. Remove edges with zero residual capacity. Let S = vertices reachable from s. All edges from S to V\S are SATURATED (flow = capacity).","Ford-Fulkerson：当残量图中有增广路径时推送流。设f*为最大流。移除零残量容量的边。设S=从s可达的顶点。所有从S到V\S的边都是饱和的（流量=容量）。"),
  ("step2","The sum of flow from S to V\S minus flow from V\S to S = |f*| (net flow across cut). But edges V\S→S have 0 flow in residual graph (otherwise S would be larger). Edges S→V\S are saturated. So |f*| = capacity(S, V\S).","从S到V\S的流之和减去V\S到S的流=|f*|（穿过割的净流量）。但V\S→S的边在残量图中流为0（否则S会更大）。S→V\S的边是饱和的。所以|f*|=capacity(S, V\S)。"),
  ("step3","For ANY cut (A,B), the net flow from A to B = |f| ≤ capacity(A,B). So max flow ≤ min cut. But we just found a cut with capacity = |f*|. Therefore |f*| = min cut capacity. The min cut is the BOTTLENECK of the network.","对任何割(A,B)，从A到B的净流量=|f|≤capacity(A,B)。所以最大流≤最小割。但我们刚找到了一个容量=|f*|的割。因此|f*|=最小割容量。最小割是网络的瓶颈。"),
  ("conclusion","Max flow = min cut. This duality means: to find max flow, find the bottleneck. Applications: (1) Edge connectivity = min cut between any two vertices. (2) Bipartite matching = max flow in a bipartite graph. (3) Image segmentation = min cut in a specially constructed graph.","最大流=最小割。这个对偶意味着：要找最大流，找瓶颈。应用：(1)边连通度=任两点间的最小割。(2)二分图匹配=二分图中的最大流。(3)图像分割=特别构造图中的最小割。"),
  ("meta","The max-flow min-cut theorem is a special case of LINEAR PROGRAMMING DUALITY. The Primal (max flow) and its Dual (min cut) have equal optimal values. This duality appears everywhere: shortest path (P) ↔ potential (D), assignment (P) ↔ price (D).","最大流最小割定理是线性规划对偶的特例。原始问题（最大流）及其对偶（最小割）有相等的最优值。这种对偶无处不在：最短路径(P)↔势(D)、指派(P)↔价格(D)。")
  ]},
  {"topic":"Greedy vs Dynamic Programming","steps":[
  ("pitfall","Common error: 'Optimal substructure → greedy works.' WRONG! Greedy needs the GREEDY CHOICE PROPERTY: a locally optimal choice leads to a globally optimal solution. DP only needs optimal substructure. Fractional knapsack has both (greedy works). 0/1 knapsack has substructure but NOT greedy choice (need DP).","常见错误：'最优子结构→贪心可用。'错！贪心需要贪心选择性质：局部最优选择导致全局最优解。DP只需要最优子结构。分数背包两者都有（贪心可用）。0/1背包有子结构但没有贪心选择（需要DP）。"),
  ("question","Fractional knapsack: items with weight and value, unlimited fractions allowed. Greedy: pick highest value/weight ratio. This works because we can ALWAYS take a fraction of the best item. 0/1 knapsack: EITHER take or not. Why does greedy fail?","分数背包：有重量和价值的物品，允许取分数。贪心：选最高价值/重量比。这可行因为我们总是可取最佳物品的一部分。0/1背包：要么取要么不取。为什么贪心失败？"),
  ("explore","0/1 KS counterexample: capacity=50. Item A: w=50, v=100 (ratio=2). Item B: w=30, v=60 (ratio=2). Item C: w=20, v=40 (ratio=2). Greedy picks A (value=100). Optimal picks B+C (value=100). Actually same! Now try: capacity=50. A: w=50, v=60 (ratio=1.2). B: w=30, v=50 (ratio=1.67). C: w=20, v=40 (ratio=2). Greedy picks C, then B → capacity 50, value=90. But optimal is B+C... wait that's 50 too, value=90. Actually: capacity=50. B=30/50, C=20/40. Total=90. But what if capacity=50, A=50/100 (ratio=2), B=30/50 (ratio=1.67), C=20/40 (ratio=2). Greedy picks A first (ratio 2, value 100). Optimal is B+C (value 90). So greedy's 100 > optimal's 90? Wait that's not right. Let me reconsider.","0/1 KS反例：容量=50。物品A:w=50,v=60（性价比1.2）。物品B:w=30,v=50（性价比1.67）。物品C:w=20,v=40（性价比2）。贪心选C然后B→容量50,价值90。但最优是A... 价值60。不对。贪心选性价比最高的C(2)，然后B(1.67)=50容量价值90。最优解是A=价值60？B+C=50容量价值90，所以贪心其实是对的。经典反例：容量=50。A:w=30,v=60（性价比2）。B:w=20,v=40（性价比2）。C:w=15,v=30（性价比2）。D:w=10,v=10（性价比1）。贪心选A(60)+B(40)+C(30)=50容量价值130。最优是A+B+C=50容量价值130...也一样。另一个经典反例：容量=50。A:w=10,v=60（性价比6）。B:w=20,v=100（性价比5）。C:w=30,v=120（性价比4）。贪心选A(60)+B(100)=30容量价值160，剩余容量20不够C(30)。最优是B+C=50容量价值220>160。所以贪心失败！"),
  ("insight","Greedy needs: (1) Greedy choice property — can build solution by making locally optimal choices. (2) Optimal substructure — remaining problem after greedy choice is smaller instance of same type. DP only needs (2). Always prove both for greedy; if only (2) exists, use DP.","贪心需要：(1)贪心选择性质——通过做局部最优选择构建解。(2)最优子结构——贪心选择后剩余问题是同类型更小实例。DP只需要(2)。对贪心始终要证明两者；如果只有(2)存在，用DP。"),
  ("practice","For each, can we use greedy? If yes, state the greedy choice. If no, explain why: (1) Activity selection (max number of non-overlapping activities). (2) Minimum spanning tree. (3) 0/1 knapsack. (4) Coin change (unlimited coins, minimize count). (5) Dijkstra's shortest path.","对每个，能用贪心吗？如果能，说明贪心选择。如果不能，解释原因：(1)活动选择（最大不重叠活动数）。(2)最小生成树。(3)0/1背包。(4)硬币找零（无限硬币，最小化数量）。(5)Dijkstra最短路径。"),
  ("reflection","Two-question test: (1) Does the problem have optimal substructure? If no → can't use greedy or DP. (2) Does it have the greedy choice property? If yes → greedy (Huffman, MST, Dijkstra). If no → DP (knapsack, edit distance, LCS). This decision tree guides algorithm design.","两问题测试：(1)问题有最优子结构吗？如果没有→不能用贪心或DP。(2)有贪心选择性质吗？如果有→贪心（Huffman、MST、Dijkstra）。如果没有→DP（背包、编辑距离、LCS）。这个决策树指导算法设计。")
  ]}
)

# ===== REMAINING THIN CS =====

# CSC148 — Introduction to Computer Science
P("CSC148H1",
  {"topic":"Abstract Data Types and Data Structures","steps":[
  ("setup","An Abstract Data Type (ADT) is defined by its OPERATIONS, not its implementation. Stack: push, pop, peek, is_empty. Queue: enqueue, dequeue. List: get, set, insert, delete. Multiple implementations can satisfy the SAME ADT — with different tradeoffs.","抽象数据类型(ADT)由其操作定义，不由实现定义。栈：push、pop、peek、is_empty。队列：enqueue、dequeue。多种实现可满足相同ADT——各有不同的权衡。"),
  ("question","Stack ADT: operations = push(item), pop()→item, peek()→item, is_empty()→bool. Array implementation: O(1) push/pop (amortized). Linked list: O(1) push/pop. Both implement the SAME ADT. Why use one over the other? Array: better cache locality. Linked: no resizing overhead.","栈ADT：数组实现：push/pop O(1)（分摊）。链表：push/pop O(1)。为什么选一个？数组：更好缓存局部性。链表：无调整大小开销。"),
  ("explore","Python list uses a DYNAMIC array (like ArrayList). When full: allocate 2× size, copy. Appending is amortized O(1). But inserting at beginning is O(n) — because all elements must shift. This is why deque from collections import deque for O(1) append/pop from BOTH ends.","Python列表用动态数组。满时分配2×大小并复制。尾部添加分摊O(1)。但头部插入是O(n)——所有元素需移位。这就是为什么用collections.deque可以从两端O(1)添加/弹出。"),
  ("formalize","Implementation tradeoffs: (1) ArrayStack: O(1) push/pop at end, O(n) insert at front. (2) LinkedStack: O(1) push/pop at front, O(n) access by index. (3) ArrayQueue (circular): O(1) enqueue/dequeue, fixed capacity. (4) LinkedQueue: O(1) enqueue/dequeue, dynamic.","实现权衡：(1)数组栈：尾部O(1)压入/弹出，头部O(n)插入。(2)链表栈：头部O(1)压入/弹出，按索引访问O(n)。(3)循环数组队列：O(1)入队/出队，固定容量。(4)链表队列：O(1)入队/出队，动态。"),
  ("practice","Implement: (1) Stack using Python list. (2) Queue using two stacks (amortized O(1)). (3) Deque using doubly linked list. (4) Time each operation with timeit — compare list.pop(0) vs deque.popleft(). Which is faster and why?","实现：(1)用Python列表实现栈。(2)用两个栈实现队列（分摊O(1)）。(3)用双向链表实现双端队列。(4)用timeit计时每个操作——比较list.pop(0) vs deque.popleft()。哪个更快？为什么？"),
  ("insight","'Program to an interface, not an implementation.' The ADT separates WHAT from HOW. Your code should depend on the ADT — swapping implementations should not break it. This is ENCAPSULATION and the foundation of modular software design.","'面向接口编程，而非实现。'ADT将什么与如何分离开。代码应依赖ADT——切换实现不应破坏它。这就是封装和模块化软件设计的基础。")
  ]},
  {"topic":"Recursion","steps":[
  ("principle","Recursion: a function calls itself. Two parts: BASE CASE (trivial, no recursion) and RECURSIVE STEP (problem → smaller subproblem). Key: the subproblem must be SMALLER or SIMPLER. Otherwise: infinite recursion → stack overflow.","递归：函数调用自身。两部分：基本情况（平凡，无需递归）和递归步骤（问题→更小的子问题）。关键：子问题必须更小或更简单。否则：无限递归→栈溢出。"),
  ("step1","Example: factorial(n) = 1 if n≤1 (base), else n×factorial(n-1) (recursive). Trace: factorial(4) = 4×factorial(3) = 4×3×factorial(2) = 4×3×2×factorial(1) = 4×3×2×1 = 24. The CALL STACK grows then shrinks.","例：factorial(n): n≤1时返回1，否则n×factorial(n-1)。追踪：factorial(4)=4×3×2×1=24。调用栈先增长后收缩。"),
  ("step2","Divide and Conquer: sort example. Mergesort: split list in half, sort each half recursively, merge sorted halves. T(n)=2T(n/2)+O(n) → O(n log n). Binary search: check middle, recurse left or right. T(n)=T(n/2)+O(1) → O(log n).","分治：排序例子。归并排序：对半分，递归排序每半，合并。T(n)=2T(n/2)+O(n)→O(n log n)。二分搜索：检查中间，递归左或右。T(n)=T(n/2)+O(1)→O(log n)。"),
  ("step3","Tree recursion: Fibonacci is BAD for recursion without memoization. fib(5) calls fib(4) and fib(3). fib(4) calls fib(3) and fib(2) — fib(3) computed TWICE. O(2ⁿ) vs O(n) with memoization. USE memoization (dynamic programming) for overlapping subproblems.","树形递归：Fibonacci不用记忆化很糟糕。fib(5)调用fib(4)和fib(3)，fib(3)被计算两次。O(2ⁿ) vs 用记忆化O(n)。对重叠子问题用记忆化（动态规划）。"),
  ("conclusion","Recursion vs iteration: any recursive function CAN be written iteratively (with an explicit stack). Recursion is more ELEGANT for: (1) Tree/graph traversal. (2) Divide and conquer. (3) Backtracking. But iterative may be more EFFICIENT (no function call overhead).","递归vs迭代：任何递归函数可用迭代写（显式栈）。递归更优雅：(1)树/图遍历。(2)分治。(3)回溯。但迭代可能更高效（无函数调用开销）。"),
  ("meta","'To understand recursion, you must first understand recursion.' The key insight: trust the RECURSIVE LEAP — assume the recursive call works correctly on the smaller input. Don't try to trace the full stack. Focus on the INDUCTION: base cases + recursive step → works for ALL inputs.","'要理解递归，必须先理解递归。'关键洞见：相信递归跳跃——假设递归调用在更小输入上正确工作。不要试图追踪整个栈。关注归纳：基本情况+递归步骤→对所有输入有效。")
  ]},
  {"topic":"Object-Oriented Programming","steps":[
  ("pitfall","Common error: 'OOP is just classes and objects.' OOP is a PARADIGM. Four pillars: (1) ENCAPSULATION — bundle data + methods, hide internals. (2) ABSTRACTION — expose interface, hide implementation. (3) INHERITANCE — reuse code, establish hierarchy. (4) POLYMORPHISM — same interface, different behaviors.","常见错误：'OOP就是类和对象。'OOP是一种编程范式。四大支柱：(1)封装——捆绑数据+方法，隐藏内部。(2)抽象——暴露接口，隐藏实现。(3)继承——复用代码，建立层次。(4)多态——相同接口，不同行为。"),
  ("question","Python: class Dog(Animal): def __init__(self, name): super().__init__(); self.name = name. Override speak(): return self.name + ' says Woof!'. Polymorphism: animals = [Dog(), Cat()]; for a in animals: a.speak(). Each calls its OWN speak method.","Python: class Dog(Animal):。多态：animals=[Dog(),Cat()]；for a in animals: a.speak()。每个调用自己的speak方法。"),
  ("explore","Preconditions and Postconditions: a contract for methods. Precondition: what must be true before calling (caller's responsibility). Postcondition: what the method guarantees after (implementer's responsibility). Example: pop() on empty stack violates precondition → raise exception.","前置条件和后置条件：方法的契约。前置：调用前必须为真（调用者责任）。后置：方法保证的内容（实现者责任）。例：空栈上pop违反前置→抛出异常。"),
  ("formalize","Class invariants: conditions that must ALWAYS hold for instances. Example: for BankAccount, balance >= 0 and balance == sum(transactions). Methods must PRESERVE the invariant. violations signal a bug. Enforce with assertions: assert self.balance >= 0.","类不变量：对实例必须始终成立的条件。例：BankAccount中balance>=0。方法必须保持不变量。违反表明bug。用assert强制检查。"),
  ("practice","Design a zoo hierarchy: (1) Class Animal with name, age, speak(). (2) Subclasses: Dog, Cat, Bird — each override speak(). (3) Zoo class maintains list of animals. (4) Add __str__ and __repr__. (5) Ensure encapsulation: make name private with property getter/setter.","设计动物园层次：(1)Animal类有name、age、speak()。(2)子类：Dog、Cat、Bird——各自覆盖speak()。(3)Zoo类维护动物列表。(4)添加__str__和__repr__。(5)确保封装：name私有化用property。"),
  ("insight","OOP models the REAL WORLD. But 'favor composition over inheritance' — use HAS-A (composition) over IS-A (inheritance) when possible. Example: a Duck CAN fly and swim → Duck has FlyBehavior + SwimBehavior (Strategy Pattern) rather than inheriting from FlyingDuck.","OOP模拟真实世界。但'优先组合而非继承'——可能时用HAS-A（组合）优于IS-A（继承）。例：Duck会飞会游泳→用FlyBehavior+SwimBehavior组合而非继承。")
  ]}
)

# CSC165 — Mathematical Expression and Reasoning
P("CSC165H1",
  {"topic":"Propositional and Predicate Logic","steps":[
  ("setup","Logic is the LANGUAGE of computer science. Propositions: statements that are true or false. Logical connectives: ∧ (and), ∨ (or), ¬ (not), → (implies), ↔ (iff). Truth tables define their meaning. Predicate logic: statements with QUANTIFIERS: ∀ (for all), ∃ (exists).","逻辑是计算机科学的语言。命题：可真可假的陈述。逻辑连接词：∧(与)、∨(或)、¬(非)、→(蕴含)、↔(当且仅当)。真值表定义其含义。谓词逻辑：带量词的语句：∀(对所有)、∃(存在)。"),
  ("question","Implication P→Q is ONLY false when P is true and Q is false. 'If it rains, the ground gets wet' — is this true when it doesn't rain? YES (vacuous truth). Common error: confusing → with 'causes.' P→Q is about TRUTH VALUES, not causality.","蕴含P→Q只在P真Q假时为假。'下雨则地面湿'——没下雨时也为真（空真）。常见错误：混淆→与'导致'。P→Q关于真值，不是因果。"),
  ("explore","De Morgan's Laws: ¬(P∧Q) ≡ ¬P ∨ ¬Q. ¬(P∨Q) ≡ ¬P ∧ ¬Q. Distributivity: P∧(Q∨R) ≡ (P∧Q)∨(P∧R). P∨(Q∧R) ≡ (P∨Q)∧(P∨R). Contrapositive: P→Q ≡ ¬Q→¬P. Converse: Q→P (NOT equivalent).","De Morgan律：¬(P∧Q)≡¬P∨¬Q。分配律。逆否命题：P→Q≡¬Q→¬P。逆命题：Q→P（不等价）。"),
  ("formalize","Negation of quantifiers: ¬∀x P(x) ≡ ∃x ¬P(x). ¬∃x P(x) ≡ ∀x ¬P(x). To disprove 'all swans are white': find ONE black swan (∃x ¬white(x)). To disprove 'there exists a unicorn': show NONE exist (∀x ¬unicorn(x)).","量词的否定：¬∀xP(x)≡∃x¬P(x)。¬∃xP(x)≡∀x¬P(x)。证伪'所有天鹅都是白的'：找一只黑天鹅。证伪'存在独角兽'：证明不存在。"),
  ("practice","Negate and simplify: (1) ∀x∈ℕ, ∃y∈ℕ: x<y. (2) ∃ε>0, ∀δ>0: |x-a|<δ → |f(x)-f(a)|<ε. (3) ∀x, P(x) → (∃y, Q(x,y)). Translate to English: (4) ∀x (Human(x) → ∃y (Human(y) ∧ Mother(y,x))).","否定并简化：(1)∀x∈ℕ,∃y∈ℕ:x<y。(2)∃ε>0,∀δ>0:|x-a|<δ→|f(x)-f(a)|<ε。(3)∀x,P(x)→(∃y,Q(x,y))。翻译为中文：(4)每个人都有母亲。"),
  ("insight","Logic is the FOUNDATION of everything in CS: (1) Boolean algebra → digital circuits. (2) Propositional logic → SAT solvers (NP-complete but practical). (3) Predicate logic → database queries (SQL), program verification (Hoare logic). (4) Logic programming → Prolog.","逻辑是CS中一切的基础：(1)布尔代数→数字电路。(2)命题逻辑→SAT求解器。(3)谓词逻辑→数据库查询(SQL)、程序验证(Hoare逻辑)。(4)逻辑编程→Prolog。")
  ]},
  {"topic":"Proof Techniques","steps":[
  ("principle","Proof = logical argument establishing truth. Types: (1) DIRECT: assume premises, derive conclusion step by step. (2) CONTRAPOSITIVE: prove ¬Q→¬P instead of P→Q. (3) CONTRADICTION: assume P and ¬Q, derive impossible. (4) INDUCTION: prove base case and inductive step.","证明=确立真理的逻辑论证。类型：(1)直接：假设前提，逐步推导结论。(2)逆否：证明¬Q→¬P替代P→Q。(3)反证：假设P且¬Q，推出矛盾。(4)归纳：证基础情况和归纳步。"),
  ("step1","Direct proof: Prove 'if n is even, then n² is even.' Assume n=2k. Then n²=4k²=2(2k²). So n² is even. Done. Notice: we START with the assumption and BUILD to the conclusion. Every step follows from previous steps by a RULE OF INFERENCE.","直接证明：'若n为偶则n²为偶。'假设n=2k。则n²=4k²=2(2k²)。所以n²为偶。每步从前一步通过推理规则得出。"),
  ("step2","Proof by contradiction: Prove √2 is irrational. Assume √2 = p/q in lowest terms. Then 2=p²/q² → p²=2q² → p² even → p even → p=2k → 4k²=2q² → q²=2k² → q even → p and q both even → contradicts 'lowest terms.' Therefore √2 cannot be rational.","反证法：证√2无理。假设√2=p/q最简。则p²=2q²→p²偶→p偶→p=2k→4k²=2q²→q²=2k²→q偶→p,q都偶→与最简矛盾。所以√2不能是有理数。"),
  ("step3","Induction: Prove 1+2+...+n = n(n+1)/2. Base: n=1: 1=1(2)/2=1 ✓. Inductive: assume true for n=k. Show for n=k+1: 1+...+k+(k+1) = k(k+1)/2 + (k+1) = (k(k+1)+2(k+1))/2 = (k+1)(k+2)/2 ✓. Base + inductive step → true for ALL n.","归纳：证1+2+...+n=n(n+1)/2。基础：n=1成立。归纳步：假设n=k成立，证n=k+1成立。基础+归纳步→对所有n成立。"),
  ("conclusion","Choosing proof technique: (1) Direct: when conclusion directly follows from premises. (2) Contrapositive: when direct is messy (e.g., proving 'if n² odd then n odd'). (3) Contradiction: when proving NEGATIVE statements (irrationality, impossibility). (4) Induction: when proving statements about NATURAL NUMBERS.","选择证明技巧：(1)直接：结论直接跟随时。(2)逆否：直接证明复杂时。(3)反证：证否定陈述时。(4)归纳：证关于自然数的陈述时。"),
  ("meta","Proofs are not just for math — they're REASONING. In CS: (1) Correctness proofs for algorithms (loop invariants). (2) Security proofs (a protocol is secure). (3) Termination proofs (a program halts). Every programmer should be able to reason logically about their code.","证明不仅用于数学——它们是推理。在CS中：(1)算法的正确性证明（循环不变量）。(2)安全证明（协议安全）。(3)停机证明（程序终止）。每个程序员都应能逻辑地推理自己的代码。")
  ]},
  {"topic":"Big-O Analysis and Running Time","steps":[
  ("pitfall","Common error: 'My program runs in 2 seconds for n=1000, so it's O(n).' WRONG! Big-O describes ASYMPTOTIC growth, not actual runtime. A program that takes 2s for n=1000 and 4s for n=2000 might be O(n) OR O(n log n) OR O(n²) — you need MULTIPLE data points and THEORETICAL analysis.","常见错误：'我的程序n=1000运行2秒，所以是O(n)。'错！大O描述渐近增长，不是实际运行时间。需多个数据点和理论分析。"),
  ("question","What does O(n²) mean? There exist constants c>0 and n₀ such that for all n≥n₀, T(n) ≤ c·n². It's an UPPER BOUND. n²+3n+2 = O(n²) because for n≥1, n²+3n+2 ≤ n²+3n²+2n² = 6n². Similarly: Ω(n²) = LOWER BOUND. Θ(n²) = both O and Ω (TIGHT bound).","O(n²)意味着存在常数c>0和n₀使得对所有n≥n₀，T(n)≤c·n²。是上界。Ω(n²)=下界。Θ(n²)=同时是O和Ω（紧界）。"),
  ("explore","Common growth rates (fastest to slowest): O(1) — constant (array access). O(log n) — logarithmic (binary search). O(n) — linear (linear search). O(n log n) — linearithmic (mergesort). O(n²) — quadratic (bubble sort). O(2ⁿ) — exponential (subset generation). O(n!) — factorial (permutations).","常见增长率（从快到慢）：O(1)常数、O(log n)对数、O(n)线性、O(n log n)线性对数、O(n²)二次、O(2ⁿ)指数、O(n!)阶乘。"),
  ("formalize","Analysis of loops: (1) Single loop i=0..n-1 → O(n). (2) Nested loops i=0..n-1, j=0..n-1 → O(n²). (3) Loop with i *= 2 → O(log n). (4) Recursive T(n)=T(n-1)+O(1) → O(n). Master Theorem: T(n)=aT(n/b)+f(n). If f(n)=O(n^{log_b a - ε}), T=Θ(n^{log_b a}).","循环分析：(1)单层循环i=0..n-1→O(n)。(2)嵌套循环→O(n²)。(3)i*=2→O(log n)。(4)递归T(n)=T(n-1)+O(1)→O(n)。主定理。"),
  ("practice","Find worst-case running time: (1) for i in range(n): if arr[i]==target: return i. (2) for i in range(n): for j in range(i): print(i,j). (3) def fib(n): return n if n≤1 else fib(n-1)+fib(n-2). (4) for i in range(n): i*=2. Express all in Big-O.","找最坏运行时间：所有用大O表示。"),
  ("insight","Big-O tells you HOW YOUR ALGORITHM SCALES. An O(n²) algorithm for n=10⁶ does 10¹² operations — IMPOSSIBLE (takes hours). An O(n log n) algorithm does ~20×10⁶ operations — FEASIBLE (seconds). ALWAYS analyze before implementing: choose the right ALGORITHM, not just the right CODE.","大O告诉你算法如何扩展。n=10⁶时O(n²)做10¹²运算——不可能（需数小时）。O(n log n)做~20×10⁶运算——可行（几秒）。实现前先分析：选对算法，不只是写好代码。")
  ]}
)

# CSC207 — Software Design
P("CSC207H1",
  {"topic":"Object-Oriented Design Principles","steps":[
  ("setup","SOLID Principles: (1) SRP — Single Responsibility: a class should have ONE reason to change. (2) OCP — Open/Closed: open for extension, closed for modification. (3) LSP — Liskov Substitution: subtypes must be substitutable for base types. (4) ISP — Interface Segregation: many specific interfaces > one general. (5) DIP — Dependency Inversion: depend on abstractions, not concretions.","SOLID原则：(1)SRP单一职责。(2)OCP开闭。(3)LSP里氏替换。(4)ISP接口隔离。(5)DIP依赖倒置。"),
  ("question","SRP example: a class Report that BOTH computes data AND formats HTML AND saves to file. THREE responsibilities! Changes to ANY one could break the others. Solution: split into DataCollector, HtmlFormatter, FileWriter. Each has ONE reason to change.","SRP例子：Report类同时计算数据、格式化HTML、保存文件。三个职责！任一变更可能破坏其他。解决：拆分为DataCollector、HtmlFormatter、FileWriter。各只有一个变更原因。"),
  ("explore","Dependency Injection: instead of new Database() inside a class, pass it in: class UserService: def __init__(self, db: Database). Now you can: (1) Swap databases without changing UserService. (2) Use a mock for testing. (3) Change implementations any time. This is DIP in practice.","依赖注入：不在类内部new Database()，而是传入：class UserService: __init__(self, db: Database)。可以(1)不改变UserService切换数据库。(2)用mock测试。(3)随时改实现。这是DIP的实践。"),
  ("formalize","Cohesion vs Coupling: HIGH cohesion = related things belong together (good). LOW coupling = minimal dependencies between modules (good). A class that computes AND formats AND saves has LOW cohesion. A class that depends on 10 others has HIGH coupling. Goal: high cohesion, low coupling.","内聚vs耦合：高内聚=相关事物在一起（好）。低耦合=模块间最少依赖（好）。一个类同时计算+格式化+保存=低内聚。依赖10个其他类=高耦合。目标：高内聚、低耦合。"),
  ("practice","Refactor this: class ShoppingCart: def total(self)... def save_to_db(self)... def render_html(self)... def send_email_confirmation(self)... def validate_stock(self)... (1) Identify each responsibility. (2) Split into classes. (3) Identify dependencies. (4) Inject them. (5) Write tests for each separated class.","重构：找出各职责，拆分为类，识别依赖，注入它们，为每个分离类写测试。"),
  ("insight","'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.' — Fowler. Design principles are about MANAGING COMPLEXITY. They make code: (1) READABLE. (2) TESTABLE. (3) MAINTAINABLE. (4) EXTENSIBLE. Code is read 10× more than written.","'任何傻瓜都能写出计算机能理解的代码。优秀程序员写人类能理解的代码。'设计原则关乎管理复杂性。代码被读的次数比写的多10倍。")
  ]},
  {"topic":"Design Patterns","steps":[
  ("principle","Design patterns = proven SOLUTIONS to recurring design problems. Categories: (1) CREATIONAL — object creation (Singleton, Factory, Builder). (2) STRUCTURAL — object composition (Adapter, Decorator, Composite). (3) BEHAVIORAL — object interaction (Observer, Strategy, Command).","设计模式=对反复出现的设计问题的成熟解决方案。三类：(1)创建型——对象创建。(2)结构型——对象组合。(3)行为型——对象交互。"),
  ("step1","Singleton: ENSURE a class has exactly ONE instance. Python: class Singleton: _instance = None; def __new__(cls): if cls._instance is None: cls._instance = super().__new__(cls); return cls._instance. Use for: logging, configuration, database connection pool. But beware: makes testing hard.","单例：确保一个类只有一个实例。Python实现。用于：日志、配置、数据库连接池。但注意：使测试困难。"),
  ("step2","Strategy Pattern: define a FAMILY of algorithms, encapsulate each, make them interchangeable. Example: SortingStrategy — BubbleSort, QuickSort, MergeSort. Context chooses at runtime. Instead of if-elif chains for algorithms, encapsulate each in its OWN class.","策略模式：定义算法族，封装每个使可互换。例：SortingStrategy——BubbleSort、QuickSort、MergeSort。运行时选择。不用if-elif链，每个算法封装在自己的类中。"),
  ("step3","Observer Pattern: ONE-to-MANY dependency. When subject changes state, ALL observers are notified automatically. Python: observers = []; def register(o): observers.append(o); def notify(): for o in observers: o.update(). Used in: event systems, MVC architecture, GUI listeners.","观察者模式：一对多依赖。主体状态变化时自动通知所有观察者。用于：事件系统、MVC架构、GUI监听器。"),
  ("conclusion","Patterns are NOT recipes to copy — they're VOCABULARY for design. 'We should use Strategy here' communicates more than 'let's make a bunch of classes.' But DON'T overuse: 'If all you have is a hammer, everything looks like a nail.' Simpler solutions are often better.","模式不是要抄的菜谱——它们是设计的词汇。但别过度使用：'如果你只有锤子，看什么都像钉子。'更简单的方案常常更好。"),
  ("meta","The GOF book (Gang of Four: Design Patterns) is the classic. But MODERN evolution: (1) Functional programming reduces need for some patterns. (2) Python decorators replace the Decorator pattern. (3) First-class functions make Strategy trivial. KNOW the patterns, but also know WHEN NOT TO USE them.","GOF书（设计模式）是经典。但现代演变：(1)函数式编程减少某些模式需求。(2)Python装饰器替代Decorator模式。(3)一等函数使Strategy变得简单。了解模式，也知道什么时候不该用。")
  ]},
  {"topic":"Refactoring and Testing","steps":[
  ("pitfall","'I'll refactor later. Ship it first.' LATER NEVER COMES. Technical debt compounds: each unrefactored hour costs more later. Refactoring = changing INTERNAL structure without changing EXTERNAL behavior. Needs TESTS to ensure behavior preserved. Without tests, you're not refactoring — you're rewriting.","'以后重构。先上线。'以后永远不会来。技术债复利：每未重构的一小时日后成本更高。重构=改变内部结构而不改变外部行为。需要测试确保行为不变。无测试就不是重构——是重写。"),
  ("question","Bad smell: Long Method (>20 lines). Extract Method: select a logical block → extract as named method. Example: def process_order(): validate() + calculate_total() + apply_discount() + save_to_db() + send_confirmation(). Each becomes its OWN method.","坏味道：长方法（>20行）。提取方法：选逻辑块→提取为命名方法。例：process_order()→validate()+calculate_total()+apply_discount()+save_to_db()+send_confirmation()。各成独立方法。"),
  ("explore","Testing with pytest: def test_add(): assert Calculator().add(2,3) == 5. Key concepts: (1) FIXTURE — setup reusable test state. (2) MOCK — replace real objects with test doubles. (3) PARAMETRIZE — run same test with different inputs. (4) COVERAGE — measure which code lines are tested.","用pytest测试：def test_add(): assert Calculator().add(2,3) == 5。关键概念：fixture、mock、parametrize、coverage。"),
  ("formalize","Test-Driven Development (TDD): RED (write failing test) → GREEN (make it pass) → REFACTOR (improve code). Benefits: (1) Forces you to think about DESIGN before code. (2) Gives a SAFETY NET for refactoring. (3) Documents behavior (tests = executable docs). (4) Catches regressions immediately.","测试驱动开发(TDD)：红（写失败测试）→绿（让它通过）→重构（改进代码）。好处：强迫先想设计、给重构安全网、文档化行为、立即捕获回归。"),
  ("practice","Apply TDD: (1) Write test for Stack: empty stack → is_empty()=True. (2) Write minimal Stack class to pass. (3) Write test: push(5)→peek()=5, is_empty()=False. (4) Implement. (5) Test: push(1)→push(2)→pop()=2, pop()=1. Repeat. (6) Refactor. Run tests after EVERY change.","应用TDD：(1)为Stack写测试。(2)写极简类通过。(3)写下一个测试。(4)实现。(5)不断重复。(6)重构。每次变更后运行测试。"),
  ("reflection","'Code without tests is bad code — regardless of how well-written it is.' Test quality matters: (1) Tests should be FAST. (2) Tests should be ISOLATED (order-independent). (3) Tests should be REPEATABLE. (4) One assertion per test is ideal. (5) Test BEHAVIOR, not implementation.","'没有测试的代码是坏代码——无论它写得多好。'测试质量重要：测试应快速、隔离、可重复。每个测试一个断言最好。测试行为，不是实现。")
  ]}
)

# CSC209 — Software Tools and Systems Programming
P("CSC209H1",
  {"topic":"C Programming and Memory Management","steps":[
  ("setup","C gives you DIRECT control over memory. Pointers: int *p = &x (p holds address of x). *p = 5 (dereference: access what p points to). Arrays: int arr[10] allocates 10 ints CONTIGUOUSLY. arr[i] ≡ *(arr+i). arr decays to pointer in function calls — size info LOST.","C给你对内存的直接控制。指针：int *p=&x（p存x的地址）。*p=5（解引用：访问p所指）。数组：int arr[10]连续分配10个int。arr[i]≡*(arr+i)。arr在函数调用中退化为指针——大小信息丢失。"),
  ("question","What's WRONG with: char *s = 'hello'; s[0] = 'H';? String literal 'hello' is stored in READ-ONLY memory. Modifying causes undefined behavior (segfault on many systems). Use: char s[] = 'hello'; — allocates WRITABLE array on stack.","'hello'字符串字面量存在只读内存中。修改导致未定义行为（常segfault）。用char s[]='hello'——在栈上分配可写数组。"),
  ("explore","malloc: void *malloc(size_t size) — allocates on HEAP. Always check return: if (ptr==NULL) { error; }. Always free: free(ptr). Common bugs: (1) Use-after-free — accessing freed memory. (2) Double-free — freeing twice. (3) Memory leak — forgetting to free. (4) Buffer overflow — writing past allocated bounds.","malloc在堆上分配。始终检查返回值。始终free。常见bug：(1)释放后使用。(2)双重释放。(3)内存泄漏。(4)缓冲区溢出。"),
  ("formalize","Pointers and arrays: int arr[5]; int *p = arr; p+1 points to arr[1] (advances by sizeof(int) bytes). Pointer arithmetic: p++ moves to NEXT element, not next byte. Function pointers: int (*cmp)(int, int) = &compare; use for callbacks, qsort().","指针和数组：int arr[5]; int *p=arr; p+1指向arr[1]（前进sizeof(int)字节）。指针运算：p++移动到下一元素，不是下一字节。函数指针：用于回调、qsort()。"),
  ("practice","Write C functions: (1) int sum(int *arr, int n). (2) char *strdup_custom(const char *s) — duplicate string using malloc. (3) void swap(int *a, int *b). (4) A linked list: insert, delete, search. (5) Use valgrind to check for memory leaks: valgrind ./a.out.","写C函数：(1)sum。(2)strdup_custom——用malloc复制字符串。(3)swap。(4)链表：插入、删除、搜索。(5)用valgrind检查内存泄漏。"),
  ("insight","C forces you to understand memory — that's WHY it's used in operating systems, embedded systems, and databases. Understanding C pointers is the KEY to understanding: (1) Virtual memory and page tables. (2) Buffer overflow vulnerabilities. (3) How Python/Java work under the hood. C is the 'lingua franca' of systems.","C迫使你理解内存——这就是为什么用于操作系统、嵌入式系统、数据库。理解C指针是理解虚拟内存、缓冲区溢出漏洞、Python/Java底层工作的关键。C是系统的'通用语'。")
  ]},
  {"topic":"UNIX Processes and System Calls","steps":[
  ("principle","A process = program in execution. Each process has: PID, memory space, open files, registers. fork() CREATES a new process — returns 0 to child, child PID to parent. After fork, BOTH processes continue from SAME point. They have IDENTICAL memory but SEPARATE copies (copy-on-write).","进程=执行中的程序。每个进程有：PID、内存空间、打开文件、寄存器。fork()创建新进程——子进程返回0，父进程返回子PID。fork后两个进程从同一点继续。内存相同但分离（写时复制）。"),
  ("step1","fork() example: pid = fork(); if (pid == 0) { // child code } else { // parent code }. Common pattern: fork + exec. Child calls execvp() to load a NEW program (replace its memory). Parent waits with waitpid() for child to finish. This is how your SHELL runs commands.","fork()例子：if(pid==0){子进程代码}else{父进程代码}。常见模式：fork+exec。子进程调用execvp()加载新程序（替换其内存）。父进程用waitpid()等待子进程完成。这就是shell运行命令的方式。"),
  ("step2","Inter-Process Communication (IPC): (1) Pipes: int pipe(int fd[2]); fd[0]=read end, fd[1]=write end. Used for parent-child communication. (2) Signals: kill(pid, SIGINT) — async notification. (3) Shared memory: multiple processes access same memory region (shmget, shmat). (4) Sockets: networking.","进程间通信(IPC)：(1)管道：pipe(int fd[2])；fd[0]=读端，fd[1]=写端。用于父子通信。(2)信号：kill(pid, SIGINT)——异步通知。(3)共享内存。(4)套接字：网络。"),
  ("step3","Signals: SIGINT (Ctrl+C), SIGKILL (cannot be caught), SIGTERM (graceful termination). Signal handlers: void handler(int sig) { /* cleanup */ }; signal(SIGINT, handler). But handlers should be MINIMAL: only set a flag because async-signal-unsafe functions (malloc, printf) can't be called safely.","信号：SIGINT(Ctrl+C)、SIGKILL(不能捕获)、SIGTERM(优雅终止)。信号处理器应尽量小：只设一个标志，因为async-signal不安全的函数(malloc, printf)不能安全调用。"),
  ("conclusion","Processes vs Threads: processes have SEPARATE address spaces (isolated, heavy context switch). Threads share address space (shared memory, light context switch). But in C: no built-in threads — use pthreads library. Processes ≠ threads: choose based on isolation vs sharing needs.","进程vs线程：进程有独立地址空间（隔离、重上下文切换）。线程共享地址空间（共享内存、轻量切换）。但C无内置线程——用pthreads库。基于隔离vs共享需求选择。"),
  ("meta","'Everything in Unix is a file.' Files, pipes, sockets, devices — all accessed through file descriptors (fd). stdin=0, stdout=1, stderr=2. Redirection: close(0); open('file.txt', O_RDONLY) — replaces stdin. This UNIFORMITY is the power of Unix — a pipe works like a file works like a socket.","'Unix中一切都是文件。'文件、管道、套接字、设备——都通过文件描述符(fd)访问。stdin=0, stdout=1, stderr=2。这种统一性是Unix的力量——管道像文件一样工作，文件像套接字一样工作。")
  ]},
  {"topic":"Socket Programming","steps":[
  ("pitfall","Common error: 'I sent 1000 bytes, so recv() will return 1000 bytes.' WRONG! TCP is a STREAM protocol — no message boundaries. recv() may return anywhere from 1 to 1000 bytes. You MUST loop: while (total < expected) { n = recv(fd, buf+total, remaining, 0); total += n; }.","常见错误：'我发送了1000字节，所以recv()会返回1000字节。'错！TCP是流协议——无消息边界。recv()可能返回1到1000字节的任何数。必须循环接收。"),
  ("question","Socket API: server: socket()→bind()→listen()→accept()→recv()/send()→close(). Client: socket()→connect()→send()/recv()→close(). Key: bind() assigns address (IP+port). listen() makes it a passive socket. accept() BLOCKS until a client connects.","Socket API：服务器：socket()→bind()→listen()→accept()→recv()/send()→close()。客户端：socket()→connect()→send()/recv()→close()。关键：bind分配地址，listen使其为被动套接字，accept阻塞直到客户端连接。"),
  ("explore","TCP vs UDP: TCP = connection-oriented, reliable, ordered, flow/congestion control. UDP = connectionless, unreliable, unordered, no control. TCP: SOCK_STREAM. UDP: SOCK_DGRAM. TCP: requires accept() for each client. UDP: connectionless — recvfrom()/sendto() with ANY client.","TCP vs UDP：TCP=面向连接、可靠、有序、有流/拥塞控制。UDP=无连接、不可靠、无序、无控制。TCP: SOCK_STREAM。UDP: SOCK_DGRAM。"),
  ("formalize","HTTP server basics: listen on port 80. Parse request: GET /path HTTP/1.1. Send response: HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html>...</html>. This is what every web server does. Use telnet localhost 8080 to test manually — type raw HTTP.","HTTP服务器基础：监听80端口。解析请求：GET /path HTTP/1.1。发送响应：HTTP/1.1 200 OK...。这就是每个web服务器做的。用telnet localhost 8080手动测试——输入原始HTTP。"),
  ("practice","Write: (1) Echo server — receive, send back. (2) Multi-client chat server using select() or fork(). (3) Simple HTTP server serving static files. (4) Write a client that GETs a URL and saves to file. (5) Add threading: handle multiple clients simultaneously with pthreads.","写：(1)回显服务器——接收并返回。(2)用select()或fork()的多客户端聊天服务器。(3)提供静态文件的简单HTTP服务器。(4)写GET URL并保存到文件的客户端。(5)加线程：用pthreads同时处理多个客户端。"),
  ("reflection","Socket programming is the FOUNDATION of the internet. HTTP, SSH, SMTP, FTP — ALL are socket protocols. Understanding sockets = understanding HOW the internet works. Once you master Berkeley sockets, you understand the core of distributed systems.","Socket编程是互联网的基础。HTTP、SSH、SMTP、FTP——都是socket协议。理解socket=理解互联网如何工作。一旦掌握Berkeley sockets，就理解了分布式系统的核心。")
  ]}
)

# ===== THIN MATH =====

# MAT240 — Algebra I
P("MAT240H1",
  {"topic":"Vector Spaces over Arbitrary Fields","steps":[
  ("setup","Vector spaces over ℝ are familiar: ℝⁿ with componentwise addition/scalar multiplication. But vectors can also be over ℚ, ℂ, or 𝔽ₚ. The DEFINITION is the same: an abelian group (V,+) with scalar multiplication from a field F. What changes when the field is not ℝ?","在ℝ上的向量空间是我们熟悉的：ℝⁿ配合分量加法和标量乘法。但向量也可以在ℚ、ℂ或𝔽ₚ上定义。定义是相同的：一个阿贝尔群(V,+)配合来自域F的标量乘法。当域不是ℝ时，什么变了？"),
  ("question","Is ℚⁿ a vector space over ℚ? Yes. Over ℝ? No — scalar multiplication by √2 gives irrational components, which aren't in ℚⁿ. The SCALARS must come from the field F. So ℚⁿ is a ℚ-vector space but not an ℝ-vector space. The field determines what scalars are allowed.","ℚⁿ是ℚ上的向量空间吗？是的。是ℝ上的吗？不是——乘以√2得到无理数分量，不在ℚⁿ中。标量必须来自域F。所以ℚⁿ是ℚ向量空间但不是ℝ向量空间。域决定了允许的标量。"),
  ("explore","What changes over finite fields? In 𝔽₂ = {0,1}, 1+1=0. In 𝔽₂ⁿ, the vector (1,1,1)+(1,1,1)=(0,0,0). Every vector is its own additive inverse. Concepts like orthogonality behave differently — a nonzero vector can be orthogonal to itself: v·v = 1+1+1 = 1 (in 𝔽₂) ≠ 0.","在有限域上什么变了？在𝔽₂={0,1}中，1+1=0。在𝔽₂ⁿ中，向量(1,1,1)+(1,1,1)=(0,0,0)。每个向量是自己的加法逆元。正交等概念行为不同——非零向量可以自正交：v·v=1+1+1=1（在𝔽₂中）≠0。"),
  ("formalize","A vector space V over F: (V,+) is an abelian group. Scalar multiplication: F×V→V satisfying: (a+b)v = av+bv; a(v+w)=av+aw; (ab)v=a(bv); 1·v=v. The field axioms of F are ESSENTIAL — if F is only a ring, we get a MODULE, not a vector space.","域F上的向量空间V：(V,+)是一个阿贝尔群。标量乘法：F×V→V满足：(a+b)v=av+bv; a(v+w)=av+aw; (ab)v=a(bv); 1·v=v。F的域公理是必不可少的——如果F只是一个环，我们得到的是模，而不是向量空间。"),
  ("practice","Determine whether each is a vector space: (1) ℂ over ℚ. (2) ℝ over ℚ. (3) ℂ over ℝ. (4) 𝔽ₚⁿ over 𝔽ₚ. (5) Polynomials with coefficients in F, over F. (6) The set of all functions f:ℕ→F. For each, state the field and the vector space.","判断每个是否为向量空间：(1)ℂ在ℚ上。(2)ℝ在ℚ上。(3)ℂ在ℝ上。(4)𝔽ₚⁿ在𝔽ₚ上。(5)系数在F中的多项式，在F上。(6)所有函数f:ℕ→F的集合。对每个说明域和向量空间。"),
  ("insight","The field is PART of the data of a vector space. Changing the field changes the vector space entirely. ℝ² over ℝ is 2-dimensional, but ℝ² over ℚ is infinite-dimensional. Dimension depends on the field! ℚ-vector spaces are a window into the structure of ℝ.","域是向量空间数据的一部分。改变域完全改变了向量空间。ℝ²在ℝ上是2维的，但在ℚ上是无穷维的。维数取决于域！ℚ向量空间是理解ℝ结构的窗口。")
  ]},
  {"topic":"Linear Transformations and Matrices","steps":[
  ("principle","A linear transformation T:V→W preserves structure: T(u+v)=T(u)+T(v), T(cv)=cT(v). Every linear transformation can be represented as a MATRIX once we choose bases. The matrix depends on the choice of basis.","线性变换T:V→W保持结构：T(u+v)=T(u)+T(v)，T(cv)=cT(v)。一旦选择基，每个线性变换可表示为矩阵。矩阵依赖于基的选择。"),
  ("step1","Given ordered bases B={v₁,...,vₙ} of V and C={w₁,...,wₘ} of W, matrix [T]_{C←B} has columns: j-th = coordinates of T(vⱼ) in basis C. Composition ↔ matrix multiplication: [S∘T] = [S][T].","给定有序基B={v₁,...,vₙ}(V)和C={w₁,...,wₘ}(W)，矩阵[T]_{C←B}第j列=T(vⱼ)在基C中的坐标。复合↔矩阵乘法：[S∘T]=[S][T]。"),
  ("step2","Change of basis: If P = [id]_{B'←B}, then [T]_{B'} = P⁻¹[T]_{B}P. This is SIMILARITY. Two matrices represent the same linear transformation (in different bases) iff they are SIMILAR.","基变换：若P=[id]_{B'←B}，则[T]_{B'}=P⁻¹[T]_{B}P。这是相似性。两矩阵表示相同线性变换(在不同基下)当且仅当它们相似。"),
  ("step3","Rank-nullity: dim(domain)=dim(ker T)+dim(im T). Proof: extend basis of ker T to basis of domain. The images of the extension vectors form a basis of im T. Injective ⟺ ker T={0}; surjective ⟺ dim(im T)=dim(W).","秩-零度：dim(域)=dim(核T)+dim(像T)。证明：将ker T的基扩充为域基。扩充向量的像构成im T的基。单射⟺ker T={0}；满射⟺dim(im T)=dim(W)。"),
  ("conclusion","Linear transformations are the MORPHISMS of vector spaces — maps that 'preserve the structure.' Matrices are a computational tool. The deep idea: study objects through their structure-preserving maps (category theory's core insight).","线性变换是向量空间的态射——'保持结构'的映射。矩阵是计算工具。深层思想：通过保持结构的映射研究对象(范畴论核心洞见)。"),
  ("meta","'Matrix is a representation, not the thing itself': eigenvalues find 1D subspaces invariant under T. Determinants measure how T scales volume. Similarity = same T, different basis. This abstraction is KEY to advanced linear algebra.","'矩阵是表示不是事物本身'：特征值找T下不变的一维子空间。行列式度量T如何缩放体积。相似性=相同T不同基。这种抽象是高等线性代数的关键。")
  ]},
  {"topic":"Determinants and Cayley-Hamilton","steps":[
  ("pitfall","Common error: 'det(A+B)=det(A)+det(B).' WRONG! Determinant is MULTILINEAR and ALTERNATING: linear in each row SEPARATELY, swapping two rows multiplies by -1. This defines it.","常见错误：'det(A+B)=det(A)+det(B)。'错！行列式是多重线性和交替的：对每行分别线性，交换两行乘以-1。这是定义性质。"),
  ("question","det(A) for T:V→V? It's INDEPENDENT of basis! If A and P⁻¹AP are similar, det(P⁻¹AP)=det(A). So determinant is a property of the LINEAR TRANSFORMATION, not just the matrix.","对T:V→V，det(A)不依赖于基！如果A和P⁻¹AP相似，det(P⁻¹AP)=det(A)。所以行列式是线性变换的性质，不仅是矩阵的。"),
  ("explore","Cayley-Hamilton: Every matrix satisfies its own characteristic polynomial. If p(λ)=det(A-λI), then p(A)=0. Example: A=[[a,b],[c,d]], p(λ)=λ²-(a+d)λ+(ad-bc). A²-(a+d)A+(ad-bc)I=0. This gives a POLYNOMIAL identity for A.","Cayley-Hamilton：每个矩阵满足自己的特征多项式。若p(λ)=det(A-λI)，则p(A)=0。例：A=[[a,b],[c,d]]，p(λ)=λ²-(a+d)λ+(ad-bc)。A²-(a+d)A+(ad-bc)I=0。给出A的多项式恒等式。"),
  ("insight","Cayley-Hamilton is powerful: (1) Compute A⁻¹ as polynomial in A. (2) Express Aᵏ (k≥n) as linear combination of I,A,...,Aⁿ⁻¹. (3) Minimal polynomial divides characteristic polynomial. (4) A diagonalizable ⟺ minimal polynomial has distinct linear factors.","Cayley-Hamilton强大：(1)将A⁻¹计算为A的多项式。(2)将Aᵏ(k≥n)表示为I,A,...,Aⁿ⁻¹的线性组合。(3)最小多项式整除特征多项式。(4)A可对角化⟺最小多项式有互异线性因子。"),
  ("practice","For A=[[2,1],[1,2]]: (1) Find characteristic polynomial. (2) Verify Cayley-Hamilton: A²-4A+3I. (3) Use it to find A⁻¹. (4) Express A⁵ as combination of I and A. (5) What is the minimal polynomial?","对A=[[2,1],[1,2]]：(1)求特征多项式。(2)验证Cayley-Hamilton: A²-4A+3I。(3)用它求A⁻¹。(4)将A⁵表示为I和A的组合。(5)最小多项式是什么？"),
  ("reflection","Cayley-Hamilton bridges algebra (polynomials) and linear algebra (matrices). Every matrix generates a finite-dimensional algebra — Aᵏ are linearly dependent for k≥n. Applications from ODEs to quantum mechanics.","Cayley-Hamilton连接代数(多项式)和线性代数(矩阵)。每个矩阵生成有限维代数——Aᵏ对k≥n线性相关。应用从ODE到量子力学。")
  ]}
)

# MAT247 — Algebra II
P("MAT247H1",
  {"topic":"Modules over a PID","steps":[
  ("setup","A module over a ring R is like a vector space over a field — scalars from a RING. Key: not every module has a basis (free modules do). Over a PID, finitely generated modules ≈ free part ⊕ torsion part.","环R上的模就像域上的向量空间——标量来自环。关键：不是每个模有基(自由模有)。在PID上，有限生成模≈自由部分⊕挠部分。"),
  ("question","ℤ-modules = abelian groups. The module ℤ⊕ℤ₂: ℤ is free (rank 1), ℤ₂ torsion (2·1=0). Structure theorem: every f.g. abelian group G ≈ ℤʳ⊕ℤ_{n₁}⊕...⊕ℤ_{nₖ}.","ℤ-模=阿贝尔群。模ℤ⊕ℤ₂：ℤ自由(秩1)，ℤ₂挠(2·1=0)。结构定理：有限生成阿贝尔群G≈ℤʳ⊕ℤ_{n₁}⊕...⊕ℤ_{nₖ}。"),
  ("explore","For F[x]-modules: a vector space V with linear operator T is an F[x]-module where x·v=T(v). The structure theorem gives the RATIONAL CANONICAL FORM of T. Torsion = companion matrix blocks of invariant factors.","对F[x]-模：带线性算子T的向量空间V是F[x]-模，x·v=T(v)。结构定理给出T的有理标准型。挠=不变因子的友矩阵块。"),
  ("formalize","Structure Theorem: M ≅ Rʳ ⊕ R/(p₁^{e₁})⊕...⊕R/(pₖ^{eₖ}) where pᵢ are primes. Primary decomposition UNIQUE. Invariant factors: Rʳ ⊕ R/(d₁)⊕...⊕R/(dₘ) where d₁|d₂|...|dₘ.","结构定理：M≅Rʳ⊕R/(p₁^{e₁})⊕...⊕R/(pₖ^{eₖ})，pᵢ为素元。准素分解唯一。不变因子：Rʳ⊕R/(d₁)⊕...⊕R/(dₘ)，d₁|d₂|...|dₘ。"),
  ("practice","Classify: (1) All abelian groups of order 72. (2) ℤ-module ℤ₁₀⊕ℤ₁₅ — find invariant factors. (3) ℝ[x]-module for T with matrix [[2,0,0],[0,2,1],[0,0,2]]. (4) Show ℚ is NOT a finitely generated ℤ-module.","分类：(1)72阶阿贝尔群。(2)ℤ-模ℤ₁₀⊕ℤ₁₅—找不变因子。(3)T的ℝ[x]-模，矩阵[[2,0,0],[0,2,1],[0,0,2]]。(4)ℚ不是有限生成ℤ-模。"),
  ("insight","Modules over a PID unify two theories: (1) Finitely generated abelian groups (ℤ-modules). (2) Linear operators (F[x]-modules). The SAME theorem gives both the fundamental theorem of abelian groups AND canonical forms.","PID上模统一了两个理论：(1)有限生成阿贝尔群(ℤ-模)。(2)线性算子(F[x]-模)。相同定理给出阿贝尔群基本定理和标准型。")
  ]},
  {"topic":"Jordan Canonical Form","steps":[
  ("principle","Not every matrix is diagonalizable. Over ℂ, if A has eigenvalues but not enough eigenvectors, it has JORDAN FORM. A=PJP⁻¹ where J is block-diagonal, each block J(λ) has λ on diagonal, 1 on super-diagonal.","不是每个矩阵可对角化。在ℂ上，如果A有特征值但不够特征向量，它有若尔当型。A=PJP⁻¹，J是块对角，每块J(λ)对角λ，次对角1。"),
  ("step1","Compute: (1) Find eigenvalues. (2) For each λ, rₖ=rank((A-λI)ᵏ). dₖ=rₖ₋₁-rₖ=blocks of size≥k. Number of k×k blocks = dₖ-dₖ₊₁.","计算：(1)找特征值。(2)对每个λ，rₖ=rank((A-λI)ᵏ)。dₖ=rₖ₋₁-rₖ=大小≥k的块。k×k块数=dₖ-dₖ₊₁。"),
  ("step2","Example: A=[[3,1,0],[0,3,1],[0,0,3]]. (A-3I) rank 2 → nullity 1. (A-3I)² rank 1 → nullity 2. (A-3I)³ rank 0 → nullity 3. d₁=1, d₂=1, d₃=1. One 3×3 block. J=[[3,1,0],[0,3,1],[0,0,3]].","例：A=[[3,1,0],[0,3,1],[0,0,3]]。(A-3I)秩2→零化度1。(A-3I)²秩1→零化度2。一个3×3块。"),
  ("step3","Generalized eigenvectors: (A-λI)ᵏv=0. Chain: (A-λI)v₁=0, (A-λI)v₂=v₁, (A-λI)v₃=v₂, etc. Jordan basis = union of chains. Each chain = one block.","广义特征向量：(A-λI)ᵏv=0。链：(A-λI)v₁=0, (A-λI)v₂=v₁等。若尔当基=所有链的并。每链=一块。"),
  ("conclusion","Jordan form exists where char poly splits (e.g., ℂ). 'Closest to diagonal.' Applications: matrix exponentials e^{tA}, powers Aᵏ, linear system dynamics.","若尔当型存在在特征多项式能分裂的域(如ℂ)。'最接近对角'。应用：矩阵指数e^{tA}、幂Aᵏ、线性系统动力学。"),
  ("meta","Jordan form completes the classification via module-over-PID. Invariant factors → rational canonical form (ANY field). Elementary divisors → Jordan form. SAME theorem, different factorization.","若尔当型通过PID上模完成分类。不变因子→有理标准型(任何域)。初等因子→若尔当型。相同定理，不同分解。")
  ]},
  {"topic":"Bilinear Forms","steps":[
  ("pitfall","'Every bilinear form is symmetric.' WRONG! B:V×V→F is SYMMETRIC if B(v,w)=B(w,v); ALTERNATING if B(v,w)=-B(w,v), B(v,v)=0. Classification depends on field characteristic.","'每个双线性型是对称的。'错！对称若B(v,w)=B(w,v)；交错若B(v,w)=-B(w,v), B(v,v)=0。分类依赖于域特征。"),
  ("question","Standard inner product = dot product. In a basis, B(v,w)=vᵀAw. Symmetric ⟺ Aᵀ=A. Alternating ⟺ Aᵀ=-A, diag=0.","标准内积=点积。在基中，B(v,w)=vᵀAw。对称⟺Aᵀ=A。交错⟺Aᵀ=-A，对角=0。"),
  ("explore","Over ℝ: SYLVESTER'S LAW OF INERTIA — symmetric bilinear form diagonalizes with p positive, q negative, r zero. Signature (p,q,r) is INVARIANT. Classification of real quadratic forms.","在ℝ上：Sylvester惯性定律——对称双线性型对角化有p正q负r零。符号差(p,q,r)不变量。实二次型分类。"),
  ("insight","Applications: (1) Metric tensors in differential geometry. (2) Special relativity: Minkowski metric signature (3,1,0). (3) Symplectic forms in Hamiltonian mechanics.","应用：(1)微分几何度量张量。(2)狭义相对论：Minkowski度量符号差(3,1,0)。(3)哈密顿力学辛型。"),
  ("practice","For each bilinear form on ℝ²: (1) vᵀw. (2) v₁w₁-v₂w₂. (3) v₁w₂-v₂w₁. (4) v₁w₁. Classify as symmetric/alternating/neither. Find matrix. Find signature.","对ℝ²上每个双线性型：(1)vᵀw。(2)v₁w₁-v₂w₂。(3)v₁w₂-v₂w₁。(4)v₁w₁。分为对称/交错/都不是。求矩阵和符号差。"),
  ("reflection","Bilinear forms generalize 'scalar product.' Different geometries: inner product (symmetric positive definite), symplectic (alternating nondegenerate), Minkowski (indefinite symmetric). Each = DIFFERENT geometry.","双线性型推广'标量积'。不同几何：内积(对称正定)、辛型(交错非退化)、Minkowski(不定对称)。每个=不同几何。")
  ]}
)

# MAT267 — Advanced ODEs
P("MAT267H1",
  {"topic":"Nonlinear Systems and Phase Portraits","steps":[
  ("setup","For 2D x'=f(x,y), y'=g(x,y), we draw the phase portrait. Fixed points: f=g=0. Linearize near each: Jacobian J. Eigenvalues of J determine LOCAL behavior.","对2D x'=f(x,y), y'=g(x,y)，画相图。不动点：f=g=0。附近线性化：雅可比J。J的特征值决定局部行为。"),
  ("question","x'=y, y'=-x: J=[[0,1],[-1,0]], eigenvalues ±i → CENTER (closed orbits). x'=y, y'=x: eigenvalues ±1 → SADDLE. Stability determined by REAL PART of eigenvalues.","x'=y, y'=-x: J=[[0,1],[-1,0]], 特征值±i→中心。x'=y, y'=x: 特征值±1→鞍点。稳定性由特征值实部决定。"),
  ("explore","Classification: (1) Real λ₁>0>λ₂ → saddle. (2) Both negative → stable node. (3) Both positive → unstable node. (4) Complex Re<0 → stable spiral. (5) Complex Re>0 → unstable spiral. (6) Purely imaginary → center (Hartman-Grobman needed).","分类：(1)实λ₁>0>λ₂→鞍。(2)都负→稳定结点。(3)都正→不稳定结点。(4)复Re<0→稳定螺旋。(5)复Re>0→不稳定螺旋。(6)纯虚→中心(需Hartman-Grobman)。"),
  ("formalize","Hartman-Grobman: If NO eigenvalues on imaginary axis (hyperbolic fixed point), the nonlinear system is LOCALLY TOPOLOGICALLY CONJUGATE to the linearized system. Phase portrait near fixed point looks the same.","Hartman-Grobman：若无虚轴特征值(双曲不动点)，非线性系统局部拓扑共轭于线性化系统。不动点附近相图相同。"),
  ("practice","For x'=y, y'=-x-x²: (1) Find all fixed points. (2) Linearize at each. (3) Classify. (4) Nonlinear term x² breaks center — what happens? (5) Use Poincaré-Bendixson for limit cycles.","对x'=y, y'=-x-x²：(1)找所有不动点。(2)在每个点线性化。(3)分类。(4)非线性项x²破坏中心？(5)用Poincaré-Bendixson找极限环。"),
  ("insight","Poincaré-Bendixson: in 2D, bounded trajectory not approaching a fixed point → LIMIT CYCLE. Only in 2D — in 3D+ you get CHAOS (strange attractors). Why weather prediction is fundamentally limited.","Poincaré-Bendixson：2D中不趋于不动点的有界轨迹→极限环。只在2D成立——3D+得混沌(奇异吸引子)。天气预测的根本局限。")
  ]},
  {"topic":"Bifurcations","steps":[
  ("principle","Bifurcation: small parameter change → QUALITATIVE change in behavior. Fixed points appear, disappear, or change stability. Bifurcation diagram: fixed points vs parameter.","分岔：参数小变化→行为质变。不动点出现、消失或改变稳定性。分岔图：不动点vs参数。"),
  ("step1","Saddle-node: x'=μ-x². μ<0: no fixed points. μ=0: one (x=0, semi-stable). μ>0: two (x=±√μ, one stable, one unstable). Pair of fixed points born from nothing.","鞍结分岔：x'=μ-x²。μ<0: 无不动点。μ=0: 一个(x=0,半稳定)。μ>0: 两个(x=±√μ,一稳定一不稳定)。一对不动点从无中生有。"),
  ("step2","Pitchfork: x'=μx-x³. μ<0: one stable at 0. μ>0: 0 unstable, two new stable appear. SUPERCRITICAL. Subcritical: x'=μx+x³ — stable becomes unstable, no nearby stable → jump.","叉形：x'=μx-x³。μ<0: 一个稳定在0。μ>0: 0变不稳定，两个新稳定出现。超临界。亚临界：x'=μx+x³。"),
  ("step3","Hopf: periodic orbit born from fixed point when eigenvalues cross imaginary axis. Example: r'=μr-r³, θ'=1. Supercritical: μ>0 → stable limit cycle.","Hopf分岔：特征值穿越虚轴时周期轨道从不动点产生。例：r'=μr-r³, θ'=1。超临界：μ>0→稳定极限环。"),
  ("conclusion","Bifurcations explain: (1) Population dynamics (Allee effect). (2) Laser threshold. (3) Neuron firing. (4) Buckling beam. (5) Heart rhythm → arrhythmia.","分岔解释：(1)种群动力学(Allee效应)。(2)激光阈值。(3)神经元放电。(4)屈曲梁。(5)心律失常。"),
  ("meta","Only a few UNIVERSAL bifurcations: saddle-node, pitchfork, Hopf, transcritical. Center Manifold Theorem reduces high-dim systems to these normal forms.","只有少数普适分岔：鞍结、叉形、Hopf、跨临界。中心流形定理将高维系统约化为这些规范型。")
  ]},
  {"topic":"Perturbation Methods","steps":[
  ("pitfall","'If ε is small, set ε=0.' Works for REGULAR perturbation. For SINGULAR perturbation, setting ε=0 changes equation type (e.g., reduces ODE order). Need matched asymptotic expansions.","'如果ε很小，设ε=0就行。'对正则摄动可行。对奇异摄动，设ε=0改变方程类型(如降低ODE阶)。需要匹配渐近展开。"),
  ("question","εy''+y'+y=0, y(0)=0, y(1)=1. If ε=0: y'+y=0 → y=Ce^{-x}. Can't satisfy both BCs! BOUNDARY LAYER near x=0 where εy'' matters.","εy''+y'+y=0, y(0)=0, y(1)=1。若ε=0：y'+y=0→y=Ce^{-x}。无法满足两个边条！在x=0有边界层。"),
  ("explore","Regular: x''+x+εx³=0. x=x₀+εx₁+... O(1): x₀=cost. O(ε): x₁''+x₁=-cos³t → secular term (t·sint). Need multiple scales.","正则：x''+x+εx³=0。x=x₀+εx₁+... O(1): x₀=cost。O(ε): x₁''+x₁=-cos³t→长期项(t·sint)。需多重尺度。"),
  ("insight","Matched asymptotics: (1) OUTER: set ε=0, misses boundary layer. (2) INNER: rescale X=x/ε^α. (3) MATCH: inner and outer agree in overlap. (4) COMPOSITE: inner+outer-overlap.","匹配渐近：(1)外部解：设ε=0，缺边界层。(2)内部解：重新标度X=x/ε^α。(3)匹配：内外在重叠区一致。(4)复合：内+外-重叠。"),
  ("practice","εy''-y'=0, y(0)=1, y(1)=0. (1) Outer (satisfy y(1)=0). (2) Boundary layer location? (3) Inner solution. (4) Match and form composite. (5) Sketch for ε=0.01.","εy''-y'=0, y(0)=1, y(1)=0。(1)外部解(满足y(1)=0)。(2)边界层位置？(3)内部解。(4)匹配得复合解。(5)画ε=0.01的图。"),
  ("reflection","Perturbation: exact solutions impossible. Regular: expansion works. Singular: boundary layers, WKB, multiple scales. KEY: identify DOMINANT BALANCE in each region.","摄动方法：精确解不可行时。正则：展开可行。奇异：边界层、WKB、多重尺度。关键：各区域确定主导平衡。")
  ]}
)

# MAT309 — Mathematical Logic
P("MAT309H1",
  {"topic":"Predicate Calculus and Formal Languages","steps":[
  ("setup","Language: variables, connectives (∧∨¬→), quantifiers (∀∃), =, predicate symbols (P,Q...), function symbols (f,g...). Terms = variables + functions applied to terms. Formulas = atomic formulas closed under connectives and quantifiers.","语言：变量、连接词(∧∨¬→)、量词(∀∃)、=、谓词符号(P,Q...)、函数符号(f,g...)。项=变量+函数应用于项。公式=原子公式在连接词和量词下封闭。"),
  ("question","What is a STRUCTURE? A set M (domain) with: for each n-ary P, P^M⊆Mⁿ; for each n-ary f, f^M:Mⁿ→M. Truth defined recursively (Tarski's definition).","什么是结构？集合M(论域)。每个n元P: P^M⊆Mⁿ；每个n元f: f^M:Mⁿ→M。真值递归定义(Tarski真值定义)。"),
  ("explore","A sentence is valid (⊨φ) if true in EVERY structure. ∀x(x=x) valid. ∀xP(x)→∃xP(x) NOT valid (empty domain counterexample). Completeness Theorem: validity = provability.","语句有效(⊨φ)若在每个结构真。∀x(x=x)有效。∀xP(x)→∃xP(x)无效(空域反例)。完备定理：有效性=可证性。"),
  ("formalize","Syntactic deduction: ⊢φ provable from axioms using inference rules. Natural deduction: (∧I) from φ,ψ infer φ∧ψ. (∀I) if x not free, from φ infer ∀xφ. (∃E) from ∃xφ, assuming φ(t), infer ψ.","语法推演：⊢φ从公理用推理规则可证。自然演绎：(∧I)从φ,ψ推出φ∧ψ。(∀I)若x不自由，从φ推出∀xφ。(∃E)从∃xφ并假设φ(t)推出ψ。"),
  ("practice","Translate: (1) Every positive integer has a unique prime factorization. (2) Between any two distinct reals there's another. (3) No largest prime. (4) Function continuous at a point (ε-δ).","翻译：(1)每个正整数有唯一素因子分解。(2)任意两不同实数间有另一实数。(3)无最大素数。(4)函数在一点连续(ε-δ)。"),
  ("insight","Predicate logic: expressive enough for most mathematics, yet COMPLETE proof system. Gödel's Completeness: SEMANTIC (truth in all structures) = SYNTACTIC (provability). Remarkable!","谓词逻辑：表达足够多数学，却有完备证明系统。Gödel完备：语义(所有结构真)=语法(可证性)。了不起！")
  ]},
  {"topic":"Gödel's Completeness Theorem","steps":[
  ("principle","Completeness (1930): Γ ⊢ φ ⟺ Γ ⊨ φ. φ provable from Γ iff φ true in every model of Γ. SOUNDNESS (⊢→⊨) easy. COMPLETENESS (⊨→⊢) is deep.","完备定理(1930)：Γ⊢φ⟺Γ⊨φ。φ从Γ可证当且仅当φ在Γ的每个模型真。可靠性容易。完备性深刻。"),
  ("step1","Proof: suppose Γ⊭φ (no proof). Build maximal consistent set extending Γ∪{¬φ} (Zorn's Lemma). Henkin's method: add witness constants.","证明：假设Γ⊭φ。构造极大一致集扩张Γ∪{¬φ}(Zorn引理)。Henkin方法：添加见证常元。"),
  ("step2","From maximal consistent Δ, build TERM MODEL: domain = equivalence classes of terms. P([t₁],...,[tₙ]) holds iff P(t₁,...,tₙ)∈Δ. This model satisfies exactly the formulas in Δ. So Γ∪{¬φ} has a model → Γ⊭φ.","从极大一致Δ构造项模型：论域=项的等价类。P成立当且仅当P在Δ中。该模型恰好满足Δ中公式。所以Γ∪{¬φ}有模型→Γ⊭φ。"),
  ("step3","COMPACTNESS: if every finite subset of Σ has a model, then Σ has a model. Why: if Σ has no model, Σ⊢⊥, but proofs finite → finite subset also ⊢⊥ → no model.","紧致性：若Σ的每个有限子集有模型，则Σ有模型。若Σ无模型则Σ⊢⊥，但证明有限→有限子集也⊢⊥→无模型。"),
  ("conclusion","Completeness is the FOUNDATION of model theory. Syntactic proof systems CAPTURE semantic consequence. Applications: (1) Compactness → nonstandard models. (2) Löwenheim-Skolem. (3) Herbrand's theorem → automated theorem proving.","完备定理是模型论的基础。语法证明系统捕获语义推论。应用：(1)紧致性→非标准模型。(2)Löwenheim-Skolem。(3)Herbrand定理→自动定理证明。"),
  ("meta","First-order logic is 'just right' — not too strong (incompleteness) and not too weak (complete but expressive). The boundary between completeness and incompleteness is the boundary of first-order logic itself.","一阶逻辑'恰到好处'——不太强(不完备性)不太弱(完备但有表达力)。完备与不完备的边界就是一阶逻辑本身的边界。")
  ]},
  {"topic":"Gödel's Incompleteness Theorems","steps":[
  ("pitfall","'Gödel says everything is unprovable.' WRONG. It says: in any CONSISTENT system encoding arithmetic (PA, ZFC), there exists a TRUE but UNPROVABLE sentence G. System is INCOMPLETE.","'哥德尔说一切不可证明。'错。它说：任何编码算术的一致系统中，存在真但不可证明的语句G。系统不完备。"),
  ("question","How is G built? Gödel numbering → Prov(m,n). Diagonal lemma: for any φ(x), there exists ψ such that ψ↔φ(⌜ψ⌝). Take φ(x)=¬Prov(x). Then G↔¬Prov(⌜G⌝). G says 'I am not provable.'","G如何构造？哥德尔配数→Prov(m,n)。对角引理：对任何φ(x)，存在ψ使ψ↔φ(⌜ψ⌝)。取φ(x)=¬Prov(x)。则G↔¬Prov(⌜G⌝)。G说'我不可证明。'"),
  ("explore","(1) If G provable: Prov(⌜G⌝) holds, but G says ¬Prov(⌜G⌝) → contradiction. (2) If ¬G provable: ¬Prov(⌜G⌝) false → Prov(⌜G⌝) → G provable → contradiction. Neither G nor ¬G is provable.","(1)若G可证：Prov(⌜G⌝)成立但G说¬Prov(⌜G⌝)→矛盾。(2)若¬G可证：¬Prov(⌜G⌝)假→Prov(⌜G⌝)→G可证→矛盾。G和¬G都不可证明。"),
  ("insight","2nd Incompleteness: A consistent system that proves its OWN consistency is inconsistent. Con(PA) not provable in PA. Shattered Hilbert's program.","第二不完备定理：证明自身一致的系统不一致。Con(PA)在PA中不可证明。粉碎了Hilbert计划。"),
  ("practice","(1) Why doesn't completeness of FOL contradict incompleteness? (Completeness about LOGICAL truths, incompleteness about ARITHMETICAL truths.) (2) If ZFC proves Con(ZFC), is ZFC consistent? (3) Can a computer decide all math truths?","(1)一阶逻辑完备性为什么不与不完备性矛盾？(完备性关于逻辑真理，不完备性关于算术真理。)(2)若ZFC证明Con(ZFC)，ZFC一致吗？(3)计算机能判定所有数学真理吗？"),
  ("reflection","Gödel SHOWS limits of formalization: strong enough system → inconsistent or incomplete. No algorithm decides all math truths (Turing halting problem). Math requires CREATIVITY — not just symbol manipulation. That's beautiful.","哥德尔展示形式化极限：足够强→不一致或不完备。无算法能判定所有数学真理(Turing停机问题)。数学需要创造力——不仅是符号操作。很美。")
  ]}
)

# ===== STA COURSES =====

# STA130 — Statistical Reasoning
P("STA130H1",
  {"topic":"Exploratory Data Analysis","steps":[
  ("setup","EDA is the FIRST step. Understand data: distributions (histogram, boxplot), relationships (scatterplot), summaries (mean, median, variance). 'What does the data look like?' is the first question.","EDA是第一步。理解数据：分布(直方图、箱线图)、关系(散点图)、汇总(均值、中位数、方差)。'数据看起来什么样？'是第一个问题。"),
  ("question","Anscombe's Quartet: four datasets with IDENTICAL summaries (mean x=9, mean y=7.5, r=0.816) have VERY different patterns. Why is visualization essential?","Anscombe四重奏：四个相同汇总的数据集有非常不同的模式。为什么可视化至关重要？"),
  ("explore","In R: geom_histogram(), geom_boxplot(), geom_point(), geom_density(). Use facet_wrap(~group). Key patterns: skewness, multimodality, outliers, gaps.","在R中：geom_histogram()、geom_boxplot()、geom_point()、geom_density()。使用facet_wrap(~group)。关键模式：偏度、多峰、异常值、缺口。"),
  ("formalize","Summaries: mean (sensitive), median (robust), IQR (robust spread), variance/SD (sensitive), skewness, kurtosis. Always report BOTH center AND spread. For categorical: proportions, contingency tables.","汇总：均值(敏感)、中位数(稳健)、IQR(稳健散布)、方差/SD(敏感)、偏度、峰度。始终报告中心和散布。分类：比例、列联表。"),
  ("practice","Using mpg dataset: (1) Histogram of highway mileage. (2) Boxplot of city mileage by cylinders. (3) Scatterplot of displacement vs city mpg. (4) Mean, median, SD, IQR by cylinders. (5) Identify outliers.","用mpg数据集：(1)公路里程直方图。(2)按气缸分组的城市里程箱线图。(3)排量vs城市里程散点图。(4)按气缸的均值、中位数、SD、IQR。(5)找异常值。"),
  ("insight","'A picture is worth a thousand p-values.' EDA before formal modeling. Tukey: 'Exploratory data analysis is an attitude, a flexibility, and a reliance on display, NOT a collection of techniques.'","'一图胜千个p值。'EDA先于建模。Tukey：'EDA是一种态度、灵活性和对展示的依赖，不是一套技术。'")
  ]},
  {"topic":"Hypothesis Testing and p-values","steps":[
  ("principle","H₀ (no effect) vs H₁ (effect). Assume H₀ true, calculate p = P(data as extreme or more | H₀). If p < α (usually 0.05), REJECT H₀.","H₀(无效应)vs H₁(有效应)。假设H₀真，计算p=P(数据同样或更极端|H₀)。若p<α(通常0.05)，拒绝H₀。"),
  ("step1","Coin fairness: 100 flips, 65 heads. H₀: p=0.5. X~Bin(100,0.5). P(X≥65 or X≤35)=0.0035. p<0.05, reject H₀. Evidence the coin is biased.","硬币公平性：100次，65次正面。H₀:p=0.5。p<0.05，拒绝H₀。硬币有偏的证据。"),
  ("step2","p-value MISINTERPRETATIONS: (1) NOT P(H₀ true). (2) NOT P(result by chance). (3) NOT P(Type I error). p = P(data|H₀). P(H₀|data) needs BAYES.","p值误解：(1)不是P(H₀真)。(2)不是P(结果偶然)。(3)不是P(I类错)。p=P(数据|H₀)。P(H₀|数据)需贝叶斯。"),
  ("step3","Type I: reject true H₀ (α). Type II: fail to reject false H₀ (β). Power = 1-β = P(reject|H₁ true). Power depends on: effect size, n, α, variability. More n → more power.","I类：拒绝真H₀。II类：未能拒绝假H₀。功效=1-β=P(拒绝|H₁真)。取决于效应量、n、α、变异性。"),
  ("conclusion","'p<0.05' is CONVENTION, not truth. Problems: p-hacking, multiple comparisons (20 tests → 1 significant by chance). Solutions: pre-registration, Bonferroni, effect sizes, CIs.","'p<0.05'是惯例，不是真理。问题：p操纵、多重比较。解决：预先注册、Bonferroni、效应量、CI。"),
  ("meta","ASA statement (2016): 'By itself, a p-value does not provide a good measure of evidence.' Better: effect sizes, CIs, Bayes factors. Statistical significance ≠ practical significance.","ASA声明(2016)：'p值本身不提供良好证据度量。'更好：效应量、CI、贝叶斯因子。统计显著性≠实际显著性。")
  ]},
  {"topic":"Confidence Intervals","steps":[
  ("pitfall","'95% CI means 95% probability parameter is in [a,b].' WRONG! Parameter is FIXED. 95% CI: if repeated sampling, ~95% of intervals would contain the true parameter.","'95%CI意味着参数95%概率在区间内。'错！参数固定。95%CI：重复抽样时约95%区间含真实参数。"),
  ("question","For x̄ from N(μ,σ²) with known σ: 95% CI = x̄±1.96σ/√n. Unknown σ: use t: x̄±t_{n-1}·s/√n. Why t? Estimating σ adds uncertainty → wider intervals.","σ已知：x̄±1.96σ/√n。σ未知：用t: x̄±t_{n-1}·s/√n。为什么t？估计σ增加了不确定性→更宽区间。"),
  ("explore","CI = set of parameter values NOT rejected by two-sided test at α. Inversion: 95% CI contains all μ₀ where t-test fails to reject H₀: μ=μ₀. Duality is FUNDAMENTAL.","CI=在α水平双侧检验中不被拒绝的参数值集合。95%CI包含所有t检验不拒绝的μ₀。对偶性是基本的。"),
  ("insight","95% CI communicates BOTH estimate (center) AND precision (width). Wide CI → imprecise. Narrow CI → precise. CI is MORE INFORMATIVE than p-value — shows RANGE of plausible effect sizes.","95%CI同时传达估计(中心)和精度(宽度)。宽CI→不精确。窄CI→精确。CI比p值更提供信息——展示可能的效应量范围。"),
  ("practice","Study: mean diff=2.3, 95% CI=[0.8,3.8], p=0.003. (1) Interpret CI correctly. (2) Would 99% CI be wider/narrower? (3) Would 90% CI include 0? (4) If n doubled, interval wider/narrower? (5) What does CI tell that p doesn't?","研究：均值差=2.3, 95% CI=[0.8,3.8], p=0.003。(1)正确解释CI。(2)99%CI更宽/窄？(3)90%CI包含0吗？(4)n翻倍区间更宽/窄？(5)CI告诉了什么p没告诉的？"),
  ("reflection","CI ≠ Bayesian credible interval (though numerically similar). 95% credible: '95% probability parameter is in this range (given data + prior).' What most people THINK a CI means — needs Bayes.","CI≠贝叶斯可信区间(数值常相似)。95%可信：'参数有95%概率在此范围(给定数据和先验)。'大多数人认为CI的意思——需贝叶斯。")
  ]}
)

# STA237 — Probability, Statistics and Data Analysis I
P("STA237H1",
  {"topic":"Probability Spaces and Random Variables","steps":[
  ("setup","Probability space (Ω,F,P): Ω=sample space, F=σ-algebra (events), P=probability measure. Random variable X:Ω→ℝ is a FUNCTION assigning a number to each outcome. P(X≤x)=P({ω:X(ω)≤x}).","概率空间(Ω,F,P)：Ω=样本空间，F=σ-代数，P=概率测度。随机变量X:Ω→ℝ是给每个结果赋数的函数。"),
  ("question","Roll two dice: Ω={(i,j):1≤i,j≤6}, |Ω|=36. X=sum of dice. P(X=7)=|{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)}|/36=1/6. X is a FUNCTION, not 'random.' Randomness is in Ω.","掷两个骰子：X=和。P(X=7)=1/6。X是函数不是随机，随机性在底层Ω。"),
  ("explore","PMF: p_X(x)=P(X=x). CDF: F_X(x)=P(X≤x). For continuous: PDF f_X(x) where P(a≤X≤b)=∫_a^b f_X(x)dx. CDF works for BOTH.","PMF: p_X(x)=P(X=x)。CDF: F_X(x)=P(X≤x)。连续：PDF f_X(x)，P(a≤X≤b)=∫_a^b f_X(x)dx。CDF两者都适用。"),
  ("formalize","Properties: P(A^c)=1-P(A). P(A∪B)=P(A)+P(B)-P(A∩B). If A⊆B, P(A)≤P(B). P(∪Aᵢ)≤ΣP(Aᵢ) (Boole). Law of total probability: P(B)=ΣP(B|Aᵢ)P(Aᵢ).","性质：P(A^c)=1-P(A)。P(A∪B)=P(A)+P(B)-P(A∩B)。全概率公式：P(B)=ΣP(B|Aᵢ)P(Aᵢ)。"),
  ("practice","From 52 cards, draw 5 no replacement: (1) P(all hearts)? (2) P(at least one ace)? (3) X=number of aces. Find PMF. (4) P(X≥2)? (5) With replacement, how does PMF change?","52张牌无放回抽5：(1)P(全红心)？(2)P(至少一A)？(3)X=A数，求PMF。(4)P(X≥2)？(5)有放回PMF变化？"),
  ("insight","Probability = SETS and FUNCTIONS. Kolmogorov's axioms gave rigorous foundation. Measure-theoretic foundation makes modern probability (martingales, Brownian motion) possible.","概率=集合和函数。Kolmogorov公理赋予严格基础。测度论使现代概率论(鞅、布朗运动)成为可能。")
  ]},
  {"topic":"Law of Large Numbers and Central Limit Theorem","steps":[
  ("principle","X₁,...,Xₙ i.i.d. with mean μ, variance σ². X̄ₙ=(1/n)ΣXᵢ. WLLN: P(|X̄ₙ-μ|>ε)→0. SLLN: P(lim X̄ₙ=μ)=1. Average CONVERGES to expectation. Why polling works!","WLLN: P(|X̄ₙ-μ|>ε)→0。SLLN: P(lim X̄ₙ=μ)=1。均值收敛到期望。这就是民调有效的原因！"),
  ("step1","WLLN proof (Chebyshev): P(|X̄ₙ-μ|>ε) ≤ σ²/(nε²) → 0. Needs finite variance. SLLN deeper: needs E[|X₁|]<∞, martingale convergence.","WLLN证明(Chebyshev): P(|X̄ₙ-μ|>ε)≤σ²/(nε²)→0。需方差有限。SLLN更深。"),
  ("step2","CLT: √n(X̄ₙ-μ)/σ → N(0,1) in distribution. Sample mean → NORMAL regardless of underlying distribution (if variance finite). Why normal is UNIVERSAL in statistics.","CLT: √n(X̄ₙ-μ)/σ→N(0,1)依分布。样本均值→正态不论底层分布。正态是统计中普适的。"),
  ("step3","Die roll (uniform {1..6}, μ=3.5, σ²=2.92). Roll 30 dice, average. Repeat 1000× → histogram is NORMAL, not uniform! CLT in action.","掷骰子(均匀，μ=3.5)。掷30次取平均。重复1000次→直方图正态！CLT在行动。"),
  ("conclusion","LLN: more data → better estimate. CLT: uncertainty ~ normal (large n). Together justify: polling, quality control, Monte Carlo, confidence intervals.","LLN: 更多数据→更好估计。CLT: 不确定性近似正态。一起证明：民调、质量控制、蒙特卡洛、置信区间。"),
  ("meta","'Emergence of certainty from randomness' is deepest insight. LLN+CLT explain WHY statistics works: individual unpredictable, AGGREGATES predictable. Monte Carlo method key application.","'从随机涌现确定性'是最深刻洞见。LLN+CLT解释为什么统计有效：个体不可预测，聚合可预测。")
  ]},
  {"topic":"Sampling Distributions","steps":[
  ("pitfall","'Sampling distribution of X̄ = histogram of data.' WRONG. Sampling distribution = distribution of X̄ across ALL possible samples of size n. A theoretical concept — we usually see ONE sample.","'X̄的抽样分布=数据直方图。'错。抽样分布=所有可能样本中X̄的分布。理论概念——通常只看到一个样本。"),
  ("question","Population {1,3,5}, n=2 with replacement. Possible (1,1)→1, (1,3)→2, ..., (5,5)→5. Sampling distribution: P(1)=1/9, P(2)=2/9, ..., P(5)=1/9. E[X̄]=μ, Var(X̄)=σ²/n.","总体{1,3,5}, n=2有放回。抽样分布：E[X̄]=μ, Var(X̄)=σ²/n。"),
  ("explore","Sampling distribution: mean=μ (UNBIASED), variance=σ²/n (decreases with n). Normal data: X̄~N(μ,σ²/n). Non-normal: CLT → approx normal for large n. Enables inference.","X̄的抽样分布：均值=μ(无偏)，方差=σ²/n(随n减)。正态数据：X̄~N(μ,σ²/n)。非正态：CLT→大n近似正态。使推断可能。"),
  ("insight","Standard error SE=σ/√n. Unknown σ → use S/√n. SE tells PRECISION: smaller SE → more precise. Doubling n reduces SE by only √2 — '√n law' of diminishing returns.","标准误SE=σ/√n。σ未知→S/√n。SE告诉精度：更小SE→更精确。n翻倍SE仅降√2——'√n定律'边际递减。"),
  ("practice","Population μ=100, σ=15, n=25: (1) Sampling distribution of X̄? (2) P(X̄>106)? (3) For SE=2, what n needed? (4) Sample: X̄=104. What can we infer about μ?","总体μ=100,σ=15, n=25：(1)X̄的抽样分布？(2)P(X̄>106)？(3)SE=2需多大n？(4)样本X̄=104，推断μ？"),
  ("reflection","Sampling distribution is BRIDGE between probability and statistics. Probability: given population, likely samples? Statistics: given sample, what is population? CENTRAL concept in frequentist inference.","抽样分布是连接概率和统计的桥梁。概率：给定总体，什么样本可能？统计：给定样本，总体是什么？频率学派推断的核心概念。")
  ]}
)

# STA238 — Probability, Statistics and Data Analysis II
P("STA238H1",
  {"topic":"Maximum Likelihood Estimation","steps":[
  ("setup","Given i.i.d. data x₁,...,xₙ from distribution with θ, likelihood L(θ)=∏f(xᵢ|θ). MLE θ̂=argmax L(θ). Maximize log ℓ=Σlog f(xᵢ|θ). MLE = parameter making observed data MOST PROBABLE.","MLE θ̂=argmax L(θ)。最大化对数似然ℓ=Σlog f(xᵢ|θ)。MLE=使观测数据最可能的参数。"),
  ("question","X₁,...,Xₙ~Bernoulli(p): L(p)=p^{Σxᵢ}(1-p)^{n-Σxᵢ}. ℓ=(Σxᵢ)log p+(n-Σxᵢ)log(1-p). dℓ/dp=0 → p̂=Σxᵢ/n=x̄. MLE is the SAMPLE PROPORTION.","Bernoulli(p): ℓ=(Σxᵢ)log p+(n-Σxᵢ)log(1-p)。dℓ/dp=0→p̂=x̄。MLE=样本比例。"),
  ("explore","For N(μ,σ²): ∂ℓ/∂μ=0→μ̂=x̄. ∂ℓ/∂σ=0→σ̂²=(1/n)Σ(xᵢ-x̄)². Note: σ̂² is BIASED (divides by n, not n-1).","对N(μ,σ²): μ̂=x̄。σ̂²=(1/n)Σ(xᵢ-x̄)²。注意：σ̂²有偏(除以n不是n-1)。"),
  ("formalize","MLE properties (regular): (1) CONSISTENCY: θ̂ₙ→pθ. (2) ASYMPTOTIC NORMALITY: √n(θ̂ₙ-θ)→N(0,I(θ)⁻¹). I(θ)=Fisher info. (3) EFFICIENCY: achieves Cramér-Rao bound. (4) INVARIANCE: if τ=g(θ), τ̂=g(θ̂).","MLE性质：(1)相合。(2)渐近正态：I(θ)=Fisher信息量。(3)有效：达到Cramér-Rao下界。(4)不变性：τ=g(θ)则τ̂=g(θ̂)。"),
  ("practice","Poisson(λ): (1) Derive MLE for λ. (2) Fisher information. (3) Asymptotic variance of λ̂? (4) MLE for √λ? (5) In R: compare MLE vs method of moments for n=10 and n=1000.","Poisson(λ): (1)推导λ的MLE。(2)Fisher信息量。(3)λ̂渐近方差？(4)√λ的MLE？(5)在R中比较n=10和n=1000。"),
  ("insight","MLE is 'default' because ASYMPTOTICALLY OPTIMAL. Likelihood captures ALL info about θ. Maximizing it extracts maximum info. Fisher Info measures HOW MUCH info data provides about θ.","MLE是'默认'因渐近最优。似然捕获所有θ信息。最大化它提取最多信息。Fisher信息量衡量数据提供多少θ信息。")
  ]},
  {"topic":"Neyman-Pearson Lemma and Hypothesis Testing","steps":[
  ("principle","Neyman-Pearson Lemma: For H₀:θ=θ₀ vs H₁:θ=θ₁, MOST POWERFUL test at level α rejects when L(θ₀)/L(θ₁)<c. Threshold c chosen so P(reject|H₀)=α. Foundation of optimal testing.","Neyman-Pearson引理：水平α的最优势检验当L(θ₀)/L(θ₁)<c时拒绝H₀。c选择使P(拒绝|H₀)=α。最优检验基础。"),
  ("step1","X₁,...,Xₙ~N(μ,1). H₀:μ=0 vs H₁:μ=μ₁>0. LR: L(0)/L(μ₁)=exp[-μ₁Σxᵢ+nμ₁²/2]. Reject when Σxᵢ>k → X̄>k/n. Most powerful test rejects for LARGE X̄.","N(μ,1): H₀:μ=0 vs H₁:μ=μ₁>0。LR: 当X̄大时拒绝。最优势检验。"),
  ("step2","t-test: H₀: μ=μ₀ vs H₁: μ≠μ₀. t=(X̄-μ₀)/(S/√n)~t_{n-1} under H₀. Reject when |t|>t_{n-1,α/2}. A LIKELIHOOD RATIO TEST.","t检验：t=(X̄-μ₀)/(S/√n)~t_{n-1}。|t|>t_{n-1,α/2}时拒绝。似然比检验。"),
  ("step3","p-value = SMALLEST α where we reject H₀. t-test: p=2×P(T_{n-1}>|t_obs|). p≠P(H₀|data).","p值=拒绝H₀的最小α。t-test: p=2×P(T_{n-1}>|t_obs|)。p≠P(H₀|data)。"),
  ("conclusion","NP lemma → THEORETICAL gold standard. Practice: LRTs (asymptotically optimal). Simple vs simple: NP exactly most powerful. Composite: need UMP tests (only special cases).","NP引理→理论金标准。实践：LRT(渐近最优)。简单vs简单：NP恰好最优势。复合：需UMP检验。"),
  ("meta","Testing ASYMMETRIC: we control P(Type I)=α but H₀ gets 'benefit of the doubt.' Failing to reject ≠ H₀ true. 'Absence of evidence is not evidence of absence.'","检验不对称：控制P(I类)=α但H₀获'怀疑的好处。'没能拒绝≠H₀真。'没有证据≠证据不存在。'")
  ]},
  {"topic":"Linear Models","steps":[
  ("pitfall","'Linear regression assumes X is normal.' FALSE! Assumptions on ERRORS εᵢ: (1) E[εᵢ]=0. (2) Var(εᵢ)=σ². (3) Independent. (4) εᵢ~N(0,σ²) for inference.","'线性回归假设X正态。'错！假设在误差上：(1)E[εᵢ]=0。(2)Var(εᵢ)=σ²。(3)独立。(4)εᵢ~N(0,σ²)用于推断。"),
  ("question","Yᵢ=β₀+β₁Xᵢ+εᵢ. OLS: minimize Σ(Yᵢ-β₀-β₁Xᵢ)². β̂₁=Σ(Xᵢ-X̄)(Yᵢ-Ȳ)/Σ(Xᵢ-X̄)², β̂₀=Ȳ-β̂₁X̄. Gauss-Markov: OLS is BLUE.","OLS最小化Σ(Yᵢ-β₀-β₁Xᵢ)²。β̂₁=Σ(Xᵢ-X̄)(Yᵢ-Ȳ)/Σ(Xᵢ-X̄)²。Gauss-Markov: OLS是BLUE。"),
  ("explore","R²=1-SS_res/SS_total. adjR² adjusts for predictors. F-test: all βⱼ=0. t-test: individual βⱼ=0. Residuals vs fitted: check homoscedasticity. Q-Q: check normality.","R²=1-SS_res/SS_total。F检验：所有βⱼ=0。t检验：单个βⱼ=0。残差vs拟合检查方差齐性。Q-Q检查正态性。"),
  ("insight","Diagnostics MORE important than p-values. Check: (1) Linearity. (2) Constant variance. (3) Normality. (4) Independence. (5) Influential points (Cook's distance).","诊断比p值更重要。检查：(1)线性。(2)常数方差。(3)正态性。(4)独立性。(5)影响点(Cook距离)。"),
  ("practice","In R: lm(weight~height, data=women). (1) Interpret β̂₀, β̂₁. (2) Test H₀: β₁=0. (3) R². (4) Plot residuals. (5) Add quadratic: lm(weight~height+I(height²)). Does R² improve?","在R中拟合线性模型：(1)解释β̂₀,β̂₁。(2)检验H₀:β₁=0。(3)R²。(4)残差图。(5)加二次项：R²改善了吗？"),
  ("reflection","Linear models are the FOUNDATION. Modern extensions: GLMs (logistic, Poisson), mixed models (random effects), GAMs (smooth terms), regularization (ridge, lasso). All BUILD on linear model framework.","线性模型是基础。现代扩展：GLM、混合模型、GAM、正则化。都建立在线性模型框架上。")
  ]}
)

# STA257 — Probability and Statistics I
P("STA257H1",
  {"topic":"Measure-Theoretic Foundations","steps":[
  ("setup","Kolmogorov: (Ω,F,P). F = σ-algebra (closed under countable ops, contains Ω). P:F→[0,1] countably additive: P(∪Aᵢ)=ΣP(Aᵢ) for DISJOINT events. Required for continuous distributions and infinite processes.","Kolmogorov概率空间(Ω,F,P)。F=σ-代数，P可数可加。连续分布和无穷过程需要测度论。"),
  ("question","Why can't we define P on EVERY subset of [0,1]? Vitali: partition [0,1] by x~y if x-y∈ℚ, pick one from each class → NON-MEASURABLE. Any P on ALL subsets can't be countably additive AND translation-invariant.","为什么不能对[0,1]所有子集定义P？Vitali构造不可测集。所有子集上的概率不能同时可数可加和平移不变。"),
  ("explore","Borel σ-algebra B(ℝ): smallest σ-algebra containing all open intervals. Contains 'nice' sets. |B(ℝ)| = c, |P(ℝ)| = 2^c. MOST subsets NOT Borel. Lebesgue measure λ extends to L(ℝ) ⊃ B(ℝ).","Borel σ-代数B(ℝ)：包含所有开区间的最小σ-代数。|B(ℝ)|=c, |P(ℝ)|=2^c。大多子集非Borel。"),
  ("formalize","Measurable function X:Ω→ℝ: ∀B Borel, X⁻¹(B)∈F. Distribution = pushforward μ_X(B)=P(X⁻¹(B)). Expectation E[X]=∫_Ω X dP = ∫_ℝ x dμ_X (Lebesgue integral). Handles 'spiky' functions.","可测函数X:Ω→ℝ：每个Borel原像在F中。分布=前推测度。期望=Lebesgue积分。处理'尖刺'函数。"),
  ("practice","Show: (1) If F is σ-algebra and A∈F, A^c∈F. (2) Intersection of σ-algebras is σ-algebra. (3) If X measurable, X², |X|, e^X measurable. (4) X+Y, XY, X/Y (Y≠0) measurable.","证明：(1)若F是σ-代数且A∈F，则A^c∈F。(2)σ-代数的交是σ-代数。(3)若X可测，X²,|X|,e^X可测。"),
  ("insight","Measure theory = FOUNDATION. Tells us what events are 'legal' (measurable). Provides Lebesgue integral. Cost: check measurability. Benefit: rigorous handling of infinite-dim processes (martingales, Brownian motion).","测度论=基础。告诉我们什么事件'合法'(可测)。提供Lebesgue积分。代价：检查可测性。收益：严格处理无穷维过程。")
  ]},
  {"topic":"Borel-Cantelli Lemmas and Strong LLN","steps":[
  ("principle","BC1: if ΣP(Aₙ)<∞ then P(Aₙ i.o.)=0. If total probability finite, almost surely only finitely many events occur. Used for SLLN, Kolmogorov's Three Series Theorem.","BC1: 若ΣP(Aₙ)<∞则P(Aₙ i.o.)=0。总概率有限则几乎必然有限多事件。用于SLLN。"),
  ("step1","Example (independence NOT needed): Aₙ=[0,1/n²] in [0,1]. Σ1/n²=π²/6<∞. P(Aₙ i.o.)=0. Limsup set = {0}, P({0})=0.","例(无需独立)：Aₙ=[0,1/n²]。Σ1/n²=π²/6<∞。P(Aₙ i.o.)=0。"),
  ("step2","BC2: if Aₙ INDEPENDENT and ΣP(Aₙ)=∞, then P(Aₙ i.o.)=1. Kolmogorov 0-1 Law: tail events have P=0 or 1. BC1+BC2 give ZERO-ONE law for independent events.","BC2: 若Aₙ独立且ΣP(Aₙ)=∞, 则P(Aₙ i.o.)=1。Kolmogorov 0-1律。BC1+BC2给出独立事件0-1律。"),
  ("step3","SLLN: X₁,...,Xₙ i.i.d. with E[|X₁|]<∞, then X̄ₙ→E[X₁] a.s. Proof: split Xᵢ⁺-Xᵢ⁻, truncation, Chebyshev, BC, Kronecker's lemma. SLLN STRONGER than WLLN.","SLLN: X̄ₙ→E[X₁] a.s.。证明：分裂、截断、Chebyshev、BC、Kronecker引理。SLLN强于WLLN。"),
  ("conclusion","BC1: 'rare events almost never occur i.o.' BC2 (+independence): 'events occur i.o. a.s.' Together prove: SLLN, law of iterated logarithm, random walk properties.","BC1：'罕见事几乎从不无穷发生。'BC2(+独立)：'事件无穷发生a.s.'一起证明：SLLN、重对数律、随机游走。"),
  ("meta","Borel-Cantelli = 'sledgehammers' of probability. Convert sum calculations into almost-sure statements. To prove something happens a.s., show its complement covered by events with summable probabilities.","Borel-Cantelli=概率论'大锤'。将求和转化为几乎必然而然的陈述。要证某事a.s.发生，证其补被概率可和事件覆盖。")
  ]},
  {"topic":"Characteristic Functions and CLT","steps":[
  ("pitfall","'MGFs always exist.' WRONG! Cauchy has NO moments and NO MGF. Characteristic functions φ_X(t)=E[e^{itX}] ALWAYS exist (|e^{itX}|=1). They're the RIGHT tool for studying convergence.","'MGF总存在。'错！Cauchy无矩无MGF。特征函数φ_X(t)=E[e^{itX}]总存在。研究收敛的正确工具。"),
  ("question","φ_X(t)=E[cos(tX)]+iE[sin(tX)]. Properties: φ(0)=1. |φ(t)|≤1. φ_{aX+b}(t)=e^{ibt}φ_X(at). If X,Y independent: φ_{X+Y}=φ_Xφ_Y.","φ_X(t)=E[cos(tX)]+iE[sin(tX)]。性质：φ(0)=1。|φ(t)|≤1。独立时φ_{X+Y}=φ_Xφ_Y。"),
  ("explore","Examples: N(0,1): φ(t)=e^{-t²/2}. Bernoulli(p): 1-p+pe^{it}. Poisson(λ): exp(λ(e^{it}-1)). Cauchy: e^{-|t|}. Uniform(0,1): (e^{it}-1)/(it).","例子：N(0,1): e^{-t²/2}。Bernoulli(p): 1-p+pe^{it}。Poisson(λ): exp(λ(e^{it}-1))。Cauchy: e^{-|t|}。"),
  ("insight","Lévy Continuity: Xₙ→X in dist ⟺ φ_{Xₙ}→φ_X pointwise and limit continuous at 0. CLT proof: φ_{√n(X̄ₙ-μ)/σ}(t)=(φ_{X₁-μ}(t/(σ√n)))ⁿ→e^{-t²/2}. Cleanest proof of CLT.","Lévy连续性定理。CLT证明：φ_{√n(X̄ₙ-μ)/σ}(t)→e^{-t²/2}。CLT最干净证明。"),
  ("practice","(1) CF of Exp(λ). (2) CF of X̄ for Exp(λ) sample. (3) Use CFs to show sum of n i.i.d. Exp(λ) ~ Gamma(n,λ). (4) Show Cauchy is STABLE: average of Cauchy is still Cauchy.","(1)Exp(λ)的CF。(2)Exp(λ)样本X̄的CF。(3)用CF证i.i.d.Exp(λ)和~Gamma(n,λ)。(4)Cauchy稳定：平均还是Cauchy。"),
  ("reflection","Characteristic functions = most elegant tool: ALWAYS exist, uniquely determine distribution (inversion), convert sums → products. They're the 'Fourier transform' of probability — bridge between time and frequency domains.","特征函数=最优雅工具：总是存在、唯一确定分布、将和→积。概率的'傅里叶变换'——时域频域桥梁。")
  ]}
)

# STA261 — Probability and Statistics II
P("STA261H1",
  {"topic":"Sufficiency and Rao-Blackwell","steps":[
  ("setup","T(X) is SUFFICIENT for θ if distribution of X given T doesn't depend on θ. T captures ALL info about θ. Fisher-Neyman: T sufficient ⟺ f(x|θ)=g(T(x),θ)·h(x). h(x) free of θ.","T(X)对θ充分若给定T时的条件分布不依赖θ。T捕获所有θ信息。Fisher-Neyman因子分解。"),
  ("question","X₁,...,Xₙ~Bernoulli(p): f(x|p)=p^{Σxᵢ}(1-p)^{n-Σxᵢ}. T=Σxᵢ: g(T,p)=p^T(1-p)^{n-T}. T sufficient. Sample median? NOT sufficient — lose info.","Bernoulli(p): T=Σxᵢ充分。样本中位数？不充分——丢失信息。"),
  ("explore","Rao-Blackwell: If θ̂ unbiased and T sufficient, then θ̂*=E[θ̂|T] is: (1) VALID (function of T). (2) UNBIASED. (3) Var(θ̂*)≤Var(θ̂). Equality iff θ̂ already function of T.","Rao-Blackwell: 若θ̂无偏T充分，则θ̂*=E[θ̂|T]：(1)有效。(2)无偏。(3)方差≤Var(θ̂)。"),
  ("formalize","Example: X₁,...,Xₙ~Poisson(λ). Unbiased for e^{-λ}: δ₀=I(X₁=0). T=ΣXᵢ sufficient. δ*=E[δ₀|T=t]=((n-1)/n)^t.","例：Poisson(λ)。e^{-λ}无偏估计：δ₀=I(X₁=0)。T=ΣXᵢ充分。δ*=E[δ₀|T=t]=((n-1)/n)^t。"),
  ("practice","(1) Show X̄ sufficient for μ in N(μ,σ²) with known σ². (2) For X~Unif(0,θ), find sufficient statistic. (3) For Bernoulli(p), improve δ=I(X₁=1,X₂=0) via Rao-Blackwell. (4) UMVUE for p is X̄.","(1)N(μ,σ²)中X̄对μ充分。(2)Unif(0,θ)找充分统计量。(3)用Rao-Blackwell改进估计。(4)p的UMVUE是X̄。"),
  ("insight","Rao-Blackwell: OPTIMAL estimators by (1) any unbiased estimator → (2) condition on sufficient T. Never WORSE. Reduces search for UMVUE to functions of sufficient stats. Lehmann-Scheffé: if T COMPLETE sufficient → UNIQUE UMVUE.","Rao-Blackwell：通过(1)任意无偏估计→(2)在充分T上取条件找到最优估计。从不更差。将UMVUE搜索简化为充分统计量的函数。")
  ]},
  {"topic":"Likelihood Ratio Tests","steps":[
  ("principle","LRT: H₀:θ∈Θ₀ vs H₁:θ∈Θ₁. Λ(x)=sup_{Θ₀}L(θ)/sup_{Θ}L(θ). Reject when Λ<c (H₀ much less likely). Generalization of Neyman-Pearson to COMPOSITE hypotheses.","LRT: Λ(x)=sup_{Θ₀}L(θ)/sup_{Θ}L(θ)。Λ小时拒绝。Neyman-Pearson到复合假设的推广。"),
  ("step1","N(μ,σ²), both unknown. H₀:μ=μ₀. Λ=(σ̂₀²/σ̂²)^{-n/2}. Reject when Λ small ⟺ [Σ(xᵢ-μ₀)²/Σ(xᵢ-x̄)²] large ⟺ |t| large (t test!).","N(μ,σ²)都未知。H₀:μ=μ₀。Λ=(σ̂₀²/σ̂²)^{-n/2}。Λ小→t检验。"),
  ("step2","Wilks' Theorem: under H₀, -2logΛ→χ²_{dim(Θ)-dim(Θ₀)} in distribution. WHY we compute asymptotic p-values without exact sampling distribution! Critical values from χ² table.","Wilks定理：-2logΛ→χ²分布。这就是为什么可以计算渐近p值而无需精确抽样分布！"),
  ("step3","Logistic regression: H₀: β₁=β₂=0. Full: β₀+β₁x₁+β₂x₂. Reduced: β₀ only. Λ=L(reduced)/L(full). -2logΛ>χ²_{2,0.05} → reject. The 'deviance test' in GLM.","逻辑回归：H₀:β₁=β₂=0。全模型vs简化。-2logΛ>χ²_{2,0.05}→拒绝。GLM中的'偏差检验'。"),
  ("conclusion","LRTs WIDELY applicable: t, F, χ², deviance tests — ALL special cases. ASYMPTOTICALLY optimal. Cost: χ² approx poor for small n. Use exact (t, F) when available.","LRT广泛适用：t、F、χ²、偏差检验——都是特例。渐近最优。代价：小n时χ²近似不佳。"),
  ("meta","LRT reveals UNIFYING principle: compare MAXIMIZED likelihoods. Extends to: (1) AIC/BIC (penalized log-likelihood). (2) Score tests. (3) Wald tests. The 'Holy Trinity' of testing.","LRT揭示统一原理：比较最大化似然。扩展到AIC/BIC、Score检验、Wald检验。检验的'神圣三一'。")
  ]},
  {"topic":"Confidence Regions","steps":[
  ("pitfall","'95% CI covers 95% of data.' WRONG! CI covers TRUE PARAMETER 95% of time in repeated sampling. About PARAMETER, not data. Prediction interval covers future obs (different).","'95%CI覆盖95%数据。'错！CI覆盖真实参数。关于参数，不是数据。预测区间覆盖未来观测。"),
  ("question","For N(μ,σ²) known σ²: 95% CI = X̄±1.96σ/√n. Unknown σ²: X̄±t·S/√n. JOINT region for (μ,σ²): (n-1)S²/σ²~χ²_{n-1}. Invert → interval for σ².","μ的95%CI。联合区域：(n-1)S²/σ²~χ²_{n-1}。反演→σ²区间。"),
  ("explore","Confidence REGIONS: invert LRT. Set {θ: -2logΛ(θ|x)≤χ²_{p,α}} = asymptotic 95% region. 'Inverted test' approach — contains all θ not rejected by α-level test.","置信区域：反演LRT。区域包含所有不会被α水平检验拒绝的θ。"),
  ("insight","CIs and tests are DUAL: 95% CI for μ={μ₀: t-test fails to reject μ=μ₀ at α=0.05}. Conceptually important, practically useful. Perform test = check if value lies in CI.","CI和检验对偶：95%CI={μ₀:t检验不拒绝μ=μ₀}。概念重要实践有用。"),
  ("practice","(1) 95% CI for σ² given n=25, S²=4. (2) Joint 95% region for (μ,σ²). (3) Shape? (4) Does (μ=5,σ²=10) lie inside if X̄=3? (5) Interpret.","(1)σ²的95%CI。(2)(μ,σ²)联合95%区域。(3)形状？(4)(μ=5,σ²=10)在区域内？(5)解释。"),
  ("reflection","Confidence regions quantify UNCERTAINTY in MULTIPLE dimensions. Shape reveals correlation. In high dimensions, become 'shells' — parameter likely near boundary (curse of dimensionality).","置信区域量化多维不确定性。形状揭示相关性。高维中变'壳'——参数可能在边界附近(维数灾难)。")
  ]}
)

# STA302 — Methods of Data Analysis I
P("STA302H1",
  {"topic":"Simple Linear Regression","steps":[
  ("setup","Yᵢ=β₀+β₁Xᵢ+εᵢ, εᵢ~N(0,σ²). β₁=slope, β₀=intercept. OLS: minimize Σ(Yᵢ-β₀-β₁Xᵢ)². β̂₁=S_xy/S_xx, β̂₀=Ȳ-β̂₁X̄.","Yᵢ=β₀+β₁Xᵢ+εᵢ。OLS最小化Σ(Yᵢ-β₀-β₁Xᵢ)²。"),
  ("question","Interpretation: Y=house price, X=size. β̂₁=0.5: each additional ft² → expected price ↑ $500. β̂₀=50: expected price at 0 ft² is $50K (extrapolation).","解释：β̂₁=0.5：每增加一平方英尺，预期价格增加$500。β̂₀=50：外推可能无意义。"),
  ("explore","ANOVA: SS_total=SS_reg+SS_res. R²=SS_reg/SS_total = variance explained. H₀: β₁=0: t=β̂₁/SE(β̂₁)~t_{n-2} or F=MS_reg/MS_res~F_{1,n-2}. t²=F → same test.","R²=SS_reg/SS_total。检验H₀:β₁=0: t或F。t²=F→相同检验。"),
  ("formalize","Assumptions: (1) Linearity: E[Y|X]=β₀+β₁X. (2) Independence. (3) Homoscedasticity: Var(εᵢ)=σ². (4) Normality for exact inference. OLS: E[β̂]=β (unbiased), Var(β̂)=σ²(XᵀX)⁻¹.","假设：(1)线性。(2)独立。(3)同方差。(4)正态性用于精确推断。OLS：无偏。"),
  ("practice","In R: lm(y~x). (1) Extract β̂₀, β̂₁, R², F. (2) Test H₀:β₁=0. (3) Scatterplot + regression line. (4) Residuals vs fitted — assumptions hold? (5) Predict Y for new X + 95% PI.","在R中：(1)提取系数、R²、F。(2)检验H₀。(3)散点图+回归线。(4)残差诊断。(5)预测+95%预测区间。"),
  ("insight","'Regression to the mean' (Galton): children of tall parents taller than avg but shorter than parents. |β₁|<1 → predicted Y CLOSER TO MEAN than X. NOT artifact — real!","'均值回归'(Galton)：高个子父母的孩子比平均高但比父母矮。|β₁|<1→预测Y比X更接近均值。")
  ]},
  {"topic":"Multiple Regression and Diagnostics","steps":[
  ("principle","Y=Xβ+ε. β̂=(XᵀX)⁻¹XᵀY. Gauss-Markov: OLS is BLUE. Var(β̂)=σ²(XᵀX)⁻¹. Each β̂ⱼ = PARTIAL effect of Xⱼ on Y, holding others constant.","Y=Xβ+ε。β̂=(XᵀX)⁻¹XᵀY。Gauss-Markov: OLS是BLUE。每个β̂ⱼ是偏效应。"),
  ("step1","Residual diagnostics: (1) Constant variance: residuals vs fitted. (2) Normality: Q-Q. (3) Independence: Durbin-Watson. (4) Linearity: partial residual plots.","残差诊断：(1)同方差：残差vs拟合。(2)正态性：Q-Q。(3)独立性：Durbin-Watson。(4)线性：偏残差图。"),
  ("step2","Influential points: (1) LEVERAGE hᵢᵢ from hat matrix H. (2) OUTLIER: |studentized residual|>3. (3) INFLUENTIAL: Cook's D>4/n. High leverage + outlier = dangerous!","影响点：(1)杠杆值hᵢᵢ。(2)异常值：|学生化残差|>3。(3)影响点：Cook D>4/n。高杠杆+异常值=危险！"),
  ("step3","Multicollinearity: VIFⱼ=1/(1-R²_{Xⱼ|others}). VIF>10 → serious. Effects: inflated SEs, unstable estimates. Solutions: (1) Remove. (2) Ridge. (3) PCA.","共线性：VIF>10→严重。影响：SE膨胀、估计不稳定。解决：(1)移除。(2)岭回归。(3)主成分。"),
  ("conclusion","Variable selection: (1) Stepwise — fast but overfits. (2) All subsets — expensive. (3) AIC/BIC: lower better. (4) LASSO — L1 regularization, automatic selection.","变量选择：(1)逐步——快速但过拟合。(2)全子集——昂贵。(3)AIC/BIC：越低越好。(4)LASSO——自动选择。"),
  ("meta","Multiple regression = 'Swiss Army Knife.' Used in: economics (hedonic pricing), epidemiology (adjusting confounders), ML (linear basis expansion). Diagnostics are ESSENTIAL for valid inference.","多元回归='瑞士军刀'。用于经济学、流行病学、机器学习。诊断是有效推断的必要条件。")
  ]},
  {"topic":"Geometry of Least Squares","steps":[
  ("pitfall","'Correlation implies causation.' NO! Regression shows ASSOCIATION. Ice cream sales ↔ drowning (both ↑ in summer). CONFOUNDER = temperature. Regression doesn't identify causes.","'相关=因果。'不！回归展示关联。冰淇淋↔溺水(都夏天↑)。混杂=温度。回归不识别因果。"),
  ("question","Geometric: Y in ℝⁿ. Columns of X span subspace. β̂=(XᵀX)⁻¹XᵀY = PROJECTION of Y onto subspace. Ŷ=HY (H=hat matrix). e=Y-Ŷ=(I-H)Y orthogonal to column space.","几何：Y在ℝⁿ中。X列张成子空间。β̂=Y的投影。Ŷ=HY。e正交于列空间。"),
  ("explore","Gauss-Markov: Any linear θ̂=cᵀY. Unbiased ⟺ cᵀX=eⱼᵀ. Var(cᵀY)=σ²‖c‖². OLS c₀=X(XᵀX)⁻¹eⱼ. For any c=c₀+a with aᵀX=0: ‖c‖²=‖c₀‖²+‖a‖²≥‖c₀‖². OLS minimizes variance.","Gauss-Markov证明：OLS方差最小。任何线性无偏估计c=c₀+a，其中aᵀX=0。‖c‖²=‖c₀‖²+‖a‖²≥‖c₀‖²。"),
  ("insight","Geometry clarifies: (1) R²=cos²(θ) where θ = angle between Y and Ŷ. (2) Adding predictors NEVER reduces R². (3) Orthogonal = independent estimates. (4) F-test = ratio of squared projection lengths.","几何澄清：(1)R²=cos²(θ)。(2)添加变量从不降低R²。(3)正交=独立估计。(4)F检验=投影长度平方比。"),
  ("practice","(1) Show H symmetric and idempotent. (2) I-H also symmetric idempotent. (3) e ⟂ Ŷ. (4) Prove E[MSE]=σ². (5) In R: compute H for simple regression.","(1)证明H对称幂等。(2)I-H也对称幂等。(3)e⟂Ŷ。(4)E[MSE]=σ²。(5)R中计算简单回归的H。"),
  ("reflection","Geometric view UNIFIES: regression = projection, ANOVA = decomposition into orthogonal subspaces, mixed models = projection onto random effects. Understanding ℝⁿ projections → understanding linear models.","几何视角统一：回归=投影，ANOVA=正交子空间分解，混合模型=投影到随机效应。")
  ]}
)

# STA303 — Methods of Data Analysis II
P("STA303H1",
  {"topic":"ANOVA and Experimental Design","steps":[
  ("setup","ANOVA tests if k group means EQUAL. H₀: μ₁=μ₂=...=μₖ. Compare BETWEEN-group vs WITHIN-group variability. F = MS_between/MS_within ~ F_{k-1,n-k} under H₀.","ANOVA检验k组均值相等。H₀: μ₁=μ₂=...=μₖ。比较组间vs组内变异。F=MS_between/MS_within~F_{k-1,n-k}。"),
  ("question","One-way ANOVA: Yᵢⱼ=μ+αᵢ+εᵢⱼ, αᵢ=group effect, Σαᵢ=0. SS_between=Σnᵢ(Ȳᵢ.-Ȳ..)². SS_within. Reject if F>F_crit. Post-hoc: Tukey's HSD for pairwise comparisons.","单因素ANOVA: Yᵢⱼ=μ+αᵢ+εᵢⱼ。事后：Tukey HSD用于配对比较。"),
  ("explore","Two-way ANOVA: Yᵢⱼₖ=μ+αᵢ+βⱼ+(αβ)ᵢⱼ+εᵢⱼₖ. Tests: (1) Factor A. (2) Factor B. (3) INTERACTION. Parallel lines = no interaction. Crossing = interaction.","双因素ANOVA。检验：(1)A主效应。(2)B主效应。(3)交互。平行线=无交互。交叉=有交互。"),
  ("formalize","Assumptions: (1) Independence. (2) Homoscedasticity (Levene's test). (3) Normality (Q-Q). ANOVA ROBUST to normality violations for moderate n (CLT). Welch's ANOVA if variances unequal.","假设：(1)独立。(2)同方差(Levene检验)。(3)正态(Q-Q)。中等n时ANOVA稳健。方差不等用Welch。"),
  ("practice","In R: summary(aov(y~group)). (1) Interpret F-test. (2) Check residuals. (3) TukeyHSD(). Which groups differ? (4) Add block: aov(y~group+block). Why block? (5) Effect sizes η², ω².","在R中：(1)解释F检验。(2)检查残差。(3)TukeyHSD()。哪些组不同？(4)加区组。为什么？(5)效应量η²,ω²。"),
  ("insight","ANOVA = SPECIAL CASE of linear regression. F-test for group differences = F-test for β₁=...=β_{k-1}=0 with k-1 dummy variables. 'ANOVA' and 'regression' are SAME model — historical terminology.","ANOVA=线性回归特例。组差异F检验=有k-1个虚拟变量的回归。'ANOVA'和'回归'相同模型——历史术语。")
  ]},
  {"topic":"Mixed Effects Models","steps":[
  ("principle","Fixed effects: levels we care about (e.g., drug vs placebo). Random effects: SAMPLE from larger population (students from schools). Mixed = BOTH.","固定效应：关心的水平(如药物vs安慰剂)。随机效应：大总体的样本(来自学校的学生)。混合=两者。"),
  ("step1","Y=Xβ+Zγ+ε, β=fixed, γ~N(0,G)=random, ε~N(0,R). Var(Y)=ZGZᵀ+R. Estimation: REML (unbiased variance) rather than ML.","Y=Xβ+Zγ+ε。估计：REML(无偏方差)优于ML。"),
  ("step2","Students nested in schools: Yᵢⱼ=μ+Schoolᵢ+εᵢⱼ, Schoolᵢ~N(0,σ²_school). ICC=σ²_school/(σ²_school+σ²)=intraclass correlation — variance due to schools.","学生嵌套学校：Yᵢⱼ=μ+Schoolᵢ+εᵢⱼ。ICC=组内相关系数。"),
  ("step3","Longitudinal: Yᵢⱼ=β₀+β₁tⱼ+uᵢ+εᵢⱼ (random intercept). Can add random slope: Yᵢⱼ=β₀+β₁tⱼ+u_{0i}+u_{1i}tⱼ+εᵢⱼ (own trajectory per subject).","纵向：随机截距。可加随机斜率：每个受试者自己的轨迹。"),
  ("conclusion","Why mixed models? (1) Correct SEs for clustered data. (2) Borrow strength: partial pooling (shrinkage). (3) Unbalanced data. (4) Complex correlations.","为什么混合模型？(1)聚类数据校正SE。(2)借用力量：部分池化。(3)不平衡数据。(4)复杂相关。"),
  ("meta","Mixed models use SHRINKAGE (like ridge): random effects 'shrunk' toward zero vs fitting each group separately. Improves prediction (bias-variance tradeoff). ESSENTIAL for small group sizes.","混合模型使用收缩(如岭)：随机效应'收缩'向零。改进预测(偏差-方差权衡)。小组样本量时至关重要。")
  ]},
  {"topic":"Generalized Linear Models","steps":[
  ("pitfall","'Logistic regression = logit transform Y.' WRONG! Logistic models log-ODDS. Y is BINARY. Y~Bernoulli(p), model log(p/(1-p))=Xβ. We model PROBABILITY through LINK FUNCTION.","'逻辑回归=logit变换Y。'错！Y二元，Y~Bernoulli(p)，通过连接函数建模概率。"),
  ("question","GLM = distribution + link function. (1) RANDOM: Y~Exponential Family. (2) SYSTEMATIC: η=Xβ. (3) LINK: g(μ)=η where μ=E[Y]. Link connects mean to linear predictor.","GLM=分布+连接函数。连接函数将均值连接到线性预测器。"),
  ("explore","Common GLMs: (1) Linear: Normal, identity. (2) Logistic: Binomial, logit. (3) Poisson: Poisson, log. (4) Gamma: Gamma, inverse. Each natural for the data type.","常见GLM：(1)线性：恒等。(2)逻辑：logit。(3)泊松：log。(4)Gamma：倒数。"),
  ("insight","Estimation via IRLS: compute working weights and response at each step, fit weighted LS. Converges rapidly. Deviance = -2log-likelihood ratio, generalizes residual SS.","通过IRLS估计：每步计算工作权重和响应，拟合加权最小二乘。快速收敛。偏差=-2对数似然比。"),
  ("practice","For a binary outcome: (1) Fit logistic: glm(y~x, family=binomial). (2) Interpret coefficients as log-odds ratios. (3) Compute odds ratios. (4) Predict probabilities. (5) Check goodness-of-fit: deviance residuals.","二分类结果：(1)拟合逻辑回归。(2)解释系数为log-比值比。(3)计算比值比。(4)预测概率。(5)检查拟合优度。"),
  ("reflection","GLMs UNIFY linear, logistic, Poisson, Gamma regression under one framework. They're the workhorse of applied statistics. Modern extensions: GAMs (smooth terms), GLMMs (random effects), zero-inflated models.","GLM在线性、逻辑、泊松、Gamma回归下统一。现代扩展：GAM(平滑项)、GLMM(随机效应)、零膨胀模型。")
  ]}
)

# STA304 — Surveys, Sampling and Observational Data
P("STA304H1",
  {"topic":"Survey Design and Sampling Methods","steps":[
  ("setup","Goal: estimate population parameters from a sample. The SAMPLING DESIGN determines how representative the sample is. Key: probability sampling (every unit has known selection probability).","目标：从样本估计总体参数。抽样设计决定样本代表性。关键：概率抽样(每单元有已知选择概率)。"),
  ("question","Simple Random Sample (SRS): each subset of size n equally likely. Estimator for μ: ȳ = (1/n)Σyᵢ. Unbiased: E[ȳ]=μ. Variance: Var(ȳ)=σ²/n·(1-n/N) (finite population correction).","简单随机抽样(SRS)：每个大小为n的子集等可能。估计量ȳ无偏。方差含有限总体校正。"),
  ("explore","Stratified sampling: split population into strata (groups), sample EACH stratum. Var(ȳ_strat) < Var(ȳ_SRS) if strata homogeneous. Optimal allocation: n_h ∝ N_h·σ_h.","分层抽样：分为层(组)，每层独立抽样。若层内同质则方差小于SRS。最优分配：n_h∝N_h·σ_h。"),
  ("formalize","Horvitz-Thompson estimator: τ̂ = Σ yᵢ/πᵢ where πᵢ = inclusion probability. UNBIASED for any sampling design where πᵢ>0. Weights wᵢ=1/πᵢ. Design effect: Var(actual)/Var(SRS).","Horvitz-Thompson估计：τ̂=Σyᵢ/πᵢ，πᵢ=入样概率。任何πᵢ>0的抽样设计下无偏。设计效应=实际方差/SRS方差。"),
  ("practice","Population size N=1000, take n=100 SRS. (1) Estimate mean and SE. (2) If population has 2 equal-sized strata with σ₁=10, σ₂=20, find optimal allocation. (3) Compute design effect. (4) Compare to stratified sample of same n.","N=1000,n=100。SRS vs 最优分层 vs 同n分层。比较精度。"),
  ("insight","'All sampling is done with a purpose.' The design determines the analysis. Complex surveys require: (1) Sampling weights. (2) Stratum indicators. (3) Cluster indicators. Ignoring design → biased SEs and wrong inferences.","'所有抽样都有目的。'设计决定分析。复杂调查需要：抽样权重、层指标、群指标。忽略设计→SE偏倚、错误推断。")
  ]},
  {"topic":"Observational Studies and Confounding","steps":[
  ("principle","Correlation ≠ Causation. Observational studies only show ASSOCIATION. Confounder: variable associated with BOTH treatment and outcome. Simpson's paradox: trend reverses when grouping by confounder.","相关≠因果。观测研究只展示关联。混杂：与处理和结果都相关的变量。Simpson悖论：按混杂分组时趋势反转。"),
  ("question","Example: Hospital A has lower survival rate than B (73% vs 79%). But within good-condition patients, A is better (93% vs 87%). Within poor-condition, A also better (73% vs 67%). A treats sicker patients → aggregation hides truth.","例：A院生存率低于B(73% vs 79%)。但良好状态患者中A更好(93% vs 87%)。差状态中A也更好。A治疗更重病人→聚合隐藏真相。"),
  ("explore","Methods to adjust for confounders: (1) Stratification. (2) Multivariable regression. (3) Propensity score matching — P(treatment|covariates). (4) Instrumental variables. (5) Difference-in-differences.","调整混杂的方法：(1)分层。(2)多元回归。(3)倾向评分匹配。(4)工具变量。(5)双重差分。"),
  ("formalize","Propensity score: e(X)=P(T=1|X). Key property: treatment assignment is INDEPENDENT of potential outcomes conditional on e(X). Matching on PS creates balanced groups.","倾向评分：e(X)=P(T=1|X)。关键：在e(X)条件下处理分配独立于潜在结果。PS匹配创建平衡组。"),
  ("practice","Study: new drug vs placebo. Patients on drug are younger. Outcomes: drug group recovers faster. (1) Is age a confounder? (2) How would you adjust? (3) Compute propensity score. (4) Match or stratify by PS. (5) After adjustment, does effect remain?","新药研究：用药组更年轻，恢复更快。(1)年龄是混杂吗？(2)如何调整？(3)计算倾向评分。(4)用PS匹配或分层。(5)调整后效应还在吗？"),
  ("insight","'Correlation does not imply causation' — the most important warning in statistics. But advanced methods (RCTs, IV, DiD, RDD) can identify causal effects. The GOLD STANDARD is the randomized controlled trial.","'相关不意味因果'——统计最重要警告。但高级方法(RCT、IV、DiD、RDD)可识别因果效应。金标准是随机对照试验。")
  ]},
  {"topic":"Sampling Bias and Nonresponse","steps":[
  ("pitfall","'A large sample automatically represents the population.' WRONG! A biased large sample is WORSE than a small unbiased one. Literary Digest poll (1936): 2.4M responses predicted Landon → Roosevelt won. Response bias!","'大样本自动代表总体。'错！有偏大样本比小的无偏样本更糟。Literary Digest民调(1936)：240万回复预测Landon→Roosevelt胜。回复偏差！"),
  ("question","US presidential election 1936: Literary Digest sent 10M postcards (from phone books + car registrations). 2.4M returned → Landon 57%. Actual: Roosevelt 62%. Why? Sampling frame excluded poor voters (Great Depression). SELECTION BIAS.","1936年大选：从电话簿+车牌发送1000万明信片。240万回复→Landon 57%。实际：Roosevelt 62%。抽样框排除穷人→选择性偏差。"),
  ("explore","Types of bias: (1) Selection bias — frame doesn't match population. (2) Nonresponse bias — respondents differ from non-respondents. (3) Response bias — lying, misunderstanding. (4) Recall bias — memory errors.","偏差类型：(1)选择性偏差。(2)无回答偏差。(3)回答偏差。(4)回忆偏差。"),
  ("insight","Nonresponse: even 70% response rate can have severe bias if non-respondents differ systematically. Solutions: (1) Increase response rate. (2) Weighting adjustments (post-stratification). (3) Imputation. (4) Sensitivity analysis.","无回答：即使70%回答率，若无回答者有系统性差异，偏差可能严重。解决：(1)提高回答率。(2)加权调整。(3)插补。(4)敏感性分析。"),
  ("practice","A mail survey gets 30% response. Respondents tend to be older, wealthier, more educated. (1) Is the sample representative? (2) How would nonresponse bias affect estimates of income? (3) Design a weighting scheme using census data. (4) What's the likely direction of bias?","邮件调查30%回答。回答者年龄更大、更富、更受教育。(1)样本有代表性吗？(2)无回答偏差如何影响收入估计？(3)用普查数据设计加权方案。(4)偏差方向？"),
  ("reflection","'The plural of anecdote is not data.' Bias can NEVER be fixed by increasing sample size — only by improving the design. Register your survey design: target population, sampling frame, response rate, weighting plan.","'轶事的复数不是数据。'偏差永远不能通过增加样本量解决——只能通过改进设计。登记调查设计：目标总体、抽样框、回答率、加权计划。")
  ]}
)

# STA314 — Statistical Methods for ML I
P("STA314H1",
  {"topic":"Supervised Learning and Regularization","steps":[
  ("setup","Supervised learning: given (xᵢ,yᵢ), learn f:X→Y. Regression (Y continuous) or classification (Y discrete). Loss function measures prediction error. Minimize expected loss, approximate with empirical loss.","监督学习：给定(xᵢ,yᵢ)，学习f:X→Y。回归(Y连续)或分类(Y离散)。损失函数度量预测误差。最小化期望损失，用经验损失近似。"),
  ("question","Overfitting: model memorizes training data but can't generalize. Bias-variance tradeoff: complex model → low bias, high variance. Simple model → high bias, low variance. Goal: minimize TOTAL error = bias²+variance+irreducible error.","过拟合：模型记忆训练数据但不能泛化。偏差-方差权衡：复杂→低偏差高方差。简单→高偏差低方差。目标：最小化总误差=偏差²+方差+不可约误差。"),
  ("explore","Regularization: add penalty to loss. L2 (ridge): λΣβⱼ². Shrinks coefficients toward zero. L1 (lasso): λΣ|βⱼ|. Shrinks AND selects (some βⱼ=0). Elastic Net: λ₁Σ|βⱼ|+λ₂Σβⱼ².","正则化：在损失上加惩罚。L2(岭)：收缩向零。L1(lasso)：收缩+选择(一些βⱼ=0)。弹性网：L1+L2。"),
  ("formalize","Cross-validation: estimate test error without a test set. k-fold CV: split data into k folds, train on k-1, validate on 1, repeat. Choose λ that minimizes CV error. NEVER use test set for model selection.","交叉验证：无需测试集估计测试误差。k折CV：数据分k份，k-1训练1验证，重复。选最小化CV误差的λ。绝不用测试集做模型选择。"),
  ("practice","With the mtcars dataset: (1) Fit ridge and lasso for mpg ~ all predictors. (2) Use cv.glmnet() to find optimal λ. (3) Compare coefficients. (4) Which predictors does lasso select? (5) Evaluate on a test set.","用mtcars数据集：(1)拟合岭和lasso。(2)用cv.glmnet()找最优λ。(3)比较系数。(4)lasso选择了哪些变量？(5)在测试集上评估。"),
  ("insight","Regularization trades bias for variance. By shrinking coefficients, we accept some bias to REDUCE variance dramatically. The net effect: LOWER prediction error. 'Shrinkage' = 'stealing strength' from other predictors.","正则化以偏差换方差。收缩系数以偏差换取方差大幅降低。净效应：更低的预测误差。'收缩'=从其他预测变量'借用力量'。")
  ]},
  {"topic":"Classification and Decision Trees","steps":[
  ("principle","Classification: predict discrete label. Logistic regression: P(Y=1|X)=1/(1+e^{-Xβ}). Decision boundary = where P=0.5. Linear boundary (in X). Can add polynomial terms for nonlinear boundaries.","分类：预测离散标签。逻辑回归：P(Y=1|X)=1/(1+e^{-Xβ})。决策边界=P=0.5处。线性边界。加多项式项得非线性边界。"),
  ("question","Decision trees: recursive partition of predictor space. At each node: find split (variable + threshold) that minimizes impurity. Gini index: 1-Σpₖ². Entropy: -Σpₖlog pₖ. Both measure NODE PURITY.","决策树：递归划分预测空间。每节点找最小化不纯度的分割。Gini指数：1-Σpₖ²。熵：-Σpₖlog pₖ。都度量节点纯度。"),
  ("explore","Tree growing: until minimum node size or no impurity reduction. PRUNING: cut back to avoid overfitting. Cost-complexity pruning: minimize Σmisclassifications + α·|tree|. α chosen by CV.","树生长：直到最小节点大小或无纯度改进。剪枝：剪回避免过拟合。成本复杂度剪枝：最小化误分类+α·|tree|。"),
  ("formalize","Random Forest: build B trees on bootstrap samples, at each split consider m random predictors. Aggregate by majority vote (classification) or average (regression). Reduces variance without increasing bias.","随机森林：在B个bootstrap样本上建树，每分割考虑m个随机变量。多数投票(分类)或平均(回归)聚合。降低方差而不增偏差。"),
  ("practice","On the iris dataset: (1) Fit a decision tree: rpart(Species~.). (2) Plot the tree. (3) Prune using cp parameter. (4) Fit random forest: randomForest(). (5) Compare accuracy vs logistic regression.","在iris数据集上：(1)拟合决策树。(2)画树。(3)用cp剪枝。(4)拟合随机森林。(5)比较准确率vs逻辑回归。"),
  ("insight","Trees are INTERPRETABLE but high variance. Random Forest: less interpretable but MUCH better accuracy. The key insight: DECORRELATE the trees by random feature selection → averaged predictions are stable and accurate.","树可解释但高方差。随机森林：解释性略差但精度好很多。关键：随机选择特征使树去相关→平均预测稳定且准确。")
  ]},
  {"topic":"Kernel Methods and Representer Theorem","steps":[
  ("pitfall","'SVM finds a separating hyperplane.' TRUE for linearly separable. But SVM WITH KERNELS finds nonlinear boundaries in ORIGINAL space by computing linear boundary in FEATURE space. The kernel trick makes this efficient.","'SVM找分离超平面。'线性可分时为真。但核SVM通过在高维特征空间找线性边界来在原空间找非线性边界。核技巧使其高效。"),
  ("question","Kernel: k(x,x') = φ(x)·φ(x'), where φ maps to feature space. RBF kernel: k(x,x')=exp(-‖x-x'‖²/σ²). Implicitly maps to INFINITE-dimensional feature space. But we never compute φ explicitly — just k(x,x').","核：k(x,x')=φ(x)·φ(x'), φ映射到特征空间。RBF核：exp(-‖x-x'‖²/σ²)。隐式映射到无穷维特征空间。但从不显式计算φ——只计算k(x,x')。"),
  ("explore","Representer Theorem: the optimal w in the feature space has the form w = Σαᵢφ(xᵢ). Thus f(x)=w·φ(x)=Σαᵢk(xᵢ,x). Learning reduces to finding αᵢ. This is why kernel methods work with ANY kernel.","Representer定理：特征空间中最优w的形式为w=Σαᵢφ(xᵢ)。学习简化为求αᵢ。这就是核方法适用于任何核的原因。"),
  ("insight","The kernel trick enables: (1) Nonlinear classification with linear methods. (2) Working in infinite-dim spaces with finite computation. (3) Using domain-specific similarity measures as kernels. (4) Combining kernels (multiple kernel learning).","核技巧使能：(1)用线性方法做非线性分类。(2)有限计算处理无穷维空间。(3)用领域特定相似度量作为核。(4)组合核(多核学习)。"),
  ("practice","On a nonlinear dataset: (1) Fit SVM with linear kernel. (2) Fit SVM with RBF kernel. (3) Tune C and γ via CV. (4) Plot decision boundaries. (5) Compare: when does RBF outperform linear?","在非线性数据集上：(1)线性核SVM。(2)RBF核SVM。(3)通过CV调整C和γ。(4)画决策边界。(5)比较：RBF何时优于线性？"),
  ("reflection","Kernel methods are 'lazy learners' — they keep training data and use it at prediction time. Computational cost O(n²) or O(n³). For large n, neural nets scale better. But for small-to-medium n, SVMs are often state-of-the-art.","核方法是'懒惰学习'——保留训练数据，预测时使用。计算成本O(n²)或O(n³)。大n时神经网络扩展性更好。但中小n时SVM常是最优的。")
  ]}
)

# STA347 — Probability
P("STA347H1",
  {"topic":"Modes of Convergence","steps":[
  ("setup","Four modes of convergence for random variables: (1) Almost surely (a.s.): P(lim Xₙ=X)=1. (2) In probability: P(|Xₙ-X|>ε)→0. (3) In distribution: F_{Xₙ}(x)→F_X(x) at continuity points. (4) In Lᵖ: E[|Xₙ-X|ᵖ]→0.","四种收敛模式：(1)几乎必然(a.s.)。(2)依概率。(3)依分布。(4)Lᵖ。"),
  ("question","Relationships: a.s. ⇒ in prob ⇒ in dist. Lᵖ ⇒ in prob. But converse fails. Example: Xₙ=1 on [0,1/n], 0 elsewhere. Xₙ→0 in prob (P(|Xₙ|>ε)=1/n→0). But NOT a.s. BC1: ΣP(|Xₙ|>ε)=∞, so P(|Xₙ|>ε i.o.)=1 not 0!","关系：a.s.⇒依概率⇒依分布。但逆不成立。例：Xₙ→0依概率但不a.s.。"),
  ("explore","Counterexample for convergence in dist NOT in prob: Let X~Bernoulli(0.5). Define Xₙ=1-X. Xₙ has SAME distribution as X (same CDF) → Xₙ→X in dist. But P(|Xₙ-X|>0)=P(Xₙ≠X)=1. Does NOT converge in prob.","依分布不蕴含依概率的反例。"),
  ("formalize","Slutsky's Theorem: if Xₙ→X in dist and Yₙ→c in prob, then Xₙ+Yₙ→X+c, XₙYₙ→cX, Xₙ/Yₙ→X/c (c≠0). Essential for asymptotics: t-statistic works because numerator converges in dist, denominator in prob.","Slutsky定理：Xₙ→X依分布且Yₙ→c依概率则Xₙ+Yₙ→X+c等。t统计量因此有效。"),
  ("practice","(1) If Xₙ a.s. and Yₙ a.s., show Xₙ+Yₙ a.s. (2) Show: Xₙ→X in prob ⟺ every subsequence has further subsequence converging a.s. (3) If Xₙ→X in L², does Xₙ→X in L¹? (4) Prove: Xₙ→X a.s. ⇒ Xₙ→X in prob.","(1)a.s.收敛的和a.s.收敛。(2)依概率收敛⇔每个子列有a.s.收敛子子列。(3)L²⇒L¹？(4)a.s.⇒依概率。"),
  ("insight","Each mode is useful: (1) a.s. for strong limit theorems (SLLN). (2) In prob for consistency (WLLN, MLE consistency). (3) In dist for CLT (the CENTRAL result in statistics). (4) L² for mean-squared prediction. Slutsky connects them.","每种模式有用：(1)a.s.用于强极限定理。(2)依概率用于相合性。(3)依分布用于CLT(统计中心结果)。(4)L²用于均方预测。Slutsky连接它们。")
  ]},
  {"topic":"Conditional Expectation","steps":[
  ("principle","E[X|Y] is a RANDOM VARIABLE — a function of Y. Defined as the UNIQUE random variable satisfying: (1) E[X|Y] is measurable w.r.t. σ(Y). (2) For any A∈σ(Y), E[E[X|Y]·I_A]=E[X·I_A]. This is the PROJECTION of X onto L²(σ(Y)).","E[X|Y]是随机变量——Y的函数。它是满足某些条件的唯一随机变量：X在L²(σ(Y))上的投影。"),
  ("question","If X and Y are independent, E[X|Y]=E[X] (knowing Y gives no info about X). If X=g(Y), E[X|Y]=g(Y). Tower property: E[E[X|Y]]=E[X]. If Z=g(Y): E[ZE[X|Y]]=E[ZX]. Linearity: E[aX+bZ|Y]=aE[X|Y]+bE[Z|Y].","X,Y独立则E[X|Y]=E[X]。塔性质：E[E[X|Y]]=E[X]。线性性。"),
  ("explore","Example: (X,Y) bivariate normal. E[X|Y=y]=μ_X+ρ(σ_X/σ_Y)(y-μ_Y). Var(X|Y=y)=σ_X²(1-ρ²). Conditional expectation is LINEAR for normal. For general, E[X|Y] minimizes MSE among ALL functions of Y.","例：(X,Y)二元正态。E[X|Y=y]线性。Var(X|Y=y)=σ_X²(1-ρ²)。一般情况E[X|Y]在所有Y的函数中最小化MSE。"),
  ("formalize","Conditional variance: Var(X|Y)=E[(X-E[X|Y])²|Y]. Law of total variance: Var(X)=E[Var(X|Y)]+Var(E[X|Y]). Decomposes variance into 'within-group' + 'between-group.'","条件方差：Var(X|Y)=E[(X-E[X|Y])²|Y]。总方差公式：Var(X)=E[Var(X|Y)]+Var(E[X|Y])。分解为'组内'+'组间'。"),
  ("practice","(1) If X~Exp(λ) and Y=I(X>1). Find E[X|Y]. (2) Roll a die, X=result, Y=parity. Find E[X|Y]. (3) Prove: Var(X)=E[Var(X|Y)]+Var(E[X|Y]). (4) Show E[(X-E[X|Y])²] ≤ E[(X-g(Y))²] for any g.","(1)X~Exp(λ), Y=I(X>1), 求E[X|Y]。(2)掷骰子。求E[X|Y]。(3)证总方差公式。(4)E[X|Y]是最小MSE预测。"),
  ("insight","Conditional expectation = BEST PREDICTION of X given Y (in MSE sense). It's the foundation of: martingales (fair games), Markov processes, Kalman filter, and the EM algorithm. 'Conditioning is the soul of statistics.'","条件期望=给定Y时X的最佳预测(MSE意义)。是鞅、Markov过程、Kalman滤波和EM算法的基础。'条件是统计的灵魂。'")
  ]},
  {"topic":"Kolmogorov's Three Series Theorem","steps":[
  ("pitfall","'If E[Xₙ]=0, ΣXₙ converges a.s.' WRONG! Need more than zero mean. Kolmogorov's Three Series Theorem gives NECESSARY AND SUFFICIENT conditions for a.s. convergence of ΣXₙ with independent Xₙ.","'若E[Xₙ]=0则ΣXₙ a.s.收敛。'错！需更多条件。Kolmogorov三系列定理给出独立变量和a.s.收敛的充要条件。"),
  ("question","Three series: Choose c>0. Let Yₙ=XₙI(|Xₙ|≤c) (truncated). Series 1: ΣP(|Xₙ|>c) < ∞. Series 2: ΣE[Yₙ] converges. Series 3: ΣVar(Yₙ) < ∞. If ALL THREE converge, then ΣXₙ converges a.s. If ANY diverges, ΣXₙ diverges a.s.","三个级数：选c>0。Yₙ=XₙI(|Xₙ|≤c)。级数1: ΣP(|Xₙ|>c)<∞。级数2: ΣE[Yₙ]收敛。级数3: ΣVar(Yₙ)<∞。三者都收敛则ΣXₙ a.s.收敛。任一发散则ΣXₙ a.s.发散。"),
  ("explore","Example: Xₙ = ±1/n with equal probability. Check: P(|Xₙ|>1)=0 so ΣP=0<∞. E[Yₙ]=0. Var(Yₙ)=1/n². Σ1/n²<∞. All three → ΣXₙ converges a.s. Contrast: Xₙ=±1/√n. Var(Yₙ)=1/n. Σ1/n diverges → diverges a.s.","例：Xₙ=±1/n等概。三个条件都满足→a.s.收敛。Xₙ=±1/√n: Σ1/n发散→a.s.发散。"),
  ("insight","The truncation is KEY: large values (Series 1) rarely occur. The mean of truncated vars (Series 2) controls drift. The variance (Series 3) controls oscillation. Together they characterize convergence.","截断是关键：大值(级数1)罕见发生。截断变量均值(级数2)控制漂移。方差(级数3)控制振荡。一起刻画收敛。"),
  ("practice","For each, does ΣXₙ converge a.s.? (1) Xₙ=(-1)ⁿ/n. (2) Xₙ=±1/n² with P(Xₙ=1/n²)=P(Xₙ=-1/n²)=0.5. (3) Xₙ=±√n with prob 1/n each, 0 otherwise. (4) Xₙ=(-1)ⁿ.","对每个，ΣXₙ a.s.收敛吗？(1)Xₙ=(-1)ⁿ/n。(2)Xₙ=±1/n²。(3)Xₙ=±√n各1/n概率否则0。(4)Xₙ=(-1)ⁿ。"),
  ("reflection","Three Series Theorem is the culmination of classical probability. It completely characterizes convergence of sums of independent RVs. Applications: SLLN, law of iterated logarithm, random walk recurrence/transience.","三系列定理是经典概率的顶峰。完全刻画独立RV和收敛。应用：SLLN、重对数律、随机游走常返/暂留。")
  ]}
)

# STA410 — Statistical Computation
P("STA410H1",
  {"topic":"Random Variate Generation","steps":[
  ("setup","We need to generate samples from distributions using only uniform(0,1) random numbers. Inverse transform: if U~Unif(0,1) and F_X is invertible, then X=F⁻¹(U) ~ F.","需要用均匀随机数从分布中生成样本。逆变换：若U~Unif(0,1)且F_X可逆，则X=F⁻¹(U)~F。"),
  ("question","Exponential: F(x)=1-e^{-λx}. F⁻¹(u)=-log(1-u)/λ. So X=-log(U)/λ ~ Exp(λ). For discrete: if F(x)=Σ_{k≤x}p_k, find x such that F(x-1) < U ≤ F(x).","指数：F(x)=1-e^{-λx}。F⁻¹(u)=-log(1-u)/λ。离散：找x使F(x-1)<U≤F(x)。"),
  ("explore","Accept-Reject: sample from proposal g, accept with probability f(x)/[M·g(x)]. Efficiency = 1/M. Choose M = sup f(x)/g(x). Needs f(x)/g(x) bounded. Example: Beta(2,2) using Unif(0,1) proposal.","接受-拒绝：从建议分布g抽样，以概率f(x)/[M·g(x)]接受。效率=1/M。选M=sup f(x)/g(x)。需f(x)/g(x)有界。"),
  ("formalize","Box-Muller: generate Z₁,Z₂~N(0,1) from U₁,U₂~Unif(0,1). Z₁=√(-2log U₁)cos(2πU₂), Z₂=√(-2log U₁)sin(2πU₂). Polar form avoids trig functions.","Box-Muller：从均匀生成正态。Z₁=√(-2log U₁)cos(2πU₂), Z₂=√(-2log U₁)sin(2πU₂)。"),
  ("practice","(1) Write R function to generate Poisson(λ) using inverse transform + recursive PMF. (2) Generate Gamma(2,1) using sum of exponentials. (3) Generate Beta(2,2) using accept-reject. Histogram + theoretical density.","(1)用逆变换写R函数生成Poisson(λ)。(2)用指数和生成Gamma(2,1)。(3)用接受-拒绝生成Beta(2,2)。直方图+理论密度。"),
  ("insight","'All of computational statistics reduces to generating uniform random numbers.' The quality of RNG matters (Mersenne Twister good). For complex distributions: MCMC (Metropolis-Hastings) — the 'universal' sampler, works when accept-reject fails.","'所有计算统计归结为生成均匀随机数。'RNG质量重要。复杂分布用MCMC(Metropolis-Hastings)——'通用'抽样器。")
  ]},
  {"topic":"Monte Carlo Methods","steps":[
  ("principle","Monte Carlo: estimate θ=E[f(X)] by θ̂=(1/n)Σf(Xᵢ) where Xᵢ~f_X. SLLN: θ̂→θ a.s. CLT: √n(θ̂-θ)→N(0,Var(f(X))). Standard error = σ/√n. Accuracy ∝ 1/√n regardless of dimension!","蒙特卡洛：用θ̂=(1/n)Σf(Xᵢ)估计θ=E[f(X)]。SLLN: θ̂→θ a.s.。CLT: 标准误=σ/√n。精度∝1/√n与维数无关！"),
  ("question","Estimate π: generate (U,V)~Unif(0,1)². Count proportion in unit circle: π̂ = 4·(count_in_circle)/n. SE = √(π(4-π)/n). For SE=0.001, n≈10⁶ needed. The 'curse' is in the CONSTANT, not the rate.","估计π：生成(U,V)~Unif(0,1)²。统计圆内比例。SE=√(π(4-π)/n)。SE=0.001需n≈10⁶。"),
  ("explore","Variance reduction: (1) Antithetic variates — use negatively correlated pairs. (2) Control variates — exploit known E[g(X)] to reduce variance. (3) Importance sampling — sample from a proposal, weight by f/proposal ratio.","方差缩减：(1)对偶变量。(2)控制变量——利用已知E[g(X)]。(3)重要性抽样——从建议分布抽样，用f/建议比加权。"),
  ("formalize","Importance sampling: θ=E[f(X)]=∫f(x)p(x)dx = ∫f(x)p(x)/q(x)·q(x)dx = E_q[f(X)p(X)/q(X)]. Choose q with heavier tails than p. Effective sample size ESS=n/(1+CV²(wᵢ)).","重要性抽样：选尾部更厚的q。有效样本量ESS=n/(1+CV²(wᵢ))。"),
  ("practice","(1) Estimate P(X>5) for X~Exp(1) using MC with n=1000. (2) Use importance sampling with Exp(0.2) proposal — compare variance. (3) Estimate ∫₀¹ cos(πx/2)dx. (4) Use antithetic: pair U and 1-U. Compare variances.","(1)估计Exp(1)的P(X>5)。(2)用Exp(0.2)建议的重要性抽样——比较方差。(3)估计积分。(4)用对偶变量：配对U和1-U。比较方差。"),
  ("insight","MC beats numerical integration in high dimensions. Quadrature: error ∝ n^{-2/d} (exponential in d). MC: error ∝ n^{-1/2} (independent of d). For d>4, MC is faster. 'The integral is the expected value, and the Monte Carlo method just computes it.'","高维中MC胜过数值积分。求积：误差∝n^{-2/d}(d的指数)。MC：误差∝n^{-1/2}(与d无关)。d>4时MC更快。")
  ]},
  {"topic":"MCMC and the EM Algorithm","steps":[
  ("pitfall","'MCMC samples are independent.' WRONG! MCMC produces CORRELATED samples. Chain must be thinned or we need larger n. Effective sample size accounts for autocorrelation. Always check trace plots and ESS.","'MCMC样本独立。'错！MCMC产生相关样本。需稀释或更大n。有效样本量考虑自相关。始终检查迹图和ESS。"),
  ("question","Metropolis-Hastings: propose θ*~q(θ*|θ_t). Accept with prob α=min(1, [π(θ*)q(θ_t|θ*)]/[π(θ_t)q(θ*|θ_t)]). Simple version: random walk MH, q(θ*|θ_t)=N(θ_t, σ²). Requires tuning σ².","Metropolis-Hastings：建议θ*~q(θ*|θ_t)。以α=min(1,...)接受。简单：随机游走MH。需要调整σ²。"),
  ("explore","Convergence diagnostics: (1) Trace plot — should look like 'hairy caterpillar.' (2) Autocorrelation — should drop quickly. (3) Gelman-Rubin: run multiple chains, compare within vs between variance. R̂≈1 means convergence.","收敛诊断：(1)迹图——应像'毛虫'。(2)自相关——应快降。(3)Gelman-Rubin：多链，比组内组间方差。R̂≈1表示收敛。"),
  ("formalize","EM Algorithm: for latent variable models. E-step: compute Q(θ|θ^{(t)}) = E_{Z|X,θ^{(t)}}[log L(θ|X,Z)]. M-step: θ^{(t+1)} = argmax Q(θ|θ^{(t)}). Guaranteed to increase observed likelihood each step.","EM算法：潜变量模型。E步：计算Q函数。M步：最大化Q。保证每步增加观测似然。"),
  ("conclusion","Together: (1) Gibbs sampling — sample from conditional distributions (special case of MH). (2) MH — general purpose. (3) HMC — Hamiltonian Monte Carlo, uses gradients. (4) EM — for MLE with missing data.","一起：(1)Gibbs抽样——从条件分布抽样(MH特例)。(2)MH——通用。(3)HMC——哈密顿MC，用梯度。(4)EM——缺失数据的MLE。"),
  ("meta","MCMC revolutionized Bayesian statistics. Before MCMC (pre-1990): Bayesian inference limited to conjugate models. After MCMC: any model is computationally feasible. 'MCMC is to Bayes what CLT is to frequentists.'","MCMC革命化了贝叶斯统计。MCMC前：贝叶斯限于共轭模型。MCMC后：任何模型计算可行。'MCMC对贝叶斯如同CLT对频率学派。'")
  ]}
)

# STA414 — Statistical Methods for ML II
P("STA414H1",
  {"topic":"Deep Learning Fundamentals","steps":[
  ("setup","Neural networks: layers of neurons. Each neuron: z = w·x + b, a = σ(z) (activation function). Universal Approximation Theorem: a single hidden layer with enough neurons can approximate ANY continuous function on a compact set.","神经网络：神经元层。通用近似定理：足够神经元的单隐层可逼近紧集上任何连续函数。"),
  ("question","Backpropagation: compute gradients via chain rule. Forward pass: compute activations layer by layer. Backward pass: compute ∂Loss/∂w for each weight. Gradient descent: w ← w - η·∂L/∂w.","反向传播：通过链式法则算梯度。前向：逐层计算激活。反向：算每权重∂Loss/∂w。梯度下降。"),
  ("explore","Activation functions: (1) Sigmoid: 1/(1+e^{-x}) — saturates, vanishing gradient. (2) ReLU: max(0,x) — non-saturating, faster. (3) Tanh: (e^x-e^{-x})/(e^x+e^{-x}). (4) Softmax: e^{zᵢ}/Σe^{zⱼ} for classification.","激活函数：(1)Sigmoid——饱和、梯度消失。(2)ReLU——不饱和、更快。(3)Tanh。(4)Softmax用于分类。"),
  ("formalize","Training challenges: (1) Vanishing/exploding gradients (use ReLU, batch norm, residual connections). (2) Overfitting (dropout, data augmentation, weight decay). (3) Local minima (plateaus, saddle points). (4) Learning rate tuning (Adam optimizer).","训练挑战：(1)梯度消失/爆炸(ReLU、批归一化)。(2)过拟合(dropout、数据增强)。(3)局部极小。(4)学习率调节(Adam)。"),
  ("practice","In R/TensorFlow: (1) Build a 2-hidden-layer net for MNIST. (2) Use ReLU activations. (3) Train with Adam. (4) Add dropout for regularization. (5) Compare with logistic regression.","在R/TensorFlow中：(1)为MNIST建2隐层网络。(2)用ReLU。(3)用Adam训练。(4)加dropout正则化。(5)与逻辑回归比较。"),
  ("insight","Deep learning's power: learn HIERARCHICAL representations — early layers detect edges, middle layers detect shapes, late layers detect objects. This hierarchy LEARNED, not hand-crafted. More data + more compute → better performance.","深度学习力量：学习层次表示——早期检边、中层检形状、晚期检物体。层次是学习来的，不是手工设计的。")
  ]},
  {"topic":"Gaussian Processes","steps":[
  ("principle","A Gaussian Process (GP) is a distribution over FUNCTIONS. f(x)~GP(m(x),k(x,x')). Mean m(x) usually 0. Covariance k(x,x') defines function properties: smoothness, periodicity, stationarity.","高斯过程(GP)是函数上的分布。f(x)~GP(m(x),k(x,x'))。协方差k(x,x')定义函数性质：平滑性、周期性、平稳性。"),
  ("question","RBF kernel: k(x,x')=σ²exp(-‖x-x'‖²/2ℓ²). ℓ=lengthscale (smoothness). σ²=signal variance. Key property: RBF generates INFINITELY smooth (C∞) functions. Matern kernel: less smooth (ν=3/2 → C¹, ν=5/2 → C²).","RBF核：k(x,x')=σ²exp(-‖x-x'‖²/2ℓ²)。ℓ=长度尺度(平滑性)。RBF产生无穷光滑函数。Matern核：较不光滑。"),
  ("explore","GP regression: given (xᵢ,yᵢ), predict f(x*). Joint: [y; f*]~N(0, [K+σ²I, K*; K*ᵀ, K**]). Predictive: f*|data ~ N(K*ᵀ(K+σ²I)⁻¹y, K**-K*ᵀ(K+σ²I)⁻¹K*). Provides UNCERTAINTY estimates.","GP回归：给定(xᵢ,yᵢ)预测f(x*)。预测分布提供不确定性估计。"),
  ("formalize","Kernel selection encodes PRIOR knowledge about the function. Additive kernels: k=k₁+k₂ (sum of independent functions). Product kernels: k=k₁·k₂ (interaction). Automatic Relevance Determination (ARD): different ℓ per dimension.","核选择编码关于函数的先验知识。加性、乘积核、ARD(每维不同ℓ)。"),
  ("practice","(1) Simulate data: y=sin(x)+ε. (2) Fit GP with RBF kernel. (3) Plot predictive mean ± 2SD. (4) Compare with Matern(3/2) kernel. (5) Optimize hyperparameters (ℓ, σ², σ²_n) via marginal likelihood.","(1)模拟y=sin(x)+ε。(2)用RBF核拟合GP。(3)画预测均值±2SD。(4)与Matern(3/2)比较。(5)通过边际似然优化超参数。"),
  ("insight","GP = 'infinite-dimensional Bayesian regression.' Training = computing posterior over functions. Prediction = posterior predictive with uncertainty. Key advantage: well-calibrated uncertainty. Key limit: O(n³) computation (n>10k hard). Solutions: sparse GPs, inducing points.","GP='无穷维贝叶斯回归'。训练=计算函数的后验。关键优势：良好校准的不确定性。关键局限：O(n³)计算。解决：稀疏GP、诱导点。")
  ]},
  {"topic":"Graphical Models","steps":[
  ("pitfall","'Directed edges mean causation.' NOT necessarily! Bayesian networks encode CONDITIONAL INDEPENDENCE, not causation. A directed edge might represent a causal relationship, but it could also be a convenient factorization.","'有向边意味因果。'不一定！贝叶斯网编码条件独立，不是因果。有向边可能表示因果关系，也可能是方便的因子分解。"),
  ("question","Directed Graphical Model (Bayesian Net): nodes=variables, edges=dependencies. Factorization: P(X₁,...,Xₙ)=∏P(Xᵢ|Pa(Xᵢ)). DAG required (no cycles). Chain: X→Y→Z ⟺ X ⟂ Z | Y.","有向图模型(贝叶斯网)：P(X₁,...,Xₙ)=∏P(Xᵢ|Pa(Xᵢ))。需DAG(无环)。链：X→Y→Z⟺X⟂Z|Y。"),
  ("explore","Undirected (Markov Random Field): factorization over cliques. P(X)∝∏_{cliques} ψ_C(X_C). Potentials ψ_C are non-negative, NOT probabilities (must normalize). Used for: image segmentation (pixel CRF), spatial statistics.","无向图(Markov随机场)：在团上分解。势函数ψ_C非负不是概率(需归一化)。用于：图像分割、空间统计。"),
  ("formalize","Conditional Random Field (CRF): P(Y|X)∝exp(Σλₖfₖ(Y_c,X)). Discriminative! Rather than modeling P(X,Y), model P(Y|X) directly. Better when X has complex dependencies we don't want to model.","条件随机场(CRF)：P(Y|X)∝exp(Σλₖfₖ(Y_c,X))。判别式！直接建模P(Y|X)。当X有复杂依赖时更好。"),
  ("practice","(1) Draw a Bayesian net for: Cloudy → Rain, Cloudy → Sprinkler. Rain → Wet Grass, Sprinkler → Wet Grass. (2) Is Rain ⟂ Sprinkler? (3) Condition on Wet Grass — are they independent? (4) What if we also condition on Cloudy?","(1)画贝叶斯网。(2)Rain和Sprinkler独立吗？(3)给定Wet Grass后独立吗？(4)再给定Cloudy呢？"),
  ("reflection","Graphical models = VISUAL language for probability. Structure LEARNING (finding the graph from data) is NP-hard. BUT given a graph, inference (computing probabilities) uses message passing (belief propagation). The junction tree algorithm generalizes this.","图模型=概率的可视化语言。结构学习(NP难)。给定图，推断用消息传递(信念传播)。联结树算法推广了这一点。")
  ]}
)

print("\nDone! All CS, thin MATH, and STA courses enriched!")
