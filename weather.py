import streamlit as st
import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = '9db8807c88b77730a57c41198b426165'  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Streamlit app layout
def main():
    st.title("Weather Forecast Application")

    # Input field for the user to enter the city
    city = st.text_input("Enter City Name", "")

    if city:
        weather_data = get_weather(city)

        if weather_data:
            st.subheader(f"Weather in {city.capitalize()}")

            # Extract relevant weather data
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']

            # Display the weather information
            st.write(f"**Temperature:** {temp} °C")
            st.write(f"**Humidity:** {humidity} %")
            st.write(f"**Wind Speed:** {wind_speed} m/s")
            st.write(f"**Description:** {description.capitalize()}")

            # Optionally, you can add icons or other enhancements
        else:
            st.error("City not found or unable to retrieve data.")
    else:
        st.write("Enter a city name to get the weather forecast.")

if __name__ == "__main__":
    main()
