import random

def hangman(word):
    lives, wordlis, copyword = 6, [], list(word)
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("lives left : 6")
    
    for i in range(len(word)):                                                    # making of dashed guess 
        wordlis.append("_")
    print("".join(wordlis))
    print(", ".join(alpha))

    while  "".join(wordlis)!=word and lives!=0:
        print("Your Guess:")
        letter= input()
        
        if letter not in word:                                                    # if wrong guess
            print("wrong guess")
            lives-=1
            print("lives left: ", lives)
            print("".join(wordlis))
            alpha.remove(letter)
            print(", ".join(alpha))
        
        elif letter in word and word.count(letter)==1:                            # if letter occurs once
            wordlis.pop(word.index(letter))
            wordlis.insert(word.index(letter), letter)
            print("lives left: ", lives)
            print("".join(wordlis))
            alpha.remove(letter)
            print(", ".join(alpha))
        
        else:                                                                    # if letter occurs multiple times
            indexs=[]                                                                                       
            for k,ele in enumerate(word):
                if ele == letter:
                    indexs.append(k)
            for j in indexs:
                wordlis.pop(j)
                wordlis.insert(j, letter)
            print("lives left: ", lives)
            print("".join(wordlis))
            alpha.remove(letter)
            print(", ".join(alpha))
    if lives==0:
        print("The Man Died")
        print("Better luck next time")
    else:
        print("Congratulation")
        print("Perfect Guess")



f=open("words.txt", 'r')
ch = f.read()
lisofwords = list(ch.split("\n"))
f.close()
word= random.choice(lisofwords)
hangman(word)