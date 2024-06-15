print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to the treasure island")
print("Your task is to survive the dangerous conditions and find the treasure.")
way = input("Choose which way you want to go : LEFT or RIGHT\n"). lower()
if way == "left":
    do = input("You see a lake infront of you leading you closer to the treasure. Would you like to swim or wait for a boat\n").lower()
    if do == "wait":
        print("You traveled to the other side of the lake safely. CONGRATULATIONS!")
        choose = input("There are 3 gates in front of you and only one of them leads to treasure. Which one would you choose? Red, Yellow or Blue. Choose wisely!!\n").lower()
        if choose == "yellow":
            print("Congratulations!! you got the treasure!!")
        elif choose == "red":
            print("You got eaten by wild beasts. Game Over")
        elif choose == "blue":
            print("You got swallowed by fire. Game Over")
        else:
            print("You did not choose any of the above gates and hence fall victim to souls of the many who tried to get their hands on the treasure that you wanted to.")
    elif do =="swim":
        print("Lake you try to swim in is infested with deadly crocodiles, you fall prey to them and die. GAME OVER")
    else:
        print("Wrong decision, you fall prey to a beast")
else:
    print("You fell into a mountain ditch and die! GAME OVER")