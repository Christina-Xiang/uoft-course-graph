# UofT Course Knowledge Graph

Interactive knowledge graphs and AI study assistants for University of Toronto Mathematics, Statistics, and Computer Science courses.

**Live site:** [uoft-course-graph.netlify.app](https://uoft-course-graph.netlify.app)

## About

Before starting university, I wanted a clear picture of what I would learn across the Mathematics Major, Statistics Major, and Computer Science Minor at UofT, and how the courses connect to each other. I used an AI coding agent (OpenCode) to research the courses, break each one down into a knowledge ontology, and turn the results into an interactive website.

The project covers **3 programs, 35 courses, and 134 knowledge topics**.

## Features

- **Knowledge graph**: an interactive graph of courses and topics showing how concepts connect across courses
- **Course pages**: for each course, a description, credit value, the later courses it opens up, the programs it belongs to, and its key knowledge topics
- **Curriculum roadmap**: a 3-year, semester-by-semester course plan
- **Preparation guide**: what to review before starting university
- **AI tutor skills**: each course is packaged as an AI skill (`SKILL.md` plus reference files) covering core concepts, key theorems, computation methods, proof techniques, common pitfalls, and study methods, so an AI assistant such as Claude can answer questions within the scope of the course

## Courses Included (examples)

| Area             | Courses                                                      |
| ---------------- | ------------------------------------------------------------ |
| Computer Science | CSC108, CSC148, CSC165, CSC207, CSC209, CSC236, CSC263, CSC311 |
| Mathematics      | MAT137, MAT237, MAT267, MAT315                               |
| Statistics       | STA130                                                       |

## Repository Structure

```
uoft-course-graph/
├── index.html          # Web app entry point
├── assets/             # Compiled JavaScript and CSS
├── *-graph.json        # Knowledge graph data for each course
├── favicon.svg
└── _redirects          # Netlify routing rules
```

## Run Locally

This folder contains the built version of the site. To view it on your own computer:

```bash
cd uoft-course-graph
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Built With

- JavaScript and Vite
- OpenCode (AI coding agent) for research, content generation, and development
- Netlify for hosting

## Disclaimer

This is a personal study project and is not affiliated with the University of Toronto. Course content was generated with the help of AI and may contain errors. Always check the official [Arts & Science Academic Calendar](https://artsci.calendar.utoronto.ca) for course requirements.

## Author

**Christina (Chuqin) Xiang**, University of Toronto
[LinkedIn](https://www.linkedin.com/in/chuqin-xiang-86b271414)
