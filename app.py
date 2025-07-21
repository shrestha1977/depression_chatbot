# app.py
import streamlit as st
from chat_module import predict_depression
from memory_test import generate_sequence, check_sequence
from mood_utils import plot_mood_graph
import matplotlib.pyplot as plt

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "memory_seq" not in st.session_state:
    st.session_state.memory_seq = []

st.title("🧠 MindBot: Depression Support Chat & Cognitive Check")

st.markdown("""
Welcome to **MindBot**, your AI mental wellness companion.  
It helps assess depressive patterns and offers a memory test and mood insights.
""")

# --- Chatbot section ---
st.header("💬 Chat with the AI")
user_input = st.text_input("You:", key="chat_input")

if st.button("Send") and user_input:
    label, score = predict_depression(user_input)
    st.markdown(f"**AI:** Based on your message, I'm sensing: `{label}` (Confidence: {score})")

    st.session_state.chat_history.append((label, score))

# --- Memory Test ---
st.header("🧠 Memory Test")

if st.button("Start Memory Test"):
    seq = generate_sequence()
    st.session_state.memory_seq = seq
    st.markdown(f"**Remember this sequence:** `{ ' '.join(map(str, seq)) }`")
    st.markdown("After a few seconds, type it back below.")

if st.session_state.memory_seq:
    user_answer = st.text_input("Enter the sequence you remember:", key="mem_test")
    if st.button("Check Memory"):
        if check_sequence(user_answer, st.session_state.memory_seq):
            st.success("✅ Great! Your memory is sharp.")
        else:
            st.error(f"❌ Incorrect. Original was: {' '.join(map(str, st.session_state.memory_seq))}")
        st.session_state.memory_seq = []

# --- Mood Chart ---
if st.session_state.chat_history:
    st.header("📊 Mood History")
    fig = plot_mood_graph(st.session_state.chat_history)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("💡 _This app is for educational/demo purposes only. Not a replacement for medical diagnosis._")
