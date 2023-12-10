def displayarrays(LastName):
  for i in range (0, 10, 1):
    print(LastName[i])


def rdisplay(LastName):
  for i in range (9, -1, -1):
    print(LastName[i])

LastName = ["Brady", "Manning", "Rodgers", "Carr", "Romo", "Wilson", "Mahomes", "Hurts", "Burrow", "Prescott"]

displayarrays(LastName)
print("\n\nREVERSE ORDER\n\n")
rdisplay(LastName)