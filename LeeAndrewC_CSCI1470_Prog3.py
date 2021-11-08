#**********************  LeeAndrewC_CSCI1470_Prog3  *********************
#
# Name: Andrew Lee
#
# Course: CSCI 1470.01
#
# Assignment: Program #3
#
# Algorithm(or a brief purpose of the assignment)
#   Prompt user for item cost and amount tendered
#   Check that amount tendered is bigger than the item cost
#   Split the amount due into its monetary components
#   Print the amount due in its separate components
#
#**********************************************************

itemCost = float(input("Enter item cost (up to a max of $5): "))
amountTendered = float(input("Enter amount tendered (must be more than cost of item up to the max of $5): "))

if(amountTendered >= itemCost):
    itemCost *= 100
    amountTendered *= 100
    amountDue = int(amountTendered - itemCost)

    # print("amount left:", amountDue)
    dollars = amountDue // 100
    # print("dollars:", dollars)
    amountDue -= dollars * 100
    # print("amount left:", amountDue)
    quarters = amountDue // 25
    # print("quarters:", quarters)
    amountDue -= quarters * 25
    # print("amount left:", amountDue)
    dimes = amountDue // 10
    # print("dimes:", dimes)
    amountDue -= dimes * 10
    # print("amount left:", amountDue)
    nickels = amountDue // 5
    # print("nickels:", nickels)
    amountDue -= nickels * 5
    # print("amount left:", amountDue)
    pennies = amountDue
    # print("pennies:", pennies)

    if dollars > 0:
        if dollars > 1:
            print("{} Dollars".format(dollars))
        else:
            print("{} Dollar".format(dollars))
    if quarters > 0:
        if quarters > 1:
            print("{} Quarters".format(quarters))
        else:
            print("{} Quarter".format(quarters))
    if dimes > 0:
        if dimes > 1:
            print("{} Dimes".format(dimes))
        else:
            print("{} Dime".format(dimes))
    if nickels > 0:
        if dollars > 1:
            print("{} Nickels".format(nickels))
        else:
            print("{} Nickel".format(nickels))
    if pennies > 0:
        if pennies > 1:
            print("{} Pennies".format(pennies))
        else:
            print("{} Penny".format(pennies))

else:
    print("Did not provide enough money to pay for item")

