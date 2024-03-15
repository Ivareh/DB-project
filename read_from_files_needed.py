# Open the file and read the data
from typing import List, Tuple
import pandas as pd

from db_utils import (
    create_chair_with_id,
    create_ticket,
    get_area_id_from_area_name,
    get_random_ticket_price_id,
    get_random_ticket_purchase_id,
)


def open_file(file_path: str):
    with open(file_path, "r") as file:
        data = file.read()
    return data


# Used to check if a line (string) in the file contains a number, which means it is a line of chairs (not area)
def has_numbers(inputString: str):
    return any(char.isdigit() for char in inputString)


# Get the date from the file, method from files_needed/tips.txt
def get_date_from_file(file_path: str):
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


# Read the file and create chairs in the database
def read_and_create_chairs(
    conn, file_path: str, *, performances, hall_id: int, reset_lines: bool = False
):
    data = open_file(file_path)
    lines = [line for line in data.split("\n") if line][
        1:
    ]  # [1:] means to remove the date line in beginning

    # Inverse the order of the rows in the areas, because the first row in the file is the top row
    areas_with_rows = inverse_area_with_rows(lines)

    # Create the chairs in the database
    chair_number = 1
    row_number = 1
    current_area = None
    for area_row in areas_with_rows:
        if not has_numbers(
            area_row
        ):  # If the line does not contain numbers, it is an area
            current_area = area_row
            row_number = 1
        else:
            if reset_lines:
                chair_number = 1
            for chair in area_row:
                chair_id = f"{chair_number}_{row_number}_{current_area}_{hall_id}"
                area_id = get_area_id_from_area_name(conn, current_area, hall_id)
                if (
                    chair == "x"
                ):  # If the chair is marked as "x" in the file, there is no chair
                    chair_number += 1
                    continue
                elif (
                    chair == "1"
                ):  # If the chair is marked as "1" in the file, it is a purchased chair
                    create_purchased_chair(
                        conn,
                        chair=(
                            chair_id,
                            chair_number,
                            row_number,
                            area_id,
                            hall_id,
                        ),
                        performances=performances,
                    )
                elif (
                    chair == "0"
                ):  # If the chair is marked as "0" in the file, it is a chair that is not purchased
                    create_chair_with_id(
                        conn, (chair_id, chair_number, row_number, area_id, hall_id)
                    )

                chair_number += 1  # Increment the chair number
            row_number += 1  # Increment the row number


# We have to reverse the order of the rows in the areas, because the first row in the file is the top row
def inverse_area_with_rows(lines):
    areas_with_rows = []

    # Create sublists of the lines into areas with rows
    for area_row in lines:
        if not has_numbers(area_row):
            areas_with_rows.append([area_row])
        else:
            areas_with_rows[-1].append(area_row)

    # Iterate through the areas with rows and reverse the order of the rows
    for index, area_with_row in enumerate(areas_with_rows):
        area = area_with_row[0]
        area_with_row = area_with_row[1:][
            ::-1
        ]  # Reverse the order of the rows except the first row (area)
        areas_with_rows[index] = [
            area
        ] + area_with_row  # Add the area to the beginning of the list
    # Flatten the list of areas with rows to original format
    flatten_areas_with_rows = [row for area_row in areas_with_rows for row in area_row]
    return flatten_areas_with_rows


def create_purchased_chair(
    conn,
    *,
    chair: Tuple,
    performances: List[Tuple],
):
    create_chair_with_id(conn, chair)  # Create the chair in the database

    random_ticket_purchase_id = get_random_ticket_purchase_id(
        conn
    )  # Get a random ticket purchase id
    random_ticket_price_id = get_random_ticket_price_id(
        conn
    )  # Get a random ticket price id

    performance_ids = [
        performance[0] for performance in performances
    ]  # Get the performance ids

    # Create a ticket for each performance
    for performance_id in performance_ids:
        ticket = (
            random_ticket_purchase_id,
            performance_id,
            chair[0],  # chair_id for the purchased chair
            chair[3],  # area_id for the purchased chair
            random_ticket_price_id,
        )
        create_ticket(conn, ticket)
