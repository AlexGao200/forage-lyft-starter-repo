from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        if sum(self.sensors) >= 3:
            return True
        else:
            return False