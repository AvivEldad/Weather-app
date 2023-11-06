import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Whether forcast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forcast days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temps = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temps, labels={"x": "Dates", "y": "Temperatures"})
            st.plotly_chart(figure)

        else:
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            images_path = [images[condition] for condition in filtered_data]
            st.image(images_path, width=115)
    except KeyError:
        st.write("That place does not exist")
