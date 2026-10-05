import streamlit as st


def apply_styles():

    st.markdown("""
    <style>

    .stApp {
        background-color: #EAECF0;
    }

    .block-container {
        max-width: 800px;
        padding-top: 3rem;
        padding-bottom: 5rem;
    }

    h1, h2, h3 {
        color: #000000 !important;
    }

    p {
        color: #233D4D;
    }

    .stCaption {
        color: #233D4D !important;
        font-weight: 600 !important;
    }

    .stButton > button {
        background-color: #233D4D !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 55px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #FE7F2D !important;
        transform: translateY(-2px);
    }

    .stButton > button,
    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #FFFFFF !important;
    }

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    [data-testid="stFileUploader"] {
        background-color: rgba(255, 255, 255, 0.45);
        border-radius: 14px;
        padding: 10px;
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """, unsafe_allow_html=True)