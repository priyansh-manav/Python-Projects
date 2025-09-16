import random
print("Let's Start the number guessing game :)")

while True:
    random_num = random.randrange(11)
    num = int(input("Enter the number between 1 to 10 : "))
    if num == random_num:
        print("YO! you win!")
        print(f"You chose : {num}")
        print(f"Computer chose : {random_num}")
        break
    else:
        print("You loss!")
        print("Try again")
        print(f"You chose : {num}")
        print(f"Computer chose : {random_num}")
