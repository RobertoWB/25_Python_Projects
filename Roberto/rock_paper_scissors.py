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


print(play())