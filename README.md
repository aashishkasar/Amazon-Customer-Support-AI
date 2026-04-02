# 📦 Amazon Customer Support AI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Project Overview

An AI-powered customer support system that answers queries **strictly based on policy** using **Prompt Engineering**.

⚠️ No assumptions
❌ No external knowledge
✅ Fully policy-driven AI

---

## ✨ Features

* 📜 Policy-based reasoning (strict compliance)
* 📂 Upload policy via **PDF / TXT**
* 🧠 Structured AI output (Answer + Reason + Confidence)
* 🔐 Dynamic API key support (user input + secrets)
* ⚡ Built using Prompt Engineering (No RAG / No Agents)

---

## 🖥️ UI Preview

<img width="497" height="900" alt="image" src="https://github.com/user-attachments/assets/33ee8209-2d5f-417b-9cc5-60a534fec676" />


---

## 🧠 Architecture Diagram

```mermaid
flowchart TD
    A["User Input"] --> B["Query + Policy"]
    B --> C["Prompt Engineering Layer"]
    C --> D["LLM (Groq)"]
    D --> E["Generate Multiple Answers"]
    E --> F["Select Best Answer"]
    F --> G["Verification Step"]
    G --> H["Final JSON Output"]
```

---

## ⚙️ How It Works

```text
User Query + Policy
        ↓
Understand Policy
        ↓
Reason Internally
        ↓
Generate Answer
        ↓
Verify
        ↓
Return JSON Output
```

---

## 📌 Example

### Input:

```json
{
  "query": "Can I return opened headphones after 5 days?",
  "policy": "Electronics cannot be returned if opened."
}
```

### Output:

```json
{
  "answer": "Return is not allowed",
  "reason": "Opened electronics cannot be returned",
  "confidence": "high"
}
```

---

## 🛠️ Tech Stack

* 🐍 Python
* 🎨 Streamlit
* 🔗 LangChain
* ⚡ Groq LLM
* 🧠 Prompt Engineering

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/amazon-support-ai.git
cd amazon-support-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment

* Streamlit Cloud
* Hugging Face Spaces

---

## 🔐 API Key Handling

* User input (UI)
* Environment variable (`.env`)
* Streamlit Secrets (for deployment)

---

## 🚨 Constraints

* ❌ No RAG
* ❌ No Vector DB
* ❌ No Agents
* ✅ Only Prompt Engineering

---

## 💡 Key Insight

> “There is no fixed correct answer —
> the output depends entirely on the given policy.”

---

## 📁 Project Structure

```bash
amazon-support-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── utils/
│   └── llm_setup.py
│
├── prompts/
│   └── support_prompt.py
│
├── assets/
│   └── screenshot.png
```

---

## 👨‍💻 Developer

**Tekton AI**

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repo
👉 Share with others
👉 Add to your portfolio
