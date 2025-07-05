# 📰 Fake News Detection with Real-Time News Feed

This web-based application detects whether a news headline is **Real** or **Fake** using a trained machine learning model. It also fetches **live news headlines** from Indian sources using NewsAPI and displays their predictions in real time.

---

## 📌 Features

- 🔍 Detect fake/real news from manual input.
- 🌐 Shows real-time Indian news with predictions.
- 🧠 Trained PassiveAggressiveClassifier with TF-IDF vectorizer.
- ✅ Refresh button to fetch latest news live.
- 🎨 Modern, clean and responsive frontend.
- ⚡ Built using Python Flask (Backend) and HTML/CSS (Frontend).

---

## 🧠 How It Works

### 1. **Model Training** (Offline)
- Dataset used: `fake_news_dataset.csv` (from Kaggle).
- Preprocessing includes:
  - Lowercasing
  - Removing punctuation
  - Removing stopwords
- Vectorization: **TF-IDF**
- Model: **PassiveAggressiveClassifier**
- Model and vectorizer saved using `pickle`:
  - `model.pkl`
  - `vectorizer.pkl`

### 2. **User Input Prediction**
- User enters a news headline via form.
- The input is cleaned → vectorized → predicted.
- Prediction is displayed: **Real** ✅ or **Fake** ❌.

### 3. **Live News Feed**
- Headlines fetched using NewsAPI from Indian sources: