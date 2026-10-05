# /app/api.py
import json
import urllib.error
import urllib.request
import streamlit as st

from config import BACKEND_URL


# =========================================================
# Create Ticket
# =========================================================

def create_ticket():
    data = {
        "name": st.session_state.get("name", ""),
        "email": st.session_state.get("email", ""),
        "problem_category": st.session_state.get("category", ""),
        "problem_sub_category": st.session_state.get("problem", ""),
        "probelem_description": st.session_state.get("description", ""),
        "issue": st.session_state.get("impact", ""),
        "status": "Open",
        "image_data": st.session_state.get("image_data"),
    }

    try:
        url = f"{BACKEND_URL}/tickets"

        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            response_data = response.read().decode("utf-8")
            return json.loads(response_data)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        st.error(f"Backend error: {error_body}")
        return None

    except urllib.error.URLError as e:
        st.error(f"Could not connect to backend: {e.reason}")
        return None

    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None


# =========================================================
# Get All Tickets
# =========================================================

def get_tickets():
    try:
        url = f"{BACKEND_URL}/tickets"

        request = urllib.request.Request(url, method="GET")

        with urllib.request.urlopen(request, timeout=10) as response:
            response_data = response.read().decode("utf-8")
            return json.loads(response_data)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        st.error(f"Backend error: {error_body}")
        return None

    except urllib.error.URLError as e:
        st.error(f"Could not connect to backend: {e.reason}")
        return None

    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None


# =========================================================
# Update Ticket
# =========================================================

def update_ticket(ticket_id, status):
    try:
        url = f"{BACKEND_URL}/tickets/{ticket_id}"

        data = {"status": status}

        request = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="PUT",
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            response_data = response.read().decode("utf-8")
            return json.loads(response_data)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        st.error(f"Backend error: {error_body}")
        return None

    except urllib.error.URLError as e:
        st.error(f"Could not connect to backend: {e.reason}")
        return None

    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None

    