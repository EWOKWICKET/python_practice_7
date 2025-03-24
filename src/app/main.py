from .io.input import *
from .io.output import *


def main():
    input_console = console_input()
    input_file = built_in_input()
    input_pandas = pandas_input()
    
    print('Console input data:')
    console_output(input_console)

    print('File input data:')
    console_output(input_file)

    print('Pandas input data:')
    console_output(input_pandas)

    built_in_output(input_console)
    built_in_output(input_file)
    built_in_output(input_pandas)


if __name__ == "__main__":
    main()
