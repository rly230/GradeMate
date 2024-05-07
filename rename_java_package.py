import modules


def main():
    modules.rename_folders_recursively("data")
    modules.add_package_name("data")


if __name__ == "__main__":
    main()
