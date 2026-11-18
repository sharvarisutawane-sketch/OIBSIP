import random
import string

def main():
    print("=" * 42)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 42)

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    print("\\nChoose at least two character types:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    choices = input("Enter choices separated by commas (example: 1,2,3): ")
    selected = set(choices.replace(" ", "").split(","))

    groups = []
    if "1" in selected:
        groups.append(string.ascii_uppercase)
    if "2" in selected:
        groups.append(string.ascii_lowercase)
    if "3" in selected:
        groups.append(string.digits)
    if "4" in selected:
        groups.append("!@#$%^&*()-_+=")

    if len(groups) < 2:
        print("Please select at least two valid character types.")
        return

    if length < len(groups):
        print("Password length is too short for the selected types.")
        return

    password_chars = [random.choice(group) for group in groups]
    all_characters = "".join(groups)

    password_chars += [
        random.choice(all_characters)
        for _ in range(length - len(password_chars))
    ]
    random.shuffle(password_chars)

    print("\\nGenerated Password:", "".join(password_chars))

    while input("\\nGenerate another password? (y/n): ").lower() == "y":
        password_chars = [random.choice(group) for group in groups]
        password_chars += [
            random.choice(all_characters)
            for _ in range(length - len(password_chars))
        ]
        random.shuffle(password_chars)
        print("Generated Password:", "".join(password_chars))

if __name__ == "__main__":
    main()
