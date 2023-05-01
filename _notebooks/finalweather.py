# Credit to Rapid API for the headers, as well as providing data from the API to be used in this code

# Note: I collaborated on this project with Alex Kumar and the code is shared, although we have made some slight adjustments for ourselves. 

import requests

stored_data = {'pm2.5': {}, 'pm10': {}}

def find_pm(type, city):
    if type == "pm25":
        url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
        querystring = {"city": city}
        headers = {
            "X-RapidAPI-Key": "f8c1edc71amsh2ceb94e75170cf3p1172ddjsn28d9990da6a6",
            "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        pm25_concentration = data["PM2.5"]["concentration"]

        print(f"PM2.5 concentration for {city} is {pm25_concentration}")
        if pm25_concentration < 25:
            print("This is a safe level of pollution")
        else:
            print("This is unsafe")

        if city in stored_data['pm2.5']:
            print(f"{city} already exists in the PM2.5 dictionary")
        else:
            stored_data['pm2.5'][city] = pm25_concentration
            print(f"{city} added to the PM2.5 dictionary")

    elif type == "pm10":
        url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
        querystring = {"city": city}
        headers = {
            "X-RapidAPI-Key": "f8c1edc71amsh2ceb94e75170cf3p1172ddjsn28d9990da6a6",
            "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        pm10_concentration = data["PM10"]["concentration"]

        print(f"PM10 concentration for {city} is {pm10_concentration}")
        if pm10_concentration < 25:
            print("This is a safe level of pollution")
        else:
            print("This is unsafe")

        if city in stored_data['pm10']:
            print(f"{city} already exists in the PM10 dictionary")
        else:
            stored_data['pm10'][city] = pm10_concentration
            print(f"{city} added to the PM10 dictionary")

while True:
    print("Here are your options:")
    print("1. Find the PM2.5 concentration for a city")
    print("2. Find the PM10 concentration for a city")
    print("3. Here is your list of stored PM2.5 values")
    print("4. Here is your list of stored PM10 values")
    print("5. Exit")
    

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        city = input("Enter city name: ")
        find_pm("pm25", city)
    elif choice == "2":
        city = input("Enter city name: ")
        find_pm("pm10", city)
    elif choice == "3":
        pm25_data = stored_data['pm2.5']
        for city, pm in pm25_data.items():
            print(city, pm)
    elif choice == "4":
        pm10_data = stored_data['pm10']
        for city, pm in pm10_data.items():
            print (city,pm)
    elif choice == "5":
        break
    else:
        ("This was not a valid choice. Please try again.")
