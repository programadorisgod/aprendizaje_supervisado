from fastapi import APIRouter, UploadFile
from src.entity.models.patron import PatronModel
from src.entity.models.patron import FileModel


router = APIRouter()

BASE_URL = '/api/v1/error-correction'


def create_router_error_correction(controller_error_correction):
    @router.get(BASE_URL, tags=["error-correction"])
    async def get_patrons():
        return controller_error_correction.get_patrons()

    @router.get(f"{BASE_URL}/input-params", tags=["error-correction"])
    async def get_input_output_and_patterns():
        return controller_error_correction.get_input_output_and_patterns()

    @router.get(f"{BASE_URL}/threshold-and-weights", tags=["error-correction"])
    async def get_threshold_and_weights():
        return controller_error_correction.get_threshold_and_weights()

    @router.post(BASE_URL, tags=["error-correction"])
    async def post_patron(patron: PatronModel):
        return controller_error_correction.post_patron(patron)

    @router.post(f"{BASE_URL}/upload-file", tags=["error-correction"])
    async def post_patrons_by_file(file: UploadFile):
        return await controller_error_correction.post_patrons_by_file(file)

    @router.post(f"{BASE_URL}/file", tags=["error-correction"])
    async def post_weights_and_threshold(file: FileModel):
        return controller_error_correction.post_weights_and_threshold(file)

    @router.get(f"{BASE_URL}/simulation", tags=["error-correction"])
    async def get_weights_and_treshold():
        return controller_error_correction.get_weights_and_treshold()

    return router
