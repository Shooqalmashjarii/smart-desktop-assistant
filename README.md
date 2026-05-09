
# 🤖 Smart Desktop Assistant

A Python-based intelligent assistant that processes natural language commands and automates real-time desktop tasks — built with a rule-based intent detection engine and LLM integration.

---

## 📌 Overview

This project explores how natural language interfaces can be used to automate everyday desktop workflows. The assistant listens for user commands, classifies intent, and executes the appropriate action — from web searches to taking screenshots.

- **8+ supported commands** across multiple task categories
- **~85% command recognition accuracy** achieved through structured testing and iterative refinement
- Rule-based intent detection with failure-case analysis to improve robustness

---

## ⚙️ Features

| Command Type | Example |
|---|---|
| Web Search | "Search for climate change articles" |
| Screenshot | "Take a screenshot" |
| App Launch | "Open calculator" |
| Time/Date | "What time is it?" |
| System Info | "Check battery" |
| + more | ... |

---

## 🧠 How It Works

```
User Input (text)
      ↓
Intent Detection Engine
      ↓
Command Router
      ↓
Action Executor (web query / screenshot / system task / etc.)
      ↓
Response Output
```

The intent detection system uses pattern matching and keyword extraction to classify commands into one of 8+ categories. Prompt templates were designed to ensure consistent, high-quality LLM output for open-ended queries.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **LLM Integration:** OpenAI / LLM API
- **Libraries:** `os`, `subprocess`, `datetime`, `webbrowser`, `pyautogui` (or similar)
- **Testing:** Manual structured testing with failure-case logging

---

## 📊 Performance

| Metric | Result |
|---|---|
| Commands Supported | 8+ |
| Recognition Accuracy | ~85% |
| Testing Method | Structured manual testing |
| Failure Analysis | Iterative refinement based on edge cases |

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run
```bash
python main.py
```

---

## 📁 Project Structure

```
SMARTASSISTANCE/
├── main.py              # Entry point
├── intent_detector.py   # Command classification logic
├── executor.py          # Action execution per command type
├── requirements.txt     # Dependencies
└── demo/                # Demo video / screenshots
```

---

## 💡 Key Learnings

- Designing intent detection systems and understanding where rule-based approaches break down
- Prompt engineering for reliable LLM output in constrained task environments
- Iterative testing methodology — logging failures and systematically improving coverage

---

## 👩‍💻 Author

**Shooq Al Mashjari** — Computer Engineering Student, Khalifa University  
[LinkedIn](http://www.linkedin.com/in/shooq-al-mashjari-521b85353)
