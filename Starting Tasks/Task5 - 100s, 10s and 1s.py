#take input
value = int(input("Enter value between 100-999"))

#calculate the hundreds, tens and units
hundreds = value //100
value = value - (hundreds*100)
tens = value//10
value = value - (tens*10)
units = value // 1

#print output
print(hundreds, "hundreds", tens, "tens", units, "units")