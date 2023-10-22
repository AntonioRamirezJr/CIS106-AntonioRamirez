#Input Phase
ApplianceName = input("Enter the name of the appliance: ")
ApplianceCost = float(input("Enter the cost of the appliance: "))

#Processing Phase: 
WarrantyCost = ApplianceCost * 0.1 if ApplianceCost > 1000 else ApplianceCost * 0.05
Total = ApplianceCost + WarrantyCost

#Output Phase
print("\n\nAppliance Name: ", ApplianceName)
print("Appliance Cost: $", format(ApplianceCost, ".2f"))
print("Warranty Cost: $", format(WarrantyCost, ".2f"))
print("Total: $", format(Total, ".2f"))