from fastapi import APIRouter, UploadFile
from src.entity.models.sensor import SensorModel
from src.entity.models.sensor import FileModel


sensor_route = APIRouter()

BASE_URL = '/api/v1/sensors'


def create_router_sensor(sensor_controller):
    @sensor_route.get(BASE_URL, tags=["sensors"])
    async def get_sensors():
        return sensor_controller.get_sensors()

    @sensor_route.get(f"{BASE_URL}/input-params", tags=["sensors"])
    async def get_input_output_and_patterns():
        return sensor_controller.get_input_output_and_patterns()

    @sensor_route.get(f"{BASE_URL}/threshold-and-weights", tags=["sensors"])
    async def get_threshold_and_weights():
        return sensor_controller.get_threshold_and_weights()

    @sensor_route.post(BASE_URL, tags=["sensors"])
    async def post_sensor(sensor: SensorModel):
        return sensor_controller.post_sensor(sensor)

    @sensor_route.post(f"{BASE_URL}/upload-file", tags=["sensors"])
    async def post_sensor_by_file(file: UploadFile):
        return await sensor_controller.post_sensor_by_file(file)

    @sensor_route.post(f"{BASE_URL}/file", tags=["sensors"])
    async def post_weights_and_threshold(file: FileModel):
        return sensor_controller.post_weights_and_threshold(file)

    @sensor_route.get(f"{BASE_URL}/simulation", tags=["sensors"])
    async def get_weights_and_treshold():
        return sensor_controller.get_weights_and_treshold()

    return sensor_route
