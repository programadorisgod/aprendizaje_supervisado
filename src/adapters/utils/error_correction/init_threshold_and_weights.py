from src.entity.patron import Patron
from src.adapters.utils.counting_input_output_and_patterns import counting_input_output_and_patterns
import random


def init_threshold_and_weights(patrons: list[Patron]) -> list:

    try:
        result = counting_input_output_and_patterns(patrons)
        inner_list = result[0]
        m, n, _ = inner_list

        threshold_and_weights: list = []
        # Inicializar weight_matrix como una lista de m listas, cada una de las cuales contiene n elementos
        weight_matrix: list[list[float]] = [
            [0.0 for _ in range(m)] for _ in range(n)]

        threshold: list[float] = [0.0 for _ in range(n)]

        for i in range(n):
            for j in range(m):
                weight_matrix[i][j] = round(random.uniform(-1, 1), 1)

        for k in range(n):
            threshold[k] = round(random.uniform(-1, 1), 1)

        threshold_and_weights.append({
            "weight_matrix": weight_matrix,
            "threshold": threshold
        })

        return threshold_and_weights
    except Exception as error:
        print(error, 'error')


if __name__ == '__main__':
    listx = [
        {
            "_id": "65e87f6ff765e9ec56db980a",
            "s1": "0",
            "s2": "0",
            "s3": "0",
            "yd1": "0",
            "yd2": "0"
        },
        {
            "_id": "65e87f6ff765e9ec56db980b",
            "s1": "1",
            "s2": "0",
            "s3": "0",
            "yd1": "0",
            "yd2": "1"
        },
        {
            "_id": "65e87f6ff765e9ec56db980c",
            "s1": "1",
            "s2": "1",
            "s3": "1",
            "yd1": "1",
            "yd2": "0"
        },
        {
            "_id": "65e87f6ff765e9ec56db980d",
            "s1": "1",
            "s2": "1",
            "s3": "1",
            "yd1": "1",
            "yd2": "1"
        }
    ]
    
    init_threshold_and_weights(listx)
