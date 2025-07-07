# 🛡️ PhishML – AI-Powered Phishing Email Detector

PhishML is a lightweight, intelligent web application that detects phishing emails using a trained machine learning model (XGBoost) and TF-IDF-based NLP preprocessing.

## 🚀 Features

- 🔐 Classifies email content as **Phishing 🚨** or **Legitimate ✅**
- ⚡ Powered by **XGBoost** and **TF-IDF vectorization with bi-grams**
- 🧠 Custom stopword filtering (offline-ready, no NLTK downloads needed)
- 🌐 Flask-based web app for instant predictions

---

## 🧩 Tech Stack

- Python 3.x
- Flask (Web Framework)
- XGBoost (ML Model)
- Scikit-learn & Joblib (Model Ops)
- HTML (Jinja Templates)

---

## 📁 Project Structure

PhishML_Final/
│
├── app.py # Flask web app
├── phish_model.pkl # Trained XGBoost model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── sample_emails.csv # Sample training data
├── classification_report.txt # Model evaluation
└── templates/
└── index.html # Frontend UI

---

## 🛠️ How to Run Locally

1. **Clone the repo**
   ``bash
   git clone https://github.com/yourusername/phishml.git
   cd phishml

Install dependencies

pip install flask scikit-learn xgboost joblib
Run the app

python app.py
Open in browser


http://127.0.0.1:5000/

📊 Model Performance
Check classification_report.txt for precision, recall, and F1-score.

Note: The current model is trained on a small, realistic dataset. For production, it’s recommended to retrain on a large dataset from Kaggle.

🎯 Sample Use Cases
Email spam/phishing detection apps

Cybersecurity awareness projects

NLP-based risk classification tools

📌 Future Enhancements
Use real-world datasets (e.g., Enron, SpamAssassin)

Add email header parsing

Export predictions as PDF

Deploy to Render / Heroku

🙌 Acknowledgements
XGBoost

Scikit-learn

Flask
