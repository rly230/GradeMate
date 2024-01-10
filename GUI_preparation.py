from modules.java_utils import add_package_name
from modules.utilities import add_str
from modules.utilities import rename_folders


def main():
    rename_folders("data")
    add_str("data")
    add_package_name("data")


if __name__ == "__main__":
    main()
