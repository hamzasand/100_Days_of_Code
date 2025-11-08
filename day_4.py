rock  ='''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

   '''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

secissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
import random
game_image = [rock,secissor,paper]
ply_sel =int(input("Please select 0 for rock 1 for secissor and 2 for paper"))
print("player select:", game_image[ply_sel])
com_sel = random.randint(0,2)
print("computer selected:",game_image[com_sel])

if ply_sel >= 3 or ply_sel < 0:
    print("You chose invalid number")
elif ply_sel == 0 and com_sel == 2:
    print("you win!")
elif ply_sel == 2 and com_sel == 0:
    print("You lose!")
elif com_sel > ply_sel:
    print("You lose!")
elif ply_sel > com_sel:
    print("You win!")
elif com_sel == ply_sel:
    print("its draw!")
