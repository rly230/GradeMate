import modules


def main():
    target_path = "data"
    modules.rename_folders_recursively(target_path)
    modules.add_package_name(target_path)


if __name__ == "__main__":
    main()
