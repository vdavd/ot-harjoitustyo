from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            username TEXT PRIMARY KEY,
            hiscore INTEGER
        );
    ''')

    connection.commit()


def initialize_database(mode="production"):
    connection = get_database_connection(mode)

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
