import streamlit as st
import cohere
from dotenv import load_dotenv
import os

#Load secret key
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

#Page config
st.set_page_config(page_title="Motivation Booster", page_icon="💬", layout="centered")

#Header
st.markdown("<h1 style='text-align:center;'>💬 Motivation Booster</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Feeling something? Let us lift you up with words of encouragement.</p>", unsafe_allow_html=True)
st.markdown("---")

# Mood selection
st.subheader("💭 What's your current mood?")
mood = st.selectbox("", [
    "-- Select Mood --",
    "Anxious", "Tired", "Unmotivated", "Stressed", "Lacking Focus", "Overwhelmed", "Lonely", "Insecure", "Hopeless",
    "Uncertain about the future", "Need clarity", "Seeking purpose", "Feeling lost", "Want to restart",
    "Excited but nervous", "Grateful", "Motivated", "Hopeful", "Ready for change", "Feeling inspired",
    "Want to stay consistent", "Looking for discipline", "Calm and focused"
])

# User input
st.subheader("📝 What's going on?")
user_input = st.text_input("", placeholder="e.g. feeling tensed about exams")

#Generate motivation
st.markdown("###")
if st.button("💡 Get Motivation", use_container_width=True):
    if not user_input.strip():
        st.warning("Please describe your situation.")
    else:
        prompt = f"Write a short, comforting and realistic motivational message for someone who is {user_input.strip()}."
        try:
            response = co.chat(
                message=prompt,
                model='command-r',
                temperature=0.9,
                max_tokens=100
            )
            st.success(f"💬 {response.text.strip()}")
        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; font-size:12px;'>This space is here to remind you: you're not alone, and you've got this. 💪</p>", unsafe_allow_html=True)

