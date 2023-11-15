Response = input("Would you like to calculate interest? (Yes or No) ")

while Response == "Yes":
  
  Principle = float(input("Enter the principle amount: "))
  Rate = float(input("Enter the interest rate: "))
  
  TotalInterest = 0
  
  print("\n\nYear:", "  Beginning Balance:", "  Ending Balance:")
  for Year in range (1, 6, 1):
    InterestAmt = Principle * Rate
    TotalInterest = TotalInterest + InterestAmt
    EndingBal = Principle + InterestAmt
    print(Year, "      $", (format(Principle, ".2f")),  "          $", format(EndingBal, ".2f"))
    Principle = EndingBal
  print("\n\nAccumulated interest over 5 years: $", format(TotalInterest, ".2f"))
  
  Response = input("\n\nWould you like to calculate interest again? (Yes or No) ")