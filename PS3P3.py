#Input Phase
Name1 = input("enter your last name: ")
Name2 = input("enter your first friend's last name: ")
Name3 = input("enter your second friend's last name: ")
AmtReceived = float(input("enter the amount you received from the job: $"))

#Processing Phase
AmtName1 = AmtReceived / 3
AmtName2 = AmtReceived / 3
AmtName3 = AmtReceived / 3

#Output Phase
print("The amount each person person will receive is as follows")
print(Name1, ": $", format(AmtName1, ",.2f"))
print(Name2, ": $", format(AmtName2, ",.2f"))
print(Name3, ": $", format(AmtName3, ",.2f"))