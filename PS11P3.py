def FunctionSalesReport(LastName, Sales):
  if Sales > 100000.00:
    Rate = 0.10
  else:
    Rate = 0.05
    
  Commission = Sales * Rate
  TargetSales = Sales * 1.05
  
  return Commission, TargetSales

LastName = input("Enter Last Name: ")
Sales = float(input("Enter Current Year Sales: "))

Commission, TargetSales = FunctionSalesReport(LastName, Sales)

print("\n\nSalesperson: ", LastName)
print("Commission: $", format(Commission, ".2f"))
print("Next Year's Target Sales: $", format(TargetSales, ".2f"))