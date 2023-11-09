NumOfStudents = 0

Response = input("Would you like to calculate a student's exam scores? (Yes or No) ")

while Response == "Yes":
  NumOfStudents = NumOfStudents + 1
  Lname = (input("Enter the student's last name: "))
  Score1 = float(input("Enter the first exam Score: "))
  Score2 = float(input("Enter the second exam score: "))
  AvgExamScore = (Score1 + Score2) / 2
  print(Lname, "has an average exam score of ", AvgExamScore)
  Response = input("\n\nWould you like to calculate another student's exam scores? (Yes or No) ")

print("\n\nYou have calculated ", NumOfStudents, "students' exam scores.")