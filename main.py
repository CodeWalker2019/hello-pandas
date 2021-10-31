from inquirer import prompt
from numpy import int64
from pandas.core.frame import DataFrame
from const import ATTRIBUTES, Options, Questions, mock_data

df = DataFrame(mock_data, columns=[col for col in ATTRIBUTES])
answers = prompt(Questions.OPTION.value)

while answers[Questions.OPTION.name] != Options.EXIT.value:

    if answers[Questions.OPTION.name] == Options.ADD_TO_FRAME.value:
        answers = prompt(Questions.NEW_ROW.value)
        df = df.append(answers, ignore_index=True)
        print("\nData has been added!\n")

    elif answers[Questions.OPTION.name] == Options.SORT_BY_ATTRIBUTE.value:
        answers = prompt(Questions.ATTRIBUTE.value)
        df = df.sort_values(
            answers[Questions.ATTRIBUTE.name], ascending=False)
        print('Data has been sorted!\n')

    elif answers[Questions.OPTION.name] == Options.DELETE_BY_ATTRIBUTE.value:
        answers = prompt(Questions.ATTRIBUTE.value)
        attribute = answers[Questions.ATTRIBUTE.name]
        answers = prompt(Questions.NEW_ROW.value[attribute])
        value = answers[attribute]
        rows_to_delete = df.index[df[attribute] == value].tolist()
        df = df.drop(rows_to_delete)

    elif answers[Questions.OPTION.name] == Options.DELETE_BY_INDEX.value:
        answers = prompt(Questions.INDEX.value)
        index = int(answers[Questions.INDEX.name])
        df.drop(index)

    elif answers[Questions.OPTION.name] == Options.PRINT_BY_ATTRIBUTE.value:
        answers = prompt(Questions.ATTRIBUTE.value)
        attribute = answers[Questions.ATTRIBUTE.name]
        answers = prompt(Questions.NEW_ROW.value[attribute])
        value = answers[attribute]

        if df[attribute].dtype == int64():
            value = int(value)

        result = df[df[attribute].isin([value])]
        print(result, "\n")

    elif answers[Questions.OPTION.name] == Options.PRINT_ALL.value:
        print(df, "\n")

    answers = prompt(Questions.OPTION.value)
