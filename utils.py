def get_integer_input():
    try:
        inpt = int(input())
        return inpt
    except:
        raise Exception("Input must be of type integer")