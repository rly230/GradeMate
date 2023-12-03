import re


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
