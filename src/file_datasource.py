from csv import reader
from datetime import datetime
from typing import List
from domain.aggregated_data import AggregatedData
from domain.accelerometer import Accelerometer
from domain.gps import Gps

class FileDatasource:
    def __init__(self, accelerometer_filename: str, gps_filename: str) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        pass

    def file_reader(self, path: str):
        with open(path) as file:
            data_reader = reader(file)
            header = next(data_reader)  # Skip the header

            for row in data_reader:
                yield row

    def startReading(self, *args, **kwargs):
        """Метод повинен викликатись перед початком читання даних"""
        self.accelerometer_file_reader = self.file_reader(self.accelerometer_filename)
        self.gps_file_reader = self.file_reader(self.gps_filename)

    def read(self) -> List[AggregatedData]:
        """Метод повертає дані отримані з датчиків"""
        data = []
        while True:
            try:
                accelerometer_data = next(self.accelerometer_file_reader)
                gps_data = next(self.gps_file_reader)
            except StopIteration:
                break

            data.append(
                AggregatedData(
                    Accelerometer(*accelerometer_data),
                    Gps(*gps_data),
                    datetime.now()
                )
            )

        return data

    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
