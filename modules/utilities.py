import re
import os


def parse_student_id(student_id):
    """
    学籍番号を解析して、入学年、学部、個人番号に分割する。

    :param student_id: 学籍番号。
    :return: 入学年、学部、個人番号のタプル、または無効な場合はNoneを返す。
    """
    pattern = re.compile(r"^(\d{2})([A-Z]{2})(\d{3})$")
    match = pattern.match(student_id)
    if not match:
        print(f"Invalid student ID: {student_id}")
        return None
    year, faculty, number = match.groups()
    return int(year), faculty, int(number)


def extract_lesson_number(lesson_name):
    """
    授業回数を表す文字列から数値を抽出する。

    :param lesson_name: 授業回数のカラム名（例：「第01回」）。
    :return: 数値部分（例：1）。
    """
    match = re.search(r"\d+", lesson_name)
    return int(match.group()) if match else None


def rename_folders(directory_path, prefix="class"):
    """
    「第01回」のようなフォルダ名を「prefix+"01"」のように変更

        directory_path (str): 対象のディレクトリパス
    """
    # ディレクトリ内のすべてのアイテムに対してループ処理
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        if os.path.isdir(item_path) and re.match(r"第(\d{2})回", item):
            new_name = prefix + re.match(r"第(\d{2})回", item).group(1)
            new_path = os.path.join(directory_path, new_name)
            os.rename(item_path, new_path)
            print("Renamed: " + new_path)


def add_str(directory_path, prefix="stu"):
    # ディレクトリ内のすべてのアイテムをループ処理
    for class_ in os.listdir(directory_path):
        class_path = os.path.join(directory_path, class_)

        # class_pathがディレクトリでなければスキップ
        if not os.path.isdir(class_path):
            continue

        for item in os.listdir(class_path):
            item_path = os.path.join(class_path, item)

            # アイテムがディレクトリの場合に名前を変更
            if os.path.isdir(item_path):
                new_name = prefix + item
                new_path = os.path.join(class_path, new_name)
                os.rename(item_path, new_path)

        print("Add str: " + class_)
