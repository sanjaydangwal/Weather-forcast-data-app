import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Next Days.")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of forecasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

if place:
    # Get the Temperature/sky data.
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dictionary["main"]["temp"]/10 for dictionary in filtered_data]
            dates = [dictionary["dt_txt"] for dictionary in filtered_data]
            # Plot temperature figure
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            sky_conditions = [dictionary["weather"][0]["main"] for dictionary in filtered_data]
            print(sky_conditions)
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=150)
    except KeyError:
        st.write("That place does not exist.")
