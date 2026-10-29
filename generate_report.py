#!/usr/bin/env python3
"""Generate PDF report for Web Scraping ETL Pipeline project."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.platypus import (
    HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

NAVY = colors.HexColor("#1F2D3D")
TEAL = colors.HexColor("#2A9D8F")
INK = colors.HexColor("#1A1A1A")
GREY = colors.HexColor("#5A5A5A")
LIGHT = colors.HexColor("#F4F6F8")

OUT = Path(__file__).resolve().parent / "reports" / "Web_Scraping_ETL_Report.pdf"

doc = SimpleDocTemplate(
    str(OUT), pagesize=A4,
    leftMargin=18 * mm, rightMargin=18 * mm,
    topMargin=16 * mm, bottomMargin=16 * mm,
    title="Web Scraping ETL Pipeline - Report",
    author="Hassan Jumaa (Riq)",
)

styles = getSampleStyleSheet()
TITLE = ParagraphStyle("TITLE", parent=styles["Title"], fontSize=22, textColor=NAVY, spaceAfter=6)
SUBTITLE = ParagraphStyle("SUBTITLE", parent=styles["Normal"], fontSize=11, textColor=GREY, spaceAfter=14)
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=15, textColor=NAVY, spaceBefore=14, spaceAfter=8)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12, textColor=TEAL, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("BODY", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=7)
BUL = ParagraphStyle("BUL", parent=styles["Normal"], fontSize=10, leading=14, leftIndent=14, spaceAfter=3)

story = []

# ---- Title ----
story.append(HRFlowable(width="100%", thickness=3, color=NAVY, spaceAfter=10))
story.append(Paragraph("Web Scraping ETL Pipeline", TITLE))
story.append(Paragraph("End-to-End Data Extraction, Transformation, and Loading Report", SUBTITLE))
story.append(Paragraph("Prepared by Hassan Jumaa (Riq)  ·  Data Analyst  ·  riq-wq.github.io/Myportfolio", BODY))
story.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=14))

# ---- 1. Executive Summary ----
story.append(Paragraph("1. Executive Summary", H1))
story.append(Paragraph(
    "This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built in a single "
    "Jupyter Notebook. It scrapes 1,000 book listings across 50 paginated pages from a live website "
    "(books.toscrape.com), cleans the data with Pandas, and loads the final dataset into a MySQL database. "
    "The pipeline handles real-world data quality issues including character encoding bugs, inconsistent "
    "text formatting, and dynamic pagination.",
    BODY,
))
story.append(Paragraph("Key outcomes:", BODY))
for b in [
    "<b>1,000 records</b> scraped from 50 pages (20 books per page) with zero null values after cleaning.",
    "<b>4 columns</b> extracted: title, price, availability, rating — all type-safe after transformation.",
    "<b>Dynamic pagination</b> — loop stops on HTTP 404 instead of hardcoding 50 pages.",
    "<b>Encoding bug fixed</b> — forced UTF-8 encoding prevents '£' from rendering as 'Â£'.",
    "<b>Rate-limited requests</b> — 1-second delay between pages for responsible scraping.",
    "<b>Loaded into MySQL</b> — cleaned data stored in `scraped_books` table via SQLAlchemy + PyMySQL.",
]:
    story.append(Paragraph(f"\u2022&nbsp;&nbsp;{b}", BUL))
story.append(PageBreak())

# ---- 2. Methodology ----
story.append(Paragraph("2. Methodology & Pipeline", H1))
story.append(Paragraph("The analysis followed a three-stage ETL pipeline:", BODY))
story.append(bullet if False else None)
for b in [
    "<b>Extract (requests + BeautifulSoup):</b> Fetched each page from books.toscrape.com, "
    "parsed HTML with lxml, and collected title, price, availability, and rating from each book listing.",
    "<b>Transform (Pandas):</b> Stripped currency symbols, converted prices to float, mapped word-based "
    "ratings to integers, converted availability to boolean, and verified zero nulls.",
    "<b>Load (MySQL):</b> Connected via SQLAlchemy + PyMySQL using credentials from a .env file, "
    "and loaded the cleaned DataFrame into a MySQL table with if_exists='replace'.",
]:
    story.append(Paragraph(f"\u2022&nbsp;&nbsp;{b}", BUL))
story.append(PageBreak())

# ---- 3. Data Cleaning ----
story.append(Paragraph("3. Data Cleaning & Transformation", H1))
story.append(Paragraph("Cleaning steps applied to the raw scraped data:", BODY))
data = [
    ["Step", "Action", "Result"],
    ["Encoding fix", "response.encoding = 'utf-8'", "Prevents '£' → 'Â£' corruption"],
    ["Price parsing", "str.replace('£', '') + astype(float)", "51.77 (float64)"],
    ["Availability", "str.contains('In stock') → bool", "True/False (bool)"],
    ["Rating mapping", "map({'One':1, ..., 'Five':5})", "1-5 (int64)"],
    ["Null check", "df.isnull().sum()", "0 nulls across all 4 columns"],
    ["Type verification", "df.info()", "title: object, price: float64, rating: int64, in_stock: bool"],
]
t = Table(data, colWidths=[1.3 * inch, 2.8 * inch, 2.4 * inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9DEE3")),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D9DEE3")),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(t)
story.append(Spacer(1, 12))

story.append(Paragraph("Key data-quality observations:", H2))
for b in [
    "No duplicate rows — all 1,000 book titles are unique.",
    "No missing values — all 1,000 records have title, price, rating, and availability.",
    "Price range: £10.00 – £59.99 (average ~£35.00).",
    "Rating scale: 1–5 stars (mapped from word-based ratings).",
    "Availability: 100% in stock (all books available at scrape time).",
]:
    story.append(Paragraph(f"\u2022&nbsp;&nbsp;{b}", BUL))
story.append(PageBreak())

# ---- 4. Pagination ----
story.append(Paragraph("4. Dynamic Pagination", H1))
story.append(Paragraph(
    "The scraper uses a while True loop that increments the page number each iteration. "
    "The loop breaks when the response status code is not 200 (HTTP 404 when the page doesn't exist). "
    "This is more robust than hardcoding 50 pages — if the site adds more pages, the scraper will "
    "still find them, and if pages are removed, it stops gracefully.",
    BODY,
))
story.append(Paragraph("Results: 50 pages scraped (20 books each) = 1,000 total records. Stopped at page 51 (404).", BODY))
story.append(Paragraph("Rate limiting: time.sleep(1) between each page request — responsible scraping practice.", BODY))
story.append(PageBreak())

# ---- 5. Sample Output ----
story.append(Paragraph("5. Sample Output", H1))
data = [
    ["Title", "Price", "Rating", "In Stock"],
    ["A Light in the Attic", "£51.77", "3", "True"],
    ["Tipping the Velvet", "£53.74", "1", "True"],
    ["Soumission", "£50.10", "1", "True"],
    ["Sharp Objects", "£47.82", "4", "True"],
    ["Sapiens: A Brief History of Humankind", "£54.23", "5", "True"],
]
t = Table(data, colWidths=[2.5 * inch, 0.8 * inch, 0.7 * inch, 0.8 * inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9DEE3")),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D9DEE3")),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(t)
story.append(Spacer(1, 12))

# ---- 6. Recommendations ----
story.append(Paragraph("6. Recommendations", H1))
for b in [
    "Add <b>error handling and retries</b> for failed requests (e.g., exponential backoff).",
    "Schedule the pipeline to run automatically (cron job or Airflow).",
    "Build a Power BI dashboard on top of the scraped_books table.",
    "Extend to a real e-commerce site with anti-bot handling.",
    "Add a <b>data-quality gate</b> to validate scraped data before loading to MySQL.",
    "Store data in a data warehouse (BigQuery, Snowflake) for production scale.",
]:
    story.append(Paragraph(f"\u2022&nbsp;&nbsp;{b}", BUL))
story.append(PageBreak())

# ---- 7. Conclusion ----
story.append(Paragraph("7. Conclusion", H1))
story.append(Paragraph(
    "The ETL pipeline successfully scraped 1,000 book listings from books.toscrape.com, cleaned the "
    "data by fixing encoding bugs, converting currency strings to floats, mapping word-based ratings "
    "to integers, and converting availability text to booleans. The cleaned data was loaded into a "
    "MySQL database for further analysis. The pipeline demonstrates real-world data engineering "
    "skills including dynamic pagination, rate limiting, and type-safe transformations.",
    BODY,
))

story.append(Paragraph("Data Source", H2))
story.append(Paragraph("books.toscrape.com — a practice website for web scraping (static HTML, no anti-bot measures).", BODY))

story.append(Paragraph("Tools Used", H2))
story.append(Paragraph("Python · requests · BeautifulSoup4 · lxml · Pandas · SQLAlchemy · PyMySQL · MySQL", BODY))

doc.build(story)
print(f"Report written to {OUT}")
PYEOF