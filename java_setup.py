import modules


def main(directory_path = "data"):
    # フォルダ名を適切なものに変更
    modules.rename_folders(directory_path)

    # コピーが疑われるjavaファイルをMD5で検出
    modules.find_copyfile(directory_path)

    # package宣言を適切なものに変更
    modules.add_package(directory_path)


if __name__ == "__main__":
    main()
