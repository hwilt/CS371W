def convert_format(filename):
    """
    Convert the file ending from .jpg to .png
    Parameters
    ----------
    filename: string
     Name of some file that ends in .jpg
    """
    ## TODO: Change result so that it ends with .png
    result = filename[:-3] + "png"
    return result


# Run some tests on the method
print(convert_format("chris.jpg"), end='_')
print(convert_format("celia.jpg"), end='_')
print(convert_format("drscoville.jpg"))