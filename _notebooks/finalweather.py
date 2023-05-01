# Credit to Rapid API for the the headers and code to retrieve data from the API
# Note: collaboration with Samit Poojary on the idea and some coding is shared.
import requests
storeddata = [{'pm2.5': {}}, {'pm10': {}}]
# API call that adds the pm25 to the list
def findpm(type, city):
    if (type == "pm25"):
        url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"

        querystring = {"city": city}

        headers = {
            "X-RapidAPI-Key": "f8c1edc71amsh2ceb94e75170cf3p1172ddjsn28d9990da6a6",
            "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        pm25_concentration = data["PM2.5"]
        print("pm25_concentration for " + str(city) + " is " +  str(pm25_concentration["concentration"]))

        if pm25_concentration["concentration"] < 25:
            print("This is a safe level of pollution")
        else: 
            print("This is unsafe")
        if city in storeddata[0]['pm2.5']:
            print(f"{city} already exists in pm2.5 dictionary")
        else:
            storeddata[0]['pm2.5'][city] = pm25_concentration["concentration"]
            print(f"{city} added to pm2.5 dictionary")
            
    # checks to see what type
    elif (type == "pm10"): 
        # Credit to Rapid API for the the headers and code to retrieve data from the API
        url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"

        querystring = {"city": city}

        headers = {
            "X-RapidAPI-Key": "f8c1edc71amsh2ceb94e75170cf3p1172ddjsn28d9990da6a6",
            "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        pm10_concentration = data["PM2.5"]
        print("pm10_concentration for " + str(city) + " is " +  str(pm10_concentration["concentration"]))

        if pm10_concentration["concentration"] < 25:
            print("This is a safe level of pollution")
        else: 
            print("This is unsafe")

        # This adds the data to the list of stored values
        if city in storeddata[1]['pm10']:
            print(f"{city} already exists in pm2.5 dictionary")
        else:
            storeddata[1]['pm10'][city] = pm10_concentration["concentration"]
            print(f"{city} added to pm10 dictionary")

# Menu function that will continue to loop over the choices allowing user to do menu multiple times
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
        findpm("pm25", city)
    elif choice == "2":
        city = input("Enter city name: ")

        findpm("pm10", city)
        
    elif choice == "3":
        pm25data = storeddata[0]['pm2.5']
        for city, pm in pm25data.items():
            print(city, pm)
        
    
    elif choice == "4":
        pm10data = storeddata[1]['pm10']
        for city, pm in pm10data.items():
            print(city, pm)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")