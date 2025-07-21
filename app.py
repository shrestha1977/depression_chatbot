import streamlit as st
from transformers import pipeline
import random

st.set_page_config(page_title="AI Depression Detection Chatbot", layout="centered")

# Load sentiment analysis pipeline
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="bhadresh-savani/bert-base-uncased-emotion")

nlp = load_model()

# Simulated chatbot response (can be expanded)
def get_bot_response(user_input):
    responses = [
        "I see. Can you tell me more about how you've been feeling lately?",
        "I'm here for you. Do you want to talk about what's been bothering you?",
        "That sounds tough. It's okay to feel this way sometimes.",
        "Your feelings are valid. Would you like to explore them together?",
    ]
    return random.choice(responses)

# UI
st.title("🧠 AI Chatbot for Depression Detection")
st.write("This chatbot detects emotional states from your messages and flags potential signs of depression.")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Chat interface
user_input = st.text_input("You:", key="input")

if user_input:
    # Analyze emotion
    prediction = nlp(user_input)[0]
    emotion = prediction['label']
    score = prediction['score']

    # Append conversation
    st.session_state.chat.append(("You", user_input))
    bot_reply = get_bot_response(user_input)
    st.session_state.chat.append(("Bot", bot_reply))

    # Show chat
    for sender, msg in st.session_state.chat:
        st.write(f"**{sender}**: {msg}")

    # Show emotion result
    st.markdown("---")
    st.subheader("🧠 Emotional Analysis")
    st.write(f"**Detected Emotion**: {emotion}")
    st.progress(min(score, 1.0))
    if emotion.lower() in ["sadness", "fear", "anger"]:
        st.warning("⚠️ This message may indicate signs of negative emotional state or depression.")
