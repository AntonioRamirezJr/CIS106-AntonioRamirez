def FunctionSquareFootage(Length, Width, Height):

  SquareFootage = (2 * Length * Width) + (2 * Length * Height) + (2 * Width * Height)

  return SquareFootage

Response = input("Would you like to calculate the gallons needed to paint a room? ")

while Response == "Yes":
  print("\n\nEnter the dimansions of the room. ")
  Length = float(input("Length : "))
  Width = float(input("Width : "))
  Height = float(input("Height : "))
  
  SquareFootage = FunctionSquareFootage(Length, Width, Height)

  GallonsNeeded = SquareFootage / 50

  print("\n\nGallons of paint needed: ", GallonsNeeded)
  
  Response = input("\n\nWould you like to calculate the amount of paint needed for another room? (Yes or No) ")