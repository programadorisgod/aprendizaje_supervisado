from src.adapters.utils.read_file import read_file
from fastapi import UploadFile, HTTPException


class Controller_error_correction:
    def __init__(self, use_case_error_correction) -> None:
        self.use_case_error_correction = use_case_error_correction

    def post_patron(self, data):
        try:
            result = self.use_case_error_correction.post_patron(data)
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def post_weights_and_threshold(self, file):
        try:
            result = self.use_case_error_correction.post_weights_and_threshold(
                file)
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    async def post_patrons_by_file(self, file: UploadFile):
        try:
            sensors = await read_file(file)

            result = self.use_case_error_correction.post_patrons_by_file(
                sensors)

            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_weights_and_treshold(self):
        try:
            result = self.use_case_error_correction.get_weights_and_treshold()
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_patrons(self):
        try:
            result = self.use_case_error_correction.get_patrons()

            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_threshold_and_weights(self):
        try:
            result = self.use_case_error_correction.get_threshold_and_weights()

            return result

        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")

    def get_input_output_and_patterns(self):
        try:
            result = self.use_case_error_correction.get_input_output_and_patterns()

            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server Error: {str(error)}")
