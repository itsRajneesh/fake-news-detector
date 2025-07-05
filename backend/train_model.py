# backend/train_model.py

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, classification_report
from utils import clean_text

# Load and clean dataset
df = pd.read_csv('../dataset/fake_news_dataset.csv')  
df = df[['text', 'label']]  # only keep necessary columns
df['text'] = df['text'].apply(clean_text)

# Vectorize
vectorizer = TfidfVectorizer(max_df=0.7, stop_words='english')
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = PassiveAggressiveClassifier(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred)*100)
print(classification_report(y_test, y_pred))

# Save model and vectorizer
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
