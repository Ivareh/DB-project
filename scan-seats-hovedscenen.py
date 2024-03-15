import db_utils as dbuc

from format_files_needed import (
    add_hovedscenen_chairs_to_db,
)


if __name__ == "__main__":
    conn = dbuc.create_connection("db.sqlite3")

    area_map = {"Galleri": 1, "Parkett": 3}

    hovedscenen_hall_id = 2
    add_hovedscenen_chairs_to_db(
        "files_needed/hovedscenen.txt",
        area_map,
        hovedscenen_hall_id,
        conn,
    )

