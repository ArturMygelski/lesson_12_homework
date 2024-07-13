import csv

class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = self.load_data_from_file()
        self.changes = changes
        print(self.matrix)
        print(self.changes)

    def load_data_from_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                temp_matrix.append(line)
        return temp_matrix

    def save_data_to_file(self):
        with open(self.output_file, mode="w+", newline="") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)


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