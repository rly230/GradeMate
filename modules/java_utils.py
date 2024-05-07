import os


def add_package_name(directory_path):
    # ディレクトリ内のすべてのアイテムをループ処理
    for class_ in os.listdir(directory_path):
        class_path = os.path.join(directory_path, class_)

        # class_pathがディレクトリでなければスキップ
        if not os.path.isdir(class_path):
            continue

        # 親フォルダ内のすべての子フォルダを探索
        for subdir, dirs, files in os.walk(class_path):
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(subdir, file)
                    dir_path = subdir.replace("\\", ".")

                    # Javaファイルを読み込み、既存のpackage宣言を削除
                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            lines = file.readlines()
                        lines = [
                            line
                            for line in lines
                            if not line.strip().startswith("package ")
                        ]
                    except UnicodeDecodeError as e:
                        print(f"{e}: {class_path}")

                    # 新しいpackage宣言を追加
                    package_declaration = f"package {dir_path};\n"
                    lines.insert(0, package_declaration)

                    # ファイルに書き戻す
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.writelines(lines)

        print("Add 'package': " + class_)