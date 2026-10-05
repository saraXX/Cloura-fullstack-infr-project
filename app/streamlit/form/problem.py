import streamlit as st

from state import next_step, previous_step


PROBLEMS = {

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


def show():

    st.progress(3 / 6)

    st.caption("03 / 06")

    st.title("What's going wrong?")

    st.write(
        f"You selected **{st.session_state.category}**."
    )

    st.write(
        "Choose the option that best describes the issue."
    )

    selected_problems = PROBLEMS.get(
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

                next_step()

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

    if st.button(
        "← Back",
        key="back_problem"
    ):

        previous_step()