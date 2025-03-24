import pandas as pd


def console_input():
    """
    input using console
    """

    return input("Enter data: ")


def built_in_input():
    """
    input using built-in python features
    """

    with open('./src/app/io/resources/inputs/input.txt', mode='r') as file:
        data = file.read()
        return data


def pandas_input():
    """
    input using pandas
    """

    data = pd.read_csv('./src/app/io/resources/inputs/input.txt', sep='\n+', header=None)
    return data.to_string(index=False, header=False)
