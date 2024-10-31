import pandas as pd
import os
from openpyxl import load_workbook


def df_to_excel(df, file_name) -> None:
    """
    データフレームをExcelファイルに書き込む。

    :param df: 書き込むデータフレーム。
    :param file_name: Excelファイルの名前。
    """
    try:
        # ファイルが存在するかチェックし、存在しなければ新規作成
        if not os.path.exists(file_name):
            df.to_excel(file_name, index=False)
        else:
            book = load_workbook(file_name)
            with pd.ExcelWriter(file_name, engine="openpyxl", mode="a") as writer:
                writer.book = book
                df.to_excel(writer, index=False, header=False)
    except Exception as e:
        print(f"Error writing to Excel file {file_name}: {e}")

