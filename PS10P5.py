def FunctionAssessedValue(County, MarketValue):
  if County == "Cook":
    Percent = 0.90
  elif County == "DuPage":
    Percent = 0.80
  elif County == "McHenry":
    Percent = 0.75
  elif County == "Kane":
    Percent = 0.60
  else:
    Percent = 0.70

  AssessedValue = MarketValue * Percent

  return MarketValue, AssessedValue

SumOfMarketValues = 0
SumOfAssessedValues = 0

Response = input("Would you like to calculate the assessed value of a property? (Yes or No) ")

while Response == "Yes":
  County = input("\n\nEnter the county: ")
  MarketValue = float(input("Enter the market value: "))

  MarketValue, AssessedValue = FunctionAssessedValue(County, MarketValue)

  SumOfMarketValues = SumOfMarketValues + MarketValue
  SumOfAssessedValues = SumOfAssessedValues + AssessedValue

  print("Assessed Value: $", format(AssessedValue, ".2f"))

  Response = input("\n\nWould you like to calculate the assessed value of another property? (Yes or No) " )

print("\n\nSum of all Market values: $", format(SumOfMarketValues, ".2f"))
print("Sum of all Assessed values: $", format(SumOfAssessedValues, ".2f"))