import random

def ropasi():
    
    print(''''r' for rock,'p' for paper,'s' for scissors''')
    user= input("Choose your Agent:")
    computer=random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a Tie'
    
    if is_win(user,computer):
        return 'Victory'
    
    return 'Defeat'
    
def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True


print(ropasi())
