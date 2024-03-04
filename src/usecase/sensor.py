from src.entity.sensor import Sensor


class Sensor_use_case():
    def __init__(self, repository) -> None:
        self.repository = repository

    def post_sensor(self, data) -> dict:
        data_dic = {item[0]: item[1] for item in data}
        sensor = Sensor(**data_dic)
        result = self.repository.post_sensor(sensor)
        return result

    def post_sensor_by_file(self, sensors):
        sensors = self.repository.post_sensor_by_file(sensors)
        return sensors

    def get_sensor(self):
        sensors = self.repository.get_sensors()
        return sensors
