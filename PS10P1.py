def FunctionForecast(Month, Sales):
  if Month == "January" or Month == "February" or Month == "March" or Month == "JAN" or Month == "FEB" or Month == "MAR":
    ForecastPercent = 0.10
  elif Month == "April" or Month == "May" or Month == "June" or Month == "APR" or Month == "MAY" or Month == "JUN":
    ForecastPercent = 0.15
  elif Month == "July" or Month == "August" or Month == "September" or Month == "JUL" or Month == "AUG"  or Month == "SEP" or Month == "SEPT":
    ForecastPercent = 0.20
  elif Month == "October" or Month == "November" or Month == "December" or Month == "OCT" or Month == "NOV" or Month == "DEC":
    ForecastPercent = 0.25

  FutureSales = Sales * (1 + ForecastPercent)

  return FutureSales

Response = input("Would you like to forecast the following month's sales? (Yes or No): ")

while Response == "Yes":
  LastName = input("\n\nEnter last name: ")
  Month = input("Enter the month (OR month abbreviation in ALL CAPS): ")
  Sales = float(input("Enter the current month's sales: "))

  FutureSales = FunctionForecast(Month, Sales)

  print("\n\nNext month's forecasted Sales: $", format(FutureSales, ".2f"))
  
  Response = input("\n\nWould you like to forecast another month's sales? (Yes or No): ")