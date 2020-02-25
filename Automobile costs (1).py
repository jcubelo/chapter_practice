def askForExpenses():
    monthlyloanpayment = float(input("How much do you pay for your loan every month?: "))
    monthlyinsurancepayment = float(input("How much do you pay for your insurance each month?: "))
    monthlygaspayment = float(input("How much do you pay for gas each month?: "))
    monthlyoilpayment = float(input("How much do you pay for oil each month?: "))
    monthlytirepayment = float(input("How much do you pay for your tires each month?: "))
    monthlymaintenancepayment = float(input("How much do you pay for maintenance each month?: "))
    return monthlyloanpayment, monthlyinsurancepayment, monthlygaspayment, monthlyoilpayment, monthlytirepayment, monthlymaintenancepayment
def calctotalmonth(payment1, payment2, payment3, payment4, payment5, payment6):
    totalmonth = payment1 + payment2 + payment3 + payment4 + payment5 + payment6
    return totalmonth

def calcannualtotal( totalmonth ):
    annualtotal = totalmonth * 12
    return annualtotal
def printinfo():
    print("Your monthly cost is $" + str(round(calctotalmonth(loanpayment, insurancepayment, gaspayment, oilpayment, tirepayment, maintenancepayment),2))+ \
        "\nYour total annual cost is $" + str(round(calcannualtotal(calctotalmonth(loanpayment, insurancepayment, gaspayment, oilpayment, tirepayment, maintenancepayment)),2)))
def main():
    loanpayment, insurancepayment, gaspayment, oilpayment, tirepayment, maintenancepayment = askForExpenses()
    printinfo()
main()
