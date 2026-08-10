<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f3460,100:16213e&height=200&section=header&text=Web%20Scraping%20ETL%20Pipeline&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Extract%20%E2%86%92%20Transform%20%E2%86%92%20Load%20from%20a%20live%20website&descAlignY=58&descSize=16" width="100%"/>

<a href="https://github.com/Riq-wq">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=0F3460&center=true&vCenter=true&width=600&lines=Scraping+1%2C000+records+across+50+pages;Cleaning+messy%2C+real-world+data;Loading+into+MySQL+for+analysis" alt="Typing SVG" />
</a>

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-HTML%20Parsing-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

</div>

---

## 📖 Overview

This project is an end-to-end **Extract → Transform → Load (ETL)** pipeline built entirely in a single Jupyter Notebook. It scrapes **1,000 book listings** across 50 paginated pages from a live website, cleans the data with Pandas, and loads the final dataset into a MySQL database — practicing the kind of real-world data handling that goes beyond working with an already-clean dataset.

---

## 🏗️ Pipeline Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│    EXTRACT       │     │   TRANSFORM       │     │     LOAD         │
│                  │     │                   │     │                  │
│ requests +       │ ──> │ Pandas cleaning:  │ ──> │ SQLAlchemy +     │
│ BeautifulSoup    │     │ • Currency parsing│     │ pymysql          │
│                  │     │ • Boolean casting │     │                  │
│ 50 pages scraped │     │ • Rating mapping  │     │ MySQL table:     │
│ 1,000 records    │     │                   │     │ scraped_books    │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

---

## ✨ Key Features

- **Robust pagination handling** — loops until a 404 response is hit, rather than hardcoding a page count
- **Encoding bug fix** — corrects a common `requests` character encoding issue (`£` rendering as `Â£`)
- **Rate-limited requests** — 1-second delay between page requests to scrape responsibly
- **Type-safe transformation** — converts currency strings to `float`, availability text to `bool`, and word-based ratings (`"Three"`) to `int`
- **Reusable pipeline pattern** — follows the same Extract → Transform → Load structure used in production data pipelines

---

## 🛠️ Tech Stack

| Stage | Tools |
|---|---|
| Extraction | `requests`, `BeautifulSoup4`, `lxml` |
| Transformation | `pandas` |
| Loading | `SQLAlchemy`, `pymysql`, `MySQL` |
| Environment | Jupyter Notebook |

---

## ⚙️ Setup & Usage

### 1. Clone the repo
```bash
git clone https://github.com/Riq-wq/books-toscrape-web-scraping-etl.git
cd books-toscrape-web-scraping-etl
```

### 2. Install dependencies
```bash
pip install requests beautifulsoup4 pandas lxml sqlalchemy pymysql notebook
```

### 3. Set up MySQL database
```sql
CREATE DATABASE bookstore;
```

### 4. Open and run the notebook
```bash
jupyter notebook web_scraping_etl.ipynb
```
Update the database credentials in the load step of the notebook before running, then run all cells in order.

---

## 📊 Sample Output

| title | price | rating | in_stock |
|---|---|---|---|
| A Light in the Attic | 51.77 | 3 | True |
| Tipping the Velvet | 53.74 | 1 | True |
| Soumission | 50.10 | 1 | True |
| Sharp Objects | 47.82 | 4 | True |
| Sapiens: A Brief History of Humankind | 54.23 | 5 | True |

**Total records:** 1,000 books across 50 categories

---

## 🧠 What I Learned

- How to inspect and target HTML elements using browser DevTools
- Handling real-world data quality issues: character encoding bugs and inconsistent text formatting
- Designing a pagination loop that adapts to unknown page counts instead of hardcoding
- Applying responsible scraping practices (rate limiting via delays)
- Structuring a scraping project using the same ETL pattern used in production data pipelines

---

## 🚀 Future Improvements

- [ ] Add error handling/retries for failed requests
- [ ] Schedule the pipeline to run automatically (e.g. with a cron job or Airflow)
- [ ] Build a Power BI dashboard on top of the `scraped_books` table
- [ ] Extend to a real e-commerce site (e.g. Jumia Kenya) with anti-bot handling

---

<div align="center">

### 👤 Author

**Hassan Jumaa (Riq)**
Data Analyst | BI Analyst

[![GitHub](https://img.shields.io/badge/GitHub-Riq--wq-181717?logo=github&logoColor=white)](https://github.com/Riq-wq)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f3460,100:16213e&height=100&section=footer" width="100%"/>

</div>
