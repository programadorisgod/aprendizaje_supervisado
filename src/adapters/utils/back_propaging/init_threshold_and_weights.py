from src.entity.sensor import Sensor
from src.adapters.utils.counting_input_output_and_patterns import counting_input_output_and_patterns
import random



def init_threshold_and_weights(sensors: list[Sensor], layerValues: list[int] ) -> list:
    try:
        result = counting_input_output_and_patterns(sensors)
        inner_list = result[0]
        inputs, ouputs, _ = inner_list

        threshold_and_weights: list = []

        
        for index, value in enumerate(layerValues):

            if index == 0 and value != 0:

                weight_matrix: list[list[float]] = [
                [0.0 for _ in range(inputs)] for _ in range(value)]

                threshold: list[float] = [0.0 for _ in range(value)]

                for i in range(value):
                    for j in range(inputs):
                        weight_matrix[i][j] = round(random.uniform(-1, 1), 1)

                for k in range(value):
                    threshold[k] = round(random.uniform(-1, 1), 1)

                threshold_and_weights.append({
                    f"weight_matrix_{index+1}": weight_matrix,
                    f"threshold_{index+1}": threshold
                })
            else:
                
                if index == len(layerValues) -1  and value != 0:

                    weight_matrix: list[list[float]] = [
                    [0.0 for _ in range(value)] for _ in range(ouputs)]

                    threshold: list[float] = [0.0 for _ in range(ouputs)]

                    for i in range(ouputs):
                        for j in range(value):
                            weight_matrix[i][j] = round(random.uniform(-1, 1), 1)

                    for k in range(ouputs):
                        threshold[k] = round(random.uniform(-1, 1), 1)

                    threshold_and_weights.append({
                        f"weight_matrix_{index+1}": weight_matrix,
                        f"threshold_{index+1}": threshold
                    })
                else:
                    
                    weight_matrix: list[list[float]] = [
                    [0.0 for _ in range(value-1)] for _ in range(value)]

                    threshold: list[float] = [0.0 for _ in range(value)]

                    for i in range(value):
                        for j in range(value-1):
                            weight_matrix[i][j] = round(random.uniform(-1, 1), 1)

                    for k in range(value):
                        threshold[k] = round(random.uniform(-1, 1), 1)

                    threshold_and_weights.append({
                        f"weight_matrix_{index+1}": weight_matrix,
                        f"threshold_{index+1}": threshold
                    })
        
        return print(threshold_and_weights)
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

    layers = [ 3, 5, 0 ]

    init_threshold_and_weights(listx,layers)
