# 🤖 AI Customer Support Chatbot

## A full-stack web application featuring an AI-powered chatbot  
### Built to classify customer queries using machine learning.

This project demonstrates skills in Natural Language Processing (NLP), model training, and full-stack web development.

---

## ✨ Features

- **NLP-Powered Ticket Classification**: Automatically classifies user messages into categories like `Technical Issue`, `Billing Inquiry`, or `Account Management`.
- **Interactive Chat Interface**: A clean, user-friendly web chat UI built with **React**.
- **ML Response Logic**: Responses vary by confidence level using a **Logistic Regression** model.
- **Python Flask Backend**: A REST API handles communication with the trained model.
- **Fully Local & Customizable**: Everything runs locally using your dataset (`customer_support_tickets.csv`).

---

## 🧰 Tech Stack

| Layer          | Technology                    |
|----------------|-------------------------------|
| Frontend       | React, Axios                  |
| Backend        | Python, Flask, Flask-CORS     |
| ML/NLP         | Scikit-learn, TfidfVectorizer |
| Dataset        | CSV format                    |

---

## 📁 Project Structure

customer_support_chatbot_project/
├── backend/
│ ├── app.py # Flask server
│ ├── predict.py # ML model & prediction logic
│ └── customer_support_tickets.csv # Support dataset
├── frontend/
│ ├── package.json # React dependencies
│ └── src/
│ ├── App.js # Main chat UI
│ └── index.js # React entrypoint
└── README.md # Project guide

---

## 🛠️ Running Locally

### 1. Clone the repository

👆 Everything after ` ```bash ` will be treated as code (not markdown), **until you close it**.

---

### ✅ Correct version:

```markdown
```bash
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot

2. Backend Setup (Flask + ML)
bash
Copy
Edit
cd backend
pip install flask flask-cors scikit-learn pandas
python app.py

---

### ✅ Rule of Thumb

> Always use triple backticks **only** to wrap code blocks, and never mix them with markdown text or headings.

---

Let me know if you'd like me to rewrite the full README.md with all fixes applied — copy-paste ready.
