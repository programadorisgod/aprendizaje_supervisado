from fastapi import FastAPI
from src.adapters.routes.sensor import create_router_user
from src.adapters.repository.sensor import SensorData_repository_mongo
from src.adapters.database.conexion_database import Database

app = FastAPI()

db_instace = Database().get_instance()
repository = SensorData_repository_mongo(db_instace)

app.include_router(create_router_user(repository))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.frameworks.main:app",
                host='0.0.0.0', port=8000, reload=True)
