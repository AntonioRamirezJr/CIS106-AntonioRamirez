SumOfDiscAmt = 0
NoOfOrders = 0

Response = input("Do you want to calculate the total order with discount? (Yes or No) ")

while Response == "Yes":
  Qty = float(input("Enter the quantity: "))
  Price = float(input("Enter the price: "))
  ExtPrice = Qty * Price
  DiscAmt = ExtPrice * 0.25 if ExtPrice >= 10000.0001 else ExtPrice * 0.1
  TotalOrder = ExtPrice - DiscAmt
  SumOfDiscAmt = SumOfDiscAmt + DiscAmt
  NoOfOrders = NoOfOrders + 1
  print("Extended Price: $", ExtPrice)
  print("Discount Earned: $", DiscAmt)
  print("Total Order Amount: $", TotalOrder)

  Response = input("\n\nDo you want to enter another order? (Yes or No) ")

print("Total Discount Given: $", SumOfDiscAmt)
print("Total Number of Orders: ", NoOfOrders)
AvgDiscAmt = SumOfDiscAmt / NoOfOrders
print("Average Discount Earned: $", AvgDiscAmt)