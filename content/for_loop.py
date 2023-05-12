cars = ["audi", "bmw", "hongqi", "toyota", "mercedes", "volvo"]
country = ["germany", "sweden", "japan", "netherland", "italia", "spain"]

for car in cars:
    print("The name of the car is: ", car)
    if car == "toyota":
        print("The loop has stopped")
        break
        

for x in cars:
    for y in country:
        print(x,y)
        