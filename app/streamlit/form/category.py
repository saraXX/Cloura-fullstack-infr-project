import streamlit as st

from state import next_step, previous_step


def show():

    st.progress(2 / 6)

    st.caption("02 / 06")

    st.title("What can we help you with?")

    st.write(
        "Choose the area that best matches your problem."
    )

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

        column = (
            col1
            if index % 2 == 0
            else col2
        )

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

    if st.button(
        "← Back",
        key="back_category"
    ):

        previous_step()