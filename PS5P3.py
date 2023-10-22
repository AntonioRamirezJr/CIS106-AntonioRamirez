#Input Phase
BooksQty = float(input("Enter the number of books: "))
CostPerBook = float(input("Enter the cost per book: "))

#Processing Phase
Total = BooksQty * CostPerBook
ShippingCharge = 0.0 if Total > 50 else 25.0

#Output Phase
print("\n\nOrder Total: $", format(Total, ".2f"))
print("+ Shipping Charge: $", format(ShippingCharge, ".2f"))