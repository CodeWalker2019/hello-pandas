from enum import Enum
from inquirer import Text, List


class Options(Enum):
    ADD_TO_FRAME = 'ADD TO FRAME'
    SORT_BY_ATTRIBUTE = 'SORT BY ATTRIBUTE'
    DELETE_BY_ATTRIBUTE = 'DELETE BY ATTRIBUTE'
    DELETE_BY_INDEX = 'DELETE BY INDEX'
    PRINT_BY_ATTRIBUTE = 'PRINT BY ATTRIBUTE'
    PRINT_ALL = 'PRINT ALL'
    EXIT = 'EXIT'


ATTRIBUTES = ['AUTHOR', 'TITLE', 'PUBLISHER', 'YEAR', 'PAGES']


class Questions(Enum):
    OPTION = [List(
        name='OPTION', message="Option",
        choices=[option.value for option in Options],
    )]

    ATTRIBUTE = [List(
        name='ATTRIBUTE', message='Attribute',
        choices=ATTRIBUTES
    )]

    NEW_ROW = { attribute: [Text(attribute, message=attribute)] for attribute in ATTRIBUTES }

    INDEX = [Text('INDEX', message="Index")]


mock_data = [
    ["Bjarne Stroustrup", "The C++ Programming Language", "Addison–Wesley", 1988, 1376],
    ["Bjarne Stroustrup", "The C++ Programming Language", "Addison–Wesley", 1988, 1376],
    ["Bjarne Stroustrup", "The C++ Programming Language", "Addison–Wesley", 1988, 1376],
    ["Robert Cecil Martin", "Clean Code", "Pearson Education", 2011, 464],
    ["Robert Cecil Martin", "Clean Code", "Pearson Education", 2011, 464],
    ["Robert Cecil Martin", "Clean Code", "Pearson Education", 2011, 464],
    ["Allen B. Downey", "Think Python",  "Green Tea Press", 2012, 209],
    ["Allen B. Downey", "Think Python",  "Green Tea Press", 2012, 209],
    ["Allen B. Downey", "Think Python",  "Green Tea Press", 2012, 209],
    ["Aditya Y. Bhargava", "Grokking Algorithms", "Manning", 2015, 256],
    ["Aditya Y. Bhargava", "Grokking Algorithms", "Manning", 2015, 256],
    ["Aditya Y. Bhargava", "Grokking Algorithms", "Manning", 2015, 256],
    ["J.K. Rowling", "Harry Potter and the Sorcerer's Stone", "Bloomsbury", 1997, 309],
    ["J.K. Rowling", "Harry Potter and the Sorcerer's Stone", "Bloomsbury", 1997, 309],
    ["J.K. Rowling", "Harry Potter and the Sorcerer's Stone", "Bloomsbury", 1997, 309],
    ["J.K. Rowling", "Harry Potter and the Sorcerer's Stone", "Bloomsbury", 1997, 309],
    ["J.K. Rowling", "Harry Potter and the Sorcerer's Stone", "Bloomsbury", 1997, 309],
    ["J.K. Rowling", "Harry Potter and the Chamber of Secrets", "Bloomsbury", 1998, 341],
    ["J.K. Rowling", "Harry Potter and the Chamber of Secrets", "Bloomsbury", 1998, 341],
    ["J.K. Rowling", "Harry Potter and the Chamber of Secrets", "Bloomsbury", 1998, 341],
    ["J.K. Rowling", "Harry Potter and the Prisoner of Azkaban", "Bloomsbury", 1999, 335],
    ["J.K. Rowling", "Harry Potter and the Prisoner of Azkaban", "Bloomsbury", 1999, 335],
    ["J.K. Rowling", "Harry Potter and the Prisoner of Azkaban", "Bloomsbury", 1999, 335],
    ["J.K. Rowling", "Harry Potter and the Order of the Phoenix", "Bloomsbury", 2003, 870],
    ["J.K. Rowling", "Harry Potter and the Order of the Phoenix", "Bloomsbury", 2003, 870],
    ["J.K. Rowling", "Harry Potter and the Order of the Phoenix", "Bloomsbury", 2003, 870],
]
