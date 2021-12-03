import streamlit as st
from textblob import TextBlob
input = st.text_input("Enter Your Review...")
score = TextBlob(input).sentiment.polarity
if score==0:st.write("Neutral")
elif score<0:st.write("Negative")
elif score>0:st.write("Positive")