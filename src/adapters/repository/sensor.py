from src.entity.sensor import Sensor


class Sensor_data_repository_mongo:
    def __init__(self, db_instace) -> None:
        self.db = db_instace
        self.collection = self.db['sensors']

    def post_sensor(self, data) -> dict:
        try:
            result = self.collection.insert_one(data.__dict__)
            return {"_id": str(result.inserted_id)}
        except:
            raise Exception('Error inserting data')

    def post_sensor_by_file(self, data) -> dict | Exception:
        try:
            self.collection.delete_many({})

            self.collection.insert_many(data)
            return {"message": "data inserted"}
        except:
            raise Exception('Error inserting data')

    def get_sensors(self) -> list[Sensor] | list | Exception:

        cursor = self.collection.find()
        result = [{**doc, "_id": str(doc["_id"])} for doc in cursor]

        if len(result) == 0:
            raise Exception('Sensors not found')
        try:
            return result
        except:
            raise Exception('Error getting data')
