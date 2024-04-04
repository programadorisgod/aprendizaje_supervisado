from src.adapters.utils.read_file import read_file
from fastapi import UploadFile, HTTPException


class Sensor_controller:
    def __init__(self, usecase_sensor) -> None:
        self.usecase_sensor = usecase_sensor

    def post_sensor(self, data):
        try:
            result = self.usecase_sensor.post_sensor(data)
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def post_weights_and_threshold(self, file):
        try:
            result = self.usecase_sensor.post_weights_and_threshold(file)
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    async def post_sensor_by_file(self, file: UploadFile):
        try:
            sensors = await read_file(file)

            result = self.usecase_sensor.post_sensor_by_file(sensors)

            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_weights_and_treshold(self):
        try:
            result = self.usecase_sensor.get_weights_and_treshold()
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_sensors(self):
        try:
            result = self.usecase_sensor.get_sensors()

            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_threshold_and_weights(self):
        try:
            result = self.usecase_sensor.get_threshold_and_weights()

            return result

        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_input_output_and_patterns(self):
        try:
            result = self.usecase_sensor.get_input_output_and_patterns()

            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")
