import random

def number_quest():
    print("🎮 Welcome to NUMBER QUEST!")
    print("Guess the secret number and win the game 🎯\n")

    print("Choose Difficulty:")
    print("1. Easy (1–20)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        max_num = 20
        lives = 7
    elif choice == "2":
        max_num = 50
        lives = 6
    else:
        max_num = 100
        lives = 5

    secret = random.randint(1, max_num)

    print(f"\nYou have {lives} lives. Let’s begin! 🚀\n")

    while lives > 0:
        try:
            guess = int(input(f"Guess a number between 1 and {max_num}: "))

            if guess < 1 or guess > max_num:
                print("❌ Out of range! Try again.\n")
                continue

            if guess == secret:
                print(f"🎉 BOOM! You guessed it right: {secret}")
                return

            difference = abs(secret - guess)

            if difference <= 4:
                print("🎯 You are TOO CLOSE to the number!")
            elif difference <= 8:
                print("🙂 You are close, keep trying.")
            else:
                print("📉 You are FAR from the number.")

            lives -= 1
            print(f"Lives left: {lives}\n")

        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    print(f"😢 Game Over! The number was {secret}")

# Start the game
number_quest()
