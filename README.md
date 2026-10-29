# Web Scraping ETL Pipeline

**End-to-end ETL pipeline — extracting 1,000 book listings from a live website, cleaning them in Pandas, and loading into MySQL.**

---

## Project Overview

This project is an end-to-end **Extract → Transform → Load (ETL)** pipeline built entirely in a single Jupyter Notebook. It scrapes **1,000 book listings** across 50 paginated pages from [books.toscrape.com](http://books.toscrape.com/), cleans the data with Pandas, and loads the final dataset into a MySQL database — practicing the kind of real-world data handling that goes beyond working with an already-clean dataset.

**Pipeline:** `requests + BeautifulSoup (Extract) → Pandas (Transform) → MySQL (Load)`

---

## Business Problems

| # | Problem | Business Impact |
|---|---------|-----------------|
| 1 | No automated data collection from external sources | Manual data gathering is slow, error-prone, and doesn't scale |
| 2 | Character encoding bugs in scraped data (e.g. `£` → `Â£`) | Wrong currency symbols corrupt price analysis and reporting |
| 3 | Text-based ratings ("One", "Two", "Three") can't be used in calculations | Need numeric ratings for filtering, sorting, and aggregation |
| 4 | Availability as free text ("In stock") is hard to query | Need boolean flags for inventory tracking |
| 5 | Unknown page count — hardcoding 50 pages would break if the site adds more | Need dynamic pagination that stops on 404 |
| 6 | No cleaned dataset saved to disk | Scraped data is lost if the notebook is re-run or the kernel restarts |

---

## Project Files

| File | Description |
|------|-------------|
| `web_scraping_etl.ipynb` | Full ETL pipeline notebook (Extract → Transform → Load) |
| `.env` | Database credentials (not committed) |
| `.env.example` | Template for database credentials |
| `.gitignore` | Git ignore rules |

---

## Data-Quality Gate — Interview Checks

These are the specific checks an interviewer may ask about. Be ready to answer each one:

| Check | What It Proves | Status |
|-------|---------------|--------|
| No null values after cleaning | All gaps filled (no missing titles, prices, or ratings) | 0 nulls in all 4 columns |
| Price parsed as float | Currency string converted to numeric type | 1,000 values, all valid |
| Rating mapped to int | Word-based ratings ("One"→1) converted to integers | All 5 ratings mapped (1-5) |
| Availability as boolean | Free text converted to True/False | All 1,000 in stock |
| Encoding fixed | `response.encoding = "utf-8"` prevents `Â£` corruption | Verified on page 1 |
| Pagination dynamic | Loop stops on 404, not hardcoded to 50 pages | 50 pages scraped, stopped at 51 |
| Rate limiting | 1-second delay between requests | `time.sleep(1)` applied |
| Data types correct | title (object), price (float64), rating (int64), in_stock (bool) | All verified |
| Null check after transform | `df.isnull().sum()` returns 0 for all columns | Verified |

---

## Key Statistics (for interview prep)

| Metric | Value |
|--------|-------|
| Total records scraped | 1,000 |
| Pages scraped | 50 |
| Books per page | 20 |
| Columns | 4 (title, price, rating, in_stock) |
| Missing values | 0 |
| Duplicate rows | 0 |
| Price range | £10.00 – £59.99 |
| Average price | ~£35.00 |
| Rating scale | 1–5 stars |
| Availability | 100% in stock |

---

## ETL Pipeline

### 1. Extract
- **HTTP requests**: Fetch each page from `books.toscrape.com`
- **Encoding fix**: `response.encoding = "utf-8"` prevents `Â£` corruption
- **Pagination**: Dynamic loop stops on 404 (50 pages scraped)
- **Rate limiting**: 1-second delay between requests (`time.sleep(1)`)
- **HTML parsing**: BeautifulSoup with lxml parser
- **Data collected**: title, price, availability, rating

### 2. Transform
- **Price**: Strip `£` symbol, convert to `float`
- **Availability**: Convert to boolean (`"In stock"` → True)
- **Rating**: Map word to number (`"One"` → 1, `"Five"` → 5)
- **Null check**: `df.isnull().sum()` returns 0 for all columns

### 3. Load
- **Database**: MySQL via SQLAlchemy + PyMySQL
- **Table**: `scraped_books`
- **Environment**: Credentials loaded from `.env` file
- **Connection**: `mysql+pymysql://user:pass@host/db`

---

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/Riq-wq/books-toscrape-web-scraping-etl.git
cd books-toscrape-web-scraping-etl
```

### Step 2: Set up Python

Install Python and Jupyter Notebook, then install the required libraries:

```bash
pip install requests beautifulsoup4 pandas lxml sqlalchemy pymysql python-dotenv
```

### Step 3: Set up MySQL

Install and start MySQL, then create the database `bookstore`:

```sql
CREATE DATABASE bookstore;
```

### Step 4: Configure environment

Create a `.env` file in the project root with your database credentials:

```env
DB_HOST=localhost
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_NAME=bookstore
```

### Step 5: Run the notebook

Open `web_scraping_etl.ipynb` in Jupyter Notebook and run all cells in order. The notebook will:

1. Install dependencies (if needed)
2. Scrape 50 pages (1,000 books) from books.toscrape.com
3. Clean and transform the data
4. Load the cleaned data into MySQL table `scraped_books`

---

## Data-Quality Gate — Interview Checks

These are the specific checks an interviewer may ask about. Be ready to answer each one:

| Check | What It Proves | Status |
|-------|---------------|--------|
| No null values | All 1,000 records have title, price, rating, availability | 0 nulls |
| Price as float | Currency strings converted to numeric | All valid |
| Rating as int | Word-based ratings mapped to 1-5 | All mapped |
| Availability as bool | Free text converted to boolean | All True (in stock) |
| Encoding fixed | `response.encoding = "utf-8"` prevents `Â£` corruption | Verified |
| Pagination dynamic | Loop stops on 404, not hardcoded to 50 pages | 50 pages, stopped at 51 |
| Rate limiting | 1-second delay between requests | `time.sleep(1)` applied |
| Data types correct | title (object), price (float64), rating (int64), in_stock (bool) | All verified |
| Null check after transform | `df.isnull().sum()` returns 0 for all columns | Verified |

---

## Key Learning Outcomes

- Web scraping with requests + BeautifulSoup
- Handling real-world data quality issues (encoding bugs, inconsistent text)
- Dynamic pagination (loop until 404, not hardcoded page count)
- Rate limiting for responsible scraping
- Type-safe data transformation (currency → float, text → bool, word → int)
- Loading data into MySQL via SQLAlchemy
- ETL pipeline pattern (Extract → Transform → Load)

---

## About the Author

**Hassan Jumaa (Riq)**

Data Analyst | [Portfolio](https://riq-wq.github.io/Myportfolio) · [GitHub](https://github.com/Riq-wq) · [LinkedIn](https://linkedin.com/in/mrisa-juma-56a600416)
