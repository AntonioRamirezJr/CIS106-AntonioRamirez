#Input Phase
TicketQty = float(input("Enter the number of concert tickets you want to purchase: "))

#Processing Phase
if TicketQty >= 25:
  TicketPrice = 50
elif TicketQty <= 24 and TicketQty >= 10:
  TicketPrice = 60
elif TicketQty <= 9 and TicketQty >= 5:
  TicketPrice = 70
else:
  TicketPrice = 75
TotalCost = TicketQty * TicketPrice

#Output Phase
print("Number of tickets: ", TicketQty)
print("Price per ticket: ", format(TicketPrice, ".2f"))
print("Total cost: ", format( TotalCost, ".2f"))