#Take
unit = int(input("Please enter number of unit you consumed :"))

#Checking
if(unit < 50):
    amount= unit * 2.60
    surcharge = 25

#Checking
elif(unit <= 100):
  amount= 130 + ((unit - 50) * 3.25)
  surcharge = 35

#Checking
elif(unit <= 200):
  amount= 130 + 162.50 + ((unit - 100) * 5.26)
  surcharge = 35

#Checking
else:
 amount= 130 + 162.50 + 526 + ((unit - 200) * 8.45)
 surcharge = 75

#calculate
total = amount + surcharge
print("\nElectricity bill = %.2f" %total)