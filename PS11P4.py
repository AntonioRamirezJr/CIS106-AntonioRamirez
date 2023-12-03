def FunctionBowlingAvg(Game1, Game2, Game3, Handicap):
  Sum = Game1 + Game2 + Game3
  AvgScore = Sum / 3
  HandicapAvgScore = (Sum + Handicap) / 3

  return AvgScore, HandicapAvgScore

LastName = input("Enter Last Name: ")
Game1 = float(input("Enter Game 1 Score: "))
Game2 = float(input("Enter Game 2 Score: "))
Game3 = float(input("Enter Game 3 Score: "))
Handicap = float(input("Enter Handicap: "))

AvgScore, HandicapAvgScore = FunctionBowlingAvg(Game1, Game2, Game3, Handicap)

print("\n\nBowler: ", LastName)
print("Average Score: ", format(AvgScore, ".2f"))
print("Average Score + Handicap: ", format(HandicapAvgScore, ".2f"))