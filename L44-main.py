# main.py (Streamlit)
# Switch provider bby changing the import line:
#from groq import generate_response  # For Groq
from hf import generate_response  # For Hugging Face

import io
import streamlit as st

CSS = """
<style>
    .history-wrap{
        max-height: 420px;
        overflow-y: auto;
        padding-right: 6px;
    }

    .qa-card{
        border: 1px solid #e6e6e6;
        background-color: #ffffff;
        border-radius: 10px;
        padding: 14px 16px;
        margin: 10px 0px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.04);
    }

    .q{
        font-weight: 700;
        color: #0a6ebd;
        margin-bottom: 8px;
    }

    .a{
        white-space: pre-wrap;
        color: #333;
        line-height: 1.5;
    }
</style>
"""

def export_bytes(history):
    text = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])

    return io.BytesIO(text.encode("utf-8"))

def setup_ui():
    st.set_page_config(page_title="AI Teaching Assistant", page_icon=":speech_balloon:", layout="centered")
    st.title("🤖 AI Teaching Assistant")
    st.write("Ask me anything aboout various subjects, and I'll provide an insightful answer.")
    st.session_state.setdefault("history", [])

    col_clear , col_export = st.columns([1, 2])

    with col_clear:
        if st.button("🧹 Clear Conversation"):
            st.session_state.history = []
            st.rerun()

    with col_export:
        if st.session_state.history:
            st.download_button(
                label="📤 Export Chat History",
                data=export_bytes(st.session_state.history),
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain",
            )

    user_input = st.text_input("Enter your question here: ")

    if st.button("Ask"):
        q = user_input.strip()

        if q:
            with st.spinner("Generating AI response..."):
                a = generate_response(q, temperature=0.3)

            st.session_state.history.insert(0,{"question": q,"answer": a})
            st.rerun()

        else:
            st.warning("⚠️ Please enter a question before asking.")

    st.markdown("### Conversation History")
    st.markdown(CSS, unsafe_allow_html=True)

    cards = []