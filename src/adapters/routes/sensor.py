from fastapi import APIRouter, UploadFile
from src.entity.models.sensor import SensorModel

sensor_route = APIRouter()

BASE_URL = '/api/v1/sensors'


def create_router_user(sensor_controller):
    @sensor_route.get(BASE_URL, tags=["sensors"])
    async def get_sensors():
        return sensor_controller.get_sensors()
    
    @sensor_route.get(f"{BASE_URL}/threshold_and_weights", tags=["sensors"])
    async def get_threshold_and_weights():
        return sensor_controller.get_threshold_and_weights()

    @sensor_route.post(BASE_URL, tags=["sensors"])
    async def post_sensor(sensor: SensorModel):

        return sensor_controller.post_sensor(sensor)

    @sensor_route.post(f"{BASE_URL}/upload_file", tags=["sensors"])
    async def post_sensor_by_file(file:UploadFile):
         return await sensor_controller.post_sensor_by_file(file)
    

    
    return sensor_route
