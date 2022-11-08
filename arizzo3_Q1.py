# Alec Rizzo
# Python Midterm
# Question 1
# Ask the user for 3 numbers.
#   If x is less than or equal to y, and y is less than or equal to z, print out "Ascending Order".
#   If x is greater than or equal to y, and y is greater than or equal to z, print out "Descending Order".
#   If x, y, and z are all equal, print out "All three numbers are equal"
#   If x, y, and z are not ordered - print out "These numbers are not ordered!"
# Note, your sequence should print out only one message about the entered numbers!

def getInput():
    userVal = 0
    while True:
        try:
            userVal = int(input("Please enter number: "))
            if userVal < 0:
                print("Please enter only positive integers!")
                continue
            return userVal
        except:
            print("Please enter only positive integers!")

x = getInput()
y = getInput()
z = getInput()

# equals case must go first because due to the conditions mentioned in
# the question, ascending order will register for the numbers being equal
if x == y and x == z:
    print("All three numbers are equal")
elif x >= y and y >= z:
    print("Descending Order")
elif x <= y and y <= z:
    print("Ascending Order")
else:
    print("These numbers are not ordered!")
