import modules


def main(directory_path="data", file_name="DB採点結果") -> None:
    # 採点結果を格納したDataFrame
    grading_df = modules.initialize_grading_df(directory_path)

    # 学籍番号順に並び替え
    grading_df = modules.sort_by_studentID(grading_df)

    # 授業回数順に並び替え
    grading_df = modules.sort_by_lesson_number(grading_df)

    # Excelファイルに書き込む
    modules.df_to_excel(grading_df, file_name=f"{file_name}.xlsx")

    print("採点が完了しました。")


if __name__ == "__main__":
    main(file_name="DB2024採点結果")
