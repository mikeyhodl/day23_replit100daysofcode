# def rollDice():
#   import random
#   dice = random.randint(1, 6)
#   print("You rolled", dice)
# rollDice()

# for i in range(100):
#   rollDice()

# def printMyName():
#   print("My Name is David")

# printMyName()

# def countToFive():
#   for i in range(1, 6):
#     print(i)

# countToFive()

# def countToFive():
#   for i in range(1, 6):
#     print(i)

# countToFive()

# def printfavoritecolor():
#   print("My favorite color is red.")

# printfavoritecolor()


def signin():
    while True:
        username = input("What is your username?: ")
        password = input("What is your password? ")
        if username == "mikee" and password == "0000":
            print("Welcome mikee!")
            break
        else:
            print("That is not the correct username or password. Try again!")
            continue
print("LOGIN SYSTEM")
signin()
