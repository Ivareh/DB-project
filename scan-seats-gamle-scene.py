import sqlite3
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from typing import List

import db_utils_create as dbuc


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

    area_seat_columns = ["Galleri", "Balkong", "Parkett"]

    area_seat_df = pd.DataFrame(None, index=np.arange(10), columns=area_seat_columns)

    area_seat_df = area_seat_df.rename(index=lambda x: f"Row {x}")

    area_seat_df = format_game_scene_areas_seats(
        df, area_seat_df, "areaAndSeats", area_seat_columns
    )

    area_seat_df = area_seat_df.assign(date=date)
    area_seat_df.to_csv("files_needed/area_seat_df.csv", index=False)

    return area_seat_df


def format_game_scene_areas_seats(
    df: pd.DataFrame,
    new_df: pd.DataFrame,
    column_name: str,
    column_names: List[str] = None,
):
    numbers, count = [], 0

    for row in df[column_name]:
        if row in column_names:
            new_df[column_names[count - 1]] = numbers + [None] * (10 - len(numbers))
            count += 1
            numbers = []
        else:
            numbers.append(row)

    new_df[column_names[-1]] = numbers + [None] * (10 - len(numbers))
    return new_df


def format_gamle_scene_to_db_tables(df: pd.DataFrame):
    pass


# Define a mapping for area types to area IDs
AREA_MAP = {"Galleri": 1, "Balkong": 2, "Parkett": 3}


def add_chairs_to_db(chairsDf: pd.DataFrame, conn: sqlite3.Connection):
    chairsDf = chairsDf[::-1].sort_index(ascending=False)

    global AREA_MAP
    print("REVERTED INDEX")
    print(chairsDf)

    purchased_chairs = []
    for index, row in chairsDf.iterrows():
        row_number = index[-1]
        for areaType, chairRowNumbers in row.items():
            if areaType == "date" or not chairRowNumbers:
                continue

            # print(
            #     f"Area Type={areaType} : Chair Row Numbers={chairRowNumbers} : Row Number={row_number}"
            # )

            # TODO: NOT DONE
            for chair in range(len(chairRowNumbers)):
                # print(chair)
                chair_id = f"1_{areaType}_{row_number}{chair}"
                if int(chairRowNumbers[chair]) == 1:
                    purchased_chairs.append(
                        {"chair": chair_id, "area_id": AREA_MAP[areaType]}
                    )
                # print(chairRowNumbers, type(chairRowNumbers))
                # print(chairRowNumbers[chair], type(chairRowNumbers[chair]))
                # print(f"{(chair_id, chairRowNumbers[chair], int(row_number), AREA_MAP[areaType], 1)}")
                dbuc.create_chair(
                    conn, (chair_id, chair, int(row_number), AREA_MAP[areaType], 1)
                )

    # def add_chairs_to_db(chairsDf: pd.DataFrame, conn: sqlite3.Connection):

    #     chairsDf.iloc[:] = chairsDf.iloc[::-1].values

    #     df_reverted_index = chairsDf.sort_index(ascending=False)

    #     print("REVERTED INDEX")
    #     print(df_reverted_index)
    #     df_revert_double = pd.DataFrame(index=df_reverted_index.index[::-1])
    #     df_revert_double["Galleri"] = df_reverted_index["Galleri"].values
    #     df_revert_double["Balkong"] = df_reverted_index["Balkong"].values
    #     df_revert_double["Parkett"] = df_reverted_index["Parkett"].values

    #     print(df_revert_double)
    #     purchased_chairs = []
    #     for index, row in df_revert_double.iterrows():
    #         row_number = index[-1]
    #         for areaType, chairRowNumbers in zip(row.index, row):
    #             if areaType == "date":
    #                 continue
    #             print(
    #                 "Area Type="
    #                 + str(areaType)
    #                 + " : Chair Row Numbers="
    #                 + str(chairRowNumbers)
    #                 + " : Row Number="
    #                 + str(row_number)
    #             )
    #             if chairRowNumbers:

    #                 for chair in range(len(chairRowNumbers)):
    #                     print(chair)
    #                     int_chair = int(chair)
    #                     if int_chair == 0 or int_chair == 1:
    #                         if areaType == "Galleri":
    #                             chair_id = "1_Galleri_" + str(row_number) + str(chair)
    #                             if int_chair == 1:
    #                                 purchased_chairs.append(
    #                                     {
    #                                         "chair": chair_id,
    #                                         "area_id": 1,
    #                                     }
    #                                 )
    #                             print(chairRowNumbers, type(chairRowNumbers))
    #                             print(chair, type(chair))
    #                             print(f"{(chair, int(row_number), 1, 1)}")
    #                             dbuc.create_chair(
    #                                 conn, (chair_id, chair, int(row_number), 1, 1)
    #                             )  # 1, 1 is the area_id and hall_id (Galleri, Gamle Scene)
    #                         elif areaType == "Balkong":
    #                             chair_id = "1_Balkong_" + str(row_number) + str(chair)
    #                             if int_chair == 1:
    #                                 purchased_chairs.append(
    #                                     {
    #                                         "chair": chair_id,
    #                                         "area_id": 2,
    #                                     }
    #                                 )
    #                             dbuc.create_chair(
    #                                 conn, (chair_id, chair, row_number, 2, 1)
    #                             )  # 2, 1 is the area_id and hall_id (Balkong, Gamle Scene)
    #                         elif areaType == "Parkett":
    #                             chair_id = "1_Parkett_" + str(row_number) + str(chair)
    #                             if int_chair == 1:
    #                                 purchased_chairs.append(
    #                                     {
    #                                         "chair": chair_id,
    #                                         "area_id": 3,
    #                                     }
    #                                 )
    #                             dbuc.create_chair(
    #                                 conn, (chair_id, chair, row_number, 3, 1)
    #                             )  # 3, 1 is the area_id and hall_id (Parkett, Gamle Scene)

    print("PURCHASED CHAIRS: ", purchased_chairs)
    add_purchased_chairs_to_db(purchased_chairs, conn)

    # duc.create_chair(conn, (chair, index, 1, 1))
    # area_id = row["area_id"]
    # hall_id = row["hall_id"]
    # number = row["number"]
    # row = row["row"]
    # duc.create_chair(conn, (number, row, area_id, hall_id))


def add_purchased_chairs_to_db(purchased_chairs: List[dict], conn: sqlite3.Connection):
    for chair in purchased_chairs:
        dbuc.create_ticket_chair(conn, (chair["chair"], chair["area_id"]))


if __name__ == "__main__":
    conn = dbuc.create_connection("db.sqlite3")

    data = open_file("files_needed/gamle-scene.txt")

    # add_data_to_sqlite_db('files_needed/gamle-scene.txt', 'gamle-scene.db')

    chairs = create_optimal_area_seat_db_dataframe("files_needed/gamle-scene.txt")
    add_chairs_to_db(chairs, conn)
