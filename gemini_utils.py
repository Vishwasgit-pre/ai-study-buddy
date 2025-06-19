import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(intent, topic):
    if not topic:
        return "Please enter a topic."
    if intent == "Quiz":
        prompt = f"Generate 5 MCQs on '{topic}' with 4 options. Bold the correct answer and explain briefly."
    elif intent == "Summary":
        prompt = f"Summarize '{topic}' in 5 bullet points."
    elif intent == "Explain":
        prompt = f"Explain '{topic}' simply with an example in ≤100 words."
    else:
        return "Unknown intent."

    response = model.generate_content(prompt)
    return response.text
