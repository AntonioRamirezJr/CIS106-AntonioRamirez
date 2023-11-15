File = open("StudentData1.txt", "r")

NumOfStudents = 0
TotalTuition = 0

#get the first part of the data

LastName = str(File.readline().rstrip('\n'))

while LastName != "":  #detect end of file
  DistrictCode = str(File.readline().rstrip('\n'))
  Credits = float(File.readline())

  if DistrictCode == "I":
    CostPerCredit = 250.00
  else:
    CostPerCredit = 500.00

  Tuition = CostPerCredit * Credits
  NumOfStudents = NumOfStudents + 1
  TotalTuition = TotalTuition + Tuition

  print("\n\nStudent: ",LastName)
  print("Credits Taken: ", Credits)
  print("Tuition Owed: $", format(Tuition,".2f"))

  LastName = str(File.readline().rstrip('\n'))

File.close()

print("\n\nNumber Of Students: ", NumOfStudents)
print("Total Tuition: $", format(TotalTuition, ".2f"))