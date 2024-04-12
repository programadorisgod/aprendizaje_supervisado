from src.entity.patron import Patron
from src.adapters.utils.error_correction.init_threshold_and_weights import init_threshold_and_weights
from src.adapters.utils.counting_input_output_and_patterns import counting_input_output_and_patterns
from src.adapters.utils.count_input_ouputs import couting_input_output
from src.adapters.utils.read_weights_and_threshold import read_weights_and_treshold
import os


class Error_correction_use_case():
    def __init__(self, repository) -> None:
        self.repository = repository

    def post_patron(self, data) -> dict:
        data_dic = {item[0]: item[1] for item in data}
        newPatron: Patron = Patron(**data_dic)
        result: dict | Exception = self.repository.post_patron(newPatron)
        return result

    def post_patrons_by_file(self, patrons) -> dict:
        result: dict | Exception = self.repository.post_patrons_by_file(
            patrons)
        return result

    def post_weights_and_threshold(self, file) -> dict | Exception:
        try:

            fileToDelete = '../../pesos y umbrales.txt'
            if os.path.exists(fileToDelete):
                os.remove(fileToDelete)

            flatten_weights = [
                item for sublist in file.weights for item in sublist]

            with open('pesos y umbrales.txt', "w") as archivo:
                archivo.write(' '.join(map(str, flatten_weights)) + "\n")
                archivo.write(' '.join(map(str, file.thresholds)))

            return {"mesasage": "created file"}
        except:
            raise Exception('Error creating file')

    def get_weights_and_treshold(self) -> dict | Exception:
        try:
            result = read_weights_and_treshold()
            return result
        except:

            raise Exception('Error reading file')

    def get_patrons(self):
        patrons: list[Patron] | Exception = self.repository.get_patrons()
        result: list = couting_input_output(patrons)

        return result

    def get_threshold_and_weights(self) -> list:
        patrons: list[Patron] | Exception = self.get_patrons()
        threshold_and_weights = init_threshold_and_weights(patrons)
        return threshold_and_weights

    def get_input_output_and_patterns(self):
        patrons: list[Patron] | Exception = self.repository.get_patrons()
        result = counting_input_output_and_patterns(patrons)

        return result
