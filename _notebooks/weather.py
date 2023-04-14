import requests
datalist = []


def findpm25(city):
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"

    
    querystring = {"city": city}

    headers = {
	"X-RapidAPI-Key": "093c731fb9mshd2b4db3a5a833acp172c94jsn194a4fa97d9b",
	"X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    pm25_concentration = data["PM2.5"]
    print("The pm25 concentration for " +str(city) + " is " + str(pm25_concentration["concentration"]))

    if pm25_concentration["concentration"] < 25:
        print("This is a safe level of pollution")
    else: 
        print("This is unsafe")


    datalist.append(pm25_concentration["concentration"])


def findpm10(city):
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"

    querystring = {"city": city}

    headers = {
	"X-RapidAPI-Key": "093c731fb9mshd2b4db3a5a833acp172c94jsn194a4fa97d9b",
	"X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    pm10_concentration = data["PM2.5"]
    print("The pm10 concentration for " +str(city) + " is " + str(pm10_concentration["concentration"]))

    if pm10_concentration["concentration"] < 25:
        print("This is a safe level of pollution")
    else: 
        print("This is unsafe")


    datalist.append(pm10_concentration["concentration"])

while True:
    print("Menu:")
    print("1. Find PM2.5 concentration for a city")
    print("2. Find PM10 concentration for a city")
    print("3. See your stored values in a list!")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        city = input("Enter a city:  ")
        findpm25(city)
    elif choice == "2": 
        city = input("Enter a city:  ")
        findpm10(city)

    elif choice == "3":
        print(datalist)

    elif choice == "4":
        break
    else:
        print("Sorry, but this isn't a valid choice. Please try again!")


