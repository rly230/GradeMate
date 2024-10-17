import os
import re


def read_java_file(file_path):
    """Javaファイルを読み込んで、既存のpackage宣言を削除する"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # package宣言を削除
        return [line for line in lines if not line.strip().startswith("package ")]
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError in {file_path}: {e}")
        return None


def write_java_file(file_path, lines):
    """Javaファイルに内容を書き戻す"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def generate_package_statement(root_path, subdir):
    """ディレクトリパスからpackage宣言を生成する"""
    relative_path = os.path.relpath(subdir, root_path)
    package_str = re.sub(r"[\\/]", ".", relative_path)
    return f"package {package_str};\n"


def process_java_file(file_path, package_statement):
    """Javaファイルにpackage宣言を追加して、ファイルに書き戻す"""
    lines = read_java_file(file_path)
    if lines is None:
        return
    lines.insert(0, package_statement)
    write_java_file(file_path, lines)


def add_package_name(directory_path):
    """ディレクトリ内の全ての.javaファイルにpackage宣言を追加する"""
    for class_ in os.listdir(directory_path):
        class_path = os.path.join(directory_path, class_)

        # class_pathがディレクトリでなければスキップ
        if not os.path.isdir(class_path):
            continue

        for subdir, dirs, files in os.walk(class_path):
            package_statement = generate_package_statement(directory_path, subdir)
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(subdir, file)
                    process_java_file(file_path, package_statement)

        print(f"Added 'package' to: {class_}")
