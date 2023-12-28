import pyperclip
from dateutil import parser

list_to_center = []


def is_valid_date(date_string):
    try:
        parser.parse(date_string)
        return True
    except ValueError:
        return False


list_to_center.append(is_valid_date)


def is_numeric(s):
    try:
        num = float(s)
        return isinstance(num, (int, float))
    except ValueError:
        return False


list_to_center.append(is_numeric)


def yes_no(s):
    if s.lower().strip() == "yes" or s.lower().strip() == "no":
        return True
    else:
        return False


list_to_center.append(yes_no)


def True_false(s):
    if s.strip().upper() == "TRUE" or s.strip().upper() == "FALSE":
        return True
    else:
        return False


list_to_center.append(True_false)


def should_be_centered(s):
    for i in list_to_center:
        if i(s):
            return True
    return False


def code(content):
    rows = content.split("\n")

    # Edit header and create initial 2nd row
    header = ["_" + cell.strip() + "_" for cell in rows[0].split("\t")]
    div = " -- |"
    row2 = f"| -- |{div * (len(header) - 1)}"

    # Split each row to create each row cells and create a list of the rest rows
    table_rows = ["| " + " | ".join(row.split("\t")).strip() + " |" for row in rows[1:]]

    # get indexes of columns to center (got from the 3rd row .. the first one containing data)
    cells = table_rows[2].strip().split("|")[1:-1]
    numbers = []
    for i in range(len(cells)):
        if should_be_centered(cells[i]):
            numbers.append(i)

    # for the 2nd row .. set the header (the "| -- |") of the columns-to-center .. to "| :--: |"
    for i in range(len(numbers)):
        shift = i * 2
        row2 = (
            row2[: numbers[i] * 5 + shift]
            + "| :--: |"
            + row2[(numbers[i] + 1) * 5 + shift + 1 :]
        )

    # add header and 2nd row at indexes 0 and 1
    table_rows.insert(0, f"| {' | '.join(header)} |")
    table_rows.insert(1, row2)

    # get the output as a string to copy to the clipboard
    # replacing the TRUE and FALSE with centered checkboxes (actually .. emoje)
    output = "\n".join(table_rows)
    output = output.replace("| TRUE |", "| ☑️ |")
    output = output.replace("| FALSE |", "| 🔘 ")

    # copy the output
    pyperclip.copy(output)
    return output


print(f"\n coppied md table:'\n{code(pyperclip.paste())}\n")
