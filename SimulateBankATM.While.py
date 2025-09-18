balanz = 1000
 
print("Your start balanz is 1000$")
print("Withdraw: 1, Deposit: 2, Exit: 3")

userEntry = input()

while userEntry != 3: 
    if userEntry == "1":
        print("Write your deposit: ")
        depo = int(input())
        if depo > balanz:
            print("Not enough money")
        else:
            balanz -= depo
            print("Your balanze has been changed")
    elif userEntry == "2":
        if balanz < 0:
            print("Your balanz is zero!") 
        print(f"Your balanz: {balanz}")
    elif userEntry == "3":
        print("Bye, see you!")
        break

    print("Something else? 1, 2 or 3")
    userEntry = input()

