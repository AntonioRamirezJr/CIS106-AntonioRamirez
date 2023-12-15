class Employee:
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@NFL.com'
  
  def Bonus(self, rate):
    Bonus = float(rate) * float(self.pay)
    return Bonus

  def fullname(self):
    return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Tom', 'Brady', 435000)
emp_2 = Employee('Pat', 'Mahomes', 385000)


print("Email: ", emp_1.email)
print("First Name: ", emp_1.first)
print("Last Name: ", emp_1.last)
print("Salary: $", format(emp_1.pay, ",.2f"))
print("10% Bonus: $", format(emp_1.Bonus(0.10), ",.2f"))
print("20% Bonus: $", format(emp_1.Bonus(0.20), ",.2f"))


print("\n\nEmail: ", emp_2.email)
print("First Name: ", emp_2.first)
print("Last Name: ", emp_2.last)
print("Salary: $", format(emp_2.pay, ",.2f"))
print("10% Bonus: $", format(emp_2.Bonus(0.10), ",.2f"))
print("20% Bonus: $", format(emp_2.Bonus(0.20), ",.2f"))