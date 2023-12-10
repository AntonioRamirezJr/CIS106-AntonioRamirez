print("Student's Test Scores\n\n")

def displayarrays(LastName, TestScore):
  for i in range (0, 10, 1):
    print(LastName[i], "Test Score: ", TestScore[i])

def rdisplay(LastName, TestScore):
  for i in range (9, -1, -1):
    print(LastName[i], "Test Score:", TestScore[i])

LastName = ["Brady's", "Manning's", "Rodgers's", "Carr's", "Romo's", "Wilson's", "Mahomes's", "Hurts's", "Burrow's", "Prescott's"]
TestScore = [97, 93, 90, 85, 86, 88, 99, 94, 87, 89]

displayarrays(LastName, TestScore)

print("\n\nREVERSE ORDER\n\n")
rdisplay(LastName, TestScore)