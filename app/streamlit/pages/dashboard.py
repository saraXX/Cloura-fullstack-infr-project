# /app/pages/1_Dashboard.py
import pandas as pd
import streamlit as st

from api import get_tickets

# Page setup for wide view
st.set_page_config(
    page_title="Dashboard | CloudAura",
    page_icon="📊",
    layout="wide"
)

st.title("Cloura IT Support Dashboard")
st.caption("View all submitted IT support tickets.")

# ---------------------------------------------------------
# Refresh
# ---------------------------------------------------------

if st.button("🔄 Refresh", use_container_width=True):
    st.rerun()

# ---------------------------------------------------------
# Get tickets
# ---------------------------------------------------------

tickets = get_tickets()

if tickets is None:
    st.error("Could not connect to the backend.")
    st.stop()

if not tickets:
    st.info("No tickets have been submitted yet.")
    st.stop()

df = pd.DataFrame(tickets)

# ---------------------------------------------------------
# Normalize columns
# ---------------------------------------------------------

if "status" not in df.columns:
    df["status"] = "Open"

df["status"] = df["status"].fillna("Open")

# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

total = len(df)

open_count = len(
    df[df["status"].str.lower() == "open"]
)

in_progress_count = len(
    df[df["status"].str.lower().isin(
        ["in progress", "in_progress"]
    )]
)

closed_count = len(
    df[df["status"].str.lower() == "closed"]
)

# ---------------------------------------------------------
# Dashboard metrics
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tickets", total)

with col2:
    st.metric("Open", open_count)

with col3:
    st.metric("In Progress", in_progress_count)

with col4:
    st.metric("Closed", closed_count)

st.divider()

# ---------------------------------------------------------
# All tickets table
# ---------------------------------------------------------

st.subheader("All Tickets")

display_df = df.copy()

# Exclude heavy image binary/base64 payload from table view
if "image_data" in display_df.columns:
    display_df = display_df.drop(columns=["image_data"])

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)