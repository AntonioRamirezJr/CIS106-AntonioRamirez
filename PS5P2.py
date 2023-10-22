#Input Phase
Item = (input("Enter Item (A or B): "))
Qty = float(input("Enter the item quantity: "))

#Processing Phase
UnitPrice = 10.0 if Item == "A" else 20.0
ExtPrice = Qty * UnitPrice

#Output Phase
print("\n\nItem: ", Item)
print("Unit Price: $", format(UnitPrice, ".2f"))
print("Extended Price: $", format(ExtPrice, ".2f"))