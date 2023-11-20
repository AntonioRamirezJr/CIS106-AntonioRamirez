def FunctionPayRate(Code):
  if Code == "L":
    PayRate = 25.00
  elif Code == "A":
    PayRate = 30.00
  else:
    PayRate = 50.00

  return PayRate

TotalGrossPays = 0.0

Response = input("Would you like to calculate gross pay? (Yes or No): ")

while Response == "Yes":
  LastName = input("Enter Last Name: ")
  Code = input("Enter the Job Code: ")
  Hours = float(input("Enter the amount of hours worked: "))

  PayRate = FunctionPayRate(Code)

  if Hours > 40.0:
    GrossPay = PayRate * (Hours - 40.0) * 1.5 + PayRate * 40.0
  else: 
    GrossPay = PayRate * Hours

  TotalGrossPays = TotalGrossPays + GrossPay

  print("\n\nLast Name: ", LastName)
  print("Gross Pay: $", format(GrossPay, ".2f"))

  Response = input("\n\nWould you like to calculate another gross pay? (Yes or No): ")

print("Sum of all gross pay: $", format(TotalGrossPays, ".2f"))