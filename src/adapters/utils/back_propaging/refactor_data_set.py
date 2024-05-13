from src.entity.patron import Patron

def refactor_data_set(patrons: list[Patron]):
    
    group_size = 4
    current_group = []
    all_groups = []
    binary_groups = []
    count = 0

# Mapeo para el cuarto elemento

    result_to_binary = {
        'concedido': '1',
        'denegado': '0',
        'blandas': '1',
        'duras': '0'
    }

    for patron in patrons:
        for key, value in patron.items():
            if key.lower() != '_id':
                current_group.append(value)
                if len(current_group) == group_size:
                    all_groups.append(current_group)
                    current_group = [] 


    for group in all_groups:
        print(count)
        binary_group = [bin(count)[2:].zfill(4), result_to_binary.get(group[3], '0')]
        binary_groups.append(binary_group)
        count += 1

    return binary_groups