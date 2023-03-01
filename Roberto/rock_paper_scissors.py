import random 

def play():
    user = input("What's your choise? 'r' for a rock, 'p' for paper, 's' for scissors :")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
        
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You Lost!'



def is_win(player, opponent):
    # return true if player wins 
    # r > s, s > p, p > r
    print(f'{player} vs {opponent}')
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
 

def play_until_win():
    lost = True
    cont = 1
    while lost == True:
        user = input("What's your choise? 'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r','p','s'])
        print(f'{user} vs {computer}')
        if(user == 's' and computer == 'r') or (user == 'p' and computer == 's') or (user == 'r' and computer == 'p'):
            print('You lost!!, try again')
            lost = True
            cont += 1
        elif user == computer:
            print('This was a Tie, try again')
            lost = True
            cont += 1
        else:
            if cont == 1:
                print ('One match one win, what a lucky guy')
                lost = False 
            else:
                print(f'You finally won, it took you {cont} matches to win')
                lost = False

play_until_win()

        








