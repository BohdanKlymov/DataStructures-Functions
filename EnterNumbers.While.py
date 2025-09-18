print("Write the random numbers, if you are finifed, write `done`")
n = 0
listOfNumbers = []

while n != "done":

    n = input()

    if n == "done":
        break
    else:
        print("Very nice, continue")
        listOfNumbers.append(int(n))

print(f"Here are your smallest number: {min(listOfNumbers)}")
print(f"Here are your largest number: {max(listOfNumbers)}")