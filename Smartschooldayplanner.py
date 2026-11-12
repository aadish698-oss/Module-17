print("---Smart School Day Planner---")
print("answer 3 qucik quick questions and i'll plan your day")

day = input("What day is it? (monday to sunday):" ).strip().capitalize()
weather = input("What is the weather (sunny/rainy/cloudy):").strip().lower()
homework = input( "is your homework done? (yes/no):").strip().lower()

print()
print(f"===your plane for {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day type  : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type   : First day of the week. Pack your weekly planner."  )
elif day == "Friday":
    print("Day type   : Last school day. Return Library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type  : Regular school day. Stay focused")
else:
    print("Day type  : Day not recognised - please check the spellings")

if weather == "sunny" and homework == "yes":
    print("After school : head to the park - great weacther and homeowrk is done>")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella it may get wet outisde")

if not (homework == "yes"):
    print("Homework : not done yet finish it before going out")

if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in and finish your HW!")
elif weather == "sunny" and homework == "yes" and not (day in("Saturday", "Sunday")):
    print("best plan all set for a great school day")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan: Head outside and have fun")
else:
    print("Best plan: Take it once step at a time!")

print()
print("Plan complete! Have wonderful day")


      