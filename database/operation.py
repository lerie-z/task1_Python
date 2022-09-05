import sys
from file_handlers.file_reader import FileReader
from database.connection import DBConnection
import psycopg2
import psycopg2.extras

sys.path.insert(0, '/database/')


class DBOperationHandler(DBConnection, FileReader):
    def __init__(self, database: dict, path: dict) -> None:
        super().__init__(database)
        self.__path = path

    def execute_scripts(self, rooms: dict, students: dict) -> None:
        print('conn est')
        self.create_tables()
        self.insert_rooms_table(rooms)
        self.insert_students_table(students)
        self._conn.close()

    def create_tables(self) -> None:
        try:
            path = self.__path['tables']
            with self._conn.cursor() as curs:
                curs.execute(self._get_file(path + 'drop_tables.sql'))
                print('k!')
                curs.execute(self._get_file(path + 'create_rooms_table.sql'))
                curs.execute(self._get_file(path + 'create_students_table.sql'))
            self._conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_rooms_table(self, rooms: dict) -> None:
        try:
            query = self._get_file(self.__path['inserts'] + 'insert_rooms_table.sql')
            with self._conn.cursor() as cursor:
                for room in rooms:
                    cursor.execute(query.format(room['id'], room['name']))
            self._conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_students_table(self, students: dict) -> None:
        try:
            query = self._get_file(self.__path['inserts'] + 'insert_students_table.sql')
            with self._conn.cursor() as cursor:
                for student in students:
                    cursor.execute(query.format(
                        student['id'], student['name'], student['room'], student['sex'], student['birthday']
                    ))
            self._conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
