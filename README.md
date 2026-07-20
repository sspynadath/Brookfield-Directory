# Brookfield Leadership Directory

A Python and Streamlit application for exploring Brookfield leadership data through an interactive searchable directory.

This project combines web scraping, data processing, and data visualization to create a searchable leadership database built from publicly available Brookfield leadership profiles.

---

# Features

- Search leaders by name
- Search leaders by title
- Search leadership biographies
- Filter by role level
- Filter by business sector
- Filter by region
- Generate likely Brookfield email addresses
- LinkedIn search integration
- Direct links to Brookfield profile pages
- Interactive Streamlit dashboard

---

# Repository Structure

```text
brookfield_directory.py     Streamlit application
brookfield_scraper.py       Leadership scraper
brookfield_leaders.json     Leadership dataset
requirements.txt            Python dependencies
README.md                   Project documentation
```

---

# How the Project Works

The project consists of two components:

## 1. Data Collection

The scraper collects publicly available leadership information from Brookfield's website.

Run:

```bash
python brookfield_scraper.py
```

This generates:

```text
brookfield_leaders.json
```

The dataset contains:

- Name
- Title
- Biography
- Brookfield profile URL

---

## 2. Leadership Directory

The Streamlit application reads the dataset and creates an interactive searchable directory.

The application depends on:

```text
brookfield_leaders.json
```

If the JSON file is missing, the application will not run.

---

# Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run brookfield_directory.py
```

The repository already includes a generated dataset (`brookfield_leaders.json`), so the scraper does not need to be executed before running the application.

---

# Regenerating the Dataset

If you want to refresh the leadership data:

Generate a new dataset:

```bash
python brookfield_scraper.py
```

Then launch the directory:

```bash
streamlit run brookfield_directory.py
```

---

# Example Workflow

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate a fresh dataset (optional)

```bash
python brookfield_scraper.py
```

### Launch the application

```bash
streamlit run brookfield_directory.py
```

---

# Technologies Used

- Python
- Streamlit
- Pandas
- Playwright

---

# Use Cases

- Executive research
- Stakeholder mapping
- Leadership analysis
- Market intelligence
- Business development preparation
- Industry research

---

# Data Source

All information was collected from publicly available Brookfield leadership profile pages:

https://www.brookfield.com/about-us/leadership

---

# Disclaimer

This project is an independent software project and is not affiliated with, endorsed by, or sponsored by Brookfield.

All information included in this project was collected from publicly accessible sources and is provided for research and educational purposes only.
