

class Sensor_data_repository_mongo:
    def __init__(self, db_instace) -> None:
        self.db = db_instace
        self.collection = self.db['sensors']

    def post_sensor(self, data):
        try:
            result = self.collection.insert_one(data.__dict__)
            return {"_id": str(result.inserted_id)}
        except:
            raise Exception('Error inserting data')

    def post_sensor_by_file(self, data):
        try:
            self.collection.insert_many(data)
            return {"message": "data inserted"}
        except:
            raise Exception('Error inserting data')

    def get_sensors(self):
        try:
            cursor = self.collection.find()
            result = [{**doc, "_id": str(doc["_id"])} for doc in cursor]
            return result

        except:
            raise Exception('Error getting data')
