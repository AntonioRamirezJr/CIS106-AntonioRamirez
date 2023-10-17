#Input Phase
FixedCosts = float(input("Enter the amount of fixed costs: "))
PricePerUnit = float(input("Enter the price per unit: "))
CostPerUnit = float(input("Enter the cost per unit: "))

#Process Phase
BEpoint = (FixedCosts) / (PricePerUnit - CostPerUnit)

#Output Phase
print("\n\nThe break-even point, or the amount of items that you must sell to cover your overhead expenses, is: ", BEpoint, "Units")