import random  # I use this to generate a random number

# This function lets me generate a number based on the difficulty the player chose
def generate_random(difficulty):
    if difficulty == 1:
        return random.randint(1, 10)     # If it's easy, I return a number between 1 and 10
    elif difficulty == 2:
        return random.randint(1, 50)     # If it's medium, I return a number between 1 and 50
    elif difficulty == 3:
        return random.randint(1, 100)    # If it's hard, I return a number between 1 and 100
    else:
        raise ValueError("Invalid difficulty level")  # I added this to catch wrong inputs

# I use this function to ask the player to choose the difficulty
def get_difficulty(conn):
    # I send instructions to the client so they can choose the level
    conn.sendall(b"Choose difficulty:\n1 - Easy (1 to 10)\n2 - Medium (1 to 50)\n3 - Hard (1 to 100)\n")
    while True:
        data = conn.recv(1024).decode().strip()  # I receive and clean the input from the client
        if data in ["1", "2", "3"]:              # I check if the input is valid
            return int(data)                     # I convert it to an integer and return it
        else:
            conn.sendall(b"Invalid input. Please enter 1, 2, or 3.\n")  # I tell the client to try again if input is wrong

# This function gives feedback if the player's guess is low, high, or correct
def provide_feedback(guess, target):
    if guess < target:
        return "Too low!"       # I return this if their guess is too low
    elif guess > target:
        return "Too high!"      # I return this if their guess is too high
    else:
        return "Correct!"       # If they guessed right, I return this

# I use this function to check if the input is a valid number
def is_valid_guess(guess):
    return guess.isdigit()      # I make sure the guess is a digit (not a letter or symbol)
