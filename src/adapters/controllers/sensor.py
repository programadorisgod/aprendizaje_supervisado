from src.adapters.utils.read_file import read_file


class Sensor_controller:
    def __init__(self, usecase_sensor) -> None:
        self.usecase_sensor = usecase_sensor

    def post_sensor(self, data):
        result = self.usecase_sensor.post_sensor(data)
        return result

    def post_sensor_by_file(self, file):
        sensors = read_file(file)
        result = self.usecase_sensor.post_sensor_by_file(sensors)
        return result

    def get_sensors(self):
        result = self.usecase_sensor.get_sensor()

        return result
