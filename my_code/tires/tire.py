from my_code.servicable import Servicable


class Tire(Servicable):
    def __init__(self, *args):
        self.sensor_numbers = args

    def needs_service(self):
        pass
