from fastapi import APIRouter
from src.entity.models.sensor import SensorModel

sensor_route = APIRouter()

BASE_URL = '/api/v1/sensors'


def create_router_user(sensor_controller):
    @sensor_route.get(BASE_URL, tags=["sensors"])
    async def get_sensors():
        return sensor_controller.get_sensors()

    @sensor_route.post(BASE_URL, tags=["sensors"])
    async def post_sensor(sensor: SensorModel):

        return sensor_controller.post_sensor(sensor)

    return sensor_route
