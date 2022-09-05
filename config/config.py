from configparser import ConfigParser
import sys

sys.path.insert(0, '/config/')


class DBConfig:
    @staticmethod
    def config(section, filename='database.ini'):
        # create a parser
        parser = ConfigParser()
        parser.read(filename)

        return vars(parser)['_sections'][section]
