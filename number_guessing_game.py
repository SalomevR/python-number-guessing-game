import random

def start_play():

    game_on = input('Do you want to play? Y or N.').upper()
    
    while True:
        
        if game_on not in ['Y','N']:
            game_on = input('I do not understand. Please choose Y or N').upper()
        else:
            if game_on == 'Y':
                print('Game On!')
                return True
            else:
                print('Goodbye :(')
                return False

def generate_number():

    secret = random.randint(1,100)
    return secret

def user_guess():

    guess = int(input('Enter your guess! (1 - 100)'))
    return guess

print('Guess the number!')

while start_play():

    secret = generate_number()
    max_guesses = 10
    guess_count = 0
    
    while guess_count < max_guesses:

        guess_count += 1
        print(f'Guess {guess_count} of {max_guesses}.')
        guess = user_guess()

        if guess == secret:
            break

        if guess < secret:
            print('Too low!')            
        elif guess > secret:
            print('Too high!')
    
    if guess == secret:
        print(f'Congrats! You guessed it in {guess_count} tries!')
    else:
        print(f'Sorry! You used up all {max_guesses} guesses. The number was {secret}.')
