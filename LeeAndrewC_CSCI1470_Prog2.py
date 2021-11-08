#**********************  LeeAndrewC_CSCI1470_Prog2  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #2
#
# Algorithm(or a brief purpose of the assignment)
#   Gather the low and high temps for each day of the week
#   Find the min week temp and the max week temp
#   Find average low and high temps for the week
#   Calculate the difference between high and low temp averages
#
#**********************************************************

### The given low and high temps for the week
# lowTemps =  [75, 77, 76, 78, 72, 70, 70]
# highTemps = [90, 92, 92, 93, 91, 89, 88]
###
lowTemps = []
highTemps = []
theWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Gathering the low and high temps for each day of the week from the user
theDay = 0
while(theDay < len(theWeek)):
    lowInput = float(input("Input the low temp for {}: ".format(theWeek[theDay])))
    highInput = float(input("Input the high temp for {}: ".format(theWeek[theDay])))
    lowTemps.append(lowInput)
    highTemps.append(highInput)
    theDay += 1

# Calculating the weekly min and max temps
weeklyMinTemp = min(lowTemps)
weeklyMaxTemp = max(highTemps)
print("\nThe lowest temperature this week was: {:.2f} degrees".format(weeklyMinTemp))
print("The high temperature this week was: {:.2f} degrees".format(weeklyMaxTemp))

# Calculating the weekly min average and max average temps
weeklyMinAvg = sum(lowTemps) / len(lowTemps)
weeklyMaxAvg = sum(highTemps) / len(highTemps)
print("\nThe average low temperature this week was: {:.2f} degrees".format(weeklyMinAvg))
print("The average high temperature this week was: {:.2f} degrees".format(weeklyMaxAvg))
# Calculating the difference between the two averages
print("The difference between the avg low temp and the avg high temp is: {:.2f} degrees".format(weeklyMaxTemp - weeklyMinAvg))