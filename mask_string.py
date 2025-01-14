# Mask the string with all Xs
def mask_string(input_string):
    return ''.join('X' if c not in ['-', '_'] else c for c in input_string)
