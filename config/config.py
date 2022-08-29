from configparser import ConfigParser
import sys

sys.path.insert(0, '/config/')

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# def config_path(filename='database.ini', section='paths'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)

#     pt = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             pt[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))

#     return pt