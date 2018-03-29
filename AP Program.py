#these are the variables

print("Hi Welcome to Bill Calculator. This will help you calculate your bills and live easily")
print(" ")

def Rent():
    Rent= int(input("Enter your annual rent:"))
    MonthlyRent= Rent/12

def WaterBill():
    WaterBill= int(input("Enter your annual water bill:"))
    MonthlyWaterBill= WaterBill/12

def ElectricityBill():
    ElectricityBill= int(input("Enter annual electricity bill:"))
    MonthlyElectricityBill= ElectricityBill/12

def PhoneBill():
    PhoneBill= int(input("Enter annual phone bill:"))
    MonthlyPhoneBill= PhoneBill/12

def CableandWifiBill():
    userinput= input("Is your cable and wifi on the same bill?:")
    if userinput== "Yes" or "yes":
        CableandWifiBill= int(input("Enter annual cable and wifi bill:"))
        MonthlyCableandWifiBill= CableandWifiBill/12
    elif userinput== "No" or "no":
        CableBill= int(input("Enter annual cable bill:"))
        MonthlyCableBill= CableBill/12
        WifiBill= int(input("Enter annual wifi bill:"))
        
print(" ")
print("Your monthly bill for Rent is", Rent())
print("Your monnthly bill for water is", WaterBill())
print("Your monthly bill for electricity is", ElectricityBill())
print("Your monthly bill for phone is", PhoneBill())

userinput= input("Is your cable and wifi on the same bill?")
if userinput== "Yes" or "yes":
    print("Your monthly cable and wifi bill is",CableandWifiBill())
elif userinput== "No" or "no":
    print("Your monthly cable bill is", CableBill())
    print("Your monthly wifi bill is", WifiBill())
