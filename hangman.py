
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
#word_list=["aardvark","baboon","camel"]
#chosen_word=word_list[random.randint(0,len(word_list)-1)]
#print(chosen_word,len(chosen_word))

chosen_word=random.choice(word_list)
print(chosen_word)
#guess=input("What is the letter : ").lower()
#print(guess)
#guess_word=""
#count_tr=0
#for letter in range(0,len(chosen_word)):


#for letter in chosen_word:
#    if letter==guess:
#        guess_word+=letter
#    else:
#        guess_word +="_"
#print(guess_word)



game_over= False
corrcet_letters=[]
lives=6
print(logo)
while not game_over:
    guess = input("What is the letter : ").lower()
    if guess in corrcet_letters:
        print(f"you guessed the letter {guess}")
    guess_word = ""
    for letter in chosen_word:
            if letter == guess:
                guess_word += letter
                corrcet_letters.append(guess)
            elif letter in corrcet_letters:
                guess_word += letter
            else:
                guess_word += "_"
    print(guess_word)
    if guess not in chosen_word:
        lives-=1
        print("Your lives left: ",lives)
        if lives==0:
            game_over= True
            print("-------------------------------------------Game Over, You Lose!-------------------------------------------------")
    if "_" not in guess_word:
        game_over= True
        print("-----------------------------------------Congratulations! You win!-----------------------------------------------")
    print(stages[lives])