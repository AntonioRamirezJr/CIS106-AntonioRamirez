#Input Phase
ItemQty = float(input("Enter the quantity of an item: "))

#Processing Phase
UnitPrice = 3.0 if ItemQty >= 1000 else 5.0
ExtendedPrice = ItemQty * UnitPrice
Tax = ExtendedPrice * 0.07
Total = Tax + ExtendedPrice

#Output Phase
print("\n\nItem Quantity: ", ItemQty)
print("Unit Price: $", format(UnitPrice, ".2f"))
print("Extended Price: $", format(ExtendedPrice, ".2f"))
print("Tax: $", format(Tax, ".2f"))
print("Total: $", format(Total, ".2f"))