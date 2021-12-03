import streamlit as st
from textblob import TextBlob
input = st.text_input("Enter your review and press enter")
score = TextBlob(input).sentiment.polarity
if score>0.15:st.write("Positive")
elif score<-0.15:st.write("Negative")
else:st.write("Neutral")
