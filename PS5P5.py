#Input Phase
Lname = input("Enter your last name: ")
DependentsAmt = float(input("Enter the number of dependents: "))
GrossIncome = float(input("Enter your gross income: "))

#Processing Phase
AdjustedGrossInc = GrossIncome - (DependentsAmt * 12000)
TaxRate = 0.20 if AdjustedGrossInc > 50000 else 0.10
IncomeTax = AdjustedGrossInc * TaxRate
if IncomeTax < 0: IncomeTax = 100

#Output Phase
print("\n\nLast Name: ", Lname)
print("Gross Income: $", format(GrossIncome, ".2f"))
print("Number of Dependents: ", DependentsAmt)
print("Adjusted Gross Income: $",format(AdjustedGrossInc, ".2f"))
print("IncomeTax: $", format(IncomeTax, ".2f"))