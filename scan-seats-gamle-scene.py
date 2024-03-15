import db_utils as dbuc
import db_connection as dbcon

from format_files_needed import (
    add_gamle_scene_chairs_to_db,
)


if __name__ == "__main__":
    conn = dbcon.create_connection("db.sqlite3")

    area_map = {"Galleri": 1, "Balkong": 2, "Parkett": 3}

    gamle_scene_hall_id = 1
    add_gamle_scene_chairs_to_db(
        "files_needed/gamle-scene.txt",
        area_map,
        gamle_scene_hall_id,
        conn,
    )
