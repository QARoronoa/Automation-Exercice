import configparser


def config():
    param = configparser.ConfigParser()
    param.read('utilities/proprieties.ini')
    return param