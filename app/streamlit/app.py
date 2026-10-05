import streamlit as st
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Backend API URL inside the Docker Compose network
BACKEND_URL = "http://backend:8000"

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="IT Support",
    page_icon="💻",
    layout="centeredd"
)


# =========================================================
# WEBSITE COLORS & STYLE
# =========================================================

st.markdown("""
<style>

/* =========================================
   WEBSITE BACKGROUND
========================================= */

.stApp {
    background-color: #EAECF0;
}


/* =========================================
   MAIN CONTENT
========================================= */

.block-container {
    max-width: 800px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}


/* =========================================
   HEADINGS
========================================= */

h1, h2, h3 {
    color: #000000 !important;
}


/* =========================================
   NORMAL TEXT
========================================= */

p {
    color: #233D4D;
}


/* =========================================
   CAPTIONS
========================================= */

.stCaption {
    color: #233D4D !important;
    font-weight: 600 !important;
}


/* =========================================
   NORMAL BUTTONS / OPTIONS
========================================= */

.stButton > button {
    background-color: #233D4D !important;
    border: none !important;
    border-radius: 12px !important;

    min-height: 55px;

    font-weight: 600;

    transition: all 0.2s ease;
}


/* Text inside normal buttons */

.stButton > button,
.stButton > button p,
.stButton > button span,
.stButton > button div {
    color: #FFFFFF !important;
}


/* =========================================
   NORMAL BUTTON HOVER
========================================= */

.stButton > button:hover {
    background-color: #FE7F2D !important;

    border: none !important;

    transform: translateY(-2px);
}


.stButton > button:hover,
.stButton > button:hover p,
.stButton > button:hover span,
.stButton > button:hover div {
    color: #FFFFFF !important;
}


/* =========================================
   PRIMARY BUTTONS
   Continue / Submit / Get Started
========================================= */

.stButton > button[kind="primary"] {
    background-color: #233D4D !important;

    border: none !important;
    border-radius: 12px !important;

    min-height: 55px;

    font-weight: 600;
}


.stButton > button[kind="primary"],
.stButton > button[kind="primary"] p,
.stButton > button[kind="primary"] span,
.stButton > button[kind="primary"] div {
    color: #FFFFFF !important;
}


/* Primary hover */

.stButton > button[kind="primary"]:hover {
    background-color: #FE7F2D !important;
}


.stButton > button[kind="primary"]:hover,
.stButton > button[kind="primary"]:hover p,
.stButton > button[kind="primary"]:hover span,
.stButton > button[kind="primary"]:hover div {
    color: #FFFFFF !important;
}


/* =========================================
   BACK BUTTONS ONLY
========================================= */

div[class*="st-key-back_"] button {
    background-color: #FE7F2D !important;
    color: #FFFFFF !important;

    border: none !important;
    border-radius: 12px !important;

    min-height: 55px !important;

    font-weight: 600 !important;

    transform: none !important;

    box-shadow: none !important;
}


/* Back stays orange on hover */

div[class*="st-key-back_"] button:hover {
    background-color: #FE7F2D !important;
    color: #FFFFFF !important;

    border: none !important;

    transform: none !important;

    box-shadow: none !important;
}


/* Back button text */

div[class*="st-key-back_"] button p,
div[class*="st-key-back_"] button span,
div[class*="st-key-back_"] button div {
    color: #FFFFFF !important;
}


/* =========================================
   TEXT INPUTS
========================================= */

.stTextInput input {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}


/* Placeholder */

.stTextInput input::placeholder {
    color: #6B7280 !important;
    opacity: 1 !important;
}


/* Text box background */

[data-baseweb="input"] {
    background-color: #FFFFFF !important;
}


/* Text box focus */

[data-baseweb="input"]:focus-within {
    border-color: #233D4D !important;
    box-shadow: 0 0 0 1px #233D4D !important;
}


/* =========================================
   TEXT AREA
========================================= */

.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}


/* Placeholder */

.stTextArea textarea::placeholder {
    color: #6B7280 !important;
    opacity: 1 !important;
}


/* Text area background */

[data-baseweb="textarea"] {
    background-color: #FFFFFF !important;
}


/* Text area focus */

[data-baseweb="textarea"]:focus-within {
    border-color: #233D4D !important;
    box-shadow: 0 0 0 1px #233D4D !important;
}


/* =========================================
   PROGRESS BAR
========================================= */

/* Gray empty area */

div[data-testid="stProgress"] > div > div {
    background-color: #C7CBD1 !important;
    border-radius: 100px !important;
}


/* Orange completed area */

div[data-testid="stProgress"] > div > div > div {
    background-color: #FE7F2D !important;
    border-radius: 100px !important;
}


/* =========================================
   DIVIDER
========================================= */

hr {
    border-color: rgba(35, 61, 77, 0.20) !important;
}


/* =========================================
   FILE UPLOADER
========================================= */

[data-testid="stFileUploader"] {
    background-color: rgba(255, 255, 255, 0.45);

    border-radius: 14px;

    padding: 10px;
}


/* =========================================
   ALERTS
========================================= */

[data-testid="stAlert"] {
    border-radius: 12px;
}


/* =========================================
   HIDE STREAMLIT DEFAULT ELEMENTS
========================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "name" not in st.session_state:
    st.session_state.name = ""

if "email" not in st.session_state:
    st.session_state.email = ""

if "category" not in st.session_state:
    st.session_state.category = ""

if "problem" not in st.session_state:
    st.session_state.problem = ""

if "other_problem" not in st.session_state:
    st.session_state.other_problem = ""

if "show_other_input" not in st.session_state:
    st.session_state.show_other_input = False

if "impact" not in st.session_state:
    st.session_state.impact = ""

if "description" not in st.session_state:
    st.session_state.description = ""

if "ticket_number" not in st.session_state:
    st.session_state.ticket_number = ""


# =========================================================
# FUNCTIONS
# =========================================================

def next_step():
    st.session_state.step += 1
    st.rerun()


def previous_step():
    st.session_state.step -= 1
    st.rerun()


def go_to_step(number):
    st.session_state.step = number
    st.rerun()

# Send the support ticket to the FastAPI backend
def create_ticket():
    ticket_data = {
        "name": st.session_state.name,
        "issue": (
            f"Category: {st.session_state.category}\n"
            f"Problem: {st.session_state.problem}\n"
            f"Impact: {st.session_state.impact}\n"
            f"Description: {st.session_state.description}"
        )
    }

    request = Request(
        f"{BACKEND_URL}/tickets",
        data=json.dumps(ticket_data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(request) as response:
            if response.status == 200:
                return json.loads(response.read().decode("utf-8"))
    except HTTPError:
        return None

    return None
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
# STEP 0
# WELCOME
# =========================================================

if st.session_state.step == 0:

    st.caption("COMPANY IT SUPPORT")

    st.title("Need some help? 👋")

    st.write(
        "Tell us what's going on and we'll make sure "
        "your request gets to the right IT team."
    )

    st.write("")
    st.write("")

    if st.button(
        "Get started →",
        type="primary",
        use_container_width=True
    ):
        next_step()


# =========================================================
# STEP 1
# USER INFORMATION
# =========================================================

elif st.session_state.step == 1:

    st.progress(1 / 6)

    st.caption("01 / 06")

    st.title("First, who are we helping?")

    st.write(
        "Enter your information so the IT team "
        "knows how to reach you."
    )

    st.write("")

    name = st.text_input(
        "What's your name?",
        value=st.session_state.name,
        placeholder="e.g. Wessal Ahmed"
    )

    email = st.text_input(
        "What's your work email?",
        value=st.session_state.email,
        placeholder="name@company.com"
    )

    st.write("")

    back, continue_button = st.columns([1, 2])

    with back:

        if st.button(
            "← Back",
            key="back_info",
            use_container_width=True
        ):
            previous_step()

    with continue_button:

        if st.button(
            "Continue →",
            type="primary",
            use_container_width=True
        ):

            if not name.strip():

                st.warning(
                    "Please enter your name."
                )

            elif not email.strip():

                st.warning(
                    "Please enter your work email."
                )

            elif "@" not in email:

                st.warning(
                    "Please enter a valid email address."
                )

            else:

                st.session_state.name = name
                st.session_state.email = email

                next_step()


# =========================================================
# STEP 2
# CATEGORY
# =========================================================

elif st.session_state.step == 2:

    st.progress(2 / 6)

    st.caption("02 / 06")

    st.title("What can we help you with?")

    st.write(
        "Choose the area that best matches your problem."
    )

    st.write("")

    categories = [
        ("💻", "Laptop & Hardware"),
        ("🔐", "Account & Access"),
        ("🌐", "Network & VPN"),
        ("📧", "Email & Microsoft 365"),
        ("🖥️", "Software & Applications"),
        ("📱", "Company Devices"),
    ]

    col1, col2 = st.columns(2)

    for index, (icon, category) in enumerate(categories):

        column = col1 if index % 2 == 0 else col2

        with column:

            if st.button(
                f"{icon}  {category}",
                key=category,
                use_container_width=True
            ):

                st.session_state.category = category

                st.session_state.problem = ""

                st.session_state.other_problem = ""
                st.session_state.show_other_input = False

                next_step()

    st.write("")

    if st.button(
        "← Back",
        key="back_category"
    ):
        previous_step()


# =========================================================
# STEP 3
# SPECIFIC PROBLEM
# =========================================================

elif st.session_state.step == 3:

    st.progress(3 / 6)

    st.caption("03 / 06")

    st.title("What's going wrong?")

    st.write(
        f"You selected **{st.session_state.category}**."
    )

    st.write(
        "Choose the option that best describes the issue."
    )

    st.write("")

    problems = {

        "Laptop & Hardware": [
            "Device won't turn on",
            "Device is running slowly",
            "Screen issue",
            "Battery issue",
            "Keyboard or mouse issue",
            "Other hardware issue",
        ],

        "Account & Access": [
            "Forgot password",
            "Account is locked",
            "Can't access a system",
            "Need access to a system",
            "Multi-factor authentication issue",
            "Other account issue",
        ],

        "Network & VPN": [
            "Can't connect to Wi-Fi",
            "VPN isn't working",
            "Internet is very slow",
            "Connection keeps dropping",
            "Other network issue",
        ],

        "Email & Microsoft 365": [
            "Can't send or receive email",
            "Outlook isn't working",
            "Microsoft Teams issue",
            "OneDrive issue",
            "Other Microsoft 365 issue",
        ],

        "Software & Applications": [
            "Application won't open",
            "Application keeps crashing",
            "Need software installed",
            "Can't access an application",
            "Other software issue",
        ],

        "Company Devices": [
            "Company phone issue",
            "Company tablet issue",
            "Device setup",
            "Lost company device",
            "Other device issue",
        ],
    }

    selected_problems = problems.get(
        st.session_state.category,
        ["Other IT issue"]
    )

    for problem in selected_problems:

        if st.button(
            f"{problem}  →",
            key=problem,
            use_container_width=True
        ):

            if "Other" in problem:

                st.session_state.problem = problem

                st.session_state.show_other_input = True

                st.rerun()

            else:

                st.session_state.problem = problem

                st.session_state.show_other_input = False
                st.session_state.other_problem = ""

                next_step()

    # -----------------------------------------
    # OTHER TEXT BOX
    # -----------------------------------------

    if st.session_state.show_other_input:

        other_problem = st.text_input(
            "Other",
            value=st.session_state.other_problem,
            placeholder="Type your issue here...",
            label_visibility="collapsed"
        )

        if st.button(
            "Continue →",
            type="primary",
            use_container_width=True,
            key="continue_other_problem"
        ):

            if not other_problem.strip():

                st.warning(
                    "Please enter your issue."
                )

            else:

                st.session_state.other_problem = (
                    other_problem.strip()
                )

                st.session_state.problem = (
                    other_problem.strip()
                )

                st.session_state.show_other_input = False

                next_step()

    st.write("")

    if st.button(
        "← Back",
        key="back_problem"
    ):
        previous_step()


# =========================================================
# STEP 4
# IMPACT
# =========================================================

elif st.session_state.step == 4:

    st.progress(4 / 6)

    st.caption("04 / 06")

    st.title("How is this affecting your work?")

    st.write(
        "This helps us understand how quickly "
        "you need support."
    )

    st.write("")

    impact_options = [

        (
            "😌",
            "I can still work",
            "The issue isn't stopping my work."
        ),

        (
            "😕",
            "It's slowing me down",
            "I can work, but the issue is getting in the way."
        ),

        (
            "🚨",
            "I can't work",
            "The issue is completely blocking my work."
        ),
    ]

    for icon, impact, explanation in impact_options:

        if st.button(
            f"{icon}  {impact}\n\n{explanation}",
            key=impact,
            use_container_width=True
        ):

            st.session_state.impact = impact

            next_step()

    st.write("")

    if st.button(
        "← Back",
        key="back_impact"
    ):
        previous_step()


# =========================================================
# STEP 5
# DESCRIPTION
# =========================================================

elif st.session_state.step == 5:

    st.progress(5 / 6)

    st.caption("05 / 06")

    st.title("One last thing...")

    st.write(
        "Tell us a little more about what happened."
    )

    st.write("")

    description = st.text_area(
        "Describe your issue",
        value=st.session_state.description,
        placeholder=(
            "For example: I tried connecting to the VPN "
            "this morning, but it keeps showing an error. "
            "I restarted my laptop but the problem is still happening."
        ),
        height=180
    )

    uploaded_file = st.file_uploader(
        "Add a screenshot or file (optional)",
        type=[
            "png",
            "jpg",
            "jpeg",
            "pdf"
        ]
    )

    st.write("")

    back, continue_button = st.columns([1, 2])

    with back:

        if st.button(
            "← Back",
            key="back_details",
            use_container_width=True
        ):
            previous_step()

    with continue_button:

        if st.button(
            "Continue →",
            type="primary",
            use_container_width=True
        ):

            if not description.strip():

                st.warning(
                    "Please tell us a little about the issue."
                )

            else:

                st.session_state.description = description

                next_step()


# =========================================================
# STEP 6
# REVIEW
# =========================================================

elif st.session_state.step == 6:

    st.progress(1.0)

    st.caption("06 / 06")

    st.title("Ready to send? ✓")

    st.write(
        "Take a quick look before sending your request."
    )

    st.write("")
    st.divider()

    # USER

    st.caption("REQUESTED BY")

    st.subheader(
        st.session_state.name
    )

    st.write(
        st.session_state.email
    )

    st.divider()

    # CATEGORY

    st.caption("CATEGORY")

    st.subheader(
        st.session_state.category
    )

    st.divider()

    # PROBLEM

    st.caption("PROBLEM")

    st.subheader(
        st.session_state.problem
    )

    st.divider()

    # IMPACT

    st.caption("WORK IMPACT")

    st.subheader(
        st.session_state.impact
    )

    # Calculate priority

    if st.session_state.impact == "I can't work":

        priority = "High"

    elif st.session_state.impact == "It's slowing me down":

        priority = "Medium"

    else:

        priority = "Low"

    st.caption(
        f"IT priority: {priority}"
    )

    st.divider()

    # DESCRIPTION

    st.caption("DESCRIPTION")

    st.write(
        st.session_state.description
    )

    st.divider()

    st.write("")

    back, submit = st.columns([1, 2])

    with back:

        if st.button(
            "← Back",
            key="back_review",
            use_container_width=True
        ):
            previous_step()

    with submit:

        if st.button(
            "Submit ticket →",
            type="primary",
            use_container_width=True
        ):
            try:
                ticket = create_ticket()

                if ticket:
                    # Use the ticket ID returned by the backend
                    st.session_state.ticket_number = ticket["ticket_id"]
                    next_step()
                else:
                    st.error("Could not create the ticket.")

            except URLError:
                st.error("Could not connect to the backend.")

# =========================================================
# STEP 7
# SUCCESS
# =========================================================

elif st.session_state.step == 7:

    st.write("")
    st.write("")
    st.write("")

    st.title("Your ticket is in! 🎉")

    st.write(
        f"Thanks, **{st.session_state.name}**. "
        "Our IT team has received your request."
    )

    st.write("")

    st.caption("YOUR TICKET NUMBER")

    st.header(
        f"#IT-{st.session_state.ticket_number}"
    )

    st.success(
        "✓ Your request was successfully submitted."
    )

    st.write(
        "We'll keep you updated using "
        f"**{st.session_state.email}**."
    )

    st.write("")
    st.write("")

    if st.button(
        "Create another ticket",
        type="primary",
        use_container_width=True
    ):

        st.session_state.step = 0

        st.session_state.category = ""
        st.session_state.problem = ""
        st.session_state.other_problem = ""
        st.session_state.show_other_input = False
        st.session_state.impact = ""
        st.session_state.description = ""
        st.session_state.ticket_number = ""

        st.rerun()
        