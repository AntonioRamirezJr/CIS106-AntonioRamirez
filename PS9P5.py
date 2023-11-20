def FunctionTuition(DistrictCode, Credits): 
  if DistrictCode == "I":
    TuitionRate = 250.00
  elif DistrictCode == "O":
    TuitionRate = 500.00
  TuitionOwed = TuitionRate * Credits

  return TuitionOwed

SumOfAllTuitions = 0.00

Response = input("Would you like to calculate the amount of tuition owed? (Yes or No): ")

while Response == "Yes":
  LastName = input("Enter Last Name: ")
  Credits = float(input("Enter the amount of credit hours: "))
  DistrictCode = input("Enter the District Code: ")

  TuitionOwed = FunctionTuition(DistrictCode, Credits)

  SumOfAllTuitions = SumOfAllTuitions + TuitionOwed
  print("\n\nLast Name: ", LastName)
  print("Tuition Owed: $", format(TuitionOwed, ",.2f"))

  Response = input("\n\nWould you like to calculate another student's tuition? (Yes or No): ")

print("Sum of all tuitions' owed: $", format(SumOfAllTuitions, ".2f"))