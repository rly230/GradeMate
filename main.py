from modules.file_explorer import explore_directory
from modules.docx_analyzer import analyze_docx
from modules.excel_writer import write_to_excel


def main():
    # ユーザー入力を受け取る
    course_name = input("授業名を入力してください: ")
    lesson_number = input("授業回数を入力してください（例：第01回）: ")
    base_path = f"{course_name}/{lesson_number}"

    # 授業のファイルを探索
    students_files = explore_directory(base_path)

    # 採点結果を格納する辞書
    grading_results = {}

    # 各学生のレポートを分析
    for student_id, file_path in students_files.items():
        if file_path:
            score = analyze_docx(file_path)
        else:
            score = None  # ファイルが存在しない場合
        grading_results[student_id] = score

    # Excelファイルに結果を書き込む
    file_name = f"{course_name}_採点結果.xlsx"
    sheet_name = lesson_number
    write_to_excel(grading_results, file_name, sheet_name)

    print("採点が完了しました。")


if __name__ == "__main__":
    main()
