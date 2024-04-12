from src.entity.patron import Patron


class Repository_error_correction:
    def __init__(self, db_instace) -> None:
        self.db = db_instace
        self.collection = self.db['sensors']

    def post_patron(self, data) -> dict | Exception:
        try:
            result = self.collection.insert_one(data.__dict__)
            return {"_id": str(result.inserted_id)}
        except:
            raise Exception('Error inserting data')

    def post_patrons_by_file(self, data) -> dict | Exception:
        try:
            self.collection.delete_many({})

            self.collection.insert_many(data)
            return {"message": "data inserted"}
        except:
            raise Exception('Error inserting data')

    def get_patrons(self) -> list[Patron] | Exception:

        cursor = self.collection.find()
        result = [{**doc, "_id": str(doc["_id"])} for doc in cursor]

        if len(result) == 0:
            raise Exception('Sensors not found')
        print('enntro')
        try:
            return result
        except:
            raise Exception('Error getting data')
