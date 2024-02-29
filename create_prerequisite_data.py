import sqlite3
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from typing import List


def open_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data


def get_date_from_file(file_path):
    df = pd.read_csv(file_path)
    date = df.columns[0]
    dato = None
    if "Dato" in date:
        words = date.split()
        for word in words:
            if len(word) == 10 and word[4] == "-" and word[7] == "-":
                dato = word
    else:
        raise ValueError(f"No date found in file {file_path}")
    return dato


def create_optimal_area_seat_db_dataframe(file_path):
    data = open_file(file_path)
    lines = data.split("\n")
    lines = [line for line in lines if line]
    date = get_date_from_file(file_path)
    df = pd.DataFrame(lines, columns=["areaAndSeats"])
    df = df.drop(0)

    area_seat_df = pd.DataFrame(
        None, index=np.arange(10), columns=["Galleri", "Balkong", "Parkett"]
    )

    count = 0
    numbers = []
    for row in df["areaAndSeats"]:
        if row == "Galleri" or row == "Balkong" or row == "Parkett":
            if count == 1:
                area_seat_df["Galleri"] = numbers + [None] * (10 - len(numbers))
            elif count == 2:
                area_seat_df["Balkong"] = numbers + [None] * (10 - len(numbers))
            count += 1
            numbers = []
        else:
            numbers.append(row)
    # Last column
    area_seat_df["Parkett"] = numbers

    area_seat_df = area_seat_df.assign(date=date)
    area_seat_df.to_csv("files_needed/area_seat_df.csv", index=False)
    return df


# def format_location_number_series(df: pd.DataFrame, column_name: List[str], row_values: List[str] = None):
#     numbers = []
#     df_index = df.columns.get_loc(column_name)
#     print(df_index)
#     for row in df[column_name]:
#         if row.isnumeric():
#             numbers.append(row)
#         elif row.isalpha():
#             column_name = row
#             new_df = pd.DataFrame(data=numbers, columns=[column_name])
#             print("NEWDF")
#             print(new_df)
#             print(df)
#             print("HEY")
#             return format_location_number_series(df, column_name, numbers)


def add_data_to_sqlite_db(file_path, db_name):
    connection = sqlite3.connect(db_name)
    # df.to_sql('data', con=connection, if_exists='replace', index=False)


if __name__ == "__main__":
    data = open_file("files_needed/gamle-scene.txt")

    # add_data_to_sqlite_db('files_needed/gamle-scene.txt', 'gamle-scene.db')

    create_optimal_area_seat_db_dataframe("files_needed/gamle-scene.txt")
