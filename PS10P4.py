def FunctionTicketPrice(Miles):
  if Miles >= 30:
    TicketPrice = 12
  elif Miles >= 20 and Miles < 30:
    TicketPrice = 10
  elif Miles >= 10 and Miles < 20:
    TicketPrice = 8
  else:
    TicketPrice = 5

  return TicketPrice

SumOfAllTickets = 0

Response = input("Would you like to calculate the price of a train ticket to Chicago? (Yes or No) ")

while Response == "Yes":
  LastName = input("\n\nEnter last name: ")
  Miles = float(input("Enter the distance from Downtown Chicago (in miles): "))

  TicketPrice = FunctionTicketPrice(Miles)
  print("Ticket Price: $", format(TicketPrice, ".2f"))

  SumOfAllTickets = SumOfAllTickets + TicketPrice

  Response = input("\n\nWould you like to calculate the price of another train ticket? (Yes or No) ")

print("\n\nTotal Sum of All Tickets: $", format(SumOfAllTickets, ".2f"))