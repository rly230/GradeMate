import os
import re


def is_lesson_directory(path):
    """
    パスが「第n回」の形式を持つ授業回数のディレクトリであるかを確認する。

    :param path: ディレクトリのパス。
    :return: 授業回数のディレクトリであればTrue、そうでなければFalse。
    """
    pattern = r"第\d{2}回"
    return re.search(pattern, path) is not None


def explore_directory(base_path):
    """
    指定されたpath内を探索し、すべての授業回数について学生の提出ファイル情報を収集する。

    :param base_path: 授業名のディレクトリパス。
    :return: 各授業回数における各学生のファイル情報を含む辞書。{授業回数: {学籍番号: パス}}
    """
    lesson_data = {}
    for lesson_dir in os.listdir(base_path):
        lesson_path = os.path.join(base_path, lesson_dir)
        if os.path.isdir(lesson_path) and is_lesson_directory(lesson_path):
            students_files = {}
            for student_dir in os.listdir(lesson_path):
                student_path = os.path.join(lesson_path, student_dir)
                if os.path.isdir(student_path):  # ディレクトリであることを確認
                    docx_file = find_docx_file(student_path)
                    if docx_file:
                        students_files[student_dir] = docx_file
            lesson_data[lesson_dir] = students_files
    return lesson_data


def find_docx_file(student_path):
    """
    指定された学生のフォルダ内に.docxファイルが存在するかチェックする。

    :param student_path: 学生のフォルダパス。
    :return: .docxファイルのパス、存在しない場合はNone。
    """
    for file in os.listdir(student_path):
        if file.endswith(".docx") and not file.startswith("~$"):
            return os.path.join(student_path, file)
    return None
