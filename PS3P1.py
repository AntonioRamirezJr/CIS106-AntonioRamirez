#Input Phase
StockTckr = input("Enter stock ticker symbol: ")
SharesQTY = float(input("Enter quantity of shares: "))
SharePrice = float(input("Enter price per share: "))

#Process Phase
AmtInvested = SharesQTY * SharePrice

#Output Phase
print("Stock Ticker Symbol: ", StockTckr)
print("Amount Invested: ", AmtInvested)