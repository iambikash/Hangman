import csv
from pprint import pprint
from random import choice,randint
from termcolor import colored
dic={}
with open('Dict.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) #omit header
    for i in reader:
        dic[i[1]] = i[2]
playagain='Y'        
while True:
    if playagain=='N':
        print(colored('Please come back soon!!!','red'))
        break
    elif len(dic)==0:
        print(colored('Congrats you completed the level','red'))
        break
    else:    
        word_to_guess=choice(list(dic.keys()))
        word_len = len(word_to_guess)
        guesses_count = 0
        max_guess_cnt = int(word_len/2)
        word_meaning=dic[word_to_guess]
        word_in_screen = list('-' * len(word_to_guess))



        for i in range(int(word_len/3) + 1):
            display_letter_idx = randint(0, word_len - 1)
            word_in_screen[display_letter_idx] = word_to_guess[display_letter_idx]



        print(colored('The word for you is ::: ','red'))
        print(colored(''.join(word_in_screen),'blue'))
        print(colored('Find the word!!!','blue'))



        while guesses_count < max_guess_cnt:
            guess_ip= input(colored('Guess a letter :','red'))
            guess_ip=guess_ip.lower()
            if guess_ip in word_to_guess:
                replace_in_idx = [i for i, d in enumerate(word_to_guess) if d == guess_ip]
                for i in replace_in_idx:
                    word_in_screen[i] = guess_ip
                if word_to_guess == ''.join(word_in_screen):
                        print(colored('Congrats!!!','green'))
                        print(colored('You guessed "{}" correct.','green').format(word_to_guess),end ='')
                        print(colored('Meaning of "{}" is {}','green').format(word_to_guess,word_meaning))
                        print(colored('You WIN!!!','green'))
                        break
            else:
                guesses_count += 1
                if guesses_count == max_guess_cnt:
                    print(colored('You LOST!!!!','red'))
                    print(colored('The correct word was {}','green').format(word_to_guess))
                    continue
            print(''.join(word_in_screen))
        del dic[word_to_guess]
        print(colored('Do you wanna play again.','blue'))
        print(colored('Press Y to play again and N to quit ','red' ))
        playagain=input().upper()
               
