import streamlit as st

# st.set_page_config(layout="wide")

st.title("weather forecast for the next days")
place = st.text_input("Place :")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")
