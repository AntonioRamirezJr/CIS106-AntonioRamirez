Total = 0.00
Tax = 0.00

def ComputeTotal(Quantity, Price):
  global Total 
  Total = Quantity * Price
  global Tax 
  Tax = Total * 0.07

Quantity = float(input("Enter Quantity: "))
Price = float(input("Enter Price: "))
ComputeTotal(Quantity, Price)

print("\n\nTotal: $", format(Total, ".2f"))
print("Tax: $", format(Tax, ".2f"))