text = input()

n = "1234567890"

amountOfNumbers = 0

for x in text:
    if x in n:
        amountOfNumbers += 1

print(f"The number of digits {amountOfNumbers}")
