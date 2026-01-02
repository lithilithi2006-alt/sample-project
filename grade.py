# Function to check grade based on marks
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

# Input from user
marks = float(input("Enter the student's marks (0-100): "))

# Display grade
print("Grade:", grade_checker(marks))