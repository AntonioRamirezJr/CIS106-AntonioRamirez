def FunctionCarTotalPrice(Make, Model, EVCode, MSRP):
  if Make == "Honda" and Model == "Accord" and EVCode == "N":
    PercentOff = 0.10
  elif Make == "Toyota" and Model == "Rav4" and EVCode == "N":
    PercentOff = 0.15
  elif EVCode == "Y":
    PercentOff = 0.30
  else:
    PercentOff = 0.05

  NewMSRP = MSRP - (MSRP * PercentOff)
  CarTotalPrice = NewMSRP + (NewMSRP * 0.07)

  return CarTotalPrice

SumOfAllSales = 0 
SumOfAllMSRP = 0
Response = input("Would you like to compute the total price of a car? (Yes or No) " )

while Response == "Yes":
  Make = input("\n\nEnter the Make: ")
  Model = input("Enter the Model: ")
  EVCode = input("Enter the Electric Vehicle Code (Y or N): ")
  MSRP = float(input("Enter the MSRP: "))

  CarTotalPrice = FunctionCarTotalPrice(Make, Model, EVCode, MSRP)
  SumOfAllMSRP = SumOfAllMSRP + MSRP
  SumOfAllSales = SumOfAllSales + CarTotalPrice

  print("Total price of the car: $", format(CarTotalPrice, ".2f"))

  Response = input("\n\nWould you like to calculate the total for another car? (Yes or No) ")


print("\n\nSum of all MSRPs: $", format(SumOfAllMSRP, ".2f"))
print("Sum of all Sales: $", format(SumOfAllSales, ".2f"))