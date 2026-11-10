temperature = int(input("What is the temperature today in celcius?"))
if temperature < 20:
    outfit = "Jacket"
    print("It is cold today")
    print("wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today")
    print("wear a", outfit)

is_raining = input("Is it raining today?  (yes/no)")
if is_raining == "yes":
    print("bring an umbrella")

windspeed = int(input("What is the wind speed km/h?"))
if windspeed > 30:
    Windbreaker = "yes"
    print("It is windy today")
    print("wear a windbreaker over your", outfit)
else:
    Windbreaker = "no"
    
    print("It is calm today")
    print("no need to wear a windbreaker over your", outfit)

print("")
print("weather check completer")

print("WEATHER OUTFIT PICKER")
print("temperature =", temperature)
print("outfit =", outfit)
print("raining =", is_raining)
print("wind breaker needed =", Windbreaker)
                   


