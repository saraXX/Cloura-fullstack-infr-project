import streamlit as st

from state import next_step, previous_step


def show():

    st.progress(1 / 6)

    st.caption("01 / 06")

    st.title("First, who are we helping?")

    st.write(
        "Enter your information so the IT team "
        "knows how to reach you."
    )

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