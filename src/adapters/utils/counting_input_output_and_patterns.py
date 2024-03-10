from src.entity.sensor import Sensor


def counting_input_output_and_patterns(sensors: list[Sensor]) -> list:
    input_output_patrons: list = []

    m: int = 0
    n: int = 0
    for idx, dict in enumerate(sensors):
        for key, value in dict.items():
            if f's{idx}' in key.lower():
                m += 1
            if f'yd{idx}' in key.lower():
                n += 1
    input_output_patrons.append([m, n, len(sensors)])
    return input_output_patrons
