File = open("EmployeeData.txt")

BonusTotalPaidOut = 0

#get the first part of the data
LastName = str(File.readline().rstrip('\n'))

while LastName != "": #detect end of file
  Salary = float(File.readline())
  if Salary >= 100000:
    BonusRate = .20
  elif Salary >= 50000 and Salary < 100000:
    BonusRate = .15
  else: 
    BonusRate = .10

  BonusAmt = Salary * BonusRate
  BonusTotalPaidOut = BonusTotalPaidOut + BonusAmt

  print("\n\nEmployee Last Name:", LastName)
  print("Salary: $", format(Salary, ".2f"))
  print("Bonus Amount: $", format(BonusAmt, ".2f"))

  LastName = str(File.readline().rstrip('\n'))

File.close()

print("\n\nSum of Bonuses Paid Out: $", format(BonusTotalPaidOut, ".2f"))