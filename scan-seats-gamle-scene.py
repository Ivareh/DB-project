import sqlite3
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from typing import List


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_season(conn, season):
    sql = """ INSERT INTO season(season, year)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, season)
    conn.commit()
    return cur.lastrowid


def create_theater_hall(conn, theater_hall):
    sql = """ INSERT INTO theaterHall(name, capacity)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, theater_hall)
    conn.commit()
    return cur.lastrowid


def create_play(conn, play):
    sql = """ INSERT INTO play(title, author, duration, hall_id, season_id)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, play)
    conn.commit()
    return cur.lastrowid


def create_act(conn, act):
    sql = """ INSERT INTO act(number, name, play_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, act)
    conn.commit()
    return cur.lastrowid


def create_performance(conn, performance):
    sql = """ INSERT INTO performance(datetime, hall_id, play_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, performance)
    conn.commit()
    return cur.lastrowid


def create_area(conn, area):
    sql = """ INSERT INTO area(name, hall_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, area)
    conn.commit()
    return cur.lastrowid


def create_chair(conn, chair):
    sql = """ INSERT INTO chair(row, number, area_id, hall_id)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, chair)
    conn.commit()
    return cur.lastrowid


def create_ticket(conn, ticket):
    sql = """ INSERT INTO ticket(price, play_id, group_id, purchase_id, performance_id, chair_id, area_id)
              VALUES(?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket)
    conn.commit()
    return cur.lastrowid


def create_customer_profile(conn, customer_profile):
    sql = """ INSERT INTO customerProfile(name, address, phone)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, customer_profile)
    conn.commit()
    return cur.lastrowid


def create_ticket_purchase(conn, ticket_purchase):
    sql = """ INSERT INTO ticketPurchase(datetime, customer_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket_purchase)
    conn.commit()
    return cur.lastrowid


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

    return df


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
    conn = create_connection("db.sqlite3")

    with conn:

        season = ("Spring", 2022)
        theater_hall = ("Gamle Scene", 200)
        play = (
            "The Cherry Orchard",
            "Anton Chekhov",
            "A comedy about a family who is about to lose their estate",
            120,
            1,
        )
        act = (1, "Act 1", 1)
        performance = ("2022-05-01 19:00:00", 1, 1)
        area = ("Parkett", 1)
        chair = (1, 1, 1, 1)
        ticket = (200, 1, 1, 1, 1, 1, 1)
        customer_profile = ("John Doe", "1234 Elm Street", "12345678")
        ticket_purchase = ("2022-04-01 19:00:00", 1)

        create_season(conn, season)
        create_theater_hall(conn, theater_hall)
        create_play(conn, play)
        create_act(conn, act)
        create_performance(conn, performance)
        create_area(conn, area)
        create_chair(conn, chair)
        create_ticket(conn, ticket)
        create_customer_profile(conn, customer_profile)
        create_ticket_purchase(conn, ticket_purchase)

    data = open_file("files_needed/gamle-scene.txt")

    # add_data_to_sqlite_db('files_needed/gamle-scene.txt', 'gamle-scene.db')

    create_optimal_area_seat_db_dataframe("files_needed/gamle-scene.txt")
