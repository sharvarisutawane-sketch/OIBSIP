def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=" * 40)
    print("          BMI CALCULATOR")
    print("=" * 40)

    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in metres: ")

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("\\nYour BMI is:", round(bmi, 2))
    print("Category:", category)

if __name__ == "__main__":
    main()
