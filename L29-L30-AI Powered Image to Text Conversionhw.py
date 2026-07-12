# ============================ PART 1 (EXECUTABLE) ============================
import requests, base64, os, re, time
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

HF_API_KEY = "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"

ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}

VISION_MODELS = [
    "Qwen/Qwen3-VL-8B-Instruct:together",
    "Qwen/Qwen3-VL-32B-Instruct:together",
    "Qwen/Qwen2.5-VL-7B-Instruct:together",
    "Qwen/Qwen2.5-VL-32B-Instruct:together",
    "Qwen/Qwen2-VL-2B-Instruct:together",
    "Qwen/Qwen2-VL-7B-Instruct:together",
]
TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "Qwen/Qwen2.5-14B-Instruct:together",
    "Qwen/Qwen2.5-32B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together",
    "mistralai/Mixtral-8x7B-Instruct-v0.1:together",
]

def _data_url(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," +base64.b64encode(f.read()).decode("utf-8")

def query_hf_api(payload: dict):
    try:
        r = requests.post(ROUTER_URL, headers=HEADERS, json=payload, timeout=10)
    except requests.RequestException as e:
        return None, f"Request failed: {e}"

    if r.status_code != 200:
        try:
            j = r.json()
            msg = j.get("error", {}).get() or str(j)
        except Exception:
            msg = (r.text or "").strip() or r.reason or "Request failed."
        return None, f"Status {r.status_code}: {msg}"
    try:
        return r.json(), None
    except Exception:
        return None, "Non-JSON response received from the API."

def _extract_text(data) -> str:
    msg = (data or {}).get("choices", [{}])[0].get("message", {}) or {}
    return (msg.get("content") or "").strip()

def _run_models(models, messages, max_tokens=160, temperature=0.3):
    last_err = None
    for model in models:
        data, err = query_hf_api({"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": temperature})
        if err:
            last_err = err
            continue
        out = _extract_text(data)
        if out:
            return out, None
        last_err = "Empty response from model."
    return None, last_err or "All models failed."

def _words(text: str):
    return re.findall(r"\S+", (text or "").strip())

def _exact_n_words(text: str, n: int) -> str:
    return " ".join(_words(text)[:n])

def _ensure_sentence_end(text: str, n: int) -> str:
    t = (text or "").strip()
    if t and t[-1] not in ".!?":
        t += "."
    return t

# ============================ PART 2 (EXECUTABLE) ============================
def generate_text(prompt: str, max_new_tokens: int = 220) -> str:
    msgs = [{"role": "user", "content": prompt}]
    text, err = _run_models(TEXT_MODELS, msgs, max_tokens=max_new_tokens, temperature=0.7)
    if err:
        raise Exception(err)
    return text

def generate_exact_sentence(prompt: str, n_words: int, max_new_tokens: int = 220, tries: int = 6) -> str:
    for _ in range(tries):
        out = generate_text(prompt, max_new_tokens=max_new_tokens)
        if not out:
            continue
        ws = _words(out)
        if len(ws) == n_words:
            return _ensure_sentence_end(out)
        if len(ws) > n_words:
            max_new_tokens = _ensure_sentence_end(_exact_n_words(out, n_words))
        return _ensure_sentence_end(_exact_n_words(out, n_words))
    return Exception(f"Failed to generate a sentence with exactly {n_words} words after {tries} tries.")


def get_basic_caption(image_path: str) -> str:
    print(f"{Fore.YELLOW}🖼️ Generating basic caption ...")
    msgs = [{
        "role": "user",
        "content": [
            {"type": "text", "text": "Write one complete sentence describing this image."},
            {"type": "image_url", "image_url": {"url": _data_url(image_path)}},
        ],
    }]
    cap, err = _run_models(VISION_MODELS, msgs, max_tokens=90, temperature=0.2)
    return cap if cap else f"[Error] {err}"

def print_menu():
    print(f"""{Style.BRIGHT}{Fore.GREEN}
================ Image-to-Text Conversion =================
Select output type:
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
=============================================================
""")

def main():
    image_path = input(f"{Fore.BLUE}Enter the path of the image (e.g., test.jpg): {Style.RESET_ALL}")
    if not os.path.exists(image_path):
        print(f"{Fore.RED}❌ The file '{image_path}' does not exist.")
        return
    try:
        Image.open(image_path)
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to open image: {e}")
        return

    basic_caption = get_basic_caption(image_path)
    print(f"{Fore.YELLOW}📝 Basic caption: {Style.BRIGHT}{basic_caption}\n")

    while True:
        print_menu()
        choice = input(f"{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}").strip()

        if basic_caption.startswith("[Error]") and choice in {"1", "2", "3"}:
            basic_caption = get_basic_caption(image_path)
            print(f"{Fore.YELLOW}📝 Basic caption: {Style.BRIGHT}{basic_caption}\n")

        if choice == "1":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}❌ Caption (5 words): {Style.BRIGHT}{basic_caption}\n")
            else:
                out = _ensure_sentence_end(_exact_n_words(basic_caption, 5), 5)
                print(f"{Fore.GREEN}✅ Caption (5 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")

        elif choice == "2":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}❌ Failed to generate description: {basic_caption}")
                continue
            prompt = ("Rewrite as EXACTLY 30 words. Single paragraph. One complete sentence. "
                      "End with a period. No title/bullets.\n\nText: " + basic_caption)
            try:
                out = generate_exact_sentence(prompt, 30,max_new_tokens=200, tries=6)
                print(f"{Fore.GREEN}✅ Description (30 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to generate description: {e}")

        elif choice == "3":
            if basic_caption.startswith("[Error]"):
                print(f"{Fore.RED}❌ Failed to generate summary: {basic_caption}")
                continue
            prompt = ("Write EXACTLY 50 words. Single paragraph. One complete sentence. "
                      "End with a period. No title/bullets/extra text.\n\nImage seed: " + basic_caption)
            try:

                print(f"{Fore.GREEN}✅ Summary (50 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to generate summary: {e}")

        elif choice == "4":
            print(f"{Fore.GREEN}👋 Goodbye!")
            break
        else:
            print(f"{Fore.RED}❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
