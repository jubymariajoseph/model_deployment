
import streamlit as st
import pickle

st.title("Iris Dataset Collection")
st.header("Enter the measurements")

# Load the trained model
model = pickle.load(open("model_final.pkl", 'rb'))

# User inputs
sl = st.number_input("Sepal length")
sw = st.number_input("Sepal width")
pl = st.number_input("Petal length")
pw = st.number_input("Petal width")

# Predict button
if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    st.success(f"Predicted species: {prediction[0]}")

