import os


def read_grade_categories():
    with open("Grade_Categories.txt", "r", encoding="utf-9") as file:
        for line in file:
            print(line)
