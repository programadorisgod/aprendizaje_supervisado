from src.entity.sensor import Sensor


def couting_input_output(sensors: list[Sensor]) -> list:

    keys = []
    current_leter = None
    inputs: list = []
    outputs: list = []
    firts_sensor = sensors[0]
    database: list = []

    for key, value in firts_sensor.items():
        if key.lower() != '_id':
            keys.append(key)

    for key in keys:
        if current_leter is None or current_leter == key[0]:
            current_leter = key[0]
            inputs.append(key)
        else:
            outputs.append(key)

    for sensor in sensors:
        inp: list = []
        out: list = []
        for key, value in sensor.items():
            if key != '_id':
                if key in inputs:
                    inp.append(value)

                elif key in outputs:
                    out.append(value)

        database.append((inp, out))

    return database
