import sys
import random

EXP = 100

print("WELCOME TO THE LAST STOP")
print("You start with 100 EXP. Remember this when you make decisions.")

def check_death():
    global EXP
    if EXP <= 0:
        print("\n--- GAME OVER ---")
        print("Your EXP reached 0. You didn't survive the night.")
        print("\nPlease restart THE IBRAHIM GAME")
        sys.exit()

def choice_one():
    print("\nBegin Day One...")
    print("You are sat on the last bus at 12am. A strange man approaches you and asks you to follow him")
    enter = input("Do you go with him? (yes/no): ").lower()
    if enter == "yes":
        following()
    else:
        notFollowing()

def following():
    print("\nThe man takes you to a dirty room in a run-down backroom. Before you can react, he locks the door.")
    escape = input("You look around and see a tight vent and broken window. Which escape will you attempt? (vent/window): ").lower()
    if escape == "vent":
        vent()
    else:
        window()

def notFollowing():
    bag = input("\nYou don't follow the man, but he insists. You ignore his warnings. You get onto the crowded bus and sit down. A child places a black bag in the middle of the bus and runs off. Do you check the bag? (yes/no): ").lower()
    if bag == "yes":
        searchBag()
    else:
        ignoreBag()

def vent():
    global EXP
    escape_one = input("\nYou try to squeeze through the vent but its extremely small. Do you go anyway or do you turn around and take the window? (go anyway/turn around): ").lower()
    if escape_one == "turn around":
        window()
    else:
        damage = random.randint(40, 50)
        EXP -= damage
        print(f"You took damage. Your EXP is {EXP}")
        check_death()
        alleyway()

def window():
    global EXP 
    damage = random.randint(30, 40)
    EXP -= damage
    print(f"\nYou jump through the window and get cut all over your body. You took damage! Your EXP is {EXP}")
    check_death()
    alleyway()

def searchBag():
    global EXP
    print("\nYou approach the bag and unzip it slowly... and it's a large bundle of cash, a burner phone, and a picture of YOU outside your flat.")
    EXP += 15
    print(f"The money lifts your mood and gives you a boost! Your EXP is now {EXP}")
    EXP -= 20
    print(f"\nThe picture of you sends a shiver down your spine and you throw it away. Your EXP is now {EXP}")
    check_death()
    print("Suddenly, the phone starts ringing")
    pickPhone_up = input("Are you going to pick up the phone? (yes/no): ").lower()
    if pickPhone_up == "yes":
        print("\nYou ask who the man is. He doesn't answer but tells you to stay on the line")
        line = input("Will you stay on the line? (yes/no): ").lower()
        if line == "yes":
            print("\nAfter 30 seconds you realise he could be tracking you and quickly shut down the phone; it is too late...")
            print("You make it home")
            print(f"Congrats on surviving day one. Your EXP for the day is {EXP}")
    else:
        print("You decide its not meant for you")
        print("You make it home")
        print(f"Congrats on surviving day one. Your EXP for the day is {EXP}")

def ignoreBag():
    global EXP
    print("\nYou decide that its none of your business")
    print("The bus pulls up near your home and you rest for the night")
    print(f"Congrats on surviving day one. Your EXP for the day is {EXP}")

def alleyway():
    global EXP
    print("\nYou are now in a dark alleyway...")
    print("\nYou've been running for minutes now and the exit doesn't seem to be getting any closer...")
    damage = random.randint(30, 40)
    EXP -= damage
    print(f"\nYou are completely out of breath. Your EXP is now {EXP}")
    check_death()
    print("\nA man's silhouette sticks out in the distance. Its the man from the bus")
    print("\nHe turns and dissapears. You slowly creep into the area where he stood and to either side there are doors")
    direction = input("\nWill you turn left or right? ").lower()
    if direction == "right":
        escape()
    else:
        fight()
  
def escape():
    global EXP
    print("\nYou manage to escape, but barely. You stumble home for the night")
    print(f"Congrats on surviving day one. Your EXP for the day is {EXP}")

def fight():
    global EXP
    print("\nThe man grabs you by the throat!")
    action = input("\nWill you punch him to try escape or will you kick him away? (punch/kick): ").lower()
    if action == "punch":
        print("You fail to generate any power and the man squeezes...")
        EXP -= 100
        check_death()
    else:
        print("\nYou kick him in the stomach and he reels backwards!")
        print("\nYou find your way towards the exit and stumble home")
        print(f"Congrats on surviving day one. Your EXP for the day is {EXP}")

choice_one()
