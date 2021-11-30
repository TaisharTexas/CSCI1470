daList = [78, 23, 45, 8, 32, 56, 44, 13, 29, 72, 81, 2, 9, 14, 32, 25]

# Selection Sort
for i in range(len(daList) - 1):
    # Find index of smallest remaining element
    index_smallest = i
    for j in range(i + 1, len(daList)):
        if daList[j] < daList[index_smallest]:
            index_smallest = j

    # Swap numbers[i] and numbers[index_smallest]
    temp = daList[i]
    daList[i] = daList[index_smallest]
    daList[index_smallest] = temp

# Insertion Sort
for i in range(1, len(daList)):
   j = i
   # Insert numbers[i] into sorted part
   # stopping once numbers[i] in correct position
   while j > 0 and daList[j] < daList[j - 1]:

      # Swap numbers[j] and numbers[j - 1]
      temp = daList[j]
      daList[j] = daList[j - 1]
      daList[j - 1] = temp
      j = j - 1