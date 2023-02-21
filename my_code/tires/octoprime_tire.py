from my_code.tires.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, array):
        super().__init__(array)
        self.sensor_numbers = array

    def needs_service(self):
        if sum(self.sensor_numbers) >= 3:
            return True
        return False
