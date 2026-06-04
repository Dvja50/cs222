import requests


def get_muncie_forecast():
    headers = {"User-Agent": "(myweatherapp.com, contact@example.com)"}
    points_url = "https://api.weather.gov/points/40.1934,-85.3864"
    print(f"Fetching metadata from: {points_url}...\n")

    try:
        response = requests.get(points_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        forecast_url = data["properties"]["forecast"]

        print(f"Fetching forecast from: {forecast_url}...\n")
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        periods = forecast_data["properties"]["periods"]

        print("-" * 60)
        print("7-DAY FORECAST FOR MUNCIE, IN")
        print("-" * 60)

        for period in periods:
            name = period.get("name")
            temperature = period.get("temperature")
            temperature_unit = period.get("temperatureUnit", "F")
            detailed_forecast = period.get("detailedForecast")

            print(f"Period: {name}")
            print(f"Temperature: {temperature}°{temperature_unit}")
            print(f"Forecast: {detailed_forecast}")
            print("-" * 60)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")


if __name__ == "__main__":
    get_muncie_forecast()