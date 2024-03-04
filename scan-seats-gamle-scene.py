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


# Define a mapping for area types to area IDs
AREA_MAP = {"Galleri": 1, "Balkong": 2, "Parkett": 3}


def create_optimal_area_seat_db_dataframe(file_path):
    data = open_file(file_path)
    lines = [line for line in data.split("\n") if line]

    date = get_date_from_file(file_path)

    # Use pd.Series to create the DataFrame directly
    df = pd.Series(lines[1:], name="areaAndSeats")
    
    global AREA_MAP
    area_map_keys = list(AREA_MAP.keys())

    # Create a DataFrame with the specified columns and rows
    area_seat_df = pd.DataFrame(index=range(10), columns=area_map_keys).rename(
        index=lambda x: f"Row {x}"
    )

    # Use a function to format the game scene areas and seats
    area_seat_df = format_game_scene_areas_seats(
        df, area_seat_df, area_map_keys
    )

    area_seat_df["date"] = date
    area_seat_df.to_csv("files_needed/area_seat_df.csv", index=False)

    return area_seat_df


def format_game_scene_areas_seats(
    df: pd.Series,
    new_df: pd.DataFrame,
    column_names: List[str] = None,
):
    # Invert the series and sort the index
    df = df[::-1].sort_index(ascending=False)

    numbers, count = [], 2

    for row in df:
        if row in column_names:
            new_df[column_names[count]] = numbers + [None] * (10 - len(numbers))
            count -= 1
            numbers = []
        else:
            numbers.append(row)

    return new_df


def add_chairs_to_db(chairs_df: pd.DataFrame, conn: sqlite3.Connection):
    global AREA_MAP

    purchased_chairs = []

    for index, row in chairs_df.iterrows():
        row_number = int(index[-1]) + 1  # Add 1 to row number to start from 1

        for areaType, chairRowNumbers in row.items():
            if areaType == "date" or not chairRowNumbers:
                continue

            # Use enumerate to simplify iteration and access to both index and value
            for chair, seat_status in enumerate(chairRowNumbers, start=1):
                chair_id = f"1_{areaType}_{row_number}_{chair}"

                if int(seat_status) == 1:
                    purchased_chairs.append(chair_id)

                dbuc.create_chair(
                    conn, (chair_id, chair, row_number, AREA_MAP[areaType], 1)
                )

    add_purchased_chairs_to_db(purchased_chairs, conn)


def add_purchased_chairs_to_db(purchased_chairs: List[dict], conn: sqlite3.Connection):

    # Create ticket for performance 6 and 3 on 3rd of February 2023
    ticket_performance_1_03022024 = (100, 1, 1, 6, 1)
    ticket_performance_2_03022024 = (101, 1, 1, 3, 1)
    dbuc.create_ticket_with_id(conn, ticket_performance_1_03022024)
    dbuc.create_ticket_with_id(conn, ticket_performance_2_03022024)

    for chair in purchased_chairs:
        dbuc.create_ticket_chair(conn, (100, chair))
        dbuc.create_ticket_chair(conn, (101, chair))


if __name__ == "__main__":
    conn = dbuc.create_connection("db.sqlite3")

    data = open_file("files_needed/gamle-scene.txt")

    chairs = create_optimal_area_seat_db_dataframe("files_needed/gamle-scene.txt")
    add_chairs_to_db(chairs, conn)
