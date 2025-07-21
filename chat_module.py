# chat_module.py
import pickle
import os

model_path = "models/chat_model.pkl"
vectorizer_path = "models/vectorizer.pkl"

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
else:
    model = None
    vectorizer = None

def predict_depression(text):
    if not model or not vectorizer:
        return "Model not loaded", 0.0
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X).max()
    return pred, round(prob, 2)
