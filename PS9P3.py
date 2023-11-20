def FunctionMPG(Miles, Gallons):
  MilesPerGallon = Miles / Gallons
  return MilesPerGallon


Entries = 0
Response = input("Would you like to calculate Miles per Gallon? (Yes or No): ")

while Response == "Yes":
  City = input("Enter the destination city: ")
  Miles = float(input("Enter the distance in miles: "))
  Gallons = float(input("Enter the gallons of gas used: "))

  MilesPerGallon = FunctionMPG(Miles, Gallons)

  Entries = Entries + 1
  print("\n\nDestination city: ", City)
  print("Distance in miles: ", Miles)
  print("Miles per Gallon: ", round(MilesPerGallon, 2))
  Response = input("\n\nWould you like to calculate another trip's MPG? (Yes or No): ")

print("Number of entries: ", Entries)