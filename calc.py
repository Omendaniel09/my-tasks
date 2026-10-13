def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 61:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F" 


while True:
    name = input("Enter student's name: ")

    math = float(input("Enter Mathematics score: "))
    english = float(input("Enter English score: "))
    physics = float(input("Enter Physics score: "))

    average = (math + english + physics) / 3

    grade = calculate_grade(average)

    if average >= 85:
        status = "distinction"
    elif average >= 45:
        status = "passed"
    else:
        status = "failed"

    print("\nName:", name)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Status:", status)

    again = input("\nCalculate another result? (yes/no): ")

    if again.lower() != "yes":
        print("Goodbye!")
        break