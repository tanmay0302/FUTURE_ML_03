import sys
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("customer_support_tickets.csv")
df = df.dropna(subset=['Ticket Description', 'Ticket Type'])

X = df["Ticket Description"]
y = df["Ticket Type"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

if len(sys.argv) < 2:
    print(json.dumps({'error': 'No input message provided'}))
    sys.exit()

input_text = sys.argv[1]
input_vec = vectorizer.transform([input_text])
prediction = model.predict(input_vec)[0]
probs = model.predict_proba(input_vec)[0]
confidence = round(max(probs) * 100, 2)

response_templates = {
    "Technical issue": "Looks like a technical issue. I'll help you troubleshoot or connect with tech support.",
    "Billing inquiry": "This seems like a billing issue. I can connect you with our billing team.",
    "Account management": "Seems like an account issue. I can help you log in or reset credentials."
}

response = response_templates.get(prediction, "Thanks! Let me look into this and help you further.")

if prediction == "Technical issue" and confidence < 70:
    response = "I'm not entirely sure what the issue is. Should I connect you to a live agent?"

print(json.dumps({
    "predicted_ticket_type": prediction,
    "confidence": f"{confidence}%",
    "response": response
}))
