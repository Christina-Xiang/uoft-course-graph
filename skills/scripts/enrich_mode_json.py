#!/usr/bin/env python3
"""Enrich all thin mode JSON files with rich bilingual content."""
import json, os

SKILLS_DIR = "skills"

def get_kg_nodes(cid):
    for d in ['math','stats','cs']:
        p = os.path.join(SKILLS_DIR, d)
        if not os.path.isdir(p): continue
        for s in os.listdir(p):
            if s.startswith(cid[:4].lower()):
                kp = os.path.join(p, s, 'references', f'{cid[:8]}-knowledge-graph.json')
                if os.path.exists(kp):
                    try:
                        with open(kp) as f: kg = json.load(f)
                        return [n['id'] for n in kg.get('nodes', [])[:6]]
                    except: pass
    return []

def write_mode(cpath, mode, cid, topic, steps_data):
    mlab = {'socratic':'Socratic Discovery','deductive':'Deductive Derivation','correction':'Correction Attribution'}
    stype = {'socratic':'socratic','deductive':'deductive','correction':'correction'}
    sid = {'socratic':'S','deductive':'D','correction':'C'}
    diff = {'socratic':2,'deductive':3,'correction':2}
    steps = [{"type":t,"template_en":e,"template_zh":z} for t,e,z in steps_data]
    if not steps: return 0
    kgn = get_kg_nodes(cid)
    dom = 'cs' if cid.startswith('CSC') else 'stats' if cid.startswith('STA') else 'math'
    data = {
        "name": f"{cid[:8]} — {mlab[mode]} ({topic})",
        "description": steps[0]['template_en'][:150],
        "parameters": {"type":"object","properties":{"courseId":{"type":"string","enum":[cid[:8]]},"skillId":{"type":"string","const":f"{cid[:8]}-SKILL-{sid[mode]}1"},"lang":{"type":"string","enum":["en","zh"]}},"required":["courseId","skillId","lang"]},
        "steps": steps,
        "references": ["references/formulas.md","references/proof-techniques.md","references/counterexamples.md","references/concept-map.md"],
        "metadata": {"domain":dom,"course":cid[:8],"skillType":stype[mode],"difficulty":diff[mode],"relatedUnits":["unit-1"],"version":"1.0","knowledgeGraphNodes":kgn[:5]}
    }
    with open(os.path.join(cpath,f'{mode}.json'),'w') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
    return os.path.getsize(os.path.join(cpath,f'{mode}.json'))

def find_course(cid):
    dom = 'cs' if cid.startswith('CSC') else 'stats' if cid.startswith('STA') else 'math'
    for s in os.listdir(os.path.join(SKILLS_DIR, dom)):
        if s.startswith(cid[:4].lower()):
            return os.path.join(SKILLS_DIR, dom, s)
    return None

def process(cid, s=None, d=None, c=None):
    cp = find_course(cid)
    if not cp: print(f"  X {cid}: not found"); return 0
    cnt = 0
    if s: sz = write_mode(cp,'socratic',cid,s['topic'],s['steps']); cnt+=1; print(f"  OK {cid} socratic: {sz:,}b ({len(s['steps'])} steps)")
    if d: sz = write_mode(cp,'deductive',cid,d['topic'],d['steps']); cnt+=1; print(f"  OK {cid} deductive: {sz:,}b ({len(d['steps'])} steps)")
    if c: sz = write_mode(cp,'correction',cid,c['topic'],c['steps']); cnt+=1; print(f"  OK {cid} correction: {sz:,}b ({len(c['steps'])} steps)")
    return cnt

# ═══ CSC207 — Software Design ═══
S = {"topic":"Encapsulation","steps":[
("setup","Let's discover why we hide internal state. Imagine a BankAccount class. What if balance is public? acc.balance = -1000 lets anyone overdraw without checks! Encapsulation bundles data with the methods that operate on it, hiding internal details.","让我们发现为什么隐藏内部状态。想象一个BankAccount类。如果balance是public的会怎样？acc.balance = -1000 允许任何人无检查透支！封装将数据与操作它的方法捆绑，隐藏内部细节。"),
("question","A BankAccount class has a private _balance attribute and public deposit()/withdraw() methods. What invariants can we enforce through the methods that we CANNOT enforce with public _balance? Think about: minimum balance, daily withdrawal limits, overdraft protection.","BankAccount类有私有的_balance属性和公共的deposit()/withdraw()方法。通过方法我们能强制哪些通过公共_balance无法强制的不变性？思考：最低余额、每日取款限额、透支保护。"),
("explore","Without encapsulation, callers must check conditions themselves — but they might forget! With encapsulation, the class ENFORCES its invariants. Example: if withdraw() checks balance >= amount before subtracting, callers CANNOT accidentally overdraw. This is 'defensive programming.'","没有封装，调用者必须自己检查条件——但他们可能忘记！有了封装，类强制执行其不变性。例子：如果withdraw()在扣减前检查balance >= amount，调用者就无法意外透支。这是'防御性编程'。"),
("formalize","Encapsulation: (1) Make attributes PRIVATE (prefix with _). (2) Provide PUBLIC methods that enforce invariants. (3) Never return mutable internal references (return a copy or None). Benefits: protect invariants, change implementation without breaking callers, reduce coupling.","封装：(1) 使属性私有（加_前缀）。(2) 提供强制执行不变性的公共方法。(3) 绝不返回可变的内部引用（返回副本或None）。好处：保护不变性、改变实现而不破坏调用者、减少耦合。"),
("practice","Identify encapsulation violations: (1) class Student: def __init__(self): self.grades = []. (2) class Logger: def get_log(self): return self._log. (3) class Point: x, y = 0, 0. Fix each and explain which principle was violated.","识别封装违规：(1)class Student: def __init__(self): self.grades = []。(2)class Logger: def get_log(self): return self._log。(3)class Point: x, y = 0, 0。修正每个并解释违反了哪个原则。"),
("insight","'Tell, don't ask' — instead of ASKING an object for its data and DECIDING what to do, TELL the object what to do and let it decide. obj.get_x() + obj.process(obj.get_y()) → obj.do_something(). Encapsulation is the foundation of OOP: bundling state + behavior.","'告诉，不要询问'——不要询问对象的数据然后决定做什么，告诉对象做什么让它决定。obj.get_x() + obj.process(obj.get_y()) → obj.do_something()。封装是OOP的基础：状态+行为的捆绑。")
]}
D = {"topic":"Liskov Substitution Principle","steps":[
("principle","LSP: If S is a subtype of T, then objects of T should be replaceable by objects of S WITHOUT altering the desirable properties of the program (correctness, task completion). In short: subtypes must be BEHAVIORALLY substitutable.","LSP：如果S是T的子类型，那么T的对象应能被S的对象替换而不会改变程序的理想性质（正确性、任务完成）。简言之：子类型必须在行为上可替换。"),
("step1","Consider Rectangle.setWidth(w) sets width = w, keeping height unchanged. Now Square extends Rectangle. Square.setWidth(w) sets BOTH width and height = w (to maintain squareness). This feels 'correct' for a square, but BREAKS code that uses Rectangle.","考虑Rectangle.setWidth(w)设置width=w，保持height不变。现在Square继承Rectangle。Square.setWidth(w)同时设置width和height=w（保持正方形）。这对正方形感觉'正确'，但破坏了使用Rectangle的代码。"),
("step2","Code: void f(Rectangle r) { r.setWidth(5); r.setHeight(4); assert r.area() == 20; }. Passing a Square to f fails the assertion because setWidth(5) also changed height. Square's setWidth is STRONGER than Rectangle's — it changes the postcondition (height may change).","代码：void f(Rectangle r) { r.setWidth(5); r.setHeight(4); assert r.area() == 20; }。传递Square给f会失败，因为setWidth(5)也改变了height。Square的setWidth比Rectangle的更强——它改变了后置条件（height可能改变）。"),
("step3","LSP requires: (1) Preconditions cannot be STRENGTHENED in subtypes. (2) Postconditions cannot be WEAKENED. (3) INVARIANTS of the parent must be preserved. Square.setWidth strengthens the postcondition: it now also modifies height. This violates LSP.","LSP要求：(1)前置条件不能在子类型中增强。(2)后置条件不能减弱。(3)父类的不变性必须保持。Square.setWidth增强了后置条件：它现在也修改height。这违反了LSP。"),
("conclusion","'A square is NOT a rectangle in OOP!' The mathematical IS-A relationship does NOT imply behavioral substitutability. Better design: Shape as abstract base class; Rectangle and Square both extend Shape with appropriate invariants. Or use composition.","'正方形在OOP中不是矩形！'数学上的IS-A关系不意味着行为上的可替代性。更好的设计：Shape作为抽象基类；Rectangle和Square都继承Shape并保持各自的不变性。或使用组合。"),
("meta","LSP is about CONTRACTS. Subtypes must honor the parent's contract — they can ADD to it but never REMOVE from it. This is 'Design by Contract': preconditions, postconditions, invariants. LSP = behavioral subtyping, not just code reuse.","LSP关乎契约。子类型必须遵守父类型的契约——它们可以添加但绝不能删除。这是'契约式设计'：前置条件、后置条件、不变性。LSP = 行为子类型，而不仅仅是代码复用。")
]}
C = {"topic":"Inheritance Overuse — Fragile Base Class","steps":[
("pitfall","Common error: extending a class just to reuse a few methods. 'I'll extend ArrayList to add logging!' class LogList extends ArrayList { ... }. PROBLEM: ArrayList's internals change between Java versions. Your add() override may NOT be called by all superclass methods.","常见错误：仅为了复用几个方法而继承一个类。'我要扩展ArrayList来添加日志记录！'class LogList extends ArrayList { ... }。问题：ArrayList的内部实现在Java版本间会变化。你的add()重写可能不会被所有超类方法调用。"),
("question","class LogList extends ArrayList { void add(Object o) { log('adding'); super.add(o); } }. Now we call addAll(otherList). AddAll is defined in ArrayList.addAll(), which internally calls add(). Which add() does it call — LogList's or ArrayList's?","class LogList extends ArrayList { void add(Object o) { log('adding'); super.add(o); } }。现在调用addAll(otherList)。AddAll在ArrayList.addAll()中定义，内部调用add()。它调用哪个add()——LogList的还是ArrayList的？"),
("explore","In Java, ArrayList.addAll() calls the OVERRIDDEN add() if the subclass overrides it. So LogList.addAll() calls LogList.add() — good! But ArrayList.someInternalMethod() might call add() too — and you might not know about it. The base class's internal behavior is FRAGILE and undocumented.","在Java中，如果子类重写了add()，ArrayList.addAll()会调用被重写的add()。所以LogList.addAll()调用LogList.add()——好！但ArrayList.someInternalMethod()也可能调用add()——你可能不知道。基类的内部行为是脆弱的且未文档化。"),
("insight","The 'Fragile Base Class Problem': Changes to a parent class can break subclasses in unpredictable ways. This is why frameworks warn against extending core classes. Prefer COMPOSITION over INHERITANCE: class LogList { private List inner; void add(Object o) { log('adding'); inner.add(o); } }.","'脆弱的基类问题'：对父类的更改可能以不可预测的方式破坏子类。这就是为什么框架警告不要继承核心类。优先使用组合而非继承：class LogList { private List inner; void add(Object o) { log('adding'); inner.add(o); } }。"),
("practice","For each, refactor from inheritance to composition: (1) class SafeDict extends HashMap { ... }. (2) class LoggedInputStream extends FileInputStream { ... }. (3) class CounterList extends ArrayList { ... }. After refactoring, list reasons why composition is better.","对每个，从继承重构为组合：(1)class SafeDict extends HashMap { ... }。(2)class LoggedInputStream extends FileInputStream { ... }。(3)class CounterList extends ArrayList { ... }。重构后，列出为什么组合更好的原因。"),
("reflection","Rule: Use inheritance ONLY for IS-A relationships where the subtype is BEHAVIORALLY a subtype (LSP). For HAS-A, USES-A, or 'wrapper' relationships → use composition. 'Favor composition over inheritance' is the most important design guideline in OOP.","规则：仅当子类型在行为上确实是子类型（LSP）的IS-A关系时才使用继承。对于HAS-A、USES-A或'包装器'关系→使用组合。'优先使用组合而非继承'是OOP中最重要的设计指南。")
]}
process("CSC207H1", S, D, C)

# ═══ CSC209 — Software Tools and Systems Programming ═══
process("CSC209H1",
    {"topic":"Pointers and Memory","steps":[
    ("setup","Let's discover pointers. int x = 5 stores 5 at some memory address &x. A POINTER is a variable that stores a memory address. int *p = &x. p stores x's address. *p dereferences to get 5. Pointers are INDIRECTION — a way to refer to data through its location.","让我们发现指针。int x = 5 将5存储在某内存地址&x。指针是存储内存地址的变量。int *p = &x。p存储x的地址。*p解引用得到5。指针是间接引用——通过位置引用数据的方式。"),
    ("question","void swap(int a, int b) { int t = a; a = b; b = t; }. In C, this DOES NOT swap the caller's variables. Why? What happens to a and b inside the function? Draw the stack frames. Now write swap(int *p, int *q) that actually works.","void swap(int a, int b) { int t = a; a = b; b = t; }。在C中，这不会交换调用者的变量。为什么？a和b在函数内部发生了什么？画出栈帧。现在编写真正能工作的swap(int *p, int *q)。"),
    ("explore","C passes by VALUE — the function gets COPIES. swap(a,b) copies values of a,b into parameters. The originals are unchanged. swap(&a,&b) passes ADDRESSES. Inside, *p = &a = the original a. So *p = t modifies the ORIGINAL. This is 'pass by value, where the value is an address.'","C是传值调用——函数获得副本。swap(a,b)将a,b的值复制到参数中。原变量不变。swap(&a,&b)传递地址。内部，*p = &a = 原a。所以*p = t修改了原变量。这是'传值，但值是一个地址'。"),
    ("formalize","Pointer rules: (1) p = &x makes p point to x. (2) *p accesses the value at that address. (3) malloc allocates heap memory, returns void*. (4) free releases heap memory. (5) NULL means 'points to nothing' — dereferencing NULL crashes (segfault).","指针规则：(1)p=&x使p指向x。(2)*p访问该地址的值。(3)malloc分配堆内存，返回void*。(4)free释放堆内存。(5)NULL表示'不指向任何东西'——解引用NULL会崩溃（段错误）。"),
    ("practice","Trace: int a=5, b=10; int *p=&a, *q=&b; *p = *q; p = q; *p = 15;. What are a and b after each step? Draw the pointer diagram showing stack variables, addresses, and their connections. Label which variables alias the same location.","跟踪：int a=5, b=10; int *p=&a, *q=&b; *p = *q; p = q; *p = 15;。每一步后a和b的值？画出指针图显示栈变量、地址和它们的连接。标记别名同一位置的变量。"),
    ("insight","Pointers are POWERFUL but DANGEROUS. They enable dynamic data structures (linked lists, trees), efficient array passing, and direct memory manipulation. But also cause: buffer overflows, dangling pointers, memory leaks, segmentation faults. With great power comes great responsibility.","指针强大但危险。它们使动态数据结构（链表、树）、高效数组传递和直接内存操作成为可能。但也导致：缓冲区溢出、悬空指针、内存泄漏、段错误。能力越大责任越大。")
    ]},
    {"topic":"Producer-Consumer with Bounded Buffer","steps":[
    ("principle","Producer-consumer: one thread produces data, another consumes it. They share a fixed-size buffer. We need: mutual exclusion (not modify buffer simultaneously), synchronization (don't produce when full, don't consume when empty). Semaphores are the solution.","生产者-消费者：一个线程生产数据，另一个消费。它们共享一个固定大小的缓冲区。我们需要：互斥（不同时修改缓冲区），同步（满时不生产，空时不消费）。信号量是解决方案。"),
    ("step1","Let empty = N (buffer slots available), full = 0 (items available), mutex = 1 (binary semaphore for mutual exclusion). Initialize all three. empty starts at N because buffer is empty; full starts at 0 because no items yet.","设empty=N（缓冲区可用槽位），full=0（可用项目数），mutex=1（二进制信号量，用于互斥）。初始化三者。empty从N开始因为缓冲区为空；full从0开始因为还没有项目。"),
    ("step2","Producer: wait(empty) — blocks if buffer full. wait(mutex) — ensures exclusive access. add_item(). signal(mutex) — releases lock. signal(full) — notifies consumer. Each step is essential. What happens if we swap wait(empty) and wait(mutex)? Deadlock!","生产者：wait(empty)——缓冲区满时阻塞。wait(mutex)——确保独占访问。add_item()。signal(mutex)——释放锁。signal(full)——通知消费者。每一步都必不可少。如果交换wait(empty)和wait(mutex)会发生什么？死锁！"),
    ("step3","Consumer: wait(full) — blocks if buffer empty. wait(mutex) — ensures exclusive access. remove_item(). signal(mutex) — releases lock. signal(empty) — notifies producer. This mirrors the producer exactly. The symmetry ensures correctness.","消费者：wait(full)——缓冲区空时阻塞。wait(mutex)——确保独占访问。remove_item()。signal(mutex)——释放锁。signal(empty)——通知生产者。这与生产者完全对称。对称性确保正确性。"),
    ("conclusion","wait(empty) and wait(full) are SYNCHRONIZATION semaphores — they order execution. wait(mutex) is MUTUAL EXCLUSION — it prevents simultaneous buffer access. The pattern: sync-before-mutex prevents deadlock. Signal order doesn't matter. This pattern works for N producers and M consumers too.","wait(empty)和wait(full)是同步信号量——它们排序执行。wait(mutex)是互斥信号量——它防止同时访问缓冲区。模式：同步先于互斥预防死锁。signal的顺序不重要。这个模式也适用于N个生产者和M个消费者。"),
    ("meta","This is the CLASSIC concurrent programming pattern. It appears in: OS kernel buffers, web server request queues, database transaction logs, Kafka message queues. The bounded buffer is the foundation of ALL producer-consumer architectures.","这是经典的并发编程模式。它出现在：OS内核缓冲区、Web服务器请求队列、数据库事务日志、Kafka消息队列。有界缓冲区是所有生产者-消费者架构的基础。")
    ]},
    {"topic":"Buffer Overflow — Unsafe String Handling","steps":[
    ("pitfall","char buf[10]; gets(buf); If user types 20 characters, data OVERFLOWS buf and overwrites adjacent stack memory — return address, local variables, saved frame pointer. This is THE most common security vulnerability.","char buf[10]; gets(buf); 如果用户输入20个字符，数据溢出buf并覆盖相邻的栈内存——返回地址、局部变量、保存的帧指针。这是最常见的安全漏洞。"),
    ("question","What gets overwritten when buf overflows? The stack layout: local vars → saved frame pointer → return address → caller's frame. If we overflow enough, we can overwrite the RETURN ADDRESS. When the function returns, execution jumps to the attacker's code!","buf溢出时什么会被覆盖？栈布局：局部变量→保存的帧指针→返回地址→调用者的帧。如果溢出足够，我们可以覆盖返回地址。函数返回时，执行跳转到攻击者的代码！"),
    ("explore","Call gets(buf) on a protected system. Modern defenses: (1) Stack canaries — a guard value before return addr that's checked before return. (2) ASLR — randomizes memory layout. (3) NX bit — marks stack as non-executable. But these are arms races — not foolproof.","在受保护系统上调用gets(buf)。现代防御：(1)栈金丝雀——返回地址前的守卫值，返回前检查。(2)ASLR——随机化内存布局。(3)NX位——将栈标记为不可执行。但这是军备竞赛——并非万无一失。"),
    ("insight","Solutions: (1) NEVER use gets(), strcpy(), sprintf(). Use fgets(), strncpy(), snprintf(). (2) ALWAYS check bounds before writing. (3) Use safe libraries. (4) Treat ALL input as malicious. Heartbleed bug (2014) was a buffer over-read that leaked millions of passwords.","解决方案：(1)绝不使用gets()、strcpy()、sprintf()。使用fgets()、strncpy()、snprintf()。(2)写入前始终检查边界。(3)使用安全库。(4)将所有输入视为恶意。Heartbleed漏洞（2014）是一个缓冲区过度读取，泄露了数百万密码。"),
    ("practice","Rewrite these safely: (1) char buf[100]; strcpy(buf, user_input). (2) void f(char *s) { char buf[10]; sprintf(buf, 'Hello %s', s); }. (3) int n; scanf('%d', &n); char data[n]; gets(data). Explain the vulnerability in each original version.","安全地重写这些：(1)char buf[100]; strcpy(buf, user_input)。(2)void f(char *s) { char buf[10]; sprintf(buf, 'Hello %s', s); }。(3)int n; scanf('%d', &n); char data[n]; gets(data)。解释每个原始版本的漏洞。"),
    ("reflection","Buffer overflow is the #1 software security vulnerability of all time (CWE-119). It caused Morris Worm (1988), Code Red (2001), SQL Slammer (2003), and countless others. Rule: 'All input is evil until proven safe. Always check size before writing.'","缓冲区溢出是有史以来的#1软件安全漏洞（CWE-119）。它导致了Morris蠕虫（1988）、Code Red（2001）、SQL Slammer（2003）和无数其他攻击。规则：'所有输入在证明安全前都是恶意的。写入前始终检查大小。'")
    ]}
)

print("CSC207, CSC209 done. Continuing...")
