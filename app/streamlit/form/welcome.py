import streamlit as st

from state import next_step


def show():

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