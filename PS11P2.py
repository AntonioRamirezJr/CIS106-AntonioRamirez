def FunctionAvgExam(Lname, Exam1, Exam2, Exam3):
  TotalPts = Exam1 + Exam2 + Exam3
  AvgExamScore = TotalPts / 3
  
  return AvgExamScore, TotalPts

Lname = input("Enter Student's Last Name: ")
Exam1 = float(input("Enter Exam 1 Score: "))
Exam2 = float(input("Enter Exam 2 Score: "))
Exam3 = float(input("Enter Exam 3 Score: "))

AvgExamScore, TotalPts = FunctionAvgExam(Lname, Exam1, Exam2, Exam3)

print("\n\nStudent's Name:", Lname)
print("Total Points: ", TotalPts)
print("Average Exam Score: ", format(AvgExamScore, ".2f"))