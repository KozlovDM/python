from pymongo import MongoClient


class DataBase:
    __db = None

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.__db = client['Notify']

    def get_connection(self):
        return self.__db
