import pandas as pd
import pickle

# load saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def count_caps(text):
    return sum(1 for c in text if c.isupper())

def predict_spam(sender, subject, body):
    f_sender_len = len(sender)
    f_subject_caps = count_caps(subject)

    f_text = vectorizer.transform([body]).toarray()
    f_text_df = pd.DataFrame(
        f_text,
        columns=vectorizer.get_feature_names_out()
    )

    input_data = pd.DataFrame(
        [[f_sender_len, f_subject_caps]],
        columns=['sender_length', 'subject_caps_count']
    )

    final_input = pd.concat([input_data, f_text_df], axis=1)

    prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)[0][1]

    return {
        "result": "SPAM" if prediction == 1 else "HAM (Safe)",
        "confidence": round(probability, 2)
    }
