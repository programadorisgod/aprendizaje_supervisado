from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.adapters.routes.sensor import create_router_sensor
from src.adapters.repository.sensor import Sensor_data_repository_mongo
from src.adapters.database.conexion_database import Database
from src.usecase.sensor import Sensor_use_case
from src.adapters.controllers.sensor import Sensor_controller


app = FastAPI()

origins: list[str] = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db_instace = Database().get_instance()

repository = Sensor_data_repository_mongo(db_instace)

usecase_sensor = Sensor_use_case(repository)

sensor_controller = Sensor_controller(usecase_sensor)


app.include_router(create_router_sensor(sensor_controller))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.frameworks.main:app",
                host='0.0.0.0', port=8000, reload=True)
