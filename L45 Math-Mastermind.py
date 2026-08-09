# Switch provider by changing the import line:
from hf import generate_response
# From groq import generate_response

import io, streamlit as st

SYSTEM_PROMPT = """
                    You are a Math Mastermind. For every math problem:
                    1) Show step-by-step solution 2) Explain reasoning 3) Give alternate method if possible
                    4) Verify answer if possible 5) Use proper notation 6) Break complex problems into parts
                    Format: Problem → Steps → **Final Answer** → Concepts used. Be precise and educational.
                """

def math_generate(problem: str, level: str, temperature= 0.1, max_tokens = 1024) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nMath Problem: ({level}): {problem}"

    return generate_response(prompt, temperature=temperature, max_tokens=max_tokens)

def export_txt(history):
    txt = "\n\n".join([f"Q{1}: {h['q']}\nA{i}:{h['a']}" for i, h in enumerate(history, 1)])

    return txt

def setup_ui():
    st.set_page_config(page_title="🧮Math Mastermind", layout="centered")
    st.title("🧮Math Mastermind")
    st.write("Solve math problem with detailed step-by-step explanations.")

    with st.expander("📌Example"):
        st.markdown(
            '-Algebra: Solve for x in the equation 2x + 3 = 7\n' \
            '-Calculus: Find the derivative of f(x) = x^2 + 3x + 5\n' \
            '-Geometry: Calculate the area of a triangle with base 5 and height 10\n' \
            '-Probability: What is the probability of rolling a sum of 7 with two dice?\n' \
        )

    st.session_state.setdefault("history", [])
    st.session_state.setdefault("k", 0)

    c1,c2 = st.columns([1, 2])