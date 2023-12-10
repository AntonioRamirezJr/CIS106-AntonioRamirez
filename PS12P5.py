def loadarrays(LastName, Salary):
  f = open("EmployeeData.txt", "r")
  for i in range (0, 10, 1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    LastName.append(ln)
    S = f.readline()
    S.rstrip("\n")
    Salary.append(float(S))
  
  f.close()


def darrays(LastName, Salary):
  for i in range (0, 10, 1):
    print(LastName[i], "Salary: $", Salary[i])


def rdisplay(LastName, Salary):
  for i in range (9, -1, -1):
    print(LastName[i], "Salary: $", Salary[i])


def hilow(LastName, Salary):
  hiSalary = 0.0
  hisub = 0.0
  loSalary = 999999999.99
  losub = 0.0

  for i in range (0, 10, 1):
    if Salary[i] > hiSalary:
      hiSalary = Salary[i]
      hisub = i
    elif Salary[i] < loSalary:
      loSalary = Salary[i]
      losub = i

  print("")
  print(LastName[hisub], "has the HIGHEST salary: $", Salary[hisub])
  print(LastName[losub], "has the LOWEST salary: $", Salary[losub])


def FunctionTotalSalaries(Salary):
  TotalSalaries = 0.0
  for i in range (0, 10, 1):
    TotalSalaries = TotalSalaries + Salary[i]
  
  print("\n\nSum of all employee salaries: $", TotalSalaries)


def searchLastName(LastName, Salary, NameSearch):
  foundsub = -1

  for i in range (0, 10, 1):
    if LastName[i] == NameSearch:
      foundsub = i

  if foundsub == -1:
    print(NameSearch, "= EMPLOYEE NOT FOUND")
  else:
    print(LastName[foundsub], "Salary: $", Salary[foundsub])


LastName = []
Salary = []

loadarrays(LastName, Salary)
darrays(LastName, Salary)
print("\n\nREVERSE ORDER\n\n")
rdisplay(LastName, Salary)
hilow(LastName, Salary)
FunctionTotalSalaries(Salary)

Response = input("\n\nDo you want to search an employee's salary? (Yes or No) ")

while Response == "Yes":
  NameSearch = input("Enter employee last name: ")
  searchLastName(LastName, Salary, NameSearch)
  Response = input("\n\nWould you like to search for another salary? (Yes or No) ")