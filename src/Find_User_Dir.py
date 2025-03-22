import os
import pathlib


def find(class_name):
    classes_dir = str(pathlib.Path(__file__).parent.parent / "Classes")
    os.chdir(classes_dir)
    try:
        os.chdir(class_name)
        return os.getcwd()
    except FileNotFoundError:
        if os.name == "posix":
            os.system(f"cp -r Template {class_name}")
            os.chdir(class_name)
            return os.getcwd()
        if os.name == "nt":
            os.system(f"copy Template {class_name} /E /I")
            os.chdir(class_name)
            return os.getcwd()


if __name__ == "__main__":
    import sys

    print(find(sys.argv[1]))
