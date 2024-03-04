

class Sensor_data_repository_mongo:
    def __init__(self, db_instace) -> None:
        self.db = db_instace
        self.collection = self.db['sensors']

    def post_sensor(self, data):
        result = self.collection.insert_one(data.__dict__)
        return {"_id": str(result.inserted_id)}

    def post_sensor_by_file(self, data):
        cursor = self.collection.insert_many(data)
        result = [{**doc, "_id": str(doc["_id"])} for doc in cursor]
        return result

    def get_sensors(self):
        cursor = self.collection.find()
        result = [{**doc, "_id": str(doc["_id"])} for doc in cursor]
        return result
