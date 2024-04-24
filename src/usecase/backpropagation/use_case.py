from src.adapters.utils.back_propaging.init_threshold_and_weights import init_threshold_and_weights
from src.adapters.utils.back_propaging.save_neural_configuration import save_neural_configuration


class Backpropagation_use_case:

    def __init__(self, repository) -> None:
        self.repository = repository

    def get_weights_and_threshold(self, layerValues):
        patrons = self.repository.get_patrons()
        print(layerValues)
        result = init_threshold_and_weights(patrons, layerValues)
        return result
    
    def get_neural_configuration(self, config):
        result = save_neural_configuration(config)
        return result

