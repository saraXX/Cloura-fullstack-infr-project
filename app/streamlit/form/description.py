import base64
import streamlit as st

from state import next_step, previous_step


def show():

    st.progress(5 / 6)

    st.caption("05 / 06")

    st.title("One last thing...")

    st.write(
        "Tell us a little more about what happened."
    )

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
        "Add a screenshot (optional)",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if uploaded_file is not None:

        file_bytes = uploaded_file.getvalue()

        st.session_state.image_data = (
            base64.b64encode(file_bytes)
            .decode("utf-8")
        )

        st.image(
            uploaded_file,
            caption="Preview",
            use_container_width=True
        )

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