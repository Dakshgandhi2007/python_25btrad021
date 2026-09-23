def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i+1}:")
    name = input("  Name: ")
    marks = float(input("  Marks (out of 100): "))
    grade = get_grade(marks)
    print(f"  {name} scored {marks:.2f} — Grade: {grade}")
