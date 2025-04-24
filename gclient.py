import socket
import random
import time

def start_game():
    host = "127.0.0.1"  # Server address (adjust if needed)
    port = 7777

    s = socket.socket()
    s.connect((host, port))

    # Step 1: Receive the banner or prompt from the server
    data = s.recv(1024)
    print(data.decode().strip())

    # Step 2: Bot randomly chooses difficulty (easy, medium, or hard)
    difficulty_choice = str(random.choice([1, 2, 3]))  # Randomly choose between 1 (easy), 2 (medium), or 3 (hard)
    print(f"Bot choosing difficulty: {difficulty_choice}")

    # Send the bot's chosen difficulty to the server
    s.sendall(difficulty_choice.encode())

    # Step 3: Receive confirmation or further instructions from the server
    data = s.recv(1024)
    print(data.decode().strip())

    # Step 4: Bot uses binary search algorithm to make guesses
    # Based on the difficulty, we determine the range
    if difficulty_choice == "1":  # Easy
        low = 1
        high = 10
    elif difficulty_choice == "2":  # Medium
        low = 1
        high = 50
    else:  # Hard
        low = 1
        high = 100

    # Step 5: Start binary search (Guessing process step-by-step)
    while True:
        # Bot calculates the middle point of the current range (binary search)
        guess = (low + high) // 2
        print(f"Bot guesses: {guess}")

        # Send the bot's guess to the server
        s.sendall(str(guess).encode())

        # Step 6: Wait for the server's response and adjust the guess accordingly
        reply = s.recv(1024).decode().strip()  # Wait for server response
        print(reply)

        # If the guess is correct, exit the loop
        if "CORRECT!" in reply:
            print("Bot guessed correctly!")
            break
        elif "Higher" in reply:  # If the guess is too low
            low = guess + 1  # Narrow the range to higher numbers
        elif "Lower" in reply:  # If the guess is too high
            high = guess - 1  # Narrow the range to lower numbers

        # Adding a small delay so the game feels more interactive
        time.sleep(1)

    s.close()

# Main game loop to allow the bot to play again or exit, with manual control
while True:
    start_game()

    # Ask the user if the bot should play again
    play_again = input("Do you want the bot to play again? (yes/no): ").strip().lower()

    if play_again == "no":
        print("Bot exits the game.")
        break
    elif play_again == "yes":
        print("Bot will play again...\n")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
