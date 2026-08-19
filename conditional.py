
temperature = int(input("Enter today's temerature in celsius:  "))
if temperature < 20: 
    print("It is cold today.")
else:
    print("It is warm today")


is_raining = input("Is it raining today? (yes/no): ")
if is_raining == "yes":
    print("Bring an umbrella!")
else:
    print ("DOnt bring umbrella")

wind_speed = int(input("Enter the wind speed in km/h: "))
if wind_speed > 30:
    print("It is windy today.")
else:

    print("It is calm today.")