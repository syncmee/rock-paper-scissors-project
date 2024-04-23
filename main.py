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

print("Welcome to Play Rock Paper Scissors")
user_input = input("Choose between Rock, Paper & Scissors\n")
letter = user_input[0].lower()
rps = [rock, paper, scissors]
lenght_rps = len(rps)
random_rps = random.randint(0, 2)

if letter == "r" and random_rps == 0:
  print(rps[random_rps])
  print("Its Rock\nIts A Draw!")
elif letter == "r" and random_rps == 2:
  print(rps[random_rps])
  print("Its Scissors\nYou Win!")
elif letter == "r" and random_rps == 1:
  print(rps[random_rps])
  print("Its Paper\nYou Lose!")
elif letter == "p" and random_rps == 0:
  print(rps[random_rps])
  print("Its Rock\nYou Win!")
elif letter == "p" and random_rps == 2:
  print(rps[random_rps])
  print("Its Scissors\nYou Lose!")
elif letter == "p" and random_rps == 1:
  print(rps[random_rps])
  print("Its Paper\nIts A Draw!")
elif letter == "s" and random_rps == 0:
  print(rps[random_rps])
  print("Its Rock\nYou Lose!")
elif letter == "s" and random_rps == 2:
  print(rps[random_rps])
  print("Its Scissors\nIts A Draw!")
elif letter == "s" and random_rps == 1:
  print(rps[random_rps])
  print("Its Paper\nYou win!")
