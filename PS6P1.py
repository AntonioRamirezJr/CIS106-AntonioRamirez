#Input Phase
WidgetsQty = float(input("Enter the quantity of widgets: "))

#Processing Phase
if WidgetsQty > 10000: 
  UnitPrice = 10.00
elif WidgetsQty >= 5000 and WidgetsQty <= 10000: 
  UnitPrice = 20.00
else:
  UnitPrice = 30.00

ExtendedPrice = WidgetsQty * UnitPrice
Tax = ExtendedPrice * 0.07
Total = Tax + ExtendedPrice

#Output Phase
print("\n\nExtended Price: $", format(ExtendedPrice, ".2f"))
print("Tax: $", format(Tax, ".2f"))
print("Total: $", format(Total, ".2f"))