import streamlit as st
import requests

st.set_page_config(page_title="CloudAura IT Support", page_icon="🛠️")

st.title("🛠️ CloudAura IT Support Portal")
st.write("Submit and manage IT support requests.")

st.subheader("Create a Support Ticket")

name = st.text_input("Your Name")
issue = st.text_area("Describe the Issue")

if st.button("Submit Ticket"):
    if name and issue:
        try:
            response = requests.get("http://backend:8000/health")
            if response.status_code == 200:
                st.success("Ticket submitted successfully!")
            else:
                st.error("Backend is not available.")
        except requests.exceptions.RequestException:
            st.error("Could not connect to the backend.")
    else:
        st.warning("Please enter your name and describe the issue.")
