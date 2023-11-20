def FunctionBattingAvg(Hits, AtBats):
  BattingAvg = Hits / AtBats
  
  return BattingAvg

NumOfPlayers = 0
Response = input("Would you like to calculate a player's batting average? (Yes or No): ")

while Response == "Yes":
  LastName = input("Enter the player's last name: ")
  Hits = float(input("Enter the number of hits: "))
  AtBats = float(input("Enter the number of at bats: "))
  BattingAvg = FunctionBattingAvg(Hits, AtBats)

  NumOfPlayers = NumOfPlayers + 1
  print("\n\nPlayer: ", LastName)
  print("Batting Average: ", round(BattingAvg, 3))
  Response = input("\n\nWould you like to calculate another player's batting average? (Yes or No): ")

print("Number of players calculated: ", NumOfPlayers)