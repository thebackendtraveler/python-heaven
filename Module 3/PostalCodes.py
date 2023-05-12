postal_codes = {
    1444: "Oslo", 
    2201: "Hedmark",
    3001: "Buskerud",
    3060: "Vestfold",
    3999: "Telemark", 
    4400: "Vest-Agder", 
    5003: "Hordaland",
    8001: "Nordland", 
    9006: "Troms", 
    9501: "Finnmark"
}

user_code =  int(input("Please input a postal code: "))

if user_code in postal_codes:
    print("The city is ", postal_codes[user_code])
else: 
    print("The postal code does not exist in our list")