import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.io.input import (file_input, pandas_input)


def test_file_input():
    src = './src/tests/test_io/test_resources/test_inputs/test_input.txt'
    data = 'File input test\nTest data'

    with open(src, mode='w') as file:
        file.write(data)

    result = file_input(src)
    assert result == data


def test_pandas_unput():
    src = './src/tests/test_io/test_resources/test_inputs/test_input.csv'
    data = "Pandas input test\nTest data"

    with open(src, mode='w') as file:
            file.write(data)

    result = pandas_input(src)
    assert result == data
