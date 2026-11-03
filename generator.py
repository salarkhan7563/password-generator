import random
import string

def generate_password(length=12):
    """Generates a password of the given length"""
    # Combine letters, difits and symbol into a big pool of characters
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)
    return password

def check_strength(password):
    """Evaluates the strength of a password"""
    score = 0
    feedback = []

    # Rule 1: Length Check
    if len(password) > 100:
        print("Holy! Thats a Strong password!!!")
        score += 8
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Make your password stronger. (Recomended length 12+)")
    else:
        feedback.append("Password too short. (More then 8 required)")

    # Rule 2: Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Your password must contain atleast 1 number.")

    # Rule 3: Check for punctuations
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Your password must contain atleast 1 symbol.")
    return score, feedback

def main():
    while True:
        print("\n=== Secure Password Tool ===")
        print("1. Generate a Secure Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            try:
                length_input = input("Enter your desired password length: ")
                length = int(length_input) if length_input else 12
            except ValueError:
                length_input = 12

            pwd = generate_password(length)
            print(f"\nGenerated password {pwd}")

            score, feedback = check_strength(pwd)
            print(f"Strength Score: {score}/4")

        elif choice == '2':
            pwd = input("Enter your password to test: ")
            score, feedback = check_strength(pwd)
            print(f"Strength Score: {score}/4")
            if feedback:
                print("Improvement Tips: ")
                for tip in feedback:
                    print(f" - {tip}")
            else: 
                print("Excellent! This password is very strong.")
        elif choice == "3":
            print("Stay Secure! GoodBye")
            break
        else:
            print("Invalid choice. Please pick 1, 2 or 3")


if __name__ == "__main__":
    main()

