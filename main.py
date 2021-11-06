from pandas.core.frame import DataFrame
from const import ATTRIBUTES, Option, mock_data
from input import Values, get_attribute, get_index, get_option
from utils import format_input, remove_redudant_spaces

df = DataFrame(mock_data, columns=ATTRIBUTES)
print("\nNOTE! To erase text use CTRL + BACKSPACE\n")
option = get_option()

while option != Option.EXIT.value:

    if option == Option.PRINT_ALL.value:
        print(df, "\n")

    elif option == Option.ADD_TO_FRAME.value:
        new_data = {attribute: Values[attribute]() for attribute in ATTRIBUTES}
        formatted = {key: format_input(value) for (key, value) in new_data.items()}
        df = df.append(formatted, ignore_index=True)
        print("\nData has been added!\n")

    elif option == Option.SORT_BY_ATTRIBUTE.value:
        attribute = get_attribute()
        df = df.sort_values(by=attribute, ascending=False)
        print("Data has been sorted!\n")

    elif option == Option.DELETE_BY_ATTRIBUTE.value:
        attribute = get_attribute()
        value = format_input(Values[attribute]())
        rows_to_delete = df.index[df[attribute] == value].tolist()
        msg = f"\nDeleted rows:\n{df.loc[rows_to_delete]}\n"

        if not len(rows_to_delete):
            msg = f"\nRecords with value <{value}> were not found in column <{attribute}>\n"    

        print(msg)
        df = df.drop(rows_to_delete)

    elif option == Option.DELETE_BY_INDEX.value:
        data_size = len(df)

        try:
            index = int(get_index(df.size))
            print(f"\nDeleted row:\n{df.loc[[index]]}\n")
            df = df.drop(index)

        except KeyError:
            print(f"Index <{index}> was not found!\n")

    elif option == Option.PRINT_BY_ATTRIBUTE.value:
        attribute = get_attribute()
        value = format_input(Values[attribute]())
        result = df[df[attribute].isin([value])]

        if not len(result):
            result = f"\nRecords with value <{value}> were not found in column <{attribute}>\n"

        print(f'\n{result}\n')

    option = get_option()
