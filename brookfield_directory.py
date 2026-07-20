import json
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Brookfield Leadership Directory",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

with open(
    "brookfield_leaders.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

df = pd.DataFrame(data)

# -----------------------------
# ROLE DETECTION
# -----------------------------

def get_role_level(title):

    title = str(title)

    # CEOs
    if "CEO" in title:
        return "CEO"

    # Presidents
    if "President" in title:
        return "President"

    # CFOs
    if "CFO" in title or "Chief Financial Officer" in title:
        return "CFO"

    # COOs
    if "COO" in title or "Chief Operating Officer" in title:
        return "COO"

    # CIOs
    if (
        "CIO" in title
        or "Chief Investment Officer" in title
    ):
        return "CIO"

    # Chair roles
    if (
        "Executive Chair" in title
        or "Vice Chair" in title
        or "Chairman" in title
        or "Chair" in title
    ):
        return "Chair"

    # Managing Partners
    if "Managing Partner" in title:
        return "Managing Partner"

    # Operating Partners
    if "Operating Partner" in title:
        return "Operating Partner"

    # Managing Directors
    if "Managing Director" in title:
        return "Managing Director"

    # Advisors
    if "Senior Advisor" in title:
        return "Senior Advisor"

    return "Other"

def get_sector(title):
    SECTORS = [
    "Private Equity",
    "Infrastructure",
    "Real Estate",
    "Energy",
    "Credit",
    "Public Securities",
    "Private Wealth",
    "Global Client Group",
    "Brookfield Wealth Solutions",
    "Corporate",
    "Technology",
    "Legal & Regulatory"
]

    title = str(title)

    for sector in SECTORS:
        if sector.lower() in title.lower():
            return sector

    return "Other"


# -----------------------------
# REGION DETECTION
# -----------------------------

def get_region(text):

    text = str(text).lower()

    india_words = [
        "india",
        "mumbai",
        "delhi",
        "bangalore",
        "pune"
    ]

    middle_east_words = [
        "middle east",
        "dubai",
        "saudi arabia",
        "uae",
        "gcc"
    ]

    uk_words = [
        "united kingdom",
        "u.k.",
        "london",
        "england"
    ]

    europe_words = [
        "europe",
        "spain",
        "france",
        "germany",
        "italy",
        "portugal",
        "greece"
    ]

    apac_words = [
        "asia pacific",
        "china",
        "japan",
        "korea",
        "australia",
        "singapore"
    ]

    latin_words = [
        "brazil",
        "south america",
        "latin america",
        "colombia",
        "mexico"
    ]

    if any(x in text for x in india_words):
        return "India"

    if any(x in text for x in middle_east_words):
        return "Middle East"

    if any(x in text for x in uk_words):
        return "UK"

    if any(x in text for x in europe_words):
        return "Europe"

    if any(x in text for x in apac_words):
        return "APAC"

    if any(x in text for x in latin_words):
        return "Latin America"

    return "North America"

def linkedin_search_url(name):

    query = f"{name} Brookfield LinkedIn"

    query = query.replace(" ", "+")

    return f"https://www.google.com/search?q={query}"

def generate_email(name):

    if not name:
        return ""

    email_name = (
        name.lower()
        .replace(".", "")
        .replace("'", "")
        .replace("’", "")
        .replace("-", ".")
    )

    parts = email_name.split()

    if len(parts) < 2:
        return ""

    first = parts[0]
    last = parts[-1]

    return f"{first}.{last}@brookfield.com"

# -----------------------------
# CREATE COLUMNS
# -----------------------------

df["role_level"] = df["title"].apply(get_role_level)

df["sector"] = df["title"].apply(get_sector)

df["linkedin_search"] = (
    df["name"].apply(linkedin_search_url)
)
df["email"] = df["name"].apply(generate_email)
df["region"] = (
    df["title"].fillna("")
    + " "
    + df["bio"].fillna("")
).apply(get_region)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Filters")

role_order = [
    "All",
    "CEO",
    "President",
    "CFO",
    "COO",
    "CIO",
    "Chair",
    "Managing Partner",
    "Operating Partner",
    "Managing Director",
    "Senior Advisor",
    "Other"
]

role_filter = st.sidebar.selectbox(
    "Role Level",
    role_order
)


sector_filter = st.sidebar.selectbox(
    "Sector",
    [
        "All"
    ]
    + sorted(df["sector"].unique())
)

region_filter = st.sidebar.selectbox(
    "Country / Region",
    [
        "All"
    ]
    + sorted(df["region"].unique())
)

search = st.sidebar.text_input(
    "Keyword Search"
)

# -----------------------------
# FILTERING
# -----------------------------

filtered = df.copy()

if role_filter != "All":
    filtered = filtered[
        filtered["role_level"] == role_filter
    ]

if sector_filter != "All":
    filtered = filtered[
        filtered["sector"] == sector_filter
    ]

if region_filter != "All":
    filtered = filtered[
        filtered["region"] == region_filter
    ]

if search:

    mask = (
        filtered["name"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered["title"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered["bio"].str.contains(
            search,
            case=False,
            na=False
        )
    )

    filtered = filtered[mask]

# -----------------------------
# MAIN PAGE
# -----------------------------

st.title("Brookfield Leadership Directory")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Results", len(filtered))
col2.metric(
    "Role",
    role_filter
)
col3.metric(
    "Sector",
    sector_filter
)
col4.metric(
    "Region",
    region_filter
)

st.divider()

for _, row in filtered.iterrows():

    with st.expander(
        f"{row['name']} | {row['title']}"
    ):

        st.markdown(
            f"**Role Level:** {row['role_level']}"
        )

        st.markdown(
            f"**Sector:** {row['sector']}"
        )

        st.markdown(
            f"**Region:** {row['region']}"
        )
        st.markdown(
            f"**Likely Email:** {row['email']}"
        )

        st.markdown("---")

        st.write(row["bio"])

        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "Brookfield Profile",
                row["url"]
            )

        with col2:
            st.link_button(
                "LinkedIn Search",
                row["linkedin_search"]
            )