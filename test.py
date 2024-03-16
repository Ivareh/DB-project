import db_connection as dbcon
import db_utils_query as dbuq


def main():
    conn = dbcon.create_connection("theater.db")

    available_chairs_performance_1 = dbuq.get_available_chairs_by_performance_id(
        conn, performance_id=3
    )

    print(available_chairs_performance_1)


if __name__ == "__main__":
    main()
