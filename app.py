import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.title("Email Spam Classifier")

message = st.text_area("Enter Email Message")

if st.button("Predict"):

    data = vectorizer.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Spam Email")
    else:
        st.success("Not Spam")
