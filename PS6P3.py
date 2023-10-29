#Input Phase
PrincipleAmt = float(input("Enter the principle amount: "))
MaturityYR = float(input("Enter the number of years till maturity: "))

#Processing Phase
if PrincipleAmt > 100000 and MaturityYR == 5:
  InterestRate = 0.06
elif PrincipleAmt >= 50000 and PrincipleAmt<= 100000 and MaturityYR == 10:
  InterestRate = 0.05
elif PrincipleAmt >= 50000 and PrincipleAmt <= 100000 and MaturityYR == 5:
  InterestRate = 0.04
else:
  InterestRate = 0.02
InterestAmt = PrincipleAmt * InterestRate
  
#Output Phase
print("\n\nPrinciple Amount: $", format(PrincipleAmt, ".2f"))
print("Interest Rate: ", InterestRate)
print("Interest amount for the first year: $", format(InterestAmt, ".2f"))