from fastapi import APIRouter

from src.entity.models.patron import LayerValues
from src.entity.models.patron import Configuration


BASE_URL = '/api/v1/backpropagation'

router = APIRouter()


def create_router_backpropagation(controller_backpropagation):
    @router.post(BASE_URL, tags=['Backpropagation'])
    async def get_weights_and_threshold(layerValues: LayerValues):
        return controller_backpropagation.get_weights_and_threshold(layerValues)
    
    @router.post(f"{BASE_URL}/config", tags=['Backpropagation'])
    async def get_neural_configuration(configuration: Configuration):
        return controller_backpropagation.get_neural_configuration(configuration)

    return router
