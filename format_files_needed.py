import re
import sqlite3
import pandas as pd
from typing import Dict, List

import db_utils_create as dbuc


# Open the file and read the data
def open_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data


# Get the date from the file
def get_date_from_file(file_path):
    areaSeatSeries = pd.read_csv(file_path)
    date = areaSeatSeries.columns[0]
    dato = None
    if "Dato" in date:
        words = date.split()
        for word in words:
            if len(word) == 10 and word[4] == "-" and word[7] == "-":
                dato = word
    else:
        raise ValueError(f"No date found in file {file_path}")
    return dato


def create_optimal_area_seat_dataframe(
    file_path, area_map: Dict, reset_row_chair_numbers: bool = False
):
    data = open_file(file_path)
    lines = [line for line in data.split("\n") if line]

    date = get_date_from_file(file_path)

    # Use pd.Series to create the DataFrame directly
    areaSeatSeries = pd.Series(lines[1:], name="areaAndSeats")

    max_rows = 0
    row_count = 0

    # Count the maximum number of rows in the areaSeatSeries (used to create the DataFrame later on)
    for index, row in areaSeatSeries.items():
        if row not in area_map:
            row_count += 1
        else:
            row_count = 0

        max_rows = max(max_rows, row_count)

    area_map_keys = list(area_map.keys())

    # Create a DataFrame with the specified columns and rows
    area_seat_df = pd.DataFrame(index=range(max_rows), columns=area_map_keys).rename(
        index=lambda x: f"Row {x+1}"
    )  # Rename the index to start from 1

    # Use a function to format the game scene areas and seats
    area_seat_df = format_areas_seats(
        areaSeatSeries,
        area_seat_df,
        max_rows,
        column_names=area_map_keys,
    )

    return area_seat_df


# Format the areas and seats series to a DataFrame
def format_areas_seats(
    areaSeatSeries: pd.Series,
    new_df: pd.DataFrame,
    max_rows: int,
    *,
    column_names: List[str] = None,
):
    # Invert the areaSeatSeries and sort the index
    areaSeatSeries = areaSeatSeries[::-1].sort_index(ascending=False)

    numbers, count = [], len(column_names) - 1

    # Add the numbers to the new DataFrame
    for row in areaSeatSeries:
        if row in column_names:
            new_df[column_names[count]] = numbers + [None] * (max_rows - len(numbers))
            count -= 1
            numbers = []
        else:
            numbers.append(row)

    return new_df


def add_gamle_scene_chairs_to_db(
    text_file: str,
    area_map: Dict,
    hall_id: int,
    conn: sqlite3.Connection,
):

    # Create a DataFrame with the optimal format for the gamle scene
    chairs_df = create_optimal_area_seat_dataframe(
        text_file,
        area_map,
    )

    purchased_chairs = []

    _, purchased_chairs_parkett = add_chairs_to_db_from_series(
        chairs_df["Parkett"],
        hall_id,
        conn,
        start_from_chair_number=1,
        reset_row_chair_numbers=True,
    )

    _, purchased_chairs_balkong = add_chairs_to_db_from_series(
        chairs_df["Balkong"],
        hall_id,
        conn,
        start_from_chair_number=1,
        reset_row_chair_numbers=True,
    )

    _, purchased_chairs_galleri = add_chairs_to_db_from_series(
        chairs_df["Galleri"],
        hall_id,
        conn,
        start_from_chair_number=1,
        reset_row_chair_numbers=True,
    )

    total_purchased_chairs = (
        purchased_chairs_parkett + purchased_chairs_balkong + purchased_chairs_galleri
    )
    add_purchased_chairs_to_db(total_purchased_chairs, conn)

    add_purchased_chairs_to_db(purchased_chairs, conn)


def add_hovedscenen_chairs_to_db(
    text_file: str,
    area_map: Dict,
    hall_id: int,
    conn: sqlite3.Connection,
):
    chairs_df = create_optimal_area_seat_dataframe(
        text_file,
        area_map,
    )

    last_chair_number_parkett, purchased_chairs_parkett = add_chairs_to_db_from_series(
        chairs_df["Parkett"], hall_id, conn, start_from_chair_number=1
    )

    _, purchased_chairs_galleri = add_chairs_to_db_from_series(
        chairs_df["Galleri"],
        hall_id,
        conn,
        start_from_chair_number=last_chair_number_parkett,
    )

    total_purchased_chairs = purchased_chairs_parkett + purchased_chairs_galleri
    add_purchased_chairs_to_db(total_purchased_chairs, conn)


def add_chairs_to_db_from_series(
    chairSeries: pd.Series,
    hall_id: int,
    conn: sqlite3.Connection,
    start_from_chair_number: int = 1,
    reset_row_chair_numbers: bool = False,
):
    chair_number = start_from_chair_number
    purchased_chairs = []
    for index, row in chairSeries.items():
        row_number = int(re.findall(r"\d+", index)[0])
        if not row:
            continue
        for chair, seat_status in enumerate(row, start=1):
            if reset_row_chair_numbers:
                chair_number = chair
            chair_id = f"{hall_id}_{chairSeries.name}_{row_number}_{chair_number}"
            if seat_status == "x":
                chair_number += 1
                continue

            if int(seat_status) == 1:
                purchased_chairs.append(chair_id)

            dbuc.create_chair_with_id(
                conn, (chair_id, chair_number, row_number, chairSeries.name, hall_id)
            )
            chair_number += 1

    return chair_number, purchased_chairs


def add_purchased_chairs_to_db(purchased_chairs: List[Dict], conn: sqlite3.Connection):
    # Create tickets for performances 3rd of February 2024
    tickets_performances_3rd_feb_gamle_scene_and_hovedscene = [
        (100, 1, 1, 6, 1),
        (101, 1, 1, 3, 1),
        (102, 1, 1, 6, 2),
        (103, 1, 1, 3, 2),
    ]

    if purchased_chairs:
        for ticket in tickets_performances_3rd_feb_gamle_scene_and_hovedscene:
            for chair in purchased_chairs:
                dbuc.create_ticket_chair(
                    conn, (ticket[0], chair)
                )  # ticket[0] is the ticket_id


def add_tickets_to_db(tickets: List, conn: sqlite3.Connection):
    for ticket in tickets:
        dbuc.create_ticket_with_id(conn, ticket)
