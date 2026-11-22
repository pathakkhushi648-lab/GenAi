"""
Smart Study Buddy
-----------------
A Streamlit app that uses LangChain and Google Gemini to generate
complete study material (explanation, examples, MCQs, interview
questions and a summary) for any topic at a chosen difficulty level.
"""

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------- Configuration ----------------

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

PROMPT_TEMPLATE = """
You are an expert teacher.

Topic: {topic}

Difficulty Level: {difficulty}

Generate the following study material:

##  Explanation
Explain the topic according to the selected difficulty.

##  Simple Example
Give one simple example.

##  Real-Life Example
Give one real-life example.

##  5 MCQs
Generate exactly 5 MCQs with:
- Question
- A, B, C, D options
- Correct Answer

##  5 Interview Questions
Generate 5 interview questions.

##  Summary
Summarize the topic in bullet points.

Return everything in proper Markdown.
"""


@st.cache_resource(show_spinner=False)
def get_chain():
    """Build the LangChain pipeline once and reuse it across reruns."""
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    return prompt | llm


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Smart Study Buddy", page_icon="📚", layout="centered")

st.title(" Smart Study Buddy")
st.write("Generate complete study material using Google Gemini.")

# Fail early with a helpful message if the API key is missing
if not (os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")):
    st.error(
        "API key not found. Create a `.env` file (see `.env.example`) "
        "and add your `GOOGLE_API_KEY`, then restart the app."
    )
    st.stop()

topic = st.text_input("Enter Topic", placeholder="Example: Machine Learning")

difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

generate = st.button("Generate Study Material", type="primary")

# ---------------- Generate ----------------

if generate:
    if not topic.strip():
        st.warning(" Please enter a topic.")
    else:
        try:
            with st.spinner("Generating Study Material..."):
                response = get_chain().invoke(
                    {"topic": topic.strip(), "difficulty": difficulty}
                )
            st.session_state["material"] = response.content
            st.session_state["topic"] = topic.strip()
        except Exception as exc:  # network, quota, invalid key, etc.
            st.error(f"Something went wrong while generating content: {exc}")

# Show the latest result (persists across reruns, e.g. after a download click)
if "material" in st.session_state:
    st.success("Study Material Generated Successfully!")
    st.markdown("---")
    st.markdown(st.session_state["material"])

    file_name = st.session_state["topic"].lower().replace(" ", "_") + "_study_material.md"
    st.download_button(
        label="⬇ Download as Markdown",
        data=st.session_state["material"],
        file_name=file_name,
        mime="text/markdown",
    )
