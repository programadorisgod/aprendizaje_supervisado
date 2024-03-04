from src.adapters.utils.read_file import read_file
from fastapi import UploadFile


class Sensor_controller:
    def __init__(self, usecase_sensor) -> None:
        self.usecase_sensor = usecase_sensor

    def post_sensor(self, data):
        result = self.usecase_sensor.post_sensor(data)
        return result

    def post_sensor_by_file(self, file: UploadFile):
        try:
            sensors = read_file(file)
            print(sensors)
        except ValueError as e:
            return f"Internal server Error: {e}"

    def get_sensors(self):
        result = self.usecase_sensor.get_sensor()

        return result
