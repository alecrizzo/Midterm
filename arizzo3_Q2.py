# Alec Rizzo
# Python Midterm
# Question 2
# Write a program to deduce a users tax rate and salary after taxes

# Functions ==============================================================================
# returns the tax bracket for the salary given
def getTaxRate(salary):
    if float(salary) >= 0 and float(salary) <= 7550:
        return .10
    elif float(salary) > 7550 and float(salary) <= 30650:
        return .15
    elif float(salary) > 30650 and float(salary) <= 74200:
        return .25
    elif float(salary) > 74200 and float(salary) <= 154800:
        return .28
    elif float(salary) > 154800 and float(salary) <= 336550:
        return .33
    else:
        return .35

# Function for outputting percentage of tax rates
# tried using match-case but I couldn't get it working
def getTaxPercent(taxDec):
    if taxDec == .10:
        return "10%"
    if taxDec == .15:
        return "15%"
    if taxDec == .25:
        return "25%"
    if taxDec == .28:
        return "28%"
    if taxDec == .33:
        return "33%"
    if taxDec == .35:
        return "35%"

def getAfterTaxSalary(sal, rate):
    return "{:.2f}".format(float(sal) * float(1 - rate)) # "{:.2f}" for presentation of currency
# End of Functions =======================================================================

# Main ===================================================================================
userVal = 0
while True:
    try:
        userVal = float(input("Please enter your Yearly Salary: "))
        if userVal < 0:
            print("Please enter only positive values!")
            continue
        break
    except:
        print("Please enter only positive values!")

userVal = "{:.2f}".format(userVal)  # for presentation of currency format decimal points
taxRate = getTaxRate(userVal)

print("Pre-Tax Salary: \t$",userVal)
print("Federal Tax Rate: \t ",getTaxPercent(taxRate))
print("After-tax Salary: \t$",getAfterTaxSalary(userVal, taxRate))
# End of Main ============================================================================
