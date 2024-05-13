from src.entity.patron import Patron

def refactor_data_set(patrons: list[Patron]):
    
    group_size = 4
    current_group = []
    all_groups = []
    binary_groups = []

    result_to_binary = {
        'blandas': 1,
        'duras': 0
    }

    patrons_to_binary = {
        'si': 1,
        'no': 0,
        'joven': 0,
        'pre-presbicia':1,
        'presbicia': 2,
        'miopia': 1,
        'hipermetropia': 0,
    }

    for patron in patrons:
        for key, value in patron.items():
            if key.lower() != '_id':
                current_group.append(value)
                if len(current_group) == group_size:
                    all_groups.append(current_group)
                    current_group = [] 


    for group in all_groups:
        inputs = [patrons_to_binary.get(group[0]),patrons_to_binary.get(group[1]),patrons_to_binary.get(group[2])]
        binary_groups.append([inputs, [ result_to_binary.get(group[3], 0)] ])

    return binary_groups