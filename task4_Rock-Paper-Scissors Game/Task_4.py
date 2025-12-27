"""
1 = Rock
0 = Paper
2 = Scissor
"""

import random


PlayerScore = 0
ComputerScore = 0


dic = {1: "Rock", 0: "Paper", 2: "Scissor"}
reverse_dic = {"rock": 1, "paper": 0, "scissor": 2}

computer = random.choice([0, 1, 2])
youstr = input("Enter Your Choice\n").lower()
if youstr not in reverse_dic:
    print("Invalid Choice!")
else:
    you = reverse_dic[youstr]

    print(f"\nThe computer's choice is {dic[computer]} and your choice is {dic[you]}")

    if (
        (computer == 1 and you == 2)
        or (computer == 0 and you == 1)
        or (computer == 2 and you == 0)
    ):
        print("Computer Win")
        ComputerScore += 1

    elif (
        (computer == 1 and you == 0)
        or (computer == 2 and you == 1)
        or (computer == 0 and you == 2)
    ):
        print("You Win")
        PlayerScore += 1

    elif you == computer:
        print("It's a Tie")


print(f" Score = {PlayerScore} : {ComputerScore}")
