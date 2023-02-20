from my_code.engine import Engine
from datetime import datetime


class WilloughbyEngine(Engine):
    def __init__(self, last_service_milage, current_milage):
        self.last_service_date = last_service_milage
        self.current_milage = current_milage

    def needs_service(self):
        if service_threshold_date < datetime.today().date():
            return True
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
        return False
