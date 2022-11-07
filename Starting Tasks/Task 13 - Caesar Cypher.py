word = input("Enter word to be cyphered: ")
shift = int(input("Enter shift value: "))

for i in range(len(word) + 1 ):
    word[i] = chr(int(ord(word[i])) + shift)

print(word)