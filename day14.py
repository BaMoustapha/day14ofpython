from art import logo, vs
from data import data
import random

def format_data(account):
    """Format the account data into a printable string."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Compare follower counts and check if the user's guess is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Display the logo at the start of the game
print(logo)

# Initialize score and game continuation flag
score = 0
game_should_continue = True

# Randomly select account B at the start
account_b = random.choice(data)

# Game loop
while game_should_continue:
    # Make account A the previous account B
    account_a = account_b
    # Select a new account B until it's different from account A
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Print the accounts' info
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    # Check if the guess is correct
    is_correct = check_answer(guess, a_followers, b_followers)

    # Give feedback to the user and update the score
    if is_correct:
        score += 1
        print(f"Congratulations! You guessed correctly. Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
