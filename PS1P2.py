#Input Phase
PurchPricePerShare = float(input("Enter the Purchase Price per Share: "))
CurrStockPrice = float(input("Enter the Current Stock Price: "))
StockQty = float(input("Enter the Quantity of Stock: "))

#Process Phase
NetValue = (CurrStockPrice - PurchPricePerShare) * (StockQty)

#Output Phase
print("The Net Value for the current shares on hand is: $ ", NetValue)