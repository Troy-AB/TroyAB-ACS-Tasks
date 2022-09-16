#input values

val1 = int(input("Enter Value 1: "))
val2 = int(input("Enter Value 2: "))
val3 = int(input("Enter Value 3: "))

if val1 > val2 and val1 > val3:
    highest = val1
    if val2 > val3:
        mid = val2
        lowest = val3
    else:
        mid = val3
        lowest = val2
    #endif
elif val2 > val1 and val2 > val3:
    highest = val2
    if val1 > val3:
        mid = val1
        lowest = val3
    else:
        mid = val3
        lowest = val1
    #endif
else:
    highest = val3
    if val1 > val2:
        mid = val1
        lowest = val2
    else:
        mid = val2
        lowest = val
    #endif
#endif

print(highest, mid, lowest)
