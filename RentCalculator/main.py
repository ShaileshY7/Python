# My flate rent calculator

# Total rent
# How much spend on food
# electricity Bill
# Charge per unit
# Number of persons live in flate

# output
# how much each person to pay rent

rent=int(input("Enter total rent of flate="))
food=int(input("how much spend on food="))
electricity_bill=int(input("Enter electricity unit spend="))
charge_perunit=int(input("Enter price of 1 unit electricity="))
persons=int(input("Number fo persons live in flate="))

Total_bill=electricity_bill*charge_perunit

print("how much amount to pay each person:",(rent+food+Total_bill)/persons)