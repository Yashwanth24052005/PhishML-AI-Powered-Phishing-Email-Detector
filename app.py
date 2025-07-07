import re
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
model = joblib.load('phish_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

stop_words = set([
    "the", "and", "is", "in", "to", "of", "that", "this", "for", "on", "with", "you", "your",
    "it", "at", "as", "be", "are", "was", "or", "from", "by", "an", "has", "have", "not"
])

def preprocess(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        email_text = request.form['email']
        clean_text = preprocess(email_text)
        vect_text = vectorizer.transform([clean_text])
        result = model.predict(vect_text)[0]
        prediction = 'Phishing Email 🚨' if result == 1 else 'Legitimate Email ✅'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
