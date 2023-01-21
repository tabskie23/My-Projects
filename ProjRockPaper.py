import random

print("Welcome to the final project of Day ")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor]
user = int(input('What do you choose? Type "0" for Rocks, "1" for Paper or "2" for Scissors \n'))
if user >=3 or user < 0:
    print("You type invalid number")
else:
    print(game_images[user])
    
    print("Computer chooce:")
    random_computer = random.randint(0, 2)

    print(game_images[random_computer])

    if user == 0 and random_computer == 2:
        print("Player win")
    elif random_computer == 0 and user == 2:
        print("Computer Win")
    elif user > random_computer:
        print("Player win")
    elif random_computer > user:
        print("Computer Win")
    elif random_computer > user:
        print("Computer Win")  
    elif user == random_computer:
        print("Its a draw") 

 
