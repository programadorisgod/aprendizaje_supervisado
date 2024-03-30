def read_weights_and_treshold() -> dict:
    weights: list[list[float]] = []
    thresholds: list[float] = []

    with open('pesos y umbrales.txt', "r") as archivo:
        firts_line = archivo.readline().strip()
        second_line = archivo.readline().strip()

    values_weights = firts_line.split(' ')
    values_thresholds = second_line.split(' ')

    for w in values_weights:
        weights.append([float(w)])

    for t in values_thresholds:
        thresholds.append(float(t))
    return {"weights": weights, "thresholds": thresholds}
