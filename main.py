import sys
from file_handler import FileHandler

arguments = sys.argv
print(arguments)
handler = FileHandler(input_file=arguments[1], output_file=arguments[2], changes=arguments[3:])
handler.transform()
handler.save_data_to_file()