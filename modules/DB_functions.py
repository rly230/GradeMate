import modules
import pandas as pd

def initialize_grading_df(directory_path) -> pd.DataFrame:
    # 採点結果を格納するためのdf（空で初期化）
    grading_df = pd.DataFrame(columns=["Student ID"])

    lessons_data = modules.explore_directory(directory_path)

    # 各授業回数のデータを処理
    for lesson, students_files in lessons_data.items():
        lesson_rows = []
        for student_id, file_path in students_files.items():
            score = modules.scoring_docx(file_path) if file_path else None
            lesson_rows.append({"Student ID": student_id, f"{lesson}": score})
        lesson_df = pd.DataFrame(lesson_rows)

        # 既存のデータフレームと統合（空でない場合のみ）
        if not lesson_df.empty:
            grading_df = pd.merge(grading_df, lesson_df, on="Student ID", how="outer")

    return grading_df


def sort_by_studentID(grading_df) -> pd.DataFrame:
    grading_df["Parsed ID"] = grading_df["Student ID"].apply(modules.parse_student_id)
    grading_df = grading_df[grading_df["Parsed ID"].notnull()]
    grading_df["Year"], grading_df["Faculty"], grading_df["Number"] = zip(
        *grading_df["Parsed ID"]
    )
    grading_df.sort_values(by=["Year", "Faculty", "Number"], inplace=True)
    grading_df.drop(["Year", "Faculty", "Number", "Parsed ID"], axis=1, inplace=True)

    return grading_df


def sort_by_lesson_number(grading_df) -> pd.DataFrame:
    # 授業回数のカラムを並び替え
    lesson_columns = [col for col in grading_df.columns if "第" in col]
    sorted_lesson_columns = sorted(lesson_columns, key=modules.extract_lesson_number)
    final_columns = ["Student ID"] + sorted_lesson_columns
    grading_df = grading_df[final_columns]
    return grading_df
