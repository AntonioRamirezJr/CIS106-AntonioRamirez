def loadarrays(LastName, TestScore):
  f = open("ScoreData.txt", "r")
  for i in range (0, 10, 1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    LastName.append(ln)
    S = f.readline()
    S.rstrip("\n")
    TestScore.append(float(S))

  f.close()

def darrays(LastName, TestScore):
  for i in range (0, 10, 1):
    print(LastName[i], "Test Score: ", TestScore[i])

def hilow(LastName, TestScore):
  hiScore = 0.0
  hisub = 0.0
  loScore = 999
  losub = 0.0

  for i in range (0, 10, 1):
    if (TestScore[i] > hiScore):
      hiScore = TestScore[i]
      hisub = i
    elif TestScore[i] < loScore:
      loScore = TestScore[i]
      losub = i

  print("")
  print(LastName[hisub], "has the HIGHEST test score: ", TestScore[hisub])
  print(LastName[losub], "has the LOWEST test score: ", TestScore[losub])

LastName = []
TestScore = []

loadarrays(LastName, TestScore)
darrays(LastName, TestScore)
hilow(LastName, TestScore)