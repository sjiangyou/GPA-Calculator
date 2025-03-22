import os


def read_grade_categories() -> dict:
    with open("Grade_Categories.csv", "r", encoding="utf-8") as file:
        categories = {}
        for idx, line in enumerate(file):
            if idx == 0:
                continue
            fields = line.strip().split(",")
            categories[fields[0]] = fields[1], not eval(fields[2])
        return categories


def calculate_category(category):
    with open(f"{category}.csv", "r", encoding="utf-8") as file:
        earned_points = 0
        total_points = 0
        for idx, line in enumerate(file):
            if idx == 0:
                continue
            fields = line.strip().split(",")
            earned_points += float(fields[1])
            total_points += float(fields[2])
        return earned_points / total_points
