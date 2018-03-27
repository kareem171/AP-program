#these are the variables

print("Hi Welcome to Bill Calculator. This will help you calculate your bills and live easily")
print(" ")

def Rent():
    Rent= input("Enter your annual rent")
    MonthlyRent= Rent/12

def WaterBill():
    WaterBill= input("Enter your annual water bill")
    MonthlyWaterBill= WaterBill/12

def ElectricityBill():
    ElectricityBill= input("Enter annual electricity bill")
    MonthlyElectricityBill= ElectricityBill/12

def PhoneBill():
    PhoneBill= input("Enter annual phone bill")
    MonthlyPhoneBill= PhoneBill/12

def CableandWifiBill():
    userinput= input("Is your cable and wifi on the same bill?")
    if userinput== "Yes" or "yes":
    CableandWifiBill= input("Enter annual cable and wifi bill")
    MonthlyCableandWifiBill= CableandWifiBill/12
    elif userinput== "No" or "no":
    Cable
