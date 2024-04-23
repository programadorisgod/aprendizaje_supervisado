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
        result = []
        for doc in cursor:
            doc['_id'] = str(doc['_id'])
            for key, value in doc.items():
                if isinstance(value, str) and value.isdigit():
                    doc[key] = int(value)
            result.append(doc)

        if len(result) == 0:
            raise Exception('Sensors not found')

        try:
            return result
        except:
            raise Exception('Error getting data')
