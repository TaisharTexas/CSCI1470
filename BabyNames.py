BabyNames = open("/Users/andrew/Downloads/TXBabyNames.txt")
boys1996 = 0
boysNamedLeo = 0
givenName = "Lillian"
startYr = int(input())
endYr = int(input())
countinrange = 0
for line in BabyNames:
    elements = line.split(",")
    if (elements[1] == "M") and (int(elements[2]) == 1996):
        # print("found")
        boys1996 += 1
    if elements[3] == "Leo" and elements[1] == "M":
        # print(elements[2])
        boysNamedLeo += 1
    if elements[3] == givenName and (startYr < int(elements[2]) <= endYr):
        countinrange += 1


print(countinrange)
# print("total number of boys born in 1996 is {}".format(boys1996))
# print("total number of Leos born is {}".format(boysNamedLeo))

BabyNames.close()
