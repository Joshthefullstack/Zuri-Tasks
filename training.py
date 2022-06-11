
import random

def play():
    user = input("What's your choice?: 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print("Computer's Choice is: " + computer)

    if user != "r" and user != "p" and user != "s":
        return "Not a valid option"
    elif user == computer:
        print("It's a tie")
    elif you_win(user, computer):
        print("You won")
    else:
        print("You lost")



def you_win(player, computer):
    # r > s, s > p, p > r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

play()







