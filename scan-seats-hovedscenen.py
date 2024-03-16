import db_utils_query as dbuq
import db_connection as dbcon

from read_from_files_needed import get_date_from_file, read_and_create_chairs


if __name__ == "__main__":
    conn = dbcon.create_connection("theater.db")

    date = get_date_from_file("files_needed/hovedscenen.txt")

    performances_mainscene = dbuq.get_performances_by_hall_and_date(
        conn, hall_id=1, date=date
    )

    read_and_create_chairs(
        conn,
        "files_needed/hovedscenen.txt",
        performances=performances_mainscene,
        hall_id=1,
        reset_lines=False,
    )
