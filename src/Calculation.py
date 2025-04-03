import os
from File_Inputs import read_grade_categories, calculate_category
from Find_User_Dir import find


def main():
    course = input("Course Name: ")
    os.chdir(find(course))
    categories = read_grade_categories()
    total_points = sum(float(fields[0]) for fields in categories.values() if fields[1])
    earned_points = 0
    for category in categories.items():
        category_points = calculate_category(category[0])
        if category_points == -1:
            total_points -= float(category[1][0]) if category[1][1] else 0
            continue
        earned_points += category_points * float(category[1][0])
    earned_points /= total_points
    print(f"Grade: {earned_points}")
    with open("GPA.txt", "w", encoding="utf-8") as file:
        file.write(f"{earned_points * 100} ({convert_to_letter(earned_points)})")

def convert_to_letter(gpa):
    if gpa >= 0.9:
        return "A"
    if gpa >= 0.8:
        return "B"
    if gpa >= 0.7:
        return "C"
    if gpa >= 0.6:
        return "D"
    return "F"


if __name__ == "__main__":
    main()
