import os
from File_Inputs import *
from Find_User_Dir import *


def main():
    course = input("Course Name: ")
    os.chdir(find(course))
    read_grade_categories()


if __name__ == "__main__":
    main()
