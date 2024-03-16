import sqlite3


def get_performances_by_hall_and_date(conn, hall_id, date):
    sql = """ SELECT * FROM performance 
                WHERE hall_id = ? 
                AND 
                datetime LIKE '%' || ? || '%'"""
    cur = conn.cursor()
    cur.execute(sql, (hall_id, date))
    return cur.fetchall()


def get_area_id_from_area_name(conn, area_name, hall_id):
    sql = """ SELECT area_id FROM area 
              WHERE name = ? AND hall_id = ? """
    cur = conn.cursor()
    cur.execute(sql, (area_name, hall_id))
    return cur.fetchone()[0]


def get_available_chairs_in_hall_by_performance_id(
    conn,
    performance_id,
):
    sql = """ SELECT chair_id FROM chair 
              WHERE chair_id NOT IN 
              (SELECT chair_id FROM ticket 
              WHERE performance_id = ? AND purchase_id IS NOT NULL)
              AND
              hall_id IN 
              (SELECT hall_id FROM performance WHERE performance_id = ?)
              """
    cur = conn.cursor()
    cur.execute(
        sql,
        (performance_id, performance_id),
    )
    return cur.fetchall()


def get_random_ticket_purchase_id(conn):
    sql = """ SELECT purchase_id FROM ticketPurchase
              ORDER BY RANDOM() LIMIT 1 """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]


def get_random_ticket_price_id(conn):
    sql = """ SELECT price_id FROM ticketPrice
              ORDER BY RANDOM() LIMIT 1 """
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]


def get_total_cost_on_tickets_by_performance_id(conn, performance_id):
    sql = """ SELECT SUM(price) FROM ticketPrice 
              WHERE play_id IN 
              (SELECT play_id FROM performance WHERE performance_id = ?) """
    cur = conn.cursor()
    cur.execute(sql, (performance_id,))
    return cur.fetchone()[0]