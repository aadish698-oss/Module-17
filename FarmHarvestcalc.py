#Farm harvest calculator
# Assignment Operator

Field1 = 200
Field2 = 135
Field3 = 75
Field4 = 158
Field5 = 193

total = Field1 + Field2 + Field3 + Field4 + Field5
print("Total Harvest : " , total, "Kg")

Average = total/5
print("Total Average : " , Average, "Kg")

price_per_kg = 15
earnings = total * price_per_kg
print("Total Earnings : ", earnings, "Rs")

bags = total // 25
leftover = total % 25

print("Total bags :", bags)
print(" Total Left over grains :", leftover, "kg")

#Compare this years harvest with last years
last_year = 761
print("better than last year? :", total>last_year)
print("same as last year? :", total==last_year)
print("At least as good? :", total>=last_year)

#assignment operator
total += 30
print("after bonus crop : ", total, "kg")

#subtract 15kg from the total
total -= 15
print("after seeds reserved : ", total, "kg")

#final bag count
bags = total // 25
print("Final bags packed : ", bags, "kg")