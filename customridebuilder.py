print("======= Welcome to Ride Builder? =======")

print("step 1: Pick your vehicle")
print("1 - Bike")
print("2 - Car")

choice = int(input("Enter 1 or 2:"))

if choice == 1:
    print("Step 2 pick your bike type")
    print("  1 -  scooty")
    print("  2 - Mountain bike ")
    bike_type = int(input("Enter 1 or 2:"))

    if bike_type == 1:
        print("You chose : scooter")
        print("top speed : 80km/h")
        print("Best for : city roads")
    else:
        print("You chose : Mountain Bike")
        print("top speed : 50km/h")
        print("Best for : off road trails")
elif choice == 2:
    print("Step 2 pick your car type")
    print("  1 -  Sedan")
    print("  2 - Suv ")
    car_type = int(input("Enter 1 or 2:"))
    if car_type == 1:
        print("you picked : Sedan")
        print("Seat : 5 passengers")
        print("Best for : family trips")
    else:
        print("You picked : SUV")
        print("Seat : 7 passengers")
        print("Best for : off road adventures")

else:
    print("That wasn't a valid choice")
    print("Please enter the nmber 1 for bike or 2 for car")

print("======Your Custom ride is ready! Go enjoy======")
     



    
    