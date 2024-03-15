# Open the file and read the data
from typing import List, Tuple
import pandas as pd

from db_utils import (
    create_chair_with_id,
    create_ticket,
    get_area_id_from_area_name,
    get_performances_by_hall_and_date,
    get_random_ticket_price_id,
    get_random_ticket_purchase_id,
)
from db_connection import create_connection


def open_file(file_path: str):
    with open(file_path, "r") as file:
        data = file.read()
    return data


# Used to check if a line (string) in the file contains a number, which means it is a line of chairs (not area)
def has_numbers(inputString: str):
    return any(char.isdigit() for char in inputString)


# Get the date from the file
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


def read_and_create_chairs(
    conn, file_path: str, *, performances, hall_id: int, reset_lines: bool = False
):
    data = open_file(file_path)
    date = get_date_from_file(file_path)
    print(date)
    lines = [line for line in data.split("\n") if line][
        1:
    ]  # [1:] means to remove the date line in beginning

    areas_with_rows = inverse_area_with_rows(lines)
    print(areas_with_rows)

    chair_number = 1
    row_number = 1
    current_area = None
    for area_row in areas_with_rows:
        # print(area_row_number, area_row)
        if not has_numbers(area_row):
            current_area = area_row
            row_number = 1
        else:
            if reset_lines:
                chair_number = 1
            # print("current_area", current_area)
            for chair in area_row:
                # print("chair", chair)
                chair_id = f"{chair_number}_{row_number}_{current_area}_{hall_id}"
                # print(chair_id)
                area_id = get_area_id_from_area_name(conn, current_area, hall_id)
                if chair == "x":
                    chair_number += 1
                elif chair == "1":
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
                elif chair == "0":
                    create_chair_with_id(
                        conn, (chair_id, chair_number, row_number, area_id, hall_id)
                    )

                # print("hey")
                chair_number += 1
                # print("chair_number", chair_number)
            row_number += 1


def inverse_area_with_rows(lines):
    areas_with_rows = []
    # We have to reverse the order of the rows in the areas, because the first row in the file is the top row
    for area_row in lines:
        if not has_numbers(area_row):
            areas_with_rows.append([area_row])
        else:
            areas_with_rows[-1].append(area_row)
    print(areas_with_rows)
    for index, area_with_row in enumerate(areas_with_rows):
        area = area_with_row[0]
        area_with_row = area_with_row[1:][::-1]
        areas_with_rows[index] = [area] + area_with_row
    # After inverse except for the first element
    print(areas_with_rows)
    flatten_areas_with_rows = []
    for area_row in areas_with_rows:
        for row in area_row:
            print(row)
            flatten_areas_with_rows.append(row)
    print(flatten_areas_with_rows)
    print(flatten_areas_with_rows)
    return flatten_areas_with_rows


def create_purchased_chair(
    conn,
    *,
    chair: Tuple,
    performances: List[Tuple],
):
    create_chair_with_id(conn, chair)

    random_ticket_purchase_id = get_random_ticket_purchase_id(conn)
    random_ticket_price_id = get_random_ticket_price_id(conn)

    performance_ids = [performance[0] for performance in performances]

    # create_ticket(1,)
    for performance_id in performance_ids:
        ticket = (
            random_ticket_purchase_id,
            performance_id,
            chair[0],
            chair[3],
            random_ticket_price_id,
        )
        create_ticket(conn, ticket)


def main():
    conn = create_connection("db.sqlite3")

    date = get_date_from_file("files_needed/gamle-scene.txt")

    performances_gamle_scene = get_performances_by_hall_and_date(conn, 2, date)

    read_and_create_chairs(
        conn,
        "files_needed/gamle-scene.txt",
        performances=performances_gamle_scene,
        hall_id=2,
        reset_lines=True,
    )

    # hall = 2

    # print(get_performances_by_hall_and_date(conn, hall, date))
    # print(get_random_ticket_purchase_id(conn))
    # print(get_random_ticket_price_id(conn))


if __name__ == "__main__":
    main()
