import streamlit as st
import json
import random
import requests
import os

# Hugging Face API details
HF_TOKEN = st.secrets["hf_token"] # Replace with your actual token
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Ensure correct file path
json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "interview_questions.json")

# Load predefined questions from JSON file
try:
    with open(json_path, "r") as f:
        interview_data = json.load(f)
    print("✅ Loaded Roles:", interview_data.keys())  # Debugging
except FileNotFoundError:
    print("❌ Error: interview_questions.json not found!")
    interview_data = {}

def generate_question(role):
    """Fetches a random predefined question from the JSON file or generates one using AI."""
    role_key = role.lower().replace(" ", "_")  # Convert "Data Scientist" → "data_scientist"
    
    if role_key in interview_data:
        return random.choice(interview_data[role_key])  # Get a random question from JSON

    # If role is not found, use AI to generate a question
    prompt = f"Generate an interview question for a {role}."
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return "Error: Could not generate question."

def generate_ideal_answer(question):
    """Generates an ideal answer using the AI model."""
    prompt = f"Provide a perfect interview answer to the question: '{question}'"
    
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text']
        # Remove the original question from the response
        answer_only = generated_text.replace(prompt, "").strip()

        return answer_only  # Return only the cleaned answer
    else:
        return "Error: Could not generate ideal answer."
    
    





    


