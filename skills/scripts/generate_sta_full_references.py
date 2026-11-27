#!/usr/bin/env python3
"""Generate full reference files for all 15 STA courses matching MAT137Y1 depth."""
import json, os, re

ONTOLOGY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "course-ontology")
SKILLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "skills")

STA_COURSES = {
    "STA130H1": {"name": "An Introduction to Statistical Reasoning and Data Science", "domain": "stats-intro", "slug": "sta130h1-an-introduction-to-statistical-reasoning-and-data-science"},
    "STA237H1": {"name": "Probability, Statistics and Data Analysis I", "domain": "stats-probability", "slug": "sta237h1-probability-statistics-and-data-analysis-i"},
    "STA238H1": {"name": "Probability, Statistics and Data Analysis II", "domain": "stats-inference", "slug": "sta238h1-probability-statistics-and-data-analysis-ii"},
    "STA257H1": {"name": "Probability and Statistics I", "domain": "stats-probability", "slug": "sta257h1-probability-and-statistics-i"},
    "STA261H1": {"name": "Probability and Statistics II", "domain": "stats-inference", "slug": "sta261h1-probability-and-statistics-ii"},
    "STA302H1": {"name": "Methods of Data Analysis I", "domain": "stats-regression", "slug": "sta302h1-methods-of-data-analysis-i"},
    "STA303H1": {"name": "Methods of Data Analysis II", "domain": "stats-regression", "slug": "sta303h1-methods-of-data-analysis-ii"},
    "STA304H1": {"name": "Surveys, Sampling and Observational Data", "domain": "stats-surveys", "slug": "sta304h1-surveys-sampling-and-observational-data"},
    "STA314H1": {"name": "Statistical Methods for Machine Learning I", "domain": "stats-ml", "slug": "sta314h1-statistical-methods-for-machine-learning-i"},
    "STA347H1": {"name": "Probability", "domain": "stats-probability", "slug": "sta347h1-probability"},
    "STA410H1": {"name": "Statistical Computation", "domain": "stats-computation", "slug": "sta410h1-statistical-computation"},
    "STA414H1": {"name": "Statistical Methods for Machine Learning II", "domain": "stats-ml", "slug": "sta414h1-statistical-methods-for-machine-learning-ii"},
}
