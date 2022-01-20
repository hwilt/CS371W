## TODO: Define the goes_outside method here
def goes_outside(temperature):
    """
    Checks if you should go outside 
    
    Parameters
    ----------
    temperature : number
        the outside temperature.

    Returns
    -------
    ret : bool
        returns true if temperature is between 80 and 60, false other wise.
    """
    ret = True
    if(temperature > 80 or temperature < 60):
        ret = False
    return ret


# Run some tests on the method
print(goes_outside(50), end='.')
print(goes_outside(65), end='.')
print(goes_outside(72), end='.')
print(goes_outside(83), end='.')
print(goes_outside(90), end='.')
