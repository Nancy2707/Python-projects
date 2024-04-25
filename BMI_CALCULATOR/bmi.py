def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Example usage
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}")
