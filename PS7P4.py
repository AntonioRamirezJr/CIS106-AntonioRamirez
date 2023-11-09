NumOfEmployees = 0
SumOfGrossPay = 0

Response = input("Would you like to calculate employee gross pay? (Yes or No) ")

while Response == "Yes":
  Lname = input("\n\nEnter employee's last name: ")
  HoursWorked = float(input("Enter the amount of hours worked: "))
  PayRate = float(input("Enter the employee's pay rate: "))
  if float(HoursWorked) >= 40.0:
    GrossPay = (40.0 * PayRate) + ((HoursWorked - 40.0) * PayRate * 1.5)
  else: GrossPay = HoursWorked * PayRate
  print("Employee Last Name: ", Lname)
  print("Gross Pay: $", GrossPay)
  SumOfGrossPay = SumOfGrossPay + GrossPay
  NumOfEmployees = NumOfEmployees + 1

  Response = input("\n\nWould you like to calculate another employee's gross pay? (Yes or No) ")

AvgGrossPay = SumOfGrossPay / NumOfEmployees
print("Sum of all Gross Pay: $" , SumOfGrossPay)
print("Number of employees entered: ", NumOfEmployees)
print("Average Gross Pay: $", AvgGrossPay)