from modules.file_explorer import explore_directory
from modules.docx_analyzer import analyze_docx
from modules.excel_writer import write_to_excel
from modules.utilities import *
import pandas as pd


def main():
    # ユーザー入力を受け取る
    course_name = input("授業名を入力してください: ")
    base_path = course_name

    # 授業のファイルを探索
    lessons_data = explore_directory(base_path)

    # 採点結果を格納するためのデータフレーム（空で初期化）
    grading_df = pd.DataFrame(columns=["Student ID"])

    # 各授業回数のデータを処理
    for lesson, students_files in lessons_data.items():
        lesson_rows = []
        for student_id, file_path in students_files.items():
            score = analyze_docx(file_path) if file_path else None
            lesson_rows.append({"Student ID": student_id, f"{lesson}": score})
        lesson_df = pd.DataFrame(lesson_rows)

        # lesson_dfの内容を確認するための出力
        # print(lesson_df.head())

        # 既存のデータフレームと統合（空でない場合のみ）
        if not lesson_df.empty:
            grading_df = pd.merge(grading_df, lesson_df, on="Student ID", how="outer")

    # 生徒の学籍番号に基づいてデータを整理
    grading_df["Parsed ID"] = grading_df["Student ID"].apply(parse_student_id)
    grading_df = grading_df[grading_df["Parsed ID"].notnull()]
    grading_df["Year"], grading_df["Faculty"], grading_df["Number"] = zip(
        *grading_df["Parsed ID"]
    )
    grading_df.sort_values(by=["Year", "Faculty", "Number"], inplace=True)
    grading_df.drop(["Year", "Faculty", "Number", "Parsed ID"], axis=1, inplace=True)

    # 授業回数のカラムを並び替え
    lesson_columns = [col for col in grading_df.columns if "第" in col]
    sorted_lesson_columns = sorted(lesson_columns, key=extract_lesson_number)
    final_columns = ["Student ID"] + sorted_lesson_columns
    grading_df = grading_df[final_columns]

    # Excelファイルに結果を書き込む
    file_name = f"{course_name}_採点結果.xlsx"
    write_to_excel(grading_df, file_name)

    print("採点が完了しました。")


if __name__ == "__main__":
    main()
