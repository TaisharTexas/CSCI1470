BabyNames = open("/Users/andrew/Downloads/TXBabyNames.txt")

count = 0
for line in BabyNames:
    elements = line.split(",")

    state, gender, year, firstName, freq = elements
    if gender == "M" and firstName == "Alex" and int(year) >= 2001 and int(year) <= int(year) + 10:
        count += 1 + int(freq)


print("The total number of boys born in {} named {} is {}".format("2000-2010", "John", count))

BabyNames.close()


