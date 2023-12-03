import os


def explore_directory(base_path):
    """
    指定されたディレクトリ内を探索し、学生の提出ファイル情報を収集する。

    :param base_path: 探索を開始するディレクトリのパス。
    :return: 各学生のファイル情報を含む辞書。{学籍番号:パス}
    """
    students_files = {}
    for root, dirs, files in os.walk(base_path):
        if is_lesson_directory(root):  # 授業回数のディレクトリに学番フォルダ作っちゃったうっかりさんをフィルタリング
            for dir in dirs:
                student_id = dir
                student_path = os.path.join(root, dir)
                docx_file = find_docx_file(student_path)
                if docx_file:
                    students_files[student_id] = docx_file
    return students_files


import re


def is_lesson_directory(path):
    """
    パスが「第n回」の形式を持つ授業回数のディレクトリであるかを確認する。

    :param path: ディレクトリのパス。
    :return: 授業回数のディレクトリであればTrue、そうでなければFalse。
    """
    pattern = r"第\d{2}回"
    return re.search(pattern, path) is not None


def find_docx_file(student_path):
    """
    指定された学生のフォルダ内に.docxファイルが存在するかチェックする。

    :param student_path: 学生のフォルダパス。
    :return: .docxファイルのパス、存在しない場合はNone。
    """
    for file in os.listdir(student_path):
        if file.endswith(".docx"):
            return os.path.join(student_path, file)
    return None
