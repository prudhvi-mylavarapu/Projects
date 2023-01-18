import random

def guess(x):
    print("Guess the Number")
    rand=random.randint(1,x)
    guess=int(input())
    while guess!=rand:
        if guess < rand:
            guess=int(input("Sorry too low, guess again:"))
        elif guess> rand:
            guess=int(input("Sorry too high, guess again:"))
    print(f"congo, your guess is correct {guess}")

def computer(x):
    rand=0
    print('''Please suggest computer whether if its guess is correct by giving inputs as, 'H' if High, 'L' as Low and 'C' as correct guess.''')
    ll,hl=0,x
    output='a'
    while output!='c':
        rand=random.randint(ll,hl)
        print(f"is this your guess {rand}?")
        output= input("Is it High or Low:")
        if output=='h':
            hl=rand
        elif output=='l':
            ll=rand
    print(f"your guess number is {rand}")
            


computer(1000)

