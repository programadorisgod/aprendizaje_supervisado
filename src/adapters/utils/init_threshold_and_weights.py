from src.entity.sensor import Sensor
from src.adapters.utils.counting_input_output_and_patterns import counting_input_output_and_patterns
import random


def init_threshold_and_weights(sensors: list[Sensor]) -> list:

    m, n, _ = counting_input_output_and_patterns(sensors)
    
    threshold_and_weights: list = []

    for idx, dict in enumerate(sensors):
        for key, value in dict.items():
            if f's{idx}' in key.lower():
                m += 1
            if f'yd{idx}' in key.lower():
                n += 1

    # Inicializar weight_matrix como una lista de m listas, cada una de las cuales contiene n elementos
    weight_matrix: list[list[float]] = [
        [0.0 for _ in range(n)] for _ in range(m)]

    threshold: list[float] = [0.0 for _ in range(n)]

    for i in range(n):
        for j in range(m):
            weight_matrix[j][i] = round(random.uniform(-1, 1), 1)

    for k in range(n):
        threshold[k] = round(random.uniform(-1, 1), 1)

    threshold_and_weights.append({
        "weight_matrix": weight_matrix,
        "threshold": threshold
    })

    return threshold_and_weights


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
