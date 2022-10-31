#input values
val1 = int(input("Enter Value 1: "))
val2 = int(input("Enter Value 2: "))

if val1 > val2:
    highest = val1
    lowest = val2
else:
    highest = val2
    lowest = val1
#endif

#print values
print(highest, lowest)