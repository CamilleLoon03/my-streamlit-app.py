import streamlit as st
from PIL import Image

st.title("Camille Loon's Biography")

st.sidebar.header("Edit Student Information")
student_name = st.sidebar.text_input("name", " Camille Loon")
student_id = st.sidebar.text_input("Student ID", "2024344")
age = st.sidebar.number_input("age", min_value=16, max_value=30, value=18)
major = st.sidebar.text_input("Major:", "Bachelor of Science in Computer Engineering")
bio = st.sidebar.text_area("Short Bio", "Hi! I am Camille Loon. A freshman college student at Surigao Del Norte State University (SNSU). I currently exploring the world of engineering.")

st.sidebar.header("Upload Picture")
uploaded_image = st.sidebar.file_uploader("Upload Profile Picture (optional)", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Profile Picture", width=200)
else:
    st.write("No profile picture uploaded")

st.subheader("Student Profile")
st.write(f"*Name:* {student_name}")
st.write(f"*Student ID:* {student_id}")
st.write(f"*Age:* {age}")
st.write(f"*Major:* {major}")
st.write(f"*Bio:* {bio}")
    
if st.button("Save Profile"):
    st.success("Profile information saved successfully!")