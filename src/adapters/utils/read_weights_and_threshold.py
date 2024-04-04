def read_weights_and_treshold() -> dict:
    weights: list[list[float]] = []
    thresholds: list[float] = []

    with open('pesos y umbrales.txt', "r") as archivo:
        firts_line = archivo.readline().strip()
        second_line = archivo.readline().strip()

    values_weights = firts_line.split(' ')
    values_thresholds = second_line.split(' ')

    if len(values_weights) < 3:
        for w in values_weights:
              weights.append([float(w)])
    else:    
        for i in range(0, len(values_weights), 2):
            weights.append([float(values_weights[i]), float(values_weights[i+1])])

    for t in values_thresholds:
        thresholds.append(float(t))
    return {"weights": weights, "thresholds": thresholds}
