import requests
import streamlit as st
import json

st.set_page_config(page_title="Weather Application", layout="centered")
st.title("☀️ Weather Application")

st.image("image.jpg", use_column_width=True)

st.markdown("Get real-time weather updates by selecting your state and city.")

with open('data.json', 'r') as file:
    data=json.load(file)

states=data.keys()

city_name=""

st.subheader("📍 Select the State")
state_name=st.selectbox(label="State",options=states)


if state_name:
    cities=data[state_name]
    st.subheader("🏙️ Select the City")
    city_name=st.selectbox(label="City",options=cities)

if st.button("🔍 Get Weather"):
    if city_name:
        api_key = "18354fa1a280a6aa7297561888e0c980"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_name}&appid={api_key}&units=metric"

        response=requests.get(url)

        if response.status_code == 200:
            data=response.json()
            st.write(f"✅ Current Weather Condition: {data['weather'][0]['main']}.")
            st.write(f"🌡 Current Temperature: {data['main']['temp']}°C.")
            st.write(f"🤗 Current Temperature Feels Like: {data['main']['feels_like']}°C.")
            st.write(f"💧 Humidity: {data['main']['humidity']}%.")
        else:
            st.error("Error Occured. Please check the City Name or the State Name is correct or not.")
    else:
        st.warning("Please select a city first.")
