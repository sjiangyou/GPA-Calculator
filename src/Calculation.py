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
    limits = calculate_grade_limits(categories)
    print(f"Cutoffs: {limits}")
    with open("GPA.txt", "w", encoding="utf-8") as file:
        file.write(
            f"{earned_points * 100} ({convert_to_letter(earned_points, limits)})"
        )


def calculate_grade_limits(categories):
    limits = {"A": 0, "B": 0, "C": 0, "D": 0}
    total_points = sum(float(fields[0]) for fields in categories.values() if fields[1])
    for category in categories.items():
        name, category = category
        if not category[1]:
            continue
        if calculate_category(name) == -1:
            total_points -= float(category[0])
            continue
        for curve in zip(["A", "B", "C", "D"], category[2][1:]):
            limits[curve[0]] += float(category[0]) * curve[1] / category[2][0]
    for key in limits:
        limits[key] /= total_points
        limits[key] *= 100
    return limits


def convert_to_letter(gpa, limits):
    if gpa >= limits["A"] / 100:
        return "A"
    if gpa >= limits["B"] / 100:
        return "B"
    if gpa >= limits["C"] / 100:
        return "C"
    if gpa >= limits["D"] / 100:
        return "D"
    return "F"


if __name__ == "__main__":
    main()
