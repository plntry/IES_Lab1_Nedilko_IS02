from domain.gps import Gps

class Parking:
    def __init__(self, empty_count: int, latitude: float, longitude: float) -> None:
        self.empty_count = empty_count
        self.gps = Gps(latitude, longitude)
