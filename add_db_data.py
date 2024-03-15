import db_utils as dbuc
import db_connection as dbcon


if __name__ == "__main__":
    # with DB connection:
    conn = dbcon.create_connection("db.sqlite3")

    # Theater Halls
    main_scene_hall = (1, "Main Scene", 516)
    old_scene_hall = (2, "Gamle Scene", 200)
    theater_basement_hall = (3, "Theater Basement", 60)
    theater_cafe_hall = (4, "Theater Cafe", 100)

    # Seasons
    spring_season = (1, "Spring", 2024)
    winter_season = (2, "Winter", 2024)

    # Plays
    kongsemnene_play_spring = (
        1,
        "Kongsemnene",
        "Henrik Ibsen",
        """Striden om tronen mellom kong Håkon Håkonsson og rivalen Skule Bårdsson, 
        skrevet av Henrik Ibsen.""",
        1,
        1,
    )
    kongsemnene_play_winter = (
        2,
        "Kongsemnene",
        "Henrik Ibsen",
        """Striden om tronen mellom kong Håkon Håkonsson og rivalen Skule Bårdsson, 
        skrevet av Henrik Ibsen.""",
        2,
        1,
    )
    storst_av_alt_er_kjærligheten_play_spring = (
        3,
        "Størst av alt er kjærligheten",
        "Jonas Corell Petersen",
        """Størst av alt er kjærligheten er en scenisk og 
        musikalsk utforskning av kjærligheten på Gamle Scene.""",
        1,
        2,
    )
    storst_av_alt_er_kjærligheten_play_winter = (
        4,
        "Størst av alt er kjærligheten",
        "Jonas Corell Petersen",
        """Størst av alt er kjærligheten er en scenisk og 
        musikalsk utforskning av kjærligheten på Gamle Scene.""",
        2,
        2,
    )

    # Acts
    # act = (1, "Act 1", 1)

    # Performances
    performance_feb_1_kongsemnene_spring = (1, "2024-02-01 19:00:00", 1, 1)
    performance_feb_2_kongsemnene_spring = (2, "2024-02-02 19:00:00", 1, 1)
    performance_feb_3_kongsemnene_spring = (3, "2024-02-03 19:00:00", 1, 1)
    performance_feb_5_kongsemnene_spring = (4, "2024-02-05 19:00:00", 1, 1)
    performance_feb_6_kongsemnene_spring = (5, "2024-02-06 19:00:00", 1, 1)

    performance_feb_3_storst_av_alt_er_kjærligheten_spring = (
        6,
        "2024-02-03 18:30:00",
        3,
        2,
    )
    performance_feb_6_storst_av_alt_er_kjærligheten_spring = (
        7,
        "2024-02-06 18:30:00",
        3,
        2,
    )
    performance_feb_7_storst_av_alt_er_kjærligheten_spring = (
        8,
        "2024-02-07 18:30:00",
        3,
        2,
    )
    performance_feb_12_storst_av_alt_er_kjærligheten_spring = (
        9,
        "2024-02-12 18:30:00",
        3,
        2,
    )
    performance_feb_13_storst_av_alt_er_kjærligheten_spring = (
        10,
        "2024-02-13 18:30:00",
        3,
        2,
    )
    performance_feb_14_storst_av_alt_er_kjærligheten_spring = (
        11,
        "2024-02-14 18:30:00",
        3,
        2,
    )

    # Areas
    galleri_main_scene_area = (1, "Galleri", 1)
    parkett_main_scene_area = (2, "Parkett", 1)

    galleri_old_scene_area = (3, "Galleri", 2)
    balkong_old_scene_area = (4, "Balkong", 2)
    parkett_old_scene_area = (5, "Parkett", 2)

    # Customer Profile
    customer_sjukingen_profile = (
        1,
        "Sjukingen",
        "Ole Per",
        "Elgesetergate 1",
        "12345678",
    )

    # Customer Group
    ordinary_customer_group = (1, "Ordinary")
    honour_customer_group = (2, "Honour")
    student_customer_group = (3, "Student")
    children_customer_group = (4, "Children")
    ten_customer_group = (5, "Group 10")
    ten_honour_customer_group = (6, "Group honours 10")

    # Ticket Purchase
    ticket_purchase = (1, "2024-01-01 14:00:00", 1)

    # Ticket Price, assume the prices are for only Spring 2024
    ticket_price_ordinary_kongsemnene = (1, 450, 1, 1)
    ticket_price_honour_kongsemnene = (2, 380, 2, 1)
    ticket_price_student_kongsemnene = (3, 280, 3, 1)
    ticket_price_ten_kongsemnene = (4, 420, 5, 1)
    ticket_price_ten_honours_kongsemnene = (5, 360, 6, 1)

    ticket_price_ordinary_storst_av_alt_er_kjærligheten = (6, 350, 1, 3)
    ticket_price_honour_storst_av_alt_er_kjærligheten = (7, 300, 2, 3)
    ticket_price_student_storst_av_alt_er_kjærligheten = (8, 220, 3, 3)
    ticket_price_children_storst_av_alt_er_kjærligheten = (9, 220, 4, 3)
    ticket_price_ten_storst_av_alt_er_kjærligheten = (10, 320, 5, 3)
    ticket_price_ten_honours_storst_av_alt_er_kjærligheten = (11, 270, 6, 3)

    # Acts
    act_1_kongsemnene = (1, 1, "Act 1", 1)
    act_2_kongsemnene = (2, 2, "Act 2", 1)
    act_3_kongsemnene = (3, 3, "Act 3", 1)
    act_4_kongsemnene = (4, 4, "Act 4", 1)
    act_5_kongsemnene = (5, 5, "Act 5", 1)

    act_1_storst_av_alt_er_kjærligheten = (6, 1, "Act 1", 3)

    # Roles
    role_hakon_kongsemnene = (1, "Håkon Håkonson", 1)
    role_dagfinn_kongsemnene = (2, "Dagfinn Bonde", 1)
    role_jatgeir_kongsemnene = (3, "Jatgeir Skald", 1)
    role_sigrid_kongsemnene = (4, "Sigrid", 1)
    role_ingeborg_kongsemnene = (5, "Ingeborg", 1)
    role_guttorm_kongsemnene = (6, "Guttorm Ingesson", 1)
    role_skule_kongsemnene = (7, "Skule Jarl", 1)
    role_inga_kongsemnene = (8, "Inga frå Vartejg", 1)
    role_paal_kongsemnene = (9, "Paal Flida", 1)
    role_ragnhild_kongsemnene = (10, "Ragnhild", 1)
    role_gregorius_kongsemnene = (11, "Gregorius Jonsson", 1)
    role_margrete_kongsemnene = (12, "Margrete", 1)
    role_biskop_kongsemnene = (13, "Biskop Nikolas", 1)
    role_peter_kongsemnene = (14, "Peter", 1)

    # Act roles
    act_role_1_hakon_kongsemnene = (1, 1)
    act_role_2_hakon_kongsemnene = (2, 1)
    act_role_3_hakon_kongsemnene = (3, 1)
    act_role_4_hakon_kongsemnene = (4, 1)
    act_role_5_hakon_kongsemnene = (5, 1)

    act_role_1_dagfinn_kongsemnene = (1, 2)
    act_role_2_dagfinn_kongsemnene = (2, 2)
    act_role_3_dagfinn_kongsemnene = (3, 2)
    act_role_4_dagfinn_kongsemnene = (4, 2)
    act_role_5_dagfinn_kongsemnene = (5, 2)

    act_role_4_jatgeir_kongsemnene = (4, 3)

    act_role_1_sigrid_kongsemnene = (1, 4)
    act_role_2_sigrid_kongsemnene = (2, 4)
    act_role_5_sigrid_kongsemnene = (5, 4)

    act_role_4_ingeborg_kongsemnene = (4, 5)

    act_role_1_guttorm_kongsemnene = (1, 6)

    act_role_1_skule_kongsemnene = (1, 7)
    act_role_2_skule_kongsemnene = (2, 7)
    act_role_3_skule_kongsemnene = (3, 7)
    act_role_4_skule_kongsemnene = (4, 7)
    act_role_5_skule_kongsemnene = (5, 7)

    act_role_1_inga_kongsemnene = (1, 8)
    act_role_3_inga_kongsemnene = (3, 8)

    act_role_1_paal_kongsemnene = (1, 9)
    act_role_2_paal_kongsemnene = (2, 9)
    act_role_3_paal_kongsemnene = (3, 9)
    act_role_4_paal_kongsemnene = (4, 9)
    act_role_5_paal_kongsemnene = (5, 9)

    act_role_1_ragnhild_kongsemnene = (1, 10)
    act_role_5_ragnhild_kongsemnene = (5, 10)

    act_role_1_gregorius_kongsemnene = (1, 11)
    act_role_2_gregorius_kongsemnene = (2, 11)
    act_role_3_gregorius_kongsemnene = (3, 11)
    act_role_4_gregorius_kongsemnene = (4, 11)
    act_role_5_gregorius_kongsemnene = (5, 11)

    act_role_1_margrete_kongsemnene = (1, 12)
    act_role_2_margrete_kongsemnene = (2, 12)
    act_role_3_margrete_kongsemnene = (3, 12)
    act_role_4_margrete_kongsemnene = (4, 12)
    act_role_5_margrete_kongsemnene = (5, 12)

    act_role_1_biskop_kongsemnene = (1, 13)
    act_role_2_biskop_kongsemnene = (2, 13)
    act_role_3_biskop_kongsemnene = (3, 13)

    act_role_3_peter_kongsemnene = (3, 14)
    act_role_4_peter_kongsemnene = (4, 14)
    act_role_5_peter_kongsemnene = (5, 14)

    # Add data above to the database

    dbuc.create_theater_hall_with_id(conn, main_scene_hall)
    dbuc.create_theater_hall_with_id(conn, old_scene_hall)
    dbuc.create_theater_hall_with_id(conn, theater_basement_hall)
    dbuc.create_theater_hall_with_id(conn, theater_cafe_hall)

    dbuc.create_season_with_id(conn, spring_season)
    dbuc.create_season_with_id(conn, winter_season)

    dbuc.create_play_with_id(conn, kongsemnene_play_spring)
    dbuc.create_play_with_id(conn, kongsemnene_play_winter)

    dbuc.create_play_with_id(conn, storst_av_alt_er_kjærligheten_play_spring)
    dbuc.create_play_with_id(conn, storst_av_alt_er_kjærligheten_play_winter)

    dbuc.create_performance_with_id(conn, performance_feb_1_kongsemnene_spring)
    dbuc.create_performance_with_id(conn, performance_feb_2_kongsemnene_spring)
    dbuc.create_performance_with_id(conn, performance_feb_3_kongsemnene_spring)
    dbuc.create_performance_with_id(conn, performance_feb_5_kongsemnene_spring)
    dbuc.create_performance_with_id(conn, performance_feb_6_kongsemnene_spring)

    dbuc.create_performance_with_id(
        conn, performance_feb_3_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance_with_id(
        conn, performance_feb_6_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance_with_id(
        conn, performance_feb_7_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance_with_id(
        conn, performance_feb_12_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance_with_id(
        conn, performance_feb_13_storst_av_alt_er_kjærligheten_spring
    )
    dbuc.create_performance_with_id(
        conn, performance_feb_14_storst_av_alt_er_kjærligheten_spring
    )

    dbuc.create_area_with_id(conn, galleri_main_scene_area)
    dbuc.create_area_with_id(conn, parkett_main_scene_area)
    dbuc.create_area_with_id(conn, galleri_old_scene_area)
    dbuc.create_area_with_id(conn, balkong_old_scene_area)
    dbuc.create_area_with_id(conn, parkett_old_scene_area)

    dbuc.create_customer_profile_with_id(conn, customer_sjukingen_profile)

    dbuc.create_customer_group_with_id(conn, ordinary_customer_group)
    dbuc.create_customer_group_with_id(conn, honour_customer_group)
    dbuc.create_customer_group_with_id(conn, student_customer_group)
    dbuc.create_customer_group_with_id(conn, children_customer_group)
    dbuc.create_customer_group_with_id(conn, ten_customer_group)
    dbuc.create_customer_group_with_id(conn, ten_honour_customer_group)

    dbuc.create_ticket_purchase_with_id(conn, ticket_purchase)

    dbuc.create_ticket_price_with_id(conn, ticket_price_ordinary_kongsemnene)
    dbuc.create_ticket_price_with_id(conn, ticket_price_honour_kongsemnene)
    dbuc.create_ticket_price_with_id(conn, ticket_price_student_kongsemnene)
    dbuc.create_ticket_price_with_id(conn, ticket_price_ten_kongsemnene)
    dbuc.create_ticket_price_with_id(conn, ticket_price_ten_honours_kongsemnene)

    dbuc.create_ticket_price_with_id(
        conn, ticket_price_ordinary_storst_av_alt_er_kjærligheten
    )
    dbuc.create_ticket_price_with_id(
        conn, ticket_price_honour_storst_av_alt_er_kjærligheten
    )
    dbuc.create_ticket_price_with_id(
        conn, ticket_price_student_storst_av_alt_er_kjærligheten
    )
    dbuc.create_ticket_price_with_id(
        conn, ticket_price_children_storst_av_alt_er_kjærligheten
    )
    dbuc.create_ticket_price_with_id(
        conn, ticket_price_ten_storst_av_alt_er_kjærligheten
    )
    dbuc.create_ticket_price_with_id(
        conn, ticket_price_ten_honours_storst_av_alt_er_kjærligheten
    )

    dbuc.create_act_with_id(conn, act_1_kongsemnene)
    dbuc.create_act_with_id(conn, act_2_kongsemnene)
    dbuc.create_act_with_id(conn, act_3_kongsemnene)
    dbuc.create_act_with_id(conn, act_4_kongsemnene)
    dbuc.create_act_with_id(conn, act_5_kongsemnene)

    dbuc.create_act_with_id(conn, act_1_storst_av_alt_er_kjærligheten)

    dbuc.create_role_with_id(conn, role_hakon_kongsemnene)
    dbuc.create_role_with_id(conn, role_dagfinn_kongsemnene)
    dbuc.create_role_with_id(conn, role_jatgeir_kongsemnene)
    dbuc.create_role_with_id(conn, role_sigrid_kongsemnene)
    dbuc.create_role_with_id(conn, role_ingeborg_kongsemnene)
    dbuc.create_role_with_id(conn, role_guttorm_kongsemnene)
    dbuc.create_role_with_id(conn, role_skule_kongsemnene)
    dbuc.create_role_with_id(conn, role_inga_kongsemnene)
    dbuc.create_role_with_id(conn, role_paal_kongsemnene)
    dbuc.create_role_with_id(conn, role_ragnhild_kongsemnene)
    dbuc.create_role_with_id(conn, role_gregorius_kongsemnene)
    dbuc.create_role_with_id(conn, role_margrete_kongsemnene)
    dbuc.create_role_with_id(conn, role_biskop_kongsemnene)
    dbuc.create_role_with_id(conn, role_peter_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_hakon_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_hakon_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_hakon_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_hakon_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_hakon_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_dagfinn_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_dagfinn_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_dagfinn_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_dagfinn_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_dagfinn_kongsemnene)

    dbuc.create_act_role(conn, act_role_4_jatgeir_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_sigrid_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_sigrid_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_sigrid_kongsemnene)

    dbuc.create_act_role(conn, act_role_4_ingeborg_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_guttorm_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_skule_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_skule_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_skule_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_skule_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_skule_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_inga_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_inga_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_paal_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_paal_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_paal_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_paal_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_paal_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_ragnhild_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_ragnhild_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_gregorius_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_gregorius_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_gregorius_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_gregorius_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_gregorius_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_margrete_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_margrete_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_margrete_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_margrete_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_margrete_kongsemnene)

    dbuc.create_act_role(conn, act_role_1_biskop_kongsemnene)
    dbuc.create_act_role(conn, act_role_2_biskop_kongsemnene)
    dbuc.create_act_role(conn, act_role_3_biskop_kongsemnene)

    dbuc.create_act_role(conn, act_role_3_peter_kongsemnene)
    dbuc.create_act_role(conn, act_role_4_peter_kongsemnene)
    dbuc.create_act_role(conn, act_role_5_peter_kongsemnene)
