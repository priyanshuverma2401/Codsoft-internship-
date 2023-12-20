import random
import string
import time

def generate_password(length, complexity):
    characters = ""

    if "uppercase" in complexity:
        characters += string.ascii_uppercase
    if "lowercase" in complexity:
        characters += string.ascii_lowercase
    if "digits" in complexity:
        characters += string.digits
    if "special" in complexity:
        characters += string.punctuation

    if not characters:
        print("Error: Please choose at least one complexity option.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Password Generator")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        print("\nChoose complexity options:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Digits")
        print("4. Special characters")
        print("5. Mix all options")
        time.sleep(3)

        complexity_options = {
            "1": "uppercase",
            "2": "lowercase",
            "3": "digits",
            "4": "special",
            "5": "uppercase lowercase digits special"
        }

        while True:
            choice = input("Enter t51he number(s) of the desired complexity options (e.g., 123): ")
            chosen_complexities = set(complexity_options.get(char, "") for char in choice)

            if all(chosen_complexities):
                break
            else:
                print("Invalid input. Please enter valid numbers.")

        # Generate and display the password
        password = generate_password(length, chosen_complexities)
        if password:
            print(f"\nGenerated Password: {password}")
        time.sleep(2)


if __name__ == "__main__":
    main()
