#**********************  LeeAndrewC_CSCI1470_Prog6  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #6
#
# Algorithm(or a brief purpose of the assignment):
# Need convert function that takes in a string
#   iterate through every character in the string
#       if character is numeric, add it to output
#       if character is alpha, change it to its numeric value and add to output
#       if character is a hyphen, add it to output
#       if character is a space, skip it
#   return the output string
#
# ask user for 10 digit phone number
# use convert function to display numeric version of the phone number
# continue asking for and converting numbers until user types "stop"
#
#**********************************************************

def convert(OrigNumber):
    """
    Takes in an alphanumeric phone number and returns it as a numeric phone number

    :param OrigNumber: the user-inputed phone number that needs to be converted to purely numeric form
    :return: the converted version of the user entered phone number
    """
    convertedNumber = ""
    for eachCharacter in OrigNumber:
        if eachCharacter == "-":
            convertedNumber += "-"
        elif eachCharacter.isalpha():
            if eachCharacter=="A" or eachCharacter=="B" or eachCharacter=="C":
                convertedNumber += "2"
            elif eachCharacter == "D" or eachCharacter == "E" or eachCharacter == "F":
                convertedNumber += "3"
            elif eachCharacter=="G" or eachCharacter=="H" or eachCharacter=="I":
                convertedNumber += "4"
            elif eachCharacter=="J" or eachCharacter=="K" or eachCharacter=="L":
                convertedNumber += "5"
            elif eachCharacter == "M" or eachCharacter == "N" or eachCharacter == "O":
                convertedNumber += "6"
            elif eachCharacter == "P" or eachCharacter == "Q" or eachCharacter == "R" or eachCharacter == "S":
                convertedNumber += "7"
            elif eachCharacter == "T" or eachCharacter == "U" or eachCharacter == "V":
                convertedNumber += "8"
            elif eachCharacter == "W" or eachCharacter == "X" or eachCharacter == "Y" or eachCharacter == "Z":
                convertedNumber += "9"
        else:
            if eachCharacter != " ":
                convertedNumber += eachCharacter

    return convertedNumber


if __name__ == "__main__":
    companyNumber = input("Enter an alphanumeric number of the form XXX-XXX-XXXX: ")
    while companyNumber != "stop":
        print("The numeric equivilent of the number is {}".format(convert(companyNumber)))
        companyNumber = input("Enter an alphanumeric number of the form XXX-XXX-XXXX (type stop to exit the program): ")

