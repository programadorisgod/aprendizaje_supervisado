from src.entity.sensor import Sensor
from src.adapters.utils.init_threshold_and_weights import init_threshold_and_weights
from src.adapters.utils.counting_input_output_and_patterns import counting_input_output_and_patterns
from src.adapters.utils.count_input_ouputs import couting_input_output


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
        result: list = couting_input_output(sensors)

        return result

    def get_threshold_and_weights(self) -> list:
        sensors: list[Sensor] | Exception = self.get_sensors()
        threshold_and_weights = init_threshold_and_weights(sensors)
        return threshold_and_weights

    def get_input_output_and_patterns(self):
        sensors: list[Sensor] | Exception = self.repository.get_sensors()
        result = counting_input_output_and_patterns(sensors)

        return result
