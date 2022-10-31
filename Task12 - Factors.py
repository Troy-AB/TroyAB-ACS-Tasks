value = int(input("Input a value"))

for i in range(1, value + 1):
    if value % i == 0:
        print(i)
