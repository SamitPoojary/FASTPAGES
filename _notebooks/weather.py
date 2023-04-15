import requests

data = {"pm25": {}, "pm10": {}}
headers = {
    "X-RapidAPI-Key": "093c731fb9mshd2b4db3a5a833acp172c94jsn194a4fa97d9b",
    "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
}


def find_pm25(city):
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
    querystring = {"city": city}

    response = requests.get(url, headers=headers, params=querystring)
    try:
        data_json = response.json()
        pm25_concentration = data_json["PM2.5"]
        if pm25_concentration is not None:
            print(f"The PM2.5 concentration for {city} is {pm25_concentration['concentration']}")
            if pm25_concentration["concentration"] < 25:
                print("This is a safe level of air quality. Enjoy!")
            else:
                print("This is unsafe air quality. Be cautious!")
            data["pm25"][city] = pm25_concentration["concentration"]
        else:
            print(f"Sorry, there is no PM2.5 data available for {city}.")
    except:
        print("Sorry, an error occurred while processing your request.")


def find_pm10(city):
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
    querystring = {"city": city}

    response = requests.get(url, headers=headers, params=querystring)
    try:
        data_json = response.json()
        pm10_concentration = data_json["PM10"]
        if pm10_concentration is not None:
            print(f"The PM10 concentration for {city} is {pm10_concentration['concentration']}")
            if pm10_concentration["concentration"] < 25:
                print("This is a safe level of air quality. Enjoy!")
            else:
                print("This is unsafe air quality. Be cautious!")
            data["pm10"][city] = pm10_concentration["concentration"]
        else:
            print(f"Sorry, there is no PM10 data available for {city}.")
    except:
        print("Sorry, an error occurred while processing your request.")


while True:
    print("Here are your options:")
    print("1. Find PM2.5 concentration for a city")
    print("2. Find PM10 concentration for a city")
    print("3. See your stored values in a list!")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        city = input("Enter a city:  ")
        find_pm25(city)
    elif choice == "2":
        city = input("Enter a city:  ")
        find_pm10(city)
    elif choice == "3":
        print("PM2.5 values:")
        for city, pm25 in data["pm25"].items():
            print(f"{city}: {pm25}")
        print("PM10 values:")
        for city, pm10 in data["pm10"].items():
            print(f"{city}: {pm10}")
    elif choice == "4":
        break
    else:
        print("Sorry, but this isn't a valid choice. Please try again!")





