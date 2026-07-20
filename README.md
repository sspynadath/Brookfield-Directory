# Brookfield Leadership Directory

A Python and Streamlit application for exploring Brookfield leadership data through an interactive searchable directory.

The project combines web scraping, data processing, and an interactive dashboard to make publicly available leadership information easier to search and analyze.

---

## Features

- Search leaders by name
- Search leaders by title
- Search leadership biographies
- Filter by role level
- Filter by business sector
- Filter by region
- Generate likely Brookfield email addresses
- One-click LinkedIn search links
- Direct links to Brookfield profile pages
- Interactive Streamlit dashboard

---

## Repository Contents

```text
brookfield_directory.py    Streamlit dashboard
brookfield_scraper.py      Brookfield leadership scraper
brookfield_leaders.json    Leadership dataset
requirements.txt           Python dependencies
README.md                  Documentation
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/brookfield-leadership-directory.git
cd brookfield-leadership-directory
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the Streamlit application:

```bash
streamlit run brookfield_directory.py
```

The application will open automatically in your browser.

---

## Data Source

The leadership data is sourced from publicly available Brookfield leadership profile pages:

https://www.brookfield.com/about-us/leadership

The dataset includes:

- Name
- Title
- Biography
- Profile URL

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Playwright

---

## Example Use Cases

- Executive research
- Stakeholder mapping
- Leadership analysis
- Business development preparation
- Market intelligence

---

## Disclaimer

This project is an independent software project and is not affiliated with, endorsed by, or sponsored by Brookfield.

All information contained within the dataset was sourced from publicly accessible Brookfield web pages.
