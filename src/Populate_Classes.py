import os
from Find_User_Dir import find


def create_categories_file(course):
    category, points, extra = "start", "0", "False"
    while category.lower() != "done":
        category = input("Category Name (or 'done' to finish): ")
        if category.lower() == "done":
            break
        points = input(f"Points for {category}: ")
        extra = input(f"Is {category} extra credit? (True/False): ")
        with open("Grade_Categories.csv", "a", encoding="utf-8") as file:
            file.write(f"{category},{points},{extra}\n")


def make_class_categories(course):
    categories = set()
    with open("Grade_Categories.csv", "r", encoding="utf-8") as file:
        for idx, line in enumerate(file):
            if idx == 0:
                continue
            fields = line.strip().split(",")
            categories.add(fields[0])
    for category in categories:
        with open(f"{category}.csv", "w", encoding="utf-8") as file:
            file.write("Assignment,Grade,Total\n")


if __name__ == "__main__":
    course = input("Course Name: ")
    os.chdir(find(course))
    create_categories_file(course)
    make_class_categories(course)
