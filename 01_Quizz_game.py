print("Welcome to my computer Quizz game! ")
print("")
playing = input("Are you intrested for playing Quizz game ? = yes / no : ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game :)")
print("")

score = 0

Q1 = input("Q1.ALU stands for? : ")
if Q1.lower() == "arithmetic logical unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("")


Q2 = input("Q2.The brain of any computer system is? : ")
if Q2.lower() == "cpu":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("")


Q3 = input("Q3.What does CPU stand for? : ")
if Q3.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("")


Q4 = input("Q4.What does RAM stand for? : ")
if Q4.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("")

print(f"Your score is {score} out of 4")
print(f"You got {(score/4)*100} %")