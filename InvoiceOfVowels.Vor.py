
text = input().upper()

vowels = "AIEOU"

amountOfVowels = 0

for x in text:
    if x in vowels:
        amountOfVowels += 1
        
print(amountOfVowels)