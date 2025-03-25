import pandas as pd


def console_input():
    """
    input using console
    """

    return input("Enter data: ")


def file_input(src):
    """
    input using built-in python features
    """

    with open(src, mode='r') as file:
        data = file.read()
        return data


def pandas_input(src):
    """
    input using pandas
    """

    data = pd.read_csv(src, header=None)
    result = "\n".join(data[0].astype(str))
    return result
