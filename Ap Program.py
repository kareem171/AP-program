#these are the variables

print("Hi Welcome to Bill Calculator. This will help you calculate your bills and live easily")
print(" ")

def Rent():
    Rent= int(input("Enter your annual rent:"))
    MonthlyRent= Rent/12
    return MonthlyRent

def WaterBill():
    WaterBill= int(input("Enter your annual water bill:"))
    MonthlyWaterBill= WaterBill/12
    return MonthlyWaterBill

def ElectricityBill():
    ElectricityBill= int(input("Enter annual electricity bill:"))
    MonthlyElectricityBill= ElectricityBill/12
    return MonthlyElectricityBill

def PhoneBill():
    PhoneBill= int(input("Enter annual phone bill:"))
    MonthlyPhoneBill= PhoneBill/12
    return MonthlyPhoneBill

def CableandWifiBill():
    userinput= input("Is your cable and wifi on the same bill?:")
    if userinput== "Yes" or userinput== "yes":
        CableandWifiBill= int(input("Enter annual cable and wifi bill:"))
        MonthlyCableandWifiBill= CableandWifiBill/12
        return "Yes", MonthlyCableandWifiBill
    elif userinput== "No" or userinput== "no":
        CableBill= int(input("Enter annual cable bill:"))
        MonthlyCableBill= CableBill/12
        WifiBill= int(input("Enter annual wifi bill:"))
        MonthlyWifiBill= WifiBill/12
        return "No", MonthlyCableBill, MonthlyWifiBill
        
print(" ")
MonthlyRent=Rent()
MonthlyWaterBill=WaterBill()
MonthlyElectricityBill=ElectricityBill()
MonthlyPhoneBill=PhoneBill()
MonthlyCableandWifiBill=CableandWifiBill()

print("Your monthly bill for Rent is", MonthlyRent)
print("Your monnthly bill for water is", MonthlyWaterBill)
print("Your monthly bill for electricity is", MonthlyElectricityBill)
print("Your monthly bill for phone is", MonthlyPhoneBill)




if MonthlyCableandWifiBill[0] == "No":
    print("Your monthly cable bill is", MonthlyCableandWifiBill[1])
    print("Your monthly wifi bill is", MonthlyCableandWifiBill[2])
else:
      print("Your monthly cable and wifi bill is", MonthlyCableandWifiBill[1])



if MonthlyCableandWifiBill[0] == "No":
    Total= MonthlyRent+MonthlyWaterBill+MonthlyElectricityBill+MonthlyPhoneBill+MonthlyCableandWifiBill[1]+MonthlyCableandWifiBill[2]
    print("Your total cost of bills per month is", Total)
else:
     Total=MonthlyRent+MonthlyWaterBill+MonthlyElectricityBill+MonthlyPhoneBill+MonthlyCableandWifiBill[1]
     print("Your total cost of bills per month is", Total)
     

