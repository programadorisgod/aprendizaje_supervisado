
from src.entity.patron import Patron


class Repository_backpropagation:
    def __init__(self, db_instance) -> None:
        self.db = db_instance
        self.collection = self.db['sensors']

    def get_patrons(self) -> list[Patron] | Exception:

        cursor = self.collection.find()
        result = [{**doc, "_id": str(doc["_id"])} for doc in cursor]

        if len(result) == 0:
            raise Exception('Patrons not found')
        try:
            return result
        except:
            raise Exception('Error getting data')
