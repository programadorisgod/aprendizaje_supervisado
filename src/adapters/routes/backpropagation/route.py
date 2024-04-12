from fastapi import APIRouter

from src.entity.models.patron import LayerValues


BASE_URL = '/api/v1/backpropagation'

router = APIRouter()


def create_router_backpropagation(controller_backpropagation):
    @router.get(BASE_URL, tags=['Backpropagation'])
    async def get_weights_and_threshold(layerValues: LayerValues):
        return controller_backpropagation.get_weights_and_threshold(layerValues)

    return router
