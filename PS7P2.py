StartValue = int(input("Enter the START VALUE: "))
StopValue = int(input("Enter the STOP VALUE: "))
IncValue = int(input("Enter the INCREMENT VALUE: "))

print("\n\nSTART VALUE: ", StartValue)

while StartValue <= StopValue:
  print("Loop (+ Increment Value): ", StartValue)
  StartValue += IncValue
print("STOP VALUE: ", StopValue)