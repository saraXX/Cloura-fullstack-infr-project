import streamlit as st

from api import create_ticket
from state import next_step, previous_step


def show():

    st.progress(1.0)

    st.caption("06 / 06")

    st.title("Ready to send? ✓")

    st.write(
        "Take a quick look before sending your request."
    )

    st.divider()

    st.caption("REQUESTED BY")

    st.subheader(
        st.session_state.name
    )

    st.write(
        st.session_state.email
    )

    st.divider()

    st.caption("CATEGORY")

    st.subheader(
        st.session_state.category
    )

    st.divider()

    st.caption("PROBLEM")

    st.subheader(
        st.session_state.problem
    )

    st.divider()

    st.caption("WORK IMPACT")

    st.subheader(
        st.session_state.impact
    )

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

    st.caption("DESCRIPTION")

    st.write(
        st.session_state.description
    )

    st.divider()

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

            ticket = create_ticket()

            if ticket:

                st.session_state.ticket_number = (
                    ticket["ticket_id"]
                )

                next_step()

            else:

                st.error(
                    "Could not create the ticket."
                )