from my_code.tires.tire import Tire


class CarriganTire(Tire):
    def __init__(self, array):
        super().__init__(array)
        self.sensor_numbers = array

    def needs_service(self):
        for arg in self.sensor_numbers:
            if arg >= 0.9:
                return True

        return False
