#pick random word
import random

#1. Setup
words = ["hello", "tiger", "code", "learn", "world"]
word = random.choice(words)
display = ['_'] * len(word) #shortcut: makes['_','_','_','_','_']
attempts = 6
guessed_letters =[]
print("Rules: Guess 1 letter at a time.6 wrong = lose.")

print("Welcome to Hangman!.")
print("Guess the word. you have 6 wrong guess.")

#2.Main Game loop
while attempts > 0 and '_' in display:
    print(" ".join(display))
    print("attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Guess a letter: ").lower()

   

    if guess in guessed_letters:
        print("You have already guessed that letter!")

    elif guess in word:
        print("correct!")
        guessed_letters.append(guess)
        #Reveal letter in display
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        attempts -=1
        print("Wrong guess!")
        print("attempts left:", attempts)
        

#3.Game Over

if '_' not in display:
    print("You won!")
else:
    print("You lost! The word was:",word)
    print("Final word was:", ' '.join(display))

    input("Press Enter to exit")