import db_utils_create as dbuc
import db_connection as dbcon


if __name__ == "__main__":
    # with DB connection:
    conn = dbcon.create_connection("theater.db")

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

    # Roles kongsemnene
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
    role_baard_kongsemnene = (15, "Baard Bratte", 1)
    role_tronder_kongsemnene = (16, "Trønder", 1)

    # Roles størst av alt er kjærligheten
    role_sunniva_storst_av_alt_er_kjærligheten = (17, "Sunniva", 3)
    role_jo_storst_av_alt_er_kjærligheten = (18, "Jo", 3)
    role_marte_storst_av_alt_er_kjærligheten = (19, "Marte", 3)
    role_tor_storst_av_alt_er_kjærligheten = (20, "Tor", 3)
    role_trond_storst_av_alt_er_kjærligheten = (21, "Trond-Ove", 3)
    role_natalie_storst_av_alt_er_kjærligheten = (22, "Natalie", 3)
    role_asmund_storst_av_alt_er_kjærligheten = (23, "Åsmund", 3)

    # Kongsemnene actors
    actor_arturo = (
        1,
        "Arturo Scotti",
        "arturo@gmail.com",
        "permanent employee",
        """Utdannelse ved Teaterhøgskolen KHiO (2020-2023)
           
           Skuespiller som etter endt BA i skuespill ved KHiO debuterte på Trøndelag Teater som 
           Kostja Jasji i vår dramatisering av Nino Haratischwilis roman Det åttende livet (til Brilka) i høst.
        """,
    )
    actor_ingunn = (
        2,
        "Ingunn Beate Strige Øyen",
        "ingunn@gmail.com",
        "permanent employee",
        """Født 13. august 1968
           Utdannelse ved Statens Teaterhøgskole (1989 - 1992)
           
           Skuespiller fra Inderøy som etter endt utdannelse ble ansatt på Det Norske 
           Teatret hvor hun debuterte som Cathrine i Frakt under havet av Arthur Miller.
        """,
    )
    actor_hans = (
        3,
        "Hans Petter Nilsen",
        "hans@gmail.com",
        "permanent employee",
        """Født 22. juli 1970
        
        Før han ble ansatt på Trøndelag Teater hadde Hans Petter lang fartstid i SIT 
        (Studentenes Interne Teater) og Universitetsteatret, både som tekstforfatter, 
        musiker og skuespiller. 
        """,
    )
    actor_madeleine = (
        4,
        "Madeleine Brandtzæg Nilsen",
        "madeleine@gmail.com",
        "permanent employee",
        """Født 21. januar 1986 
        Utdannelse Teaterhøgskolen HINT (2008 - 2011)
        
        Skuespiller fra Trondheim som debuterte på Trøndelag Teater
        allerede som 19-åring – som Ronja i Ronja Røverdatter i 2005.
        """,
    )
    actor_synnove = (
        5,
        "Synnøve Fossum Eriksen",
        "synnove@gmail.com",
        "permanent employee",
        """Født 6. mars 1992
        Utdannelse ved Teaterhøgskolen KHiO (2018-2021) og University of Southern 
        California, School of Dramatic Arts, Los Angeles (2010-2014)
        
        Skuespiller fra Asker som kom til Trøndelag Teater fra Teaterhøgskolen ved KHIO
        i 2021.
        """,
    )
    actor_emma = (
        6,
        "Emma Caroline Deichmann",
        "emma@gmail.com",
        "permanent employee",
        """Født 8. februar 1994
           Utdannelse ved Teaterhøgskolen, KHIO (2017-2020)
        
        Skuespiller fra Danmark som debuterte på Trøndelag Teater etter 
        skuespillerutdanningen ved KHiO i rollen som Hilde Wangel i Henrik Ibsens 
        Fruen fra havet på Gamle Scene i 2020.
        """,
    )
    actor_thomas = (
        7,
        "Thomas Jensen Takyi",
        "thomas@gmail.com",
        "permanent employee",
        """Født: 1999
        Utdannelse ved Høyskolen Kristiania/Westerdals (Bachelor skuespill, 2019–22)
        
        Skuespiller fra Trondheim som er utdannet ved Høyskolen Kristiania/Westerdals. 
        Han har medvirket i mange ulike oppsetninger både før og under utdanningen.
        """,
    )
    actor_per = (
        8,
        "Per Bogstad Gulliksen",
        "per@gmail.com",
        "permanent employee",
        """Født 13. september 1968
        Utdanning ved The Arts Educational Drama School, London, UK (1992-95)
        og Teaterhøgskolen, KHiO (2013-15)
        
        Per Bogstad Gulliksen har mastergrad i skuespillerfag fra Teaterhøgskolen, KHIO 2015.
        """,
    )
    actor_isak = (
        9,
        "Isak Holmen Sørensen",
        "isak@gmail.com",
        "permanent employee",
        """Født 10. mai 1991
        Utdannet ved skuespillerlinjen ved Högskolan för scen och musik i Göteborg (2014-2017)
        
        Skuespiller fra Oslo som har tatt sin utdannelse på Högskolan för Scen och Musik 
        ved Göteborgs universitet. 
        """,
    )
    actor_fabian = (
        10,
        "Fabian Heidelberg Lunde",
        "fabian@gmail.com",
        "permanent employee",
        """Født 19. november 1996 Utdannet ved Teatherhøgskolen, KHiO (2018-2021)
        
        Fabian vokste opp på Nøtterøy i Vestfold, og startet med teater da moren hans
        tvang han til å begynne som 10-åring. 
        """,
    )
    actor_emil = (
        11,
        "Emil Olafsson",
        "emil@gmail.com",
        "permanent employee",
        """Født 29. mars 1992
        Utdanning ved Teaterhøgskolen, KHiO (2017-2020)
        
        Skuespiller med utdannelse fra KHiO, Teaterhøgskolen i Oslo som i 2020 ankom 
        Trondheim og medvirket i Det Nye Teaterets streamede oppsetning På veg TeStiklestad.
        """,
    )
    actor_snorre = (
        12,
        "Snorre Ryen Tøndel",
        "snorre@gmail.com",
        "permanent employee",
        """Født 24. juni 1992
        Utdanning ved Högskolan för scen och musik (2014-2017)
        
        Utdannet musikalartist fra Högskolan för scen och musik i Göteborg.
        """,
    )

    # Størst av alt er kjærligheten actors
    actor_sunniva = (
        13,
        "Sunniva Du Mond Nordal",
        "sunniva@gmail.com",
        "permanent employee",
        """Født 14. januar 1993
        Utdanning ved Teaterhøgskolen, KHiO, 2015-2018
        og Musikkteaterhøyskolen 2014-2015
        
        Sunniva Du Mond Nordal er utdannet ved Teaterhøgskolen (KHiO).
        """,
    )
    actor_jo = (
        14,
        "Jo Saberniak",
        "jo@gmail.com",
        "permanent employee",
        """Født 16. februar 1990 Utdanning ved Teaterhøgskolen, KHiO (2017-2020)
        
        Skuespiller med utdannelse fra KHIO, Teaterhøgskolen i Oslo. 
        """,
    )
    actor_marte = (
        15,
        "Marte M. Steinholt",
        "marte@gmail.com",
        "permanent employee",
        """Født: 1. januar 1996 Utdannelse ved Teaterhøgskolen, KHiO (2019-2021)
        
        Marte kommer fra Trondheim og har tidligere bakgrunn fra teaterskole i Sverige.
        """,
    )
    actor_tor = (
        16,
        "Tor Ivar Hagen",
        "tor@gmail.com",
        "permanent employee",
        """Født 22. juli 1981
        Utdannelse ved Bårdarakademiet (2001-2003), Romerike Folkehøgskole (2000-2001)
        
        Hagen er frilans skuespiller ansatt i Skuespiller- og danseralliansen (SKUDA).
        """,
    )
    actor_trond = (
        17,
        "Trond-Ove Skrødal",
        "trond@gmail.com",
        "permanent employee",
        """Født 18. september 1966 
        Utdannelse ved Statens Teaterhøgskole 1986 - 1989
        
        Trond-Ove har etter endt utdannelse jobbet ved Teater Ibsen og Hålogaland Teater
        før han ble ansatt på Trøndelag Teater i 1996.
        """,
    )
    actor_natalie = (
        18,
        "Natalie Grøndahl Tangen",
        "natalie@gmail.com",
        "permanent employee",
        """Født 16. august 1998
        Utdanning ved Teaterhøgskolen, KHiO (2020-2023) og Musikkteaterhøyskolen (2017-2020)

        Natalie fullførte i fjor skuespillerutdanningen ved KHiO og debuterte på 
        Trøndelag Teater som Frida og som understudy Gabriella og Florence i musikalen 
        Så som i himmelen. 
        """,
    )
    actor_asmund = (
        19,
        "Åsmund Flaten",
        "asmund@gmail.com",
        "permanent employee",
        """Åsmund Flaten er utdannet ved NTNU og jobber frilans som musiker og arrangør.
        """,
    )

    # Employees kongsenmene
    employee_yury_kongsemnene = (
        1,
        "Yury Butusov",
        "yury@gmail.com",
        "temporary employee",
        "",
        "Regi og musikkutvelgelse",
    )
    employee_aleksandr_kongsemnene = (
        2,
        "Aleksandr Shishkin-Hokusai",
        "aleksandr@gmail.com",
        "temporary employee",
        "",
        "Scenografi og kostymer",
    )
    employee_eivind_kongsemnene = (
        3,
        "Eivind Myren",
        "eivind@gmail.com",
        "permanent employee",
        "Eivind Myren er fast lysdesigner på Trøndelag Teater.",
        "Lysdesign",
    )
    employee_mina_kongsemnene = (
        4,
        "Mina Rype Stokke",
        "mina@gmail.com",
        "temporary employee",
        "",
        "Dramaturg",
    )

    # Employees størst av alt er kjærligheten
    employee_jonas_storst_av_alt_er_kjærligheten = (
        5,
        "Jonas Corell Petersen",
        "jonas@gmail.com",
        "permanent employee",
        "Jonas Corell Petersen er en dansk regissør og dramatiker bosatt i Norge.",
        "Regi",
    )
    employee_david_storst_av_alt_er_kjærligheten = (
        6,
        "David Gehrt",
        "david@gmail.com",
        "permanent employee",
        "David Gehrt er en dansk scenograf bosatt i København.",
        "Scenografi og kostymer",
    )
    employee_gaute_storst_av_alt_er_kjærligheten = (
        7,
        "Gaute Tønder",
        "gaute@gmail.com",
        "temporary employee",
        "",
        "Musikalsk ansvarlig",
    )
    employee_magnus_storst_av_alt_er_kjærligheten = (
        8,
        "Magnus Mikaelsen",
        "magnus@gmail.com",
        "permanent employee",
        """Etter utannelse innen lysdesign på Romerike FHS i 2004/2005 jobbet 
        Mikkaelsen som lystekniker og lysmester på Nationaltheatret fra 2006 til 2010, 
        før han utdannet seg som lysdesigner ved Stockholms Dramatiska Högskola (2010–2013).
        """,
        "Lysdesign",
    )
    employee_kristoffer_storst_av_alt_er_kjærligheten = (
        9,
        "Kristoffer Spender",
        "kristoffer@gmail.com",
        "temporary employee",
        "",
        "Dramaturg",
    )

    # Actor roles kongsemnene
    actor_arturo_role_haakon = (1, 1)
    actor_ingunn_role_inga = (2, 8)
    actor_hans_role_skule = (3, 7)
    actor_madeleine_role_ragnhild = (4, 10)
    actor_synnove_role_margrete = (5, 12)
    actor_emma_role_sigrid = (6, 4)
    actor_emma_role_ingeborg = (6, 5)
    actor_thomas_role_nikolas = (7, 13)
    actor_per_role_gregorius = (8, 11)
    actor_isak_role_paal = (9, 9)
    actor_isak_role_tronder = (9, 16)
    actor_fabian_role_baard = (10, 15)
    actor_fabian_role_tronder = (10, 16)
    actor_emil_role_jatgeir = (11, 3)
    actor_emil_role_dagfinn = (11, 2)
    actor_snorre_role_peter = (12, 14)

    # Actor roles størst av alt er kjærligheten
    actor_sunniva_role_sunniva = (13, 17)
    actor_jo_role_jo = (14, 18)
    actor_marte_role_marte = (15, 19)
    actor_tor_role_tor = (16, 20)
    actor_trond_role_trond = (17, 21)
    actor_natalie_role_natalie = (18, 22)
    actor_asmund_role_asmund = (19, 23)

    # Actor plays kongsemnene
    actor_arturo_kongsemnene_play = (1, 1)
    actor_ingunn_kongsemnene_play = (2, 1)
    actor_hans_kongsemnene_play = (3, 1)
    actor_madeleine_kongsemnene_play = (4, 1)
    actor_synnove_kongsemnene_play = (5, 1)
    actor_emma_kongsemnene_play = (6, 1)
    actor_thomas_kongsemnene_play = (7, 1)
    actor_per_kongsemnene_play = (8, 1)
    actor_isak_kongsemnene_play = (9, 1)
    actor_fabian_kongsemnene_play = (10, 1)
    actor_emil_kongsemnene_play = (11, 1)
    actor_snorre_kongsemnene_play = (12, 1)

    # Actor plays størst av alt er kjærligheten
    actor_sunniva_storst_av_alt_er_kjærligheten_play = (13, 3)
    actor_jo_storst_av_alt_er_kjærligheten_play = (14, 3)
    actor_marte_storst_av_alt_er_kjærligheten_play = (15, 3)
    actor_tor_storst_av_alt_er_kjærligheten_play = (16, 3)
    actor_trond_storst_av_alt_er_kjærligheten_play = (17, 3)
    actor_natalie_storst_av_alt_er_kjærligheten_play = (18, 3)
    actor_asmund_storst_av_alt_er_kjærligheten_play = (19, 3)

    # Employee plays kongsemnene
    employee_yury_kongsemnene_play = (1, 1)
    employee_aleksandr_kongsemnene_play = (2, 1)
    employee_eivind_kongsemnene_play = (3, 1)
    employee_mina_kongsemnene_play = (4, 1)

    # Employee plays størst av alt er kjærligheten
    employee_jonas_storst_av_alt_er_kjærligheten_play = (5, 3)
    employee_david_storst_av_alt_er_kjærligheten_play = (6, 3)
    employee_gaute_storst_av_alt_er_kjærligheten_play = (7, 3)
    employee_magnus_storst_av_alt_er_kjærligheten_play = (8, 3)
    employee_kristoffer_storst_av_alt_er_kjærligheten_play = (9, 3)

    # Act roles kongsemnene
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

    # Employee playes kongsemnene
    employee_yury_kongsemnene_play = (1, 1)
    employee_aleksandr_kongsemnene_play = (2, 1)
    employee_eivind_kongsemnene_play = (3, 1)
    employee_mina_kongsemnene_play = (4, 1)

    # Employee playes størst av alt er kjærligheten
    employee_jonas_storst_av_alt_er_kjærligheten_play = (5, 3)
    employee_david_storst_av_alt_er_kjærligheten_play = (6, 3)
    employee_gaute_storst_av_alt_er_kjærligheten_play = (7, 3)
    employee_magnus_storst_av_alt_er_kjærligheten_play = (8, 3)
    employee_kristoffer_storst_av_alt_er_kjærligheten_play = (9, 3)

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

    dbuc.create_actor_with_id(conn, actor_arturo)
    dbuc.create_actor_with_id(conn, actor_ingunn)
    dbuc.create_actor_with_id(conn, actor_hans)
    dbuc.create_actor_with_id(conn, actor_madeleine)
    dbuc.create_actor_with_id(conn, actor_synnove)
    dbuc.create_actor_with_id(conn, actor_emma)
    dbuc.create_actor_with_id(conn, actor_thomas)
    dbuc.create_actor_with_id(conn, actor_per)
    dbuc.create_actor_with_id(conn, actor_isak)
    dbuc.create_actor_with_id(conn, actor_fabian)
    dbuc.create_actor_with_id(conn, actor_emil)
    dbuc.create_actor_with_id(conn, actor_snorre)

    dbuc.create_actor_with_id(conn, actor_sunniva)
    dbuc.create_actor_with_id(conn, actor_jo)
    dbuc.create_actor_with_id(conn, actor_marte)
    dbuc.create_actor_with_id(conn, actor_tor)
    dbuc.create_actor_with_id(conn, actor_trond)
    dbuc.create_actor_with_id(conn, actor_natalie)
    dbuc.create_actor_with_id(conn, actor_asmund)

    dbuc.create_employee_with_id(conn, employee_yury_kongsemnene)
    dbuc.create_employee_with_id(conn, employee_aleksandr_kongsemnene)
    dbuc.create_employee_with_id(conn, employee_eivind_kongsemnene)
    dbuc.create_employee_with_id(conn, employee_mina_kongsemnene)

    dbuc.create_employee_with_id(conn, employee_jonas_storst_av_alt_er_kjærligheten)
    dbuc.create_employee_with_id(conn, employee_david_storst_av_alt_er_kjærligheten)
    dbuc.create_employee_with_id(conn, employee_gaute_storst_av_alt_er_kjærligheten)
    dbuc.create_employee_with_id(conn, employee_magnus_storst_av_alt_er_kjærligheten)
    dbuc.create_employee_with_id(
        conn, employee_kristoffer_storst_av_alt_er_kjærligheten
    )

    dbuc.create_actor_role(conn, actor_arturo_role_haakon)
    dbuc.create_actor_role(conn, actor_ingunn_role_inga)
    dbuc.create_actor_role(conn, actor_hans_role_skule)
    dbuc.create_actor_role(conn, actor_madeleine_role_ragnhild)
    dbuc.create_actor_role(conn, actor_synnove_role_margrete)
    dbuc.create_actor_role(conn, actor_emma_role_sigrid)
    dbuc.create_actor_role(conn, actor_emma_role_ingeborg)
    dbuc.create_actor_role(conn, actor_thomas_role_nikolas)
    dbuc.create_actor_role(conn, actor_per_role_gregorius)
    dbuc.create_actor_role(conn, actor_isak_role_paal)
    dbuc.create_actor_role(conn, actor_isak_role_tronder)
    dbuc.create_actor_role(conn, actor_fabian_role_baard)
    dbuc.create_actor_role(conn, actor_fabian_role_tronder)
    dbuc.create_actor_role(conn, actor_emil_role_jatgeir)
    dbuc.create_actor_role(conn, actor_emil_role_dagfinn)
    dbuc.create_actor_role(conn, actor_snorre_role_peter)

    dbuc.create_actor_role(conn, actor_sunniva_role_sunniva)
    dbuc.create_actor_role(conn, actor_jo_role_jo)
    dbuc.create_actor_role(conn, actor_marte_role_marte)
    dbuc.create_actor_role(conn, actor_tor_role_tor)
    dbuc.create_actor_role(conn, actor_trond_role_trond)
    dbuc.create_actor_role(conn, actor_natalie_role_natalie)
    dbuc.create_actor_role(conn, actor_asmund_role_asmund)

    dbuc.create_actor_play(conn, actor_arturo_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_ingunn_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_hans_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_madeleine_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_synnove_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_emma_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_thomas_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_per_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_isak_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_fabian_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_emil_kongsemnene_play)
    dbuc.create_actor_play(conn, actor_snorre_kongsemnene_play)

    dbuc.create_actor_play(conn, actor_sunniva_storst_av_alt_er_kjærligheten_play)
    dbuc.create_actor_play(conn, actor_jo_storst_av_alt_er_kjærligheten_play)
    dbuc.create_actor_play(conn, actor_marte_storst_av_alt_er_kjærligheten_play)
    dbuc.create_actor_play(conn, actor_tor_storst_av_alt_er_kjærligheten_play)
    dbuc.create_actor_play(conn, actor_trond_storst_av_alt_er_kjærligheten_play)
    dbuc.create_actor_play(conn, actor_natalie_storst_av_alt_er_kjærligheten_play)
    dbuc.create_actor_play(conn, actor_asmund_storst_av_alt_er_kjærligheten_play)

    dbuc.create_employee_play(conn, employee_yury_kongsemnene_play)
    dbuc.create_employee_play(conn, employee_aleksandr_kongsemnene_play)
    dbuc.create_employee_play(conn, employee_eivind_kongsemnene_play)
    dbuc.create_employee_play(conn, employee_mina_kongsemnene_play)

    dbuc.create_employee_play(conn, employee_jonas_storst_av_alt_er_kjærligheten_play)
    dbuc.create_employee_play(conn, employee_david_storst_av_alt_er_kjærligheten_play)
    dbuc.create_employee_play(conn, employee_gaute_storst_av_alt_er_kjærligheten_play)
    dbuc.create_employee_play(conn, employee_magnus_storst_av_alt_er_kjærligheten_play)
    dbuc.create_employee_play(
        conn, employee_kristoffer_storst_av_alt_er_kjærligheten_play
    )

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
