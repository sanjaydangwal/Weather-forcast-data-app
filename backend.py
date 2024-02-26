import requests

API_KEY = "ec0110ca7fc909123ca48c4d6ad748b3"


def get_data(place, forcast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dictionary["main"]["temp"] for dictionary in filtered_data]
    if kind == "Sky":
        filtered_data = [dictionary["weather"][0]["main"] for dictionary in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Rishikesh", forcast_days=3, kind="Sky"))
