from fastapi import HTTPException


class Controller_backpropagation:
    def __init__(self, usecase_backpropagation) -> None:
        self.usecase_backpropagation = usecase_backpropagation

    def get_weights_and_threshold(self, data):
        layerValues = data.layerValues
        if not layerValues or not isinstance(layerValues, list):
            raise TypeError("Layer values must be a list")
        try:
            result = self.usecase_backpropagation.get_weights_and_threshold(
                layerValues)
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server error {str(error)}")

    def get_neural_configuration(self, data):
        configuration = data
        try:
            result = self.usecase_backpropagation.get_neural_configuration(
                configuration)
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server error {str(error)}")

    def get_json(self):
        try:
            result = self.usecase_backpropagation.get_json()
            return result
        except Exception as error:
            raise HTTPException(
                status_code=500, detail=f"Internal server error {str(error)}")
