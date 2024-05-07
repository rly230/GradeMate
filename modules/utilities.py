import re
import os
import pykakasi


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


def kanji_to_hiragana(text):
    """
    text中の漢字を平仮名に変換
    return :: str
    """
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    result = kks.getConverter().do(text)
    return result


def hiragana_to_romaji(text):
    """
    text中のひらがなをローマ字に変換
    return :: str
    """
    kks = pykakasi.kakasi()
    kks.setMode("H", "a")
    result = kks.getConverter().do(text)
    return result


def convert_folder_name(folder_name):
    """
    フォルダ名に含まれる日本語をローマ字に変換
    """
    hiragana_name = kanji_to_hiragana(folder_name)
    romaji_name = hiragana_to_romaji(hiragana_name)
    return romaji_name


def add_prefix_if_numeric(folder_name, prefix="a_"):
    """
    フォルダ名が数値で始まる場合に、指定した文字列を頭にくっつける
    arg :: prefix str
    return :: str
    """
    if folder_name[0].isdigit():
        new_folder_name = prefix + folder_name
        return new_folder_name
    else:
        return folder_name


def rename_folders_recursively(root_folder, prefix="a"):
    """
    再帰的にフォルダ内を探索し、以下の処理を行う
    ・フォルダ名中の日本語をローマ字に変更
    ・フォルダ名の頭に数値がある場合、適当な文字列をくっつける
    """
    for foldername in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, foldername)
        if os.path.isdir(folder_path):
            # フォルダの場合は再帰的に処理を行う
            rename_folders_recursively(folder_path)
            # フォルダ名を変換する
            foldername = convert_folder_name(foldername)
            foldername = add_prefix_if_numeric(foldername, prefix)
            new_folder_path = os.path.join(root_folder, foldername)
            os.rename(folder_path, new_folder_path)
