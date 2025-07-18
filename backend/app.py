# backend/app.py

from flask import Flask, request, render_template, after_this_request
import pickle
import requests
from backend.utils import clean_text
import os

# Load ML model and vectorizer
model = pickle.load(open(os.path.join(os.path.dirname(__file__), "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(os.path.dirname(__file__), "vectorizer.pkl"), "rb"))

# Make sure utils.py is in the backend folder
app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")



@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    # Prevent browser caching so headlines refresh every time
    @after_this_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    # Handle user form input
    if request.method == 'POST':
        user_input = request.form.get('news', '')
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

    # Fetch latest live news
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=6e213721ea8449b79324ec5e3c085677"
    response = requests.get(url)
    data = response.json()

    headlines = []
    for article in data.get("articles", []):
        title = article.get("title", "")
        news_url = article.get("url", "#")

        # Filter invalid titles
        if not title or title.strip().lower() == "google news":
            continue

        cleaned = clean_text(title)
        vectorized = vectorizer.transform([cleaned])
        pred = model.predict(vectorized)[0]

        headlines.append({
            "title": title,
            "prediction": pred,
            "url": news_url
        })

    return render_template("index.html", prediction=prediction, headlines=headlines)

if __name__ == "__main__":
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get("PORT", 5000)))