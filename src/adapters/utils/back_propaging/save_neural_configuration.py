from src.entity.models.patron import Configuration
import json
import os


def save_neural_configuration(configuration: Configuration):
    try:
        configurationDict = configuration.model_dump()

        configurationJson = json.dumps(configurationDict)
        file_path = os.path.join(".", "static", 'Config.json')
        with open(file_path, "w") as archivo:
            archivo.write(configurationJson)

        result = "Archivo guardado exitosamente ✅"

        return result
    except Exception as error:
        print("Error: ", error)
