# main.py (Streamlit)
# Switch provider bby changing the import line:
from groq import generate_response  # For Groq
# from hf import generate_response  # For Hugging Face

import streamlit as st
import re

def looks_incomplete(text: str) -> bool:
    if not text or len(text.strip()) < 10:
        return True

    t = text.strip()

    # commom "cut" signs: ends mid word, mid-markdown, or no closing punctuation
    if t.endswith(('**', '*', '-', '—', ':', ',', '(', '[', '{')):
        return True

    if re.search(r"\d+\.\s*\*\*$", t):  # like 3. **
        return True

    if not re.search(r"[.!?]\s*$", t):  # no sentence-ending punctuation
        return True

    return False

def complete_answer(question: str, max_rounds: int = 2) -> str:
    # Ask for a clean structured answer (help avoid unfinished answers)
    base_prompt = (
        "Answer clearly in numbered points."
        "Do not cut sentences. Finish each point fully.\n\n"
        f"Question: {question}"
    )

    ans = generate_response(base_prompt, temperature=0.3, max_tokens=1024)

    #2) If it looks cut, contine form last line without repeating
    rounds = 0

    
