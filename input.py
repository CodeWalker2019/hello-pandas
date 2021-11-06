import regex
from inquirer import errors
from inquirer.shortcuts import list_input, text
from const import ATTRIBUTES, OPTIONS

# ------------- VAIDATION -------------


def validate_number(_, value):
    if not regex.fullmatch(r'\d+', value):
        raise errors.ValidationError('', 'Digits only!')
    return True


def validate_year(_, value):
    if not regex.fullmatch(r'[^0]\d{1,4}', value):
        raise errors.ValidationError('', '1-4 digits only!')
    return True


def validate_text(_, value):
    if not regex.match(r'(\s*\w+\s*)+', value):
        raise errors.ValidationError('', 'Cannot be empty!')
    return True


def validate_index(value, size):
    if not (regex.fullmatch(r'\d+', value) and int(value) < size):
        raise errors.ValidationError(
            '', 'Invalid index! Value with such index doesn\'t exist!')
    return True


# ------------- USER INPUT -------------

def get_index(collection_size):
    return text(message="Index", validate=lambda _, value: validate_index(value, collection_size))


def get_attribute():
    return list_input("Attribute", choices=ATTRIBUTES)


def get_option():
    return list_input("Option", choices=OPTIONS)


Values = {
    'AUTHOR': lambda: text(message="Author", validate=validate_text),
    'TITLE': lambda: text(message="Title", validate=validate_text),
    'PUBLISHER': lambda: text(message="Publisher", validate=validate_text),
    'YEAR': lambda: text(message="Year", validate=validate_year),
    'PAGES': lambda: text(message="Pages", validate=validate_number),
}
