import streamlit as st

from streamlit_option_menu import option_menu
from features.prompt_comparison import compare_prompts

from prompts.evaluator_prompt import generate_evaluator_prompt
from features.answer_evaluator import evaluate_answer

from prompts.tutor_prompt import generate_prompt
from prompts.study_plan_prompt import generate_study_plan_prompt
from prompts.quiz_prompt import generate_quiz_prompt

from features.explanation_generator import generate_explanation
from features.study_plan_generator import generate_study_plan
from features.quiz_generator import generate_quiz

# Konfigurasi halaman
st.set_page_config(
    page_title="AI Smart Tutor",
    page_icon="🎓",
    layout="wide"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
background-color:#f8f9fc;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background-color:#ffffff;
border-right:1px solid #eaeaea;
}

/* Card */
.card{
padding:25px;
background:white;
border-radius:20px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:20px;
}

/* Title */
.main-title{
font-size:40px;
font-weight:bold;
color:#e75480;
}

/* Subtitle */
.subtitle{
font-size:18px;
color:gray;
}

/* Button */
div[data-testid="stButton"] button{
width:100%;
height:50px;
border-radius:15px;
background:#f8bbd0;
color:black;
border:none;
font-size:16px;
font-weight:bold;
}

div[data-testid="stButton"] button:hover{
background:#f48fb1;
}

</style>
""", unsafe_allow_html=True)


# ===== SIDEBAR =====
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=80
    )

    st.title("🎓 AI Smart Tutor")

    feature = option_menu(
    menu_title=None,

    options=[
        "AI Tutor",
        "Study Plan",
        "Quiz",
        "Answer Evaluator",
        "Prompt Comparison"
    ],

    icons=[
        "🎓",
        "📚",
        "📝",
        "🎯",
        "📊"],

    default_index=0,

     styles={

        "container":{
            "padding":"0!important",
            "background-color":"#FFF7FA"
        },

        "nav-link":{
            "font-family":"Poppins,sans-serif",
            "font-size":"20px",
            "font-weight":"600",
            "text-align":"left",
            "margin":"6px",
            "padding":"12px",
            "color":"#3A3A3A",
            "--hover-color":"#FCE4EC",
            "border-radius":"12px"
        },

        "nav-link-selected":{
            "background-color":"#E89AB5",
            "color":"black",
            "font-family":"Poppins,sans-serif",
            "font-weight":"700",
            "border-radius":"12px"
        }
    }
)
# ===== DASHBOARD HEADER =====

st.markdown("""
<div class="card">

<div class="main-title">
🎓 AI Smart Tutor
</div>

<div class="subtitle">

AI Learning Platform using Advanced Prompt Engineering

</div>

</div>
""", unsafe_allow_html=True)


# =========================
# AI TUTOR
# =========================
if feature == "AI Tutor":

    question = st.text_input("Enter your question:")

    level = st.selectbox(
        "Choose Explanation Level:",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Generate Explanation"):

        if question:

            prompt = generate_prompt(question, level)

            answer = generate_explanation(prompt)

            st.subheader("📘 AI Tutor Answer")
            st.write(answer)

# =========================
# STUDY PLAN
# =========================
elif feature == "Study Plan":

    topic = st.text_input("Enter topic to learn:")

    days = st.slider("Study Duration (Days)", 1, 30, 7)

    if st.button("Generate Study Plan"):

        if topic:

            prompt = generate_study_plan_prompt(topic, days)

            result = generate_study_plan(prompt)

            st.subheader("📅 Study Plan")
            st.write(result)

# =========================
# QUIZ GENERATOR
# =========================
elif feature == "Quiz":

    topic = st.text_input("Enter quiz topic:")

    if st.button("Generate Quiz"):

        if topic:

            prompt = generate_quiz_prompt(topic)

            result = generate_quiz(prompt)

            st.subheader("📝 Quiz")
            st.write(result)
            
# =========================
# ANSWER EVALUATOR
# =========================
elif feature == "Answer Evaluator":

    question = st.text_area("Enter Question:")

    student_answer = st.text_area("Enter Student Answer:")

    if st.button("Evaluate Answer"):

        if question and student_answer:

            prompt = generate_evaluator_prompt(
                question,
                student_answer
            )

            result = evaluate_answer(prompt)

            st.subheader("📊 Evaluation Result")
            st.write(result)

        else:
            st.warning("Please fill all fields.")

# =========================
# PROMPT COMPARISON
# =========================

elif feature == "Prompt Comparison":

    question = st.text_input(
        "Enter topic/question:"
    )

    if st.button("Compare Prompts"):

        if question:

            result = compare_prompts(question)

            st.subheader("📊 Prompt Comparison Result")

            st.write(result)

        else:
            st.warning("Please enter a topic/question.")