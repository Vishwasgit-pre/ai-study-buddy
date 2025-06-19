# 📚 AI Study Buddy (Gemini-powered)

An AI-powered study assistant that helps students revise any topic by generating:
- ✅ Quizzes (5 MCQs with answers and explanations)
- ✅ Bullet-point summaries
- ✅ Simple explanations with examples

Built using **Streamlit** for the frontend and **Google Gemini API** for AI.

---

## 🚀 Features

- Choose between: **Quiz**, **Summary**, or **Explain**
- Input any topic (e.g. "Photosynthesis", "Newton's Laws")
- Clean and markdown-formatted responses
- Stores recent topic in memory across requests

---

## 🛠 Tech Stack

- 🧠 **Gemini 1.5 Flash** via `google-generativeai`
- 🖥 **Streamlit** for the web UI
- 🐍 Python 3.9+

---

## 🧪 How to Run Locally

1. **Install requirements**
```bash
pip install -r requirements.txt
```

2. **Set your Gemini API Key**
Get it from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

```powershell
setx GEMINI_API_KEY "your-api-key-here"
```

🔁 Then restart your terminal.

3. **Run the app**
```bash
streamlit run app.py
```

Open browser at: `http://localhost:8501`

---

## 📷 Screenshot

> ## 📷 Screenshot

Screenshot 2025-06-19 125531.png



---

## 📂 Folder Structure

```
AI_Study_Buddy_Project/
├── app.py
├── gemini_utils.py
├── requirements.txt
└── README.md
```

---

## ✨ Credits

- Made by Vishwas 🧠
- Powered by Google Gemini and Streamlit
