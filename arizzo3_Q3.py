# Alec Rizzo
# Python Midterm
# Question 3
# Write a program to make a diamond based on users input

# Note: Sorry if this isn't planned out the best, I kept stumbling over how
# to implement this question properly

# Functions ==============================================================================
def print_row(numSpaces, numDiamonds, spaceChar, diamondChar):
    halfSpaces = numSpaces // 2
    row = ""
    for char in range(halfSpaces):
        row += spaceChar
    for char in range(numDiamonds):
        row += diamondChar
    for char in range(halfSpaces):
        row += spaceChar
    print(row)

def getSpaceChar():
    userChar = input("Enter a single character for the spaces (press enter for default): ")
    if userChar == '':
        return " "

    while(len(userChar) != 1):
        userChar = input("Please enter a single character: ")
        if userChar == '':
            return " "
    return userChar

def getDiamondChar():
    userChar = input("Enter a single character for the diamond (press enter for default): ")
    if userChar == '':
        return '+'

    while(len(userChar) != 1):
        userChar = input("Please enter a single character: ")
        if userChar == '':
            return '+'
    return userChar
# End of Functions =======================================================================


# Main ===================================================================================
topHalf = 0
while True:
    try:
        topHalf = int(input("Please enter number less than or equal to 40 for top half of diamond: "))
        if topHalf < 0 or topHalf > 40:
            print("Please enter only positive integers, less than or equal to 40")
            continue
        break
    except:
        print("Please enter only positive integers, less than or equal to 40")

space = getSpaceChar()
diamond = getDiamondChar()
spaceCount = 0
diamondCount = 0

for n in range(topHalf):
    if n == 0:
        spaceCount = (topHalf + (topHalf - 1)) - 1
        diamondCount = 1
        print_row(spaceCount, diamondCount, space, diamond)
        continue
    spaceCount -= 2
    diamondCount +=2
    print_row(spaceCount, diamondCount, space, diamond)

for n in range(topHalf-1):
    spaceCount += 2
    diamondCount -= 2
    print_row(spaceCount, diamondCount, space, diamond)
# End of Main ============================================================================
