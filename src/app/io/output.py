def console_output(data):
    """
    output using console
    """

    print(data)


def built_in_output(data):
    """
    output using built-in python features
    """

    with open('./src/app/io/resources/outputs/output.txt', mode='a') as out:
        out.write(data)
        out.write('\n')
    