import csv
import pickle
from abc import ABC, abstractmethod
class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = self.load_data_from_file()
        self.changes = changes

    @abstractmethod
    def load_data_from_file(self):
        pass

    @abstractmethod
    def save_data_to_file(self):
        pass

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            print(transformation_list)
            col = int(transformation_list[0])
            row = int(transformation_list[1])
            value = transformation_list[2]
            self.matrix[row][col] = value

        for row in self.matrix:
            print(",".join(row))

class CSVFileHandler(FileHandler):
    @abstractmethod
    def load_data_from_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                temp_matrix.append(line)
        return temp_matrix


    @abstractmethod
    def save_data_to_file(self):
        with open(self.output_file, mode="w+", newline="") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

class PickleHandler(FileHandler):
    def load_data_from_file(self):
        with open(self.input_file, mode="rb") as file:
            return pickle.load(file)

    def save_data_to_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.matrix, file)

class TXTFileHandler(FileHandler):
    def load_data_from_file(self):
        with open(self.input_file) as file:
            return [line.split() for line in file]

    def save_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            for line in self.matrix:
                file.write(" ".join(line) + "\n")