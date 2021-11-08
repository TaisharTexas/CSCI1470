#**********************  LeeAndrewC_CSCI1470_Prog4  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #4
#
# Algorithm(or a brief purpose of the assignment):
#   Take in contestant data from user until a weight below 1 is submitted
#   Sort each weight entry into appropriate categories (ie tooHigh, tooLow, or into a legal weightClass)
#   Display number of contestants in each weight class (unless there are 0 or 1)
#       If 0 contestants in weight class, dont display class
#       If 1 contestant in weight class, dont display class and append value to next highest weight class
#   Calculate average weight of all legal contestants
#
#**********************************************************

# |Class Name:	    |Weight in kg:
# |  Welterweight	|  61 – 64
# |  Lightweight	|  58 – 60
# |  Featherweight 	|  55 – 57
# |  Bantamweight	|  51 – 54

userIn = int(input())
# contestantWeights = [51, 59, 62, 63, 49, 54, 53, 52, 55, 66, 55, 50, 57, 0]
contestantWeights = []

welterweights = []
lightweights = []
featherweights = []
bantamweights = []
tooLow = []
tooHigh = []
legal = []

# Calculate the avg value of a given list
def listAvg(theList):
    theSum = 0
    for x in theList:
        theSum += x
    return (theSum / len(theList))

while userIn > 1:
    contestantWeights.append(userIn)
    userIn = int(input())

# iterate through inputted values and sort them into the appropriate categories
for x in contestantWeights:
    if x > 64:
        tooHigh.append(x)
    elif x < 51:
        tooLow.append(x)
    elif 51 <= x <= 54:
        bantamweights.append(x)
        legal.append(x)
    elif 55 <= x <= 57:
        featherweights.append(x)
        legal.append(x)
    elif 58 <= x <= 60:
        lightweights.append(x)
        legal.append(x)
    elif 61 <= x <= 64:
        welterweights.append(x)
        legal.append(x)
# Bantamweight display
if len(bantamweights) != 0:
    if len(bantamweights) == 1:
        featherweights.append(bantamweights[0])
    else:
        print("Bantamweight Class:")
        print("\tThere are {} competitors in this weight class".format(len(bantamweights)))
        print("\tThe average Bantamweight contestant weight is {:.2f} kg".format(listAvg(bantamweights)))
# Featherweight display
if len(featherweights) != 0:
    if len(featherweights) == 1:
        lightweights.append(featherweights[0])
    else:
        print("Featherweight Class:")
        print("\tThere are {} competitors in this weight class".format(len(featherweights)))
        print("\tThe average Featherweight contestant weight is {:.2f} kg".format(listAvg(featherweights)))
# Lightweight display
if len(lightweights) != 0:
    if len(lightweights) == 1:
        welterweights.append(lightweights[0])
    else:
        print("Lightweight Class:")
        print("\tThere are {} competitors in this weight class".format(len(lightweights)))
        print("\tThe average Lightweight contestant weight is {:.2f} kg".format(listAvg(lightweights)))
# Welterweight display
if len(welterweights) != 0:
    if len(featherweights) != 1:
        print("Welterweight Class:")
        print("\tThere are {} competitors in this weight class".format(len(welterweights)))
        print("\tThe average Welterweight contestant weight is {:.2f} kg".format(listAvg(welterweights)))

# Display total average weight
print("\nThe average legal contestant weight is {:.2f} kg".format(listAvg(legal)))