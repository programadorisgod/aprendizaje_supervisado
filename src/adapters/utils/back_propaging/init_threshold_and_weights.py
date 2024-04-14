from src.entity.patron import Patron
from src.adapters.utils.counting_input_output_and_patterns import counting_input_output_and_patterns
import random


def init_threshold_and_weights(patrons: list[Patron], layerValues: list[int]) -> list:
    try:

        result = counting_input_output_and_patterns(patrons)
        inner_list = result[0]
        inputs, ouputs, _ = inner_list
        C1, C2, C3 = layerValues

        weights: list = []
        threshold_list: list = []

        if layerValues[0] != 0: 
            data = [inputs, C1, ouputs]
        if layerValues[1] != 0:
            data = [inputs, C1, C2, ouputs]
        if layerValues[2] != 0:
            data = [inputs, C1, C2, C3, ouputs]

        for index, value in enumerate(data[:-1]):
            weight_matrix: list[list[float]] = [[0.0 for _ in range(value)] for _ in range(data[index+1])]

            threshold: list[float] = [0.0 for _ in range(data[index+1])]

            for i in range(data[index+1]):
                for j in range(value):
                    weight_matrix[i][j] = round(random.uniform(-1, 1), 1)

            for k in range(data[index+1]):
                threshold[k] = round(random.uniform(-1, 1), 1)

            weights.append(weight_matrix)
            threshold_list.append(threshold)

        return {f"pesos": weights, f"umbrales": threshold_list}
    
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

    layers = [3, 2, 2]

    print(init_threshold_and_weights(listx, layers))
