age = int(input())
if age < 0:
    print("You are not born")
elif age < 12:
    print("Child")
elif age < 17:
    print("Teenager")
else:
    print("Adult")