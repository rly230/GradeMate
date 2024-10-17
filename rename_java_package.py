import modules


def main():
    directory_path = "data"
    modules.rename_folders_recursively(directory_path)
    modules.add_package_name(directory_path)


if __name__ == "__main__":
    main()
