import os
import json


class Transport:
    def __init__(self, id, type, marka):
        self.id = id
        self.type = type
        self.marka = marka


class Auto(Transport):
    def __init__(self, id, type, ajtok_szama, marka):
        super().__init__(id, type, marka)
        self.ajtok_szama = ajtok_szama

    def display_info(self):
        print(f"ID: {self.id}\t"
              f"Type: {self.type}\t\t"
              f"Márka: {self.marka}\t\t"
              f"Ajtók száma: {self.ajtok_szama}")


class Bicycle(Transport):
    def __init__(self, id, type, terhelhetoseg, marka):
        super().__init__(id, type, marka)
        self.terhelhetoseg = terhelhetoseg

    def display_info(self):
        print(f"ID: {self.id}\t"
              f"Type: {self.type}\t"
              f"Márka: {self.marka}\t"
              f"Terhelhetőség: {self.terhelhetoseg}")


class DataProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.transport_list = []

    def read_data(self):
        for root, dirs, files in os.walk(self.folder_path):
            for file_name in files:
                with open(os.path.join(root, file_name), 'r') as file:
                    data = json.load(file)
                    id = file_name.split(".")[0]
                    transport = self.instantiate_transport(id, data.get('type'), data)
                    self.transport_list.append(transport)
                    print(f"Processing file: {file_name}")

    @staticmethod
    def instantiate_transport(id, transport_type, data):
        if transport_type == 'auto':
            return Auto(id, **data)
        elif transport_type == 'bicikli':
            return Bicycle(id, **data)
        else:
            raise ValueError(f"Unsupported transport type: {transport_type}")

    def display_transport_info(self):
        for transport in self.transport_list:
            transport.display_info()


if __name__ == "__main__":
    data_processor = DataProcessor("data")
    data_processor.read_data()
    data_processor.display_transport_info()
