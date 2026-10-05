import streamlit as st

import json
import urllib.error
import urllib.request

from config import BACKEND_URL
from state import initialize_state
from styles import apply_styles

from form import (
    welcome,
    user_info,
    category,
    problem,
    impact,
    description,
    review,
    success
)


# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="IT Support",
    page_icon="💻",
    layout="centered"
)


# =========================================================
# INITIALIZATION
# =========================================================

initialize_state()

apply_styles()



# =========================================================
# HEADER
# =========================================================

header_left, header_right = st.columns([3, 1])

with header_left:

    st.image(
        "assets/logo4.png",
        width=200
    )

with header_right:

    st.caption("IT SUPPORT")

st.divider()

# =========================================================
# ROUTING
# =========================================================

if st.session_state.step == 0:

    welcome.show()

elif st.session_state.step == 1:

    user_info.show()

elif st.session_state.step == 2:

    category.show()

elif st.session_state.step == 3:

    problem.show()

elif st.session_state.step == 4:

    impact.show()

elif st.session_state.step == 5:

    description.show()

elif st.session_state.step == 6:

    review.show()

elif st.session_state.step == 7:

    success.show()