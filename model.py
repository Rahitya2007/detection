from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training Data
texts = [
    "https://google.com",
    "https://youtube.com",
    "support@gmail.com",
    "hello@yahoo.com",
    "http://fake-login@bank.com",
    "winnerfreegift@bankverify.com",
    "urgent verify your bank account",
    "free money click now",
    "http://win-prize-now.com"
]

labels = [
    "Safe",
    "Safe",
    "Safe",
    "Safe",
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing"
]

# Train Model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# Prediction Function
def predict_phishing(text):
    X_test = vectorizer.transform([text])
    prediction = model.predict(X_test)[0]

    if prediction == "Phishing":
        return "Phishing ⚠️"
    else:
        return "Safe ✅"