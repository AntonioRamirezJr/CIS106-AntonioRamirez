#Input Phase
Make = input("Enter the make of the car: ")
Model = input("Enter the model of the car: ")
MSRP = float(input("Enter the MSRP of the car: "))
DiscPercent = float(input("Enter the discount percent: "))

#Process Phase
AmountOffMSRP = MSRP * DiscPercent
DiscPrice = MSRP - AmountOffMSRP

#Output Phase
print("Make: ", Make)
print("Model: ", Model)
print("MSRP: $", MSRP)
print("Discount Percent: ", DiscPercent)
print("Amount Off MSRP: $", AmountOffMSRP)
print("Discounted Price: $", DiscPrice)