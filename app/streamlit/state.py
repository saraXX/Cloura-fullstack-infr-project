import streamlit as st


def initialize_state():

    defaults = {
        "step": 0,
        "name": "",
        "email": "",
        "category": "",
        "problem": "",
        "other_problem": "",
        "show_other_input": False,
        "impact": "",
        "description": "",
        "image_data": "",
        "ticket_number": ""
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def next_step():

    st.session_state.step += 1
    st.rerun()


def previous_step():

    st.session_state.step -= 1
    st.rerun()


def go_to_step(number):

    st.session_state.step = number
    st.rerun()