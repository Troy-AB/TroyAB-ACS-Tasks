#take input
integer = int(input("enter integer"))
divisor = int(input("enter divisor"))

#calculate integer division and remainder
division = integer // divisor
remainder = integer % divisor

#print output
print(division, "remainder", remainder)