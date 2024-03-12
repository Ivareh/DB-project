import sqlite3


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


def create_theater_hall(conn, theater_hall):
    sql = """ INSERT INTO theaterHall(name, capacity)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, theater_hall)
    conn.commit()
    return cur.lastrowid


def create_season(conn, season):
    sql = """ INSERT INTO season(season, year)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, season)
    conn.commit()
    return cur.lastrowid


def create_play(conn, play):
    sql = """ INSERT INTO play(title, author, duration, hall_id, season_id)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, play)
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
    sql = """ INSERT INTO chair(number, row, area_id, hall_id)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, chair)
    conn.commit()
    return cur.lastrowid


def create_chair_with_id(conn, chair):
    sql = """ INSERT INTO chair(chair_id, number, row, area_id, hall_id)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, chair)
    conn.commit()
    return cur.lastrowid


def create_customer_profile(conn, customer_profile):
    sql = """ INSERT INTO customerProfile(name, address, phone)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, customer_profile)
    conn.commit()
    return cur.lastrowid


def create_customer_group(conn, customer_group):
    sql = """ INSERT INTO customerGroup(name)
              VALUES(?) """
    cur = conn.cursor()
    cur.execute(sql, customer_group)
    conn.commit()
    return cur.lastrowid


def create_ticket_purchase(conn, ticket_purchase):
    sql = """ INSERT INTO ticketPurchase(datetime, customer_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket_purchase)
    conn.commit()
    return cur.lastrowid


def create_ticket_price(conn, ticket_price):
    sql = """ INSERT INTO ticketPrice(price, play_id, group_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket_price)
    conn.commit()
    return cur.lastrowid


def create_ticket(conn, ticket):
    sql = """ INSERT INTO ticket(ticketPrice_id, purchase_id, performance_id, area_id)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket)
    conn.commit()
    return cur.lastrowid


def create_ticket_with_id(conn, ticket):
    sql = """ INSERT INTO ticket(ticket_id, ticketPrice_id, purchase_id, performance_id, area_id)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket)
    conn.commit()
    return cur.lastrowid


def create_act(conn, act):
    sql = """ INSERT INTO act(number, name, play_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, act)
    conn.commit()
    return cur.lastrowid


def create_role(conn, act):
    sql = """ INSERT INTO role(name, play_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, act)
    conn.commit()
    return cur.lastrowid


def create_actor(conn, actor):
    sql = """ INSERT INTO actor(name, email, status, description)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, actor)
    conn.commit()
    return cur.lastrowid


def create_employee(conn, employee):
    sql = """ INSERT INTO employee(name, email, status, description, task)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid


def create_actor_role(conn, actor_role):
    sql = """ INSERT INTO actorRole(actor_id, role_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, actor_role)
    conn.commit()
    return cur.lastrowid


def create_actor_play(conn, actor_play):
    sql = """ INSERT INTO actorPlay(actor_id, play_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, actor_play)
    conn.commit()
    return cur.lastrowid


def create_employee_play(conn, employee_play):
    sql = """ INSERT INTO employeePlay(employee_id, play_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, employee_play)
    conn.commit()
    return cur.lastrowid


def create_act_role(conn, act_role):
    sql = """ INSERT INTO actRole(act_id, role_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, act_role)
    conn.commit()
    return cur.lastrowid
