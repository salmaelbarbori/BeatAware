import streamlit as st
from PIL import Image

# Function to process symptoms and return diagnosis (example)
def diagnose_symptoms(symptoms):
    return "Based on your symptoms, you may have 'Hypertension' or 'Non-anginal chest pain'."

# Title and animation
st.title("💓 Beat Aware")
st.markdown(
    """
    <style>
        @keyframes pulse {
            0% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
            100% { opacity: 1; transform: scale(1); }
        }
        h1 {
            animation: pulse 2s infinite;
            color: #2c7f4f;
            font-weight: bold;
            font-size: 2.5em;
        }
    </style>
    """, unsafe_allow_html=True
)

# Load and resize the logo
image = Image.open('/content/Red Heartrate Icon Medical Logo .png')
st.image(image, width=50)  # Resize image width to 50px

# Input text box for symptoms
symptoms = st.text_area("Describe your symptoms, and we will provide you with the necessary help...", height=100)

# Button to trigger diagnosis
if st.button("Diagnose"):
    diagnosis = diagnose_symptoms(symptoms)
    st.text_area("Here is the diagnosis...", value=diagnosis, height=200)
