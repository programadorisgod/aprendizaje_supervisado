from src.entity.patron import Patron

def refactor_data_set(patrons: list[Patron]):
    
    group_size = 4
    current_group = []
    all_groups = []
    binary_groups = []
    count = 0

    result_to_binary = {
        'blandas': 1,
        'duras': 0,
        'concedido': 1,
        'denegado': 0
    }

    for patron in patrons:
        for key, value in patron.items():
            if key.lower() != '_id':
                current_group.append(value)
                if len(current_group) == group_size:
                    all_groups.append(current_group)
                    current_group = [] 

    for group in all_groups:
        value = bin(count)[2:].zfill(3)
        ouputs = [ result_to_binary.get(group[3], 0)]

        if len(value) != 4:
            inputs = [int(digit) for digit in value]
        else:
            address = find_address(all_groups, group[3])

            value = bin(address[0])[2:].zfill(3)
            inputs = [int(digit) for digit in value]

        binary_groups.append([inputs, ouputs ])
        count += 1
    return binary_groups


def find_address(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

