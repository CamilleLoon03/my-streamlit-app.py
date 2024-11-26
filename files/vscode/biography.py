import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Student Biography",
    page_icon="📚",
    layout="wide",
)

st.title("📖 Camille Loon's Biography")

st.sidebar.header("Edit Student Information ✍️")
student_name = st.sidebar.text_input("Name", "Camille Loon")
student_id = st.sidebar.text_input("Student ID", "2024344")
age = st.sidebar.number_input("Age", min_value=16, max_value=30, value=18)
major = st.sidebar.text_input("Major", "Bachelor of Science in Computer Engineering")
about_me = st.sidebar.text_area(
    "About Me",
    "Hi! I'm Camille Loon, a regular teenager who loves to explore new things and enjoy life to the fullest. When I'm not busy with schoolwork, you’ll find me hanging out with friends, binge-watching my favorite series, or scrolling through social media to stay updated on trends."
"I have a creative side—I enjoy painting and sketching whenever inspiration strikes. Music is a big part of my life, whether I’m singing my favorite songs or discovering new artists to add to my playlist. I’m also a foodie who loves trying out new snacks or making late-night instant ramen while watching YouTube."
"In my free time, I enjoy playing with my pets, because they always know how to brighten up my day. On weekends, I might sleep in late, go for a casual walk, or spend hours gaming or reading webcomics. Life as a teenager is all about balance—studying, making memories, and figuring out who I want to be!",
)

st.sidebar.header("Upload Picture 🖼️")
uploaded_image = st.sidebar.file_uploader(
    "Upload Profile Picture (optional)", type=["jpg", "jpeg", "png"]
)

st.subheader("🎓 Student Profile")

col1, col2 = st.columns([1, 3])
with col1:
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Profile Picture", use_container_width=True)
    else:
        st.image(
            "https://via.placeholder.com/150",
            caption="Default Profile Picture",
            use_container_width=True,
        )

with col2:
    st.markdown(f"**👤 Name:** {student_name}")
    st.markdown(f"**🆔 Student ID:** {student_id}")
    st.markdown(f"**🎂 Age:** {age}")
    st.markdown(f"**📘 Major:** {major}")
    st.markdown(f"**💬 About Me:**\n{about_me}")

if st.button("💾 Save Profile"):
    with open("profile.txt", "w") as file:
        file.write(f"Name: {student_name}\n")
        file.write(f"Student ID: {student_id}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Major: {major}\n")
        file.write(f"About Me: {about_me}\n")
    st.success("✅ Profile information saved successfully!")

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <small>Created with ❤️ by Camille Loon</small>
    </div>
    """,
    unsafe_allow_html=True,
)
