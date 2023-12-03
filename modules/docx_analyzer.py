from docx import Document


def analyze_docx(file_path):
    """
    .docxファイルを解析し、内容が適切かどうかをチェックする。

    :param file_path: .docxファイルのパス。
    :return: 内容が適切な場合は3点、不十分な場合は1点、ファイルが存在しないまたは空の場合はNone。
    """
    try:
        doc = Document(file_path)
        text = [p.text for p in doc.paragraphs if p.text.strip()]
        if not text:
            return None  # ファイルが空の場合
        # elif is_text_length_appropriate(text, 10, 100000):
        #     return 1  # 内容が不十分な場合
        else:
            return 3  # 内容が適切な場合
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None  # ファイルを開けない場合


def is_text_length_appropriate(text_list, min_length, max_length):
    """
    テキストのリストが指定された長さの基準を満たしているかどうかを判断する。

    :param text_list: .docxファイルから抽出されたテキストのリスト。
    :param min_length: テキストが満たすべき最小長。
    :param max_length: テキストが満たすべき最大長。
    :return: 内容が基準を満たしていない場合はTrue、そうでなければFalse。
    """
    total_length = sum(len(text) for text in text_list)
    return total_length < min_length or total_length > max_length
