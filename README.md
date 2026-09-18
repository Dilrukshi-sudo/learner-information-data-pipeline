# learner-information-data-pipeline

# Learner Information Decision-Making Data Pipeline

## Project status
**Core ETL Pipeline & Visualization Complete** (Active development / Portfolio project)

## Project overview
This project builds an end-to-end data pipeline using learner survey data from the UK Government data portal. The analysis focuses on Q1 Summary from the York Consulting report *Information to aid learner decisions – November 2010*.

### Business question
> How useful do learners consider different types of information when deciding which provider and/or course/programme of study to undertake?

## Objectives
- Extract the relevant Q1 Summary data from the raw report-style CSV.
- Clean and transform the data using Python and Pandas.
- Load structured data into PostgreSQL.
- Create relational database tables and SQL queries.
- Analyse the results.
- Produce clear visualisations and findings.
- Document the complete pipeline for reproducibility.

## Technology stack
- Python
- Pandas
- PostgreSQL
- SQL
- Matplotlib
- Jupyter Notebook
- Git/GitHub

## Pipeline
Raw CSV → Extract → Clean & Transform → PostgreSQL → SQL Analysis → Visualisation → Findings

## Repository structure
```text
data/
  raw/
  processed/
src/
sql/
notebooks/
visualisations/
README.md
requirements.txt
```

## Data source
Source file: `11-1364-data-informing-choice-post-16-education-and-learning.csv`

The raw file is retained locally in `data/raw/` for development. Before publishing to GitHub, the project's redistribution/licensing terms will be checked and the repository will reference the official source if the raw file should not be redistributed.

## Current progress
- [x] Inspect raw CSV structure
- [x] Identify Q1 Summary section
- [x] Extract Q1 Summary response categories
- [x] Create cleaned long-format dataset
- [x] Create initial project structure
- [x] Finalise database schema
- [x] Load data into PostgreSQL
- [x] Write analytical SQL queries
- [x] Perform exploratory analysis
- [x] Create visualisations (q1_usefulness_chart.png, q1_needs_improvement.png)
- [x] Document findings
- [ ] Add reproducibility instructions
- [x] Publish to GitHub

## Quick Start / How to Run
- Activate your virtual environment:
.venv\Scripts\Activate

- Run the ETL pipeline:
python src/extract.py
python src/transform.py
python src/load.py

- Generate visualisations:
python visualisations/plot_q1.py
python visualisations/plot_improvements.py

## Project Screenshots

### PostgreSQL Database

The transformed learner survey data is loaded into PostgreSQL using a
relational schema consisting of information items, response categories,
and Q1 responses.

![PostgreSQL database tables](screenshots/adminer-database-tables.png)

### SQL Analysis

SQL joins are used to combine the response data with the information
items and response categories.

![SQL query results](screenshots/sql-query-results.png)

### Learner Information Considered "Very Useful"

This visualisation shows which types of information learners considered
most useful when deciding which course or provider to choose.

![Very useful information](screenshots/very-useful-chart.png)

### Full Response Distribution

The stacked bar chart shows the complete distribution of responses for
each information type.

![Full response distribution](screenshots/response-distribution.png)

## Findings
Key takeaways based on user responses regarding post-16 education information usefulness will be detailed here. Initial charts highlight specific gaps where information items received higher "not useful" or uncertain ratings.

## Limitations
- Dataset focuses on a specific historical snapshot (November 2010 report).

- Relies on structured extraction of summary-level survey blocks.

## Future improvements
Potential improvements include automated ingestion, data-quality tests, Dockerisation, scheduled execution, CI/CD and an interactive dashboard.
