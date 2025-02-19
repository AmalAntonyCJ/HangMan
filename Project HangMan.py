import random

def Car():
    Car = [ 'Maruti' , 'Maybach', 'Volkswagen', 'Hyundai' ]
    return random.choice(Car)

def play():
    chance = 10
    word = Car()
    letters = []  
    total_word = len(word)

    print(f"The selected  word has {total_word} letters")
    
    while chance > 0  :
        
        current_state = ''.join([letter if letter in letters else '_' for letter in word])
        print("Current word: ", current_state)
        
        if current_state == word:  
            print("You won!")
            return
        
        guess = input("Enter your guess,one letter at a time ").lower()
        
        if len(guess) != 1: 
            print("Please enter only one letter.")

            continue
        if guess.isnumeric ==True:
            print("Please enter alphabets only")
            continue
        
        if guess in letters:
            print("You've already guessed that letter.")
            continue
        
        letters.append(guess)  
        
        if guess not in word:
            chance -= 1
            print(f"Incorrect guess! You have {chance} chances left.")
        else:
            print("Good guess!")

    print(f"You lost! The word was '{word}'.")

play()