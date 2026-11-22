# GenAi
#  Smart Study Buddy – AI-Powered Study Material Generator

Smart Study Buddy is a Generative AI-based application that helps students generate structured study materials using Google Gemini. Users can enter any topic, select a difficulty level, and receive explanations, examples, multiple-choice questions, interview questions, and summaries.

##  Project Overview

The main objective of this project is to make learning easier and more effective through Generative AI. The application uses LangChain to connect Google Gemini with an interactive Streamlit interface.

##  Features

- **Topic-Based Learning:** Generate study material for any topic.
- **Difficulty Selection:** Choose Easy, Medium, or Hard.
- **Topic Explanation:** Get detailed explanations according to the selected level.
- **Simple Example:** Understand concepts through simple examples.
- **Real-Life Example:** Connect theoretical concepts with practical situations.
- **MCQ Generation:** Generate exactly 5 multiple-choice questions with four options and correct answers.
- **Interview Questions:** Generate 5 interview questions related to the topic.
- **Topic Summary:** Get important points in bullet format.
- **Interactive Interface:** Simple and user-friendly Streamlit application.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web application interface |
| Google Gemini 2.5 Flash Lite | Generative AI model |
| LangChain | Prompt management and LLM integration |
| LangChain Core | Prompt templates |
| python-dotenv | Environment variable management |

##  Project Structure

```text
Smart-Study-Buddy/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-Study-Buddy.git
```

### Step 2: Open the Project Folder

```bash
cd Smart-Study-Buddy
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Configure Google Gemini API Key

1. Get your API key from [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the project folder.
3. Add your API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

**Important:** Never upload your actual `.env` file or expose your API key on GitHub.

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

##  How the Application Works

1. The user enters a study topic.
2. The user selects a difficulty level.
3. LangChain prepares the prompt using the entered information.
4. Google Gemini processes the prompt.
5. The generated study material is displayed through Streamlit.

## Future Enhancements

- Download study material as PDF.
- Add interactive quizzes and score tracking.
- Save previously generated study materials.
- Support multiple languages.
- Add subject-wise learning categories.
- Add more customization options for questions.

##  Project Objective

To develop an intelligent learning assistant that uses Generative AI to create personalized and structured study material, helping students understand concepts and prepare for examinations and interviews.

##  Author

**Swarna Pathak**
