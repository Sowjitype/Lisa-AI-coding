# main_part1 (Streamlit)
import io,re
from io import BytesIO
import streamlit as st
from huggingface_hub import InferenceClient
import config

# Switch provider by changing the import line:
from groq import generate_response
#from hf import generate_response

MATH_SYSTEM = """You are a Math Mastermind.
Solve with clear step-by-step reasoning, correct notation, and a final answer.
Verify when possible; mention an alternative method briefly if relevant."""

CHAT_CSS ="""
<style>
    .wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
    
    .card{broad: 1px soild #e6e6e6; background: #fff; broader-radius: 10px; padding:14px 16px; margin: 10px 0; 
    box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
    
    .q{font-weight:700; color: #0a6ebd; margin_bottom: 8px;}

    .meta{display: inline-block; background: #FF9800; color:#ff; padding: 2px 8px; border-radius:12px; font-size:12px;}
    
    .a{white-space: pre_wrap; color: #333; line_height:1.5}
</style>
"""

def export_txt(history):
    txt = "".join([f"Q{i}: {h['question']}\A{i}: {h['answer']}\n\n" for i,h in enumerate(history, 1)])
    bio = io.BytesIO(txt.encode("utf-8")); bio.seek(0); return bio

def teaching_answer(q: str) -> str:
    return generate_response(q, temperature=0.3, max_tokens=1024)

def math_answer(q: str, level: str) -> str:
    prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\n\nMath Question: {q}"
    return generate_response(prompt, temperature=0.1, max_tokens=1024)

def run_ai_teaching_assistant():
    st.title("🤖AI Teaching Assistant")
    st.session_state.setdefault("history_ata", [])
    c1, c2 = st.columns([1, 2])
    if c1.button("🧹Clear", key="c_ata"): st.session_state.history_ata = []; st.rerun()

    if st.session_state.history_ata:
        c2.download_button("📄Export", export_txt(st.session_state.history_ata), 
                           "AI_Teaching_Assistant_History.txt", "text/plain")

    q = st.text_input("Ask a question:", key = "q_ata")

    if st.button("Ask",  key ="a_ata"):
        if not q.strip(): st.warning("⚠️Enter a question!!")
        else:
            with st.spinner("Thinking..."):
                st.session_state.history_ata.append({"question": q.strip(), "answer": teaching_answer(q.strip())})
                st.rerun()

    if not st.session_state.history_ata: return

    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    html = '<div class="wrap">'

    for i, h in enumerate(st.session_state.history_ata,1):
        html += f'<div class="card"><div class="q"Q{i}: {qa["question"]}</div><div class="a>{qa["answer"]}</div></div>'

    st.markdown(html + "</div>", unsafe_allow_html=True)

def run_math_mastermind():
    st.title("🤖Math Mastermind")
    st.session_state.setdefault("history_mm", [])
    st.session_state.setdefault("k_mm",0)
    c1, c2 = st.columns([1, 2])

    if c1.button("🧹Clear", key="c_mm"): st.session_state.history_mm = []; st.rerun()

    if st.session_state.history_mm:
        c2.download_button("📄Export", export_txt(st.session_state.history_mm), 
                           "Math_Mastermind_History.txt", "text/plain")

    with st.form("mm_form", clear_on_submit=True):
        q = st.text_area("Math question:", height=100, key =f"_mm_{st.session_state.k_mm}")
        a, b = st.columns([3, 1])
        go = a.form_submit_button("Solve", use_container_width=True)
        lvl = b._selectbox("Level", ["Basic", "Intermediate", "Advanced"], index=1)

        if go:
            if not q.strip(): st.warning("⚠️Enter a math question!!")
            else:
                with st.spinner("Solving..."):
                    ans = math_answer(q.strip(), lvl)

                st.session_state.history_mm.append({"question": q.strip(), "answer": ans, "difficulty": lvl})
                st.session_state.k_mm += 1; st.rerun()
        