from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.adapters.routes.error_correction.route import create_router_error_correction
from src.adapters.repository.error_controller.repository import Repository_error_correction
from src.adapters.database.conexion_database import Database
from src.usecase.error_correction.use_case import Error_correction_use_case
from src.adapters.controllers.error_correction.controller import Controller_error_correction

from src.adapters.repository.backpropagation.repository import Repository_backpropagation
from src.adapters.controllers.backpropagation.controller import Controller_backpropagation
from src.usecase.backpropagation.use_case import Backpropagation_use_case
from src.adapters.routes.backpropagation.route import create_router_backpropagation

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


db_instance = Database().get_instance()

repository_error_correction = Repository_error_correction(db_instance)
repository_backpropagation = Repository_backpropagation(db_instance)

usecase_error_correction = Error_correction_use_case(
    repository_error_correction)
usecase_backpropagation = Backpropagation_use_case(repository_backpropagation)

controller_error_correction = Controller_error_correction(
    usecase_error_correction)
controller_backpropagation = Controller_backpropagation(
    usecase_backpropagation)

app.include_router(create_router_error_correction(controller_error_correction))
app.include_router(create_router_backpropagation(controller_backpropagation))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.frameworks.main:app",
                host='0.0.0.0', port=8000, reload=True)
