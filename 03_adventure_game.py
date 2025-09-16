print("Welcome to my computer Adventure game! ")
print("------------------------------------------------")
user = input("Are you intrested for playing Adventure game ? = yes / no : ")

if user.lower() != "yes":
    quit()

print("Okay! Let's play the game :)")
print("------------------------------------------------")

print("You are walking down a lonely road at night. The road ends, and you see two paths:")
game = input("""Left → A narrow trail into the forest.
Right → An abandoned old mansion. : """)
print("------------------------------------------------")

if(game == "left"):
    print("You step into the forest. The trees are tall and the wind howls.")
    print("After a while, you notice a glowing sword lying on the ground.")
    q1 = input("Now, You have 2 choice : pick the sword | leave the sword, which option you chose ? =  ").lower()
    print("------------------------------------------------")

    if(q1 == "pick the sword"):
        print("""A wild beast suddenly attacks you.
You fight with the sword and defeat the beast.
Behind the beast’s den, you find a treasure chest filled with gold.
You survived and found the treasure! 🎉""")
        

    elif(q1 == "leave the sword"):
        print("""You walk deeper into the forest.
The same wild beast attacks you.
Without a weapon, you try to run but get caught.
The beast kills you. 💀 Game Over.""")
        print("------------------------------------------------")

    else:
        print("Not a valid option. you lose!")

elif(game == "right"):
    print("------------------------------------------------")
    print("You approach the mansion. The gate creaks open. Inside, it’s cold and dark.")
    print("On a dusty table, you find an old diary.")
    q2 = input("Now, You have 2 choice : read the diary | ignore the diary = ").lower()
    print("------------------------------------------------")

    if(q2 == "read the diary"):
        print("""The diary says: “A secret lies behind the old painting on the wall.”
You search, find the painting, and push it aside.
A hidden door opens to a room full of jewels.
 You discovered the mansion’s hidden treasure! 🎉""")
    elif(q2 == "ignore the diary"):
        print("""You keep exploring the mansion.
Suddenly, all doors slam shut. A ghostly figure appears.
The ghost traps you inside forever.
Your soul is taken. 💀 Game Over.""")
        print("------------------------------------------------")

    else:
        print("Not a valid option. you lose!")    
else:
    print("Not a valid option. you lose!")    