from src.entity.sensor import Sensor


class Sensor_use_case():
    def __init__(self, repository) -> None:
        self.repository = repository

    def post_sensor(self, data) -> dict:
        sensor = Sensor(*data)
        result = self.repository.post_sensor(sensor)
        return result

    def post_sensor_by_file(self, file):
        sensors = self.repository.post_sensor_by_file(file)

    def get_sensor(self):
        sensors = self.repository.get_sensors()
        return sensors
