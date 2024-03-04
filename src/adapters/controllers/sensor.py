
class Sensor_controller:
    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self, data):
        result = self.repository.post_sensor(data)
        return result

    def get_sensors(self):
        result = self.repository.get_sensors()

        return result
