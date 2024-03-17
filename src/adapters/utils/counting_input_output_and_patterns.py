from src.entity.sensor import Sensor


def counting_input_output_and_patterns(sensors: list[Sensor]) -> list:
    input_output_patrons: list = []

    m: int = 0
    n: int = 0
    headers = []
    current_letter = None
    first_sensor = sensors[0]

    for key, value in first_sensor.items():
        if key.lower() != '_id':
            headers.append(key.lower())

    for header in headers:
        if current_letter is None or header[0] == current_letter:
            current_letter = header[0]
            m += 1
        else:
            n += 1

    input_output_patrons.append([m, n, len(sensors)])
    return input_output_patrons
