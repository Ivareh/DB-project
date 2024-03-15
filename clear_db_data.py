import sqlite3

# Created with AI with prompt "How in python for sqlite3 database, clear data from all tables?"

def clear_data_from_all_tables(database_path = "theater.db"):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    try:
        # Get a list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Clear data from each table
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DELETE FROM {table_name};")
            print(f"Cleared data from table: {table_name}")

        # Commit the changes and close the connection
        connection.commit()
        print("Data cleared from all tables.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()

# Replace 'your_database.db' with the path to your SQLite database file
clear_data_from_all_tables("theater.db")
