#**********************  LeeAndrewC_CSCI1470_Prog9  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #9
#
# Algorithm(or a brief purpose of the assignment):
#   Open the existing file "Gettys2.txt"
#   Create a new file "GettysNoE.txt"
#   Check each line in Gettys2
#       check each word in the line
#           Check if the word has an e in it
#               if the word doesn't have an e in it, add it to a string container
#       after each line, write the string container to GettysNoE
#   Now GettysNoE is the Gettys2 file, but with all the "e" words removed from each line
#   Close both files
#
#**********************************************************

def hasNoE(theWord):
    if "e" not in theWord:
        return True
    else:
        return False

GettySpeech = open("/Users/andrew/Downloads/Gettys2.txt")
newSpeech = open("/Users/andrew/PycharmProjects/CSCI1470_UHCL/GettysNoE.txt", "w")

for line in GettySpeech:
    words = line.split(" ")
    # print(words)
    noEwords = ""
    for eachWord in words:
        if hasNoE(eachWord):
            noEwords += eachWord + " "
    # print(noEwords)
    newSpeech.write(noEwords)

GettySpeech.close()
newSpeech.close()
