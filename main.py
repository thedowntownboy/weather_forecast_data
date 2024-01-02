import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")
# widgets are added in the home page
st.title("weather forecast for the next days")
place = st.text_input("Place :")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        # filtered data is called
        filtered_content = get_data(place, days)

        # plotly is used to render the graph as it works with streamlit
        if option == "Temperature":
            temperature = [item['main']['temp'] - 273.15 for item in filtered_content]

            dates = [item['dt_txt'] for item in filtered_content]
            figure = px.line(x=dates, y=temperature,
                             labels={"x": "date", "y": "temperature in c"})
            st.plotly_chart(figure)

        if option == "Sky":
            filtered_content = [item['weather'][0]['main'] for item in filtered_content]
            images = {"Clear": 'images/clear.png', "Clouds": 'images/cloud.png',
                      "Rain": 'images/rain.png', "Snow": 'images/snow.png'}
            image_path = [images[condition] for condition in filtered_content]
            st.image(image_path, width=115)

except KeyError:
    st.warning("The place you entered does not exist, enter valid place")
