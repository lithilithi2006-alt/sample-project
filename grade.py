# grade_checker.py

def grade_checker(marks):
    if marks >= 95:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

while True:
    marks = float(input("\nEnter student's marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter between 0 and 100.")
        continue
    print("Grade:", grade_checker(marks))

    cont = input("Do you want to check another grade? (y/n): ").lower()
    if cont != 'y':
        print("Exiting Grade Checker...")
        break