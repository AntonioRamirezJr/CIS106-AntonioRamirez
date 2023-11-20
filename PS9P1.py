def FunctionExtPrice(Qty, UnitPrice):
  ExtPrice = Qty * UnitPrice
  
  if ExtPrice > 10000.00:
    DiscAmt = ExtPrice * 0.10
  else:
    DiscAmt = 0.00
  NewExtPrice = ExtPrice - DiscAmt
  return NewExtPrice
  
TotalExtPrice = 0.00
Response = input("Would you like to compute extended price? (Yes or No): ")

while Response == "Yes":
  Qty = float(input("Enter the quantity: "))
  UnitPrice = float(input("Enter the unit price: "))
  NewExtPrice = FunctionExtPrice(Qty, UnitPrice)
  
  TotalExtPrice = TotalExtPrice + NewExtPrice

  print("\n\nQuantity: ", Qty)
  print("Price: $", format(UnitPrice, ".2f"))
  print("Extended Price: $", format(NewExtPrice, ".2f"))

  Response = input("\n\nWould you like to compute extended price again? (Yes or No): ")

print("Total Extended Price: $", format(TotalExtPrice, ".2f"))