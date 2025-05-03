import streamlit as st
import random
from PIL import Image

# Set page config
st.set_page_config(page_title="Python MCQs for Students by Ammara Dawood", page_icon="🖋", layout="centered")

# Background and Style
page_bg_img = f'''
<style>
.stApp {{
background-image: url("https://images.unsplash.com/photo-1581090700227-1b5a00c9405d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1650&q=80");
background-size: cover;
}}

h1 {{
    animation: glow 2s ease-in-out infinite alternate;
}}

@keyframes glow {{
  from {{ text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc, 0 0 30px #00ffcc; }}
  to {{ text-shadow: 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff; }}
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Animated Logo
st.markdown("<h1 style='text-align: center;'>🐉 Python MCQs for Students <br> Created by Ammara Dawood</h1>", unsafe_allow_html=True)

# Student Info
st.subheader("📚 Student Information")
name = st.text_input("Enter your Name")
roll_no = st.text_input("Enter your Roll Number")
email = st.text_input("Enter your Email ID")

# Questions Data
questions = [
    {"question": "What is the keyword to define a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
    {"question": "Which symbol is used for comments in Python?", "options": ["//", "#", "<!-- -->", "/* */"], "answer": "#"},
    {"question": "Which data type is used to store True or False?", "options": ["int", "str", "bool", "float"], "answer": "bool"},
    {"question": "How do you create a list in Python?", "options": ["{}", "[]", "()", "<>"], "answer": "[]"},
    {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "5"], "answer": "8"},
    # Add more questions up to 100 similarly
]

# Randomize questions (limit to 10 for easy testing)
questions = random.sample(questions, len(questions))

# Start Quiz
if name and roll_no and email:
    st.success(f"Welcome {name}! Start your MCQ Test")
    
    score = 0
    total_questions = len(questions)

    for idx, q in enumerate(questions):
        st.write(f"**Q{idx+1}: {q['question']}**")
        user_answer = st.radio("Select your answer:", q['options'], key=idx)
        if st.button(f"Submit Answer for Q{idx+1}", key=f"submit{idx}"):
            if user_answer == q['answer']:
                st.success("Correct! 👍")
                score += 1
            else:
                st.error(f"Wrong! Correct answer is: {q['answer']}")

    # Final Result
    st.subheader("\n\n✨ Test Completed! ✨")
    st.write(f"### {name} ({roll_no})")
    st.write(f"Your Total Score: {score} out of {total_questions}")
    percentage = (score/total_questions)*100
    st.write(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        st.success("🎉 Excellent Work!")
    elif percentage >= 70:
        st.info("👌 Good Job, Keep Improving!")
    elif percentage >= 50:
        st.warning("⚠️ Needs More Practice!")
    else:
        st.error("❌ Poor Performance. Study Harder!")

else:
    st.warning("Please fill all student information to start the quiz.")
