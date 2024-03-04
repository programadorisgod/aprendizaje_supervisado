

class Database():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        import os
        from dotenv import load_dotenv
        from pymongo import MongoClient
        load_dotenv()

        self.client = MongoClient(os.getenv('MONGO_URI'))

        self.db = self.client['sensorsData']

    def get_instance(self):
        return self.db


if __name__ == '__main__':
    Database()
