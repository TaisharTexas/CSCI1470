#**********************  LeeAndrewC_CSCI1470_Prog7  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #7
#
# Algorithm(or a brief purpose of the assignment):
#   Get both header names from user
#   Get first author name
#   while author name isn't -1 continue
#       take number of books for the author
#       continue taking author names and number of books until -1 is entered for an author
#   display every author and their number of books in a formatted table
#   display every author and represent their number of books with an equivalent number of stars to create a histogram
#
#**********************************************************

cHeader1 = input("Enter the column 1 header: ")
print(cHeader1)
cHeader2 = input("Enter the column 2 header: ")
print(cHeader2)

authorList = []  # list of user-entered authors
bookList = []  # user-entered number of published works for each author
theAuthor = input("Enter an author (-1 to stop input): ")
while theAuthor != "-1":
    numBooks = int(input("Enter the number of books written by this author: "))
    authorList.append(theAuthor)
    bookList.append(numBooks)
    theAuthor = input("Enter an author (-1 to stop input): ")

# Display table of authors and amount of published works
format_string = "{name:<20}{fill:1}{books:>23}"
print(format_string.format(name=cHeader1, fill='|', books=cHeader2))
print("-" * 44)
for x in range(len(authorList)):
    print(format_string.format(name=authorList[x], fill='|', books=bookList[x]))

# Display Histogram
format_string = "{name:>20}"
for x in range(len(authorList)):
    print(format_string.format(name=authorList[x]), end=" ")
    print("*" * bookList[x])
