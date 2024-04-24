from src.entity.models.patron import Configuration
import json

def save_neural_configuration(configuration: Configuration):
  #print(configuration)
  try:
    configurationDict = configuration.model_dump()

    configurationJson =  json.dumps(configurationDict)

    with open("Config.json", "w") as archivo:
        archivo.write(configurationJson)
    
    result = "Archivo guardado exitosamente ✅"

    return result
  except Exception as error:
    print("Error: ", error )
