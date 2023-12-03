def FunctionDiscount(Quantity, UnitPrice, DiscRate):
  ExtendedPrice = Quantity * UnitPrice
  DiscAmt = ExtendedPrice * DiscRate
  DisPrice = ExtendedPrice - DiscAmt

  return DiscAmt, DisPrice


Quantity = float(input("Enter the quantity: "))
UnitPrice = float(input("Enter the unit price: "))
DiscRate = float(input("Enter the discount rate: "))

DiscAmt, DiscPrice = FunctionDiscount(Quantity, UnitPrice, DiscRate)

print("\n\nQuantity: ", Quantity)
print("Unit Price: $", format(UnitPrice, ",.2f"))
print("Discount Amount: $", format(DiscAmt, ",.2f"))
print("Discounted Price: $", format(DiscPrice, ",.2f"))