from src.entity.patron import Patron


def couting_input_output(patrons: list[Patron]) -> list:

    keys = []
    current_leter = None
    inputs: list = []
    outputs: list = []
    firts_patron = patrons[0]
    database: list = []

    for key, value in firts_patron.items():
        if key.lower() != '_id':
            keys.append(key)

    for key in keys:
        if current_leter is None or current_leter == key[0]:
            current_leter = key[0]
            inputs.append(key)
        else:
            outputs.append(key)

    for patron in patrons:
        inp: list = []
        out: list = []
        for key, value in patron.items():
            if key != '_id':
                if key in inputs:
                    inp.append(value)

                elif key in outputs:
                    out.append(value)

        database.append((inp, out))

    return database
