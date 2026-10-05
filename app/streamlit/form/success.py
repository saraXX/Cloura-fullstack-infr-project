import streamlit as st


def show():

    st.write("")
    st.write("")
    st.write("")

    st.title("Your ticket is in! 🎉")

    st.write(
        f"Thanks, **{st.session_state.name}**. "
        "Our IT team has received your request."
    )

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

    if st.button(
        "Create another ticket",
        type="primary",
        use_container_width=True
    ):

        st.session_state.step = 0

        st.session_state.name = ""
        st.session_state.email = ""
        st.session_state.category = ""
        st.session_state.problem = ""
        st.session_state.other_problem = ""
        st.session_state.show_other_input = False
        st.session_state.impact = ""
        st.session_state.description = ""
        st.session_state.image_data = ""
        st.session_state.ticket_number = ""

        st.rerun()