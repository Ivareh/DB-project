import sqlite3


def create_theater_hall(conn, theater_hall):
    sql = """ INSERT INTO theaterHall(name, capacity)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, theater_hall)
    conn.commit()
    return cur.lastrowid


def create_theater_hall_with_id(conn, theater_hall):
    sql = """ INSERT INTO theaterHall(hall_id, name, capacity)
              VALUES(?,?,?) """
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


def create_season_with_id(conn, season):
    sql = """ INSERT INTO season(season_id, season, year)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, season)
    conn.commit()
    return cur.lastrowid


def create_play(conn, play):
    sql = """ INSERT INTO play(title, author, description, season_id, hall_id)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, play)
    conn.commit()
    return cur.lastrowid


def create_play_with_id(conn, play):
    sql = """ INSERT INTO play(play_id, title, author, description, season_id, hall_id)
              VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, play)
    conn.commit()
    return cur.lastrowid


def create_performance(conn, performance):
    sql = """ INSERT INTO performance(datetime, play_id, hall_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, performance)
    conn.commit()
    return cur.lastrowid


def create_performance_with_id(conn, performance):
    sql = """ INSERT INTO performance(performance_id, datetime, play_id, hall_id)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, performance)
    conn.commit()
    return cur.lastrowid


def get_performances_by_hall_and_date(conn, hall_id, date):
    sql = """ SELECT * FROM performance 
                WHERE hall_id = ? 
                AND 
                datetime LIKE '%' || ? || '%'"""
    cur = conn.cursor()
    cur.execute(sql, (hall_id, date))
    return cur.fetchall()


def create_area(conn, area):
    sql = """ INSERT INTO area(name, hall_id)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, area)
    conn.commit()
    return cur.lastrowid


def create_area_with_id(conn, area):
    sql = """ INSERT INTO area(area_id, name, hall_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, area)
    conn.commit()
    return cur.lastrowid


def get_area_id_from_area_name(conn, area_name, hall_id):
    sql = """ SELECT area_id FROM area 
              WHERE name = ? AND hall_id = ? """
    cur = conn.cursor()
    cur.execute(sql, (area_name, hall_id))
    return cur.fetchone()[0]


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
    sql = """ INSERT INTO customerProfile(userName, name, address, phone)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, customer_profile)
    conn.commit()
    return cur.lastrowid


def create_customer_profile_with_id(conn, customer_profile):
    sql = """ INSERT INTO customerProfile(customer_id, userName, name, address, phone)
              VALUES(?,?,?,?,?) """
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


def create_customer_group_with_id(conn, customer_group):
    sql = """ INSERT INTO customerGroup(group_id, name)
              VALUES(?,?) """
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


def create_ticket_purchase_with_id(conn, ticket_purchase):
    sql = """ INSERT INTO ticketPurchase(purchase_id, datetime, customer_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket_purchase)
    conn.commit()
    return cur.lastrowid


def get_random_ticket_purchase_id(conn):
    sql = """ SELECT purchase_id FROM ticketPurchase
              ORDER BY RANDOM() LIMIT 1 """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]


def create_ticket_price(conn, ticket_price):
    sql = """ INSERT INTO ticketPrice(price, group_id, play_id)
              VALUES(?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket_price)
    conn.commit()
    return cur.lastrowid


def create_ticket_price_with_id(conn, ticket_price):
    sql = """ INSERT INTO ticketPrice(price_id, price, group_id, play_id)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket_price)
    conn.commit()
    return cur.lastrowid


def get_random_ticket_price_id(conn):
    sql = """ SELECT price_id FROM ticketPrice
              ORDER BY RANDOM() LIMIT 1 """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]


def create_ticket(conn, ticket):
    sql = """ INSERT INTO ticket(purchase_id, performance_id, chair_id, area_id, price_id)
              VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, ticket)
    conn.commit()
    return cur.lastrowid


def create_ticket_with_id(conn, ticket):
    sql = """ INSERT INTO ticket(ticket_id, purchase_id, performance_id, chair_id, area_id, price_id)
              VALUES(?,?,?,?,?,?) """
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


def create_act_with_id(conn, act):
    sql = """ INSERT INTO act(act_id, number, name, play_id)
              VALUES(?,?,?,?) """
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


def create_role_with_id(conn, act):
    sql = """ INSERT INTO role(role_id, name, play_id)
              VALUES(?,?,?) """
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


def create_actor_with_id(conn, actor):
    sql = """ INSERT INTO actor(actor_id, name, email, status, description)
              VALUES(?,?,?,?,?) """
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


def create_employee_with_id(conn, employee):
    sql = """ INSERT INTO employee(employee_id, name, email, status, description, task)
              VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid


# Relationship entities (many-to-many) doesn't need to be created with id


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
