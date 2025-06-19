import streamlit as st
from gemini_utils import generate_response

st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("📚 AI Study Buddy")
st.subheader("Smart quizzes, summaries, and explanations")

intent = st.selectbox("What do you want?", ["Quiz", "Summary", "Explain"])
topic = st.text_input("Enter a topic")

if st.button("Get Result"):
    if topic:
        output = generate_response(intent, topic)
        st.markdown("### 🧠 AI Output")
        st.markdown(output)
    else:
        st.warning("Please enter a topic.")
