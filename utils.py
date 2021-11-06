from numpy import int64
import regex


def remove_redudant_spaces(value):
    return regex.sub('\s+', ' ', value).strip()


def cast_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value


def format_input(value):
    value = remove_redudant_spaces(value)
    value = cast_to_int(value)
    return value
