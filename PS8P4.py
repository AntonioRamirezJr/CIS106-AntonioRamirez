File = open("ToolOrderForm.txt")

NumOfOrders = 0
SumOfExtPrices = 0

#get the first part of the data
Item = str(File.readline().rstrip('\n'))

while Item != "": #detect end of file
  Quantity = float(File.readline())
  Price = float(File.readline())
  
  ExtendedPrice = Quantity * Price
  NumOfOrders = NumOfOrders + 1
  SumOfExtPrices = SumOfExtPrices + ExtendedPrice
  AvgOrder = SumOfExtPrices / NumOfOrders
  
  print("\n\nItem:", Item)
  print("Quantity:", Quantity)
  print("Price: $", format(Price, ".2f"))
  print("Extended Price: $", format(ExtendedPrice, ".2f"))

  Item = str(File.readline().rstrip('\n'))

File.close()

print("\n\nSum Of Extended Prices: $", format(SumOfExtPrices, ".2f"))
print("Number of Orders: ", NumOfOrders)
print("Average Order Price: $", format(AvgOrder, ".2f"))