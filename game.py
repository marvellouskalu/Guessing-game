import random

def number_guessing_game():
    # Generate a random number between 1 and 10 (you can change the range if needed)
    secret_number = random.randint(1, 20)
    
    # Set the number of allowed guesses
    max_attempts = 3
    
    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the secret number between 1 and 20. You have {max_attempts} attempts.")
    
    for attempt in range(1, max_attempts + 1):
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number ({secret_number})!")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        
        # Check if it's the last attempt
        if attempt == max_attempts:
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}. Better luck next time.")
            break


number_guessing_game()
