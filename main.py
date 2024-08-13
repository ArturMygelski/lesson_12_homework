import sys
from file_handler import CSVFileHandler, PickleHandler, TXTFileHandler

def get_handler_class(input_file):
    if input_file.endswith(".csv"):
        return CSVFileHandler
    elif input_file.endswith(".pickle"):
        return PickleHandler
    elif input_file.endswith(".txt"):
        return TXTFileHandler
    else:
        raise ValueError("nieobsługiwany format pliku")

if __name__ == "__main__":
    arguments = sys.argv
    handler_class = get_handler_class(arguments[1])
    handler = handler_class(input_file=arguments[1], output_file=arguments[2], changes=arguments[3:])
    handler.transform()
    handler.save_data_to_file()