#Input Phase
TotalMealCost = float(input("Please enter the total cost of the meal: "))

#Process Phase
FifteenTipValue = TotalMealCost * 0.15
TotFifteenTip = TotalMealCost + FifteenTipValue
EighteenTipValue = TotalMealCost * 0.18
TotEighteenTip = TotalMealCost + EighteenTipValue
TwentyTipValue = TotalMealCost * 0.20
TotTwentyTip = TotalMealCost + TwentyTipValue

#Output Phase
print("\n\nWith 15% Tip: ")
print("Total: ", TotalMealCost)
print("Tip: ", FifteenTipValue)
print("Total With Tip: ", TotFifteenTip)

print("\n\nWith 18% Tip:")
print("Total: ", TotalMealCost)
print("Tip: ", EighteenTipValue)
print("Total With Tip: ", TotEighteenTip)

print("\n\nWith 20% Tip: ")
print("Total: ", TotalMealCost)
print("Tip: ", TwentyTipValue)
print("Total With Tip: ", TotTwentyTip)