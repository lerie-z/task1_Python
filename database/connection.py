import sys
import psycopg2

sys.path.insert(0, '/database/')


class DBConnection:
    def __init__(self, database: dict) -> None:
        self._conn = self.establish_connection(database)

    @staticmethod
    def establish_connection(database: dict) -> psycopg2.connect:
        conn = None
        try:
            conn = psycopg2.connect(**database)

            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
