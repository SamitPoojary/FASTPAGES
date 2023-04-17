# Importing API from RapidAPI
# Note that me and Alex Kumar collaborated on this code,  but made our own modifications to it. We planned the idea out together. 

import requests
# initializes an empty dictionary called data with two keys, "pm25" and "pm10" 
data = {"pm25": {}, "pm10": {}}
# Creates an empty list called city_list.
city_list = []
headers = {
    "X-RapidAPI-Key": "093c731fb9mshd2b4db3a5a833acp172c94jsn194a4fa97d9b",
    "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
}

# Collaborated with Alex Kumar. We made our own modifications to it regarding different dictionaries and lists, but the idea is the same - to find the PM2.5 concentration
def find_pm25(city):
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
    querystring = {"city": city}

    response = requests.get(url, headers=headers, params=querystring)
    try:
        data_json = response.json()
        pm25_concentration = data_json["PM2.5"]
        # Below, we are checking if the value of pm25_concentration is not equal to None. If it is not None, it means that the API has returned a value for the PM2.5 concentration for the given city, and the code proceeds to print the PM2.5 concentration value for that city
        if pm25_concentration is not None:
            print(f"The PM2.5 concentration for {city} is {pm25_concentration['concentration']}")
            if pm25_concentration["concentration"] < 25:
                print("This is a safe level of air quality. Enjoy!")
            else:
                print("This is unsafe air quality. Be cautious!")
            data["pm25"][city] = pm25_concentration["concentration"]
            city_list.append(city)
        # If no data is available for the entered city
        else:
            print(f"Sorry, there is no PM2.5 data available for {city}.")
    # If some other error occurred 
    except:
        print("Sorry, an error occurred while processing your request.")

# Again, collaborated with Alex Kumar. We made our own modifications to it regarding different dictionaries and lists, but the idea is the same - to find the PM10 concentration

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
            city_list.append(city)
        else:
            print(f"Sorry, there is no PM10 data available for {city}.")
    except:
        print("Sorry, an error occurred while processing your request.")

# This while loop was worked on collaboratively by myself and Alex Kumar. We both then made our own modifications to the code, but the idea was mutual. 
# The purpose of the following is to provide a list of options that continues to loop over and over, allowing the user to make multiple choices before they exit.
while True:
    print("Here are your options:")
    print("1. Find PM2.5 concentration for a city")
    print("2. Find PM10 concentration for a city")
    print("3. See all your results so far")
    print("4. See just your city list so far")
    print("5. Exit")
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        city = input("Enter a city:  ")
        find_pm25(city)
    elif choice == "2":
        city = input("Enter a city:  ")
        find_pm10(city)
    # Here we are printing out PM2.5 and PM10 concentration values for each city in the user's data, along with a message on the safety of the air quality based on the concentration level. 
    elif choice == "3":
        print("PM2.5 values:")
        for city, pm25 in data["pm25"].items():
            safe_or_not = "safe" if pm25 < 25 else "unsafe"
            print(f"{city}: {pm25} ({safe_or_not})")
        print("PM10 values:")
        for city, pm10 in data["pm10"].items():
            safe_or_not = "safe" if pm10 < 25 else "unsafe"
            print(f"{city}: {pm10} ({safe_or_not})")
    elif choice == "4":
        print("City list:")
        for item in city_list:
            city_name = item.split(":")[0]
            print(city_name)
    # Here for choice 5, I give full credit to Alex Kumar for writing the code. 
    elif choice == "5":
        break
    else:
        print("Sorry, but this isn't a valid choice. Please try again!")






