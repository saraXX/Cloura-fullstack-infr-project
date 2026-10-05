import streamlit as st

from state import next_step, previous_step


def show():

    st.progress(4 / 6)

    st.caption("04 / 06")

    st.title("How is this affecting your work?")

    st.write(
        "This helps us understand how quickly "
        "you need support."
    )

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

    if st.button(
        "← Back",
        key="back_impact"
    ):

        previous_step()