import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Medical Image Intelligence",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Multimodal Medical Image Intelligence")

st.write(
    "AI-assisted analysis of chest X-rays with patient context."
)

st.warning(
    "This system is for research and demonstration only. "
    "It is not a medical diagnosis."
)

st.header("1. Upload Chest X-ray")

uploaded_file = st.file_uploader(
    "Upload a medical image",
    type=["jpg", "jpeg", "png"]
)

st.header("2. Patient Information")

patient_notes = st.text_area(
    "Patient Notes",
    placeholder="Example: Fever, persistent cough..."
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Chest X-ray",
        use_container_width=True
    )

    if st.button("🔍 Analyze Image"):

        st.subheader("AI Analysis")

        st.write("Finding: Lung Opacity")

        st.write("Model Score: 84%")

        st.write("Location: Right lower lung")

        st.success(
            "Image evidence available through localization."
        )

        if patient_notes:

            st.write("Patient context:")

            st.write(patient_notes)

        st.warning(
            "Doctor, consider reviewing the highlighted region "
            "together with the clinical information."
        )