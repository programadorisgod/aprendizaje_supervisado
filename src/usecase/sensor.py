from src.entity.sensor import Sensor
from src.adapters.utils.init_threshold_and_weights import init_threshold_and_weights


class Sensor_use_case():
    def __init__(self, repository) -> None:
        self.repository = repository

    def post_sensor(self, data) -> dict:
        data_dic = {item[0]: item[1] for item in data}
        sensor: Sensor = Sensor(**data_dic)
        result: dict | Exception = self.repository.post_sensor(sensor)
        return result

    def post_sensor_by_file(self, sensors) -> dict:
        sensors: dict | Exception = self.repository.post_sensor_by_file(
            sensors)
        return sensors

    def get_sensors(self):
        sensors: list[Sensor] | Exception = self.repository.get_sensors()
        return sensors

    def get_threshold_and_weights(self) -> list:
        sensors: list[Sensor] | Exception = self.get_sensors()
        threshold_and_weights = init_threshold_and_weights(sensors)
        return threshold_and_weights
