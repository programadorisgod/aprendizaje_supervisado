from src.adapters.utils.back_propaging.init_threshold_and_weights import init_threshold_and_weights
from src.adapters.utils.back_propaging.save_neural_configuration import save_neural_configuration
from src.adapters.utils.back_propaging.refactor_data_set import refactor_data_set
import os
from fastapi.responses import FileResponse
from fastapi.responses import Response


class Backpropagation_use_case:

    def __init__(self, repository) -> None:
        self.repository = repository

    def get_weights_and_threshold(self, layerValues):
        patrons = self.repository.get_patrons()
        result = init_threshold_and_weights(patrons, layerValues)
        return result

    def get_neural_configuration(self, config):
        result = save_neural_configuration(config)
        return result

    def get_json(self):
        try:
            file_path = os.path.join('.', 'static', 'Config.json')
            if os.path.exists(file_path):
                return FileResponse(file_path, media_type="application/json")
            else:
                return Response('File not found', status_code=404)

        except:
            raise Exception('Error getting json')
        
    def get_vales_lettering(self):
        try:
            patrons = self.repository.get_patrons()
            result = refactor_data_set(patrons)
            return result
        except Exception as error:
            raise Exception(f"Error refactor data set: ${error}")
        
