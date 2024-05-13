from fastapi import UploadFile


async def read_file(file: UploadFile):
    try:
        content = await file.read()
        content = content.decode('utf-8')
        lines = content.split('\n')
        headers = lines[0].strip().split(' ')
        patterns = []

        for idx, line in enumerate(lines):
            """ En caso de que no sea la primera linea y no esté vacia, ya que la 1ra linea son los headers 
              no nos interesan, solo los patrones.
            """
            if idx != 0 and line.strip():
                """ Como sabemos la linea puede ser 0 0 1 0 1 entonces ya ahí estamos teniendo las partes de dicha
                 linea
                """
                parts = line.strip().split(' ')

                pattern = {}
                """
                como ya tenemos los headers que son las entradas y salidas, solo falta asignarla 
                a cada entrada y salida su valor correspondiente o patrón
                """
                for header, part in zip(headers, parts):
                    """ Recuerda, que aquí estamos asignando a cada header su valor correspondiente,"""
                    pattern[header] = part
                patterns.append(pattern)
                """ 
                 Una vez agregado todos los patrones, esta es una posible salida 
                 [{'X1': '1', 'X2': '1', 'YD1': '1'}, {'X1': '0', 'X2': '1', 'YD1': '0'}, {'X1': '1', 'X2': '0', 'YD1': '0'}, {'X1': '0', 'X2': '0', 'YD1': '0'}]
                 """
        return patterns
    except:
        raise Exception('Error reading file')
