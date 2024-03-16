import db_utils_query as dbuq
import db_connection as dbcon

from read_from_files_needed import get_date_from_file, read_and_create_chairs


if __name__ == "__main__":
    conn = dbcon.create_connection("theater.db")

    date = get_date_from_file("files_needed/gamle-scene.txt")

    performances_gamle_scene = dbuq.get_performances_by_hall_and_date(
        conn, hall_id=2, date=date
    )

    read_and_create_chairs(
        conn,
        "files_needed/gamle-scene.txt",
        performances=performances_gamle_scene,
        hall_id=2,
        reset_lines=True,
    )
