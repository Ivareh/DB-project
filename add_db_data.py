import db_utils_create as dbuc


if __name__ == "__main__":
    conn = dbuc.create_connection("db.sqlite3")

    # with conn:

    # Seasons

    spring_season = ("Spring", 2024)
    winter_season = ("Winter", 2024)

    # Theater Halls
    old_scene_hall = ("Gamle Scene", 200)
    main_scene_hall = ("Main Scene", 516)
    theater_basement_hall = ("Theater Basement", 60)
    theater_cafe_hall = ("Theater Cafe", 100)

    # Plays
    kongsemnene_play_spring = (
        "Kongsemnene",
        "Henrik Ibsen",
        "Ca. 4 timer inkludert to pauser",
        2,
        1,
    )
    kongsemnene_play_winter = (
        "Kongsemnene",
        "Henrik Ibsen",
        "Ca. 4 timer inkludert to pauser",
        2,
        2,
    )
    storst_av_alt_er_kjærligheten_play_spring = (
        "Størst av alt er kjærligheten",
        "Jonas Corell Petersen",
        "Ca. 1 time 30 minutter. Spilles uten pause",
        1,
        1,
    )
    storst_av_alt_er_kjærligheten_play_winter = (
        "Størst av alt er kjærligheten",
        "Jonas Corell Petersen",
        "Ca. 1 time 30 minutter. Spilles uten pause",
        1,
        2,
    )

    # Acts
    # act = (1, "Act 1", 1)

    # Performances
    performance_feb_1_kongsemnene_spring = ("2024-02-01 19:00:00", 2, 1)
    performance_feb_2_kongsemnene_spring = ("2024-02-02 19:00:00", 2, 1)
    performance_feb_3_kongsemnene_spring = ("2024-02-03 19:00:00", 2, 1)
    performance_feb_5_kongsemnene_spring = ("2024-02-05 19:00:00", 2, 1)
    performance_feb_6_kongsemnene_spring = ("2024-02-06 19:00:00", 2, 1)

    performance_feb_3_storst_av_alt_er_kjærligheten_spring = (
        "2022-02-03 18:30:00",
        1,
        3,
    )
    performance_feb_6_storst_av_alt_er_kjærligheten_spring = (
        "2022-02-06 18:30:00",
        1,
        3,
    )
    performance_feb_7_storst_av_alt_er_kjærligheten_spring = (
        "2022-02-07 18:30:00",
        1,
        3,
    )
    performance_feb_12_storst_av_alt_er_kjærligheten_spring = (
        "2022-02-12 18:30:00",
        1,
        3,
    )
    performance_feb_13_storst_av_alt_er_kjærligheten_spring = (
        "2022-02-13 18:30:00",
        1,
        3,
    )
    performance_feb_14_storst_av_alt_er_kjærligheten_spring = (
        "2022-02-14 18:30:00",
        1,
        3,
    )

    # Areas
    galleri_old_scene_area = ("Galleri", 1)
    balkong_old_scene_area = ("Balkong", 1)
    parkett_old_scene_area = ("Parkett", 1)

    galleri_main_scene_area = ("Galleri", 2)
    parkett_main_scene_area = ("Parkett", 2)

    # Chairs
    # chair = (1, 1, 1, 1)

    # Ticket Prices
    # ticket_price = (200, 1, 1)

    # Tickets
    # ticket = (1, 1, 1, 1)

    # Customer Group
    ordinary_customer_group = ("Ordinary",)
    honour_customer_group = ("Honour",)
    student_customer_group = ("Student",)
    children_customer_group = ("Children",)
    ten_customer_group = ("Group 10",)
    ten_honour_customer_group = ("Group honours 10",)

    # Ticket Price
    ticket_price_ordinary_kongsemnene = (450, 1, 1)
    ticket_price_honour_kongsemnene = (380, 1, 2)
    ticket_price_student_kongsemnene = (280, 1, 3)
    ticket_price_ten_kongsemnene = (420, 1, 5)
    ticket_price_ten_honours_kongsemnene = (360, 1, 6)

    ticket_price_ordinary_storst_av_alt_er_kjærligheten = (350, 3, 1)
    ticket_price_honour_storst_av_alt_er_kjærligheten = (300, 3, 2)
    ticket_price_student_storst_av_alt_er_kjærligheten = (220, 3, 3)
    ticket_price_children_storst_av_alt_er_kjærligheten = (220, 3, 4)
    ticket_price_ten_storst_av_alt_er_kjærligheten = (320, 3, 5)
    ticket_price_ten_honours_storst_av_alt_er_kjærligheten = (270, 3, 6)

    ticket_purchase = ("2022-01-01 14:00:00", 1)

    ticket = (1, 1, 1, 1)

    # Customer Profile
    customer_sjukingen_profile = ("Sjukingen", "Elgesetergate 1", "12345678")

    # Ticket Purchase
    ticket_purchase = ("2022-04-01 19:00:00", 1)

    dbuc.create_season(conn, spring_season)
    dbuc.create_season(conn, winter_season)

    dbuc.create_theater_hall(conn, old_scene_hall)
    dbuc.create_theater_hall(conn, main_scene_hall)
    dbuc.create_theater_hall(conn, theater_basement_hall)
    dbuc.create_theater_hall(conn, theater_cafe_hall)

    dbuc.create_play(conn, kongsemnene_play_spring)
    dbuc.create_play(conn, kongsemnene_play_winter)
    dbuc.create_play(conn, storst_av_alt_er_kjærligheten_play_spring)
    dbuc.create_play(conn, storst_av_alt_er_kjærligheten_play_winter)

    dbuc.create_performance(conn, performance_feb_1_kongsemnene_spring)
    dbuc.create_performance(conn, performance_feb_2_kongsemnene_spring)
    dbuc.create_performance(conn, performance_feb_3_kongsemnene_spring)
    dbuc.create_performance(conn, performance_feb_5_kongsemnene_spring)
    dbuc.create_performance(conn, performance_feb_6_kongsemnene_spring)

    dbuc.create_performance(
        conn, performance_feb_3_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance(
        conn, performance_feb_6_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance(
        conn, performance_feb_7_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance(
        conn, performance_feb_12_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance(
        conn, performance_feb_13_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance(
        conn, performance_feb_14_storst_av_alt_er_kjærligheten_spring
    )

    dbuc.create_area(conn, galleri_old_scene_area)
    dbuc.create_area(conn, balkong_old_scene_area)
    dbuc.create_area(conn, parkett_old_scene_area)
    dbuc.create_area(conn, galleri_main_scene_area)
    dbuc.create_area(conn, parkett_main_scene_area)

    dbuc.create_customer_group(conn, ordinary_customer_group)
    dbuc.create_customer_group(conn, honour_customer_group)
    dbuc.create_customer_group(conn, student_customer_group)
    dbuc.create_customer_group(conn, children_customer_group)
    dbuc.create_customer_group(conn, ten_customer_group)
    dbuc.create_customer_group(conn, ten_honour_customer_group)

    dbuc.create_ticket_price(conn, ticket_price_ordinary_kongsemnene)
    dbuc.create_ticket_price(conn, ticket_price_honour_kongsemnene)
    dbuc.create_ticket_price(conn, ticket_price_student_kongsemnene)
    dbuc.create_ticket_price(conn, ticket_price_ten_kongsemnene)
    dbuc.create_ticket_price(conn, ticket_price_ten_honours_kongsemnene)
    dbuc.create_ticket_price(conn, ticket_price_ordinary_storst_av_alt_er_kjærligheten)
    dbuc.create_ticket_price(conn, ticket_price_honour_storst_av_alt_er_kjærligheten)
    dbuc.create_ticket_price(conn, ticket_price_student_storst_av_alt_er_kjærligheten)
    dbuc.create_ticket_price(conn, ticket_price_children_storst_av_alt_er_kjærligheten)
    dbuc.create_ticket_price(conn, ticket_price_ten_storst_av_alt_er_kjærligheten)
    dbuc.create_ticket_price(
        conn, ticket_price_ten_honours_storst_av_alt_er_kjærligheten
    )

    dbuc.create_ticket_purchase(conn, ticket_purchase)

    dbuc.create_ticket(conn, ticket)

    dbuc.create_customer_group(conn, ordinary_customer_group)
    dbuc.create_customer_group(conn, honour_customer_group)
    dbuc.create_customer_group(conn, student_customer_group)
    dbuc.create_customer_group(conn, ten_customer_group)
    dbuc.create_customer_group(conn, ten_honour_customer_group)

    dbuc.create_customer_profile(conn, customer_sjukingen_profile)
