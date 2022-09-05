import sys, os
sys.path.append('../../')
from config.config import DBConfig
from serializers.json_serializer import JsonSerializer
from serializers.xml_serializer import XmlSerializer
from args_parser import ArgParser
from database.operation import DBOperationHandler
from database.selection import DBSelectionHandler
from file_handlers.file_writer import FileWriter
import psycopg2


def main():
    """ Connect to the PostgreSQL database server """

    arg_parser = ArgParser()
    args = arg_parser.get_arguments()

    serializer = JsonSerializer()
    rooms = serializer.deserialize(args['rooms'])
    students = serializer.deserialize(args['students'])
    print(rooms)
    print(students)

    params_db = DBConfig.config('postgresql')
    params_path = DBConfig.config('paths')
    operation = DBOperationHandler(params_db, params_path)
    operation.execute_scripts(rooms, students)

    select_queries = DBSelectionHandler(DBConfig.config('postgresql'), DBConfig.config('paths')['select_queries'])
    selects = {
        'rooms_with_student_count': select_queries.select('select_rooms_with_student_count.sql'),
        'top_5_rooms_with_min_avg_age': select_queries.select('select_top_5_rooms_with_min_avg_age.sql'),
        #'top_5_rooms_with_max_diff_age': select_queries.select('select_top_5_rooms_with_max_diff_age.sql'),
        'rooms_with_diff_sex': select_queries.select('select_rooms_with_diff_sex.sql')
    }

    writer = FileWriter()
    for key, value in selects.items():
        serialized = serializer.serialize(value)
        writer._write_file(serialized, f"{DBConfig.config('paths')['resultset']}{key}.{args['format']}")


if __name__ == '__main__':
    main()
