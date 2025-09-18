password = "not_python123"

while password != "python123":

    print("Write your password:")
    password = input()

    if password == "python123":
        print("Access granted!")
    else:
        print("The password is incorrect, try agein")