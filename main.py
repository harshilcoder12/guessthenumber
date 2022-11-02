from art import logo
import random
print(logo)

def generate_number():
    num_lst = []
    for i in range(1,101):
        num_lst.append(i)
    global num 
    num = random.choice(num_lst)
    

print('welcome')
level = input('Enter the level easy/hard: ')
if level == 'easy':
    is_game_over  = False
    tries = 10
    generate_number()
    while tries > 0 and is_game_over == False:
        ask_usr = int(input(f"you have {tries} attempts remaining , please enter the number: "))
        if ask_usr > num:
          print('TOO HIGH')
          tries  = tries - 1
          is_game_over = False
        elif ask_usr < num:
            print('TOO LOW')
            tries = tries-1
            is_game_over = False
        else:
            print('you won ')
            is_game_over = True
elif level == 'hard':
    is_game_over  = False
    tries = 5
    generate_number()
    while tries > 0 and is_game_over == False:
        ask_usr = int(input(f"you have {tries} attempts remaining , please enter the number: "))
        if ask_usr > num:
          print('TOO HIGH')
          tries  = tries - 1
          is_game_over = False
        elif ask_usr < num:
            print('TOO LOW')
            tries = tries-1
            is_game_over = False
        else:
            print('you won ')
            is_game_over = True

