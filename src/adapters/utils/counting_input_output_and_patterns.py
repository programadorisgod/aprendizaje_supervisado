from src.entity.patron import Patron


def counting_input_output_and_patterns(patrons: list[Patron]) -> list:
    input_output_patrons: list = []

    m: int = 0
    n: int = 0
    headers = []
    current_letter = None
    first_patron = patrons[0]

    for key, value in first_patron.items():
        if key.lower() != '_id':
            headers.append(key.lower())

    for header in headers:
        """
        las entradas, tienen la misma letra en la primera posición, las salidas no.
        Por ende si la primera letra de la entrada es igual a la letra actual, se incrementa m, sino se incrementa n.
        ya que iniciaria current_letter en None, se le asigna la primera letra de la primera entrada. en la 2iteracion ya current_letter no es None y se compara con la primera letra de la entrada actual. y eso es basicamente en ese for
        """
        if current_letter is None or header[0] == current_letter:
            current_letter = header[0]
            m += 1
        else:
            n += 1

    input_output_patrons.append([m, n, len(patrons)])
    return input_output_patrons
