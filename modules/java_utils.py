import os
import re
import hashlib


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


def calculate_md5(file_path):
    """指定されたファイルのMD5ハッシュを計算する"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_duplicates(directory_path):
    """ディレクトリ内の.javaファイルの中で、MD5ハッシュが一致するファイルを探す"""
    md5_dict = {}
    duplicates = []

    for subdir, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(subdir, file)
                file_md5 = calculate_md5(file_path)

                if file_md5 in md5_dict:
                    original_file = md5_dict[file_md5]
                    print(f"コピーが疑われるファイルA: {original_file}")
                    print(f"コピーが疑われるファイルB: {file_path}")
                    duplicates.append((original_file, file_path))
                else:
                    md5_dict[file_md5] = file_path

    if not duplicates:
        print("コピーが疑われるファイルはありませんでした。")
