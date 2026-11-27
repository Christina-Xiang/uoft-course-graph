# UofT Course Knowledge Graph & AI Study Assistants

Knowledge graphs and AI tutor skill packages for University of Toronto Mathematics, Statistics, and Computer Science courses.

**Live site:** [uoft-course-graph.netlify.app](https://uoft-course-graph.netlify.app)

## About

Before starting university, I wanted a clear picture of what I would learn across the Mathematics, Statistics, and Computer Science programs at UofT, and how the courses connect to each other. I researched 35 courses, designed a knowledge structure and a set of teaching modes for each one, and used an AI coding agent (OpenCode) to help build the project.

The project has two parts:

1. **AI tutor skill packages**: one package per course that an AI assistant can use to tutor students within the scope of that course.
2. **An interactive website**: a knowledge graph of 134 topics and a 3-year course roadmap.

## AI Tutor Skill Packages

The `skills/` folder is the core of this project.

```
skills/
├── cs/            # Computer Science courses (CSC108, CSC148, CSC165, ...)
├── math/          # Mathematics courses
├── stats/         # Statistics courses
├── scripts/       # Python scripts used to generate, enrich, and clean the packages
└── skill.json     # Global registry of all skills
```

Each course folder contains:

| File | Purpose |
| --- | --- |
| `SKILL.md` | Entry point: instructions telling the AI how to tutor the course and which mode to use |
| `socratic.json` | **Socratic mode**: guides the student to discover a concept through questions |
| `deductive.json` | **Deductive mode**: derives a key theorem or method step by step from definitions |
| `correction.json` | **Correction mode**: diagnoses a common mistake and the misconception behind it |
| `references/` | Formulas, methods, case studies, a concept map, a self-assessment checklist, real-world applications, and the course knowledge graph |
| `README.md`, `LICENSE` | Package description and license |

### Three Teaching Modes

Each mode follows a fixed 6-step structure, written in both English and Chinese:

| Mode | When to use | Steps |
| --- | --- | --- |
| Socratic | Exploring a new concept | setup → question → explore → formalize → practice → insight |
| Deductive | Understanding why a theorem holds | principle → step 1 → step 2 → step 3 → conclusion → meta-reflection |
| Correction | Fixing a common error | pitfall → question → explore → insight → practice → reflection |

The goal is for the AI to guide students' thinking rather than just give answers.

### How to Use a Skill

**Option 1: Paste into any AI chat (no setup)**
1. Open a course folder, for example `skills/cs/csc108h1-...`.
2. Open `SKILL.md`, copy all of its text, and paste it into a chat with Claude or ChatGPT.
3. Add a line such as "Please tutor me following the instructions above," then ask your question.

**Option 2: Install in Claude**
1. Download the course folder and compress it into a `.zip` file, with `SKILL.md` at its top level.
2. In Claude, open the Skills settings page and upload the zip.
3. Claude will use the skill when you ask about that course.

**Option 3: Use with OpenCode**

Copy the course folder into OpenCode's skills directory (for example `~/.opencode/agent/skills/`), then restart OpenCode.

## How It Was Built

The full process is documented in [`SKILL_SYSTEM_BUILD_GUIDE.md`](SKILL_SYSTEM_BUILD_GUIDE.md) (in Chinese). In short:

1. **Domain modeling**: split each course into units, then listed its concepts, theorems, methods, techniques, common pitfalls, skills, and learning methods.
2. **Knowledge graph**: turned these into nodes, connected by `contains`, `requires`, `develops`, and `teaches` edges, with bilingual labels and difficulty levels.
3. **Reference materials**: wrote formulas, methodologies, case studies, concept maps, checklists, and applications for each course.
4. **Teaching modes**: wrote Socratic, Deductive, and Correction sequences using shared 6-step templates.
5. **Validation**: defined checks such as valid JSON, exactly 6 steps per mode, correct step types, complete bilingual text, and knowledge graph references that point to real nodes.
6. **Website**: converted the knowledge graphs into a format the website can render, then built and deployed it.

The approach is general, so the same framework can be adapted to other subjects.

## Website

The `uoft-course-graph/` folder contains the built website: an interactive knowledge graph, course pages, and a semester-by-semester roadmap. Built with JavaScript and Vite, and hosted on Netlify.

## Disclaimer

This is a personal study project and is not affiliated with the University of Toronto. Course content was generated with the help of AI and may contain errors. Always check the official [Arts & Science Academic Calendar](https://artsci.calendar.utoronto.ca) and your course materials.

## Author

**Christina (Chuqin) Xiang**, University of Toronto

[LinkedIn](https://www.linkedin.com/in/christinaxiangcq)
