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

    secret = random.randint(1,20)
    return secret

def user_guess():

    guess = int(input('Enter your guess! (1 - 20): '))
    return guess

print('Guess the number!')

while start_play():

    secret = generate_number()

    guess = user_guess()
    
    while guess != secret:
        
        if guess < secret:
            print('Too low!')
            guess = user_guess()
            
        elif guess > secret:
            print('Too high!')
            guess = user_guess()

    print('Congrats! You guessed it!')
