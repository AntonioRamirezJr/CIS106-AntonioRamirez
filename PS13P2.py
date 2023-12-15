class Student:
  
  def __init__(self, FirstName, LastName, District, Credits):
    self.FirstName = FirstName
    self.LastName = LastName
    self.District = District
    self.Credits = Credits

  def TuitionRate(self, District, Credits):
    if self.District == "I":
      TuitionRate = 250.00
    else:
      TuitionRate = 500.00
  
    TuitionCost = TuitionRate * Credits
    return TuitionCost

Student1 = Student("Kevin", "Durant", "I", 10)
Student2 = Student("Luka", "Doncic", "O", 12)
Student3 = Student("Stephen", "Curry", "I", 14)


print("Student Tuition Data:\n")
print("First Name: ", Student1.FirstName)
print("Last Name: ", Student1.LastName)
print("Tuition Owed: $", format(Student1.TuitionRate(Student1.District, Student1.Credits), ",.2f"))

print("\n\nFirst Name: ", Student2.FirstName)
print("Last Name: ", Student2.LastName)
print("Tuition Owed: $", format(Student2.TuitionRate(Student2.District, Student2.Credits), ",.2f"))

print("\n\nFirst Name: ", Student3.FirstName)
print("Last Name: ", Student3.LastName)
print("Tuition Owed: $", format(Student3.TuitionRate(Student3.District, Student3.Credits), ",.2f"))