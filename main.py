import streamlit as st
import plotly.express as px

# st.set_page_config(layout="wide")

st.title("weather forecast for the next days")
place = st.text_input("Place :")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")


# fake data
def get_data(days):
    date = ['11-08-2023', '12-08-2023', '13-08-2023']
    temperature = [19, 17, 25]
    temperature = [days * i for i in temperature]
    return date, temperature


d, t = get_data(days)
# plotly is used to render the graph as it works with streamlit
figure = px.line(x=d, y=t, labels={"x": "date", "y": "temperature in c"})
st.plotly_chart(figure)
