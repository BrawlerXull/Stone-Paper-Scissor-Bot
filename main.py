
import random

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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]
random_output=random.randint(0,2)

your_choice=int(input("Enter your number 0 for ROCK 1 for PAPER 2 for SCISSORS : "))
if your_choice>=0 and your_choice<3 :
  print(game_images[your_choice])
  print(game_images[random_output])

if your_choice>=3 or your_choice<0:
  print("U ENTERED INVALID NUMBER !! YOU LOST :)")

elif your_choice==random_output:
  print("IT'S A DRAW")

elif your_choice==0 and random_output==1:
  print("YOU LOST")

elif your_choice==1 and random_output==2:
  print("YOU LOST")

elif your_choice==2 and random_output==0:
  print("YOU LOST")

else:
  print("YOU WON")
  
