#Input Phase
Lname = input("Enter the employee's last name: ")
Salary = float(input("Enter the employee's salary: "))
JobLevel = int(input("Enter the employee's job level: "))

#Processing Phase
if JobLevel >= 10:
  BonusRate = 0.25
elif JobLevel <= 9 and JobLevel >= 5:
  BonusRate = 0.20
else:
  BonusRate = 0.10
BonusAmt = Salary * BonusRate

#Output Phase
print("Employee Last Name: ", Lname)
print("Employee Bonus Amount: ", format(BonusAmt, ".2f"))