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

---

## 🛠️ Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot
```
2. Backend Setup (Flask + ML)
```
cd backend
pip install flask flask-cors scikit-learn pandas
python app.py
Runs at: http://localhost:5001
```

4. Frontend Setup (React)
```
cd frontend
npm install
npm start
Runs at: http://localhost:3000

🚀 Future Improvements
Add LLM/GPT-based fallback for uncertain replies

Save trained models (joblib)

Add session memory for multi-turn chat

Deployment to cloud platforms

