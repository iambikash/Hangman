import csv
from pprint import pprint
from random import choice,randint
dic={}
with open('Dict.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) #omit header
    for i in reader:
        dic[i[1]] = i[2]
word_to_guess=choice(list(dic.keys()))
word_len = len(word_to_guess)
guesses_count = 0
max_guess_cnt = int(word_len/2)
word_meaning=dic[word_to_guess]
word_in_screen = list('-' * len(word_to_guess))

 

for i in range(int(word_len/3) + 1):
    display_letter_idx = randint(0, word_len - 1)
    word_in_screen[display_letter_idx] = word_to_guess[display_letter_idx]

 

print('The word for you is ::: ')
print(''.join(word_in_screen))
print('Find the word!!!')

 

while guesses_count < max_guess_cnt:
    guess_ip= input('Guess a letter :')
    guess_ip=guess_ip.lower()
    if guess_ip in word_to_guess:
        replace_in_idx = [i for i, d in enumerate(word_to_guess) if d == guess_ip]
        for i in replace_in_idx:
            word_in_screen[i] = guess_ip
        if word_to_guess == ''.join(word_in_screen):
                print('Congrats!!!')
                print('You guessed "{}" correct. Meaning of "{}" is {}'.format(word_to_guess,word_to_guess,word_meaning))
                print('You WIN!!!')
                break
    else:
        guesses_count += 1
        if guesses_count == max_guess_cnt:
            print('You LOST!!!!')
    print(''.join(word_in_screen))