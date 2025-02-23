import json
import streamlit as st
from utils.question_generator import generate_question, generate_ideal_answer
from utils.response_analysis import analyze_response

# Streamlit UI
st.set_page_config(page_title="AI Job Interview Coach", layout="centered")
st.title("🤖 AI Job Interview Coach")

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "submitted_answer" not in st.session_state:
    st.session_state.submitted_answer = None
if "ideal_answer" not in st.session_state:
    st.session_state.ideal_answer = ""
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # Initialize user input field state

# Select Job Role
role = st.selectbox("Select Job Role", ["Data Scientist", "Software Engineer", "HR Interview", "Motion Graphic Designer", "VFX Artist", "Video Editor"])

# Generate a new question when the button is clicked
if st.button("Get Interview Question"):
    st.session_state.current_question = generate_question(role)  # Generate new question
    st.session_state.ideal_answer = generate_ideal_answer(st.session_state.current_question)  # Generate new ideal answer
    st.session_state.submitted_answer = None  # Reset previous answer
    st.session_state.user_input = ""  # Reset user input field

# Display Question if Available
if st.session_state.current_question:
    st.write(f"**📝 Question:** {st.session_state.current_question}")

    # User input field (resets when generating a new question)
    user_answer = st.text_area("✍️ Your Answer", placeholder="Type your response here...", key="user_input", value=st.session_state.user_input)

    # Submit Answer Button
    if st.button("Submit Answer") and user_answer.strip():
        result, score = analyze_response(user_answer, st.session_state.ideal_answer)
        st.session_state.submitted_answer = (user_answer, result, score)

# Display Feedback if Answer Submitted
if st.session_state.submitted_answer:
    user_answer, result, score = st.session_state.submitted_answer
    st.write(f"**📊 Your Answer:** {user_answer}")
    st.write(f"**💡 Correctness:** {result}")
    st.write(f"**📊 Similarity Score:** {score:.2f}")
    st.write(f"**✅ Ideal Answer:** {st.session_state.ideal_answer}")
