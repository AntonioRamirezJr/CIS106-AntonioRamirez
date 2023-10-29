#Input Phase
PartNum = input("Enter the Part Number: ")
Qty = float(input("Enter the Quantity: "))

#Processing Phase
if PartNum == "10" or PartNum == "55":
  UnitCost = 1.00
elif PartNum == "99":
  UnitCost = 2.00
elif PartNum == "80" or PartNum == "70":
  UnitCost = 3.00
else: 
  UnitCost = 5.00
TotalCost = UnitCost * Qty

#Ouput Phase
print("\n\nPart Number: ", PartNum)
print("Cost per Unit: $", format(UnitCost, ".2f"))
print("Total Cost: $", format(TotalCost, ".2f"))