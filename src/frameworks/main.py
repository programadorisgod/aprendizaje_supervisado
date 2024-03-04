from fastapi import FastAPI
from src.adapters.routes.sensor import create_router_user
from src.adapters.repository.sensor import Sensor_data_repository_mongo
from src.adapters.database.conexion_database import Database
from src.usecase.sensor import Sensor_use_case
from src.adapters.controllers.sensor import Sensor_controller

app = FastAPI()

db_instace = Database().get_instance()

repository = Sensor_data_repository_mongo(db_instace)

usecase_sensor = Sensor_use_case(repository)

sensor_controller = Sensor_controller(usecase_sensor)


app.include_router(create_router_user(repository))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.frameworks.main:app",
                host='0.0.0.0', port=8000, reload=True)
