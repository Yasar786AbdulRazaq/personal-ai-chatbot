import os
import streamlit as st
from dotenv import load_dotenv
from litellm import completion

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="Gemini AI Agent", page_icon="🤖")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖Personal SDK Agent")
st.subheader("Ask anything — powered by Gemini & LiteLLM")

# Initialize session input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# User input with form
with st.form("ask_form"):
    user_input = st.text_input("📝 Your Question:", value=st.session_state.user_input, key="user_input")
    submitted = st.form_submit_button("Send")

# On submit
if submitted and user_input.strip():
    with st.spinner("Thinking..."):
        try:
            response = completion(
                model="gemini/gemini-2.0-flash",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            # Output
            reply = response["choices"][0]["message"]["content"]
            st.markdown("### 🤖 Gemini's Answer:")
            st.success(reply)

            # Clear box
            st.session_state.user_input = ""

        except Exception as e:
            st.error(f"❌ Error: {e}")
