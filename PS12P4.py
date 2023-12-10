def loadarrays(LastName, BattingAvg):
  f = open("BattingAvg.txt", "r")
  for i in range (0, 10, 1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    LastName.append(ln)
    S = f.readline()
    S.rstrip("\n")
    BattingAvg.append(float(S))

  f.close()

def darrays(LastName, BattingAvg):
  for i in range (0, 10, 1):
    print(LastName[i], "Batting Average: ", BattingAvg[i])


def searchLastName(LastName, BattingAvg, NameSearch):
  foundsub = -1

  for i in range (0, 10, 1):
    if LastName[i] == NameSearch:
      foundsub = i

  if foundsub == -1:
    print(NameSearch, "= PLAYER NOT FOUND IN LIST")
  else:
    print(LastName[foundsub], "Batting Average: ", BattingAvg[foundsub])

LastName = []
BattingAvg = []

loadarrays(LastName, BattingAvg)
darrays(LastName, BattingAvg)

Response = input("\n\nDo you want to search for a player? (Yes or No) ")
  
while Response == "Yes":
  NameSearch = input("Enter the last name of the player: ")
  searchLastName(LastName, BattingAvg, NameSearch)
  Response = input("\n\nWould you like to search for another player? (Yes or No) ")