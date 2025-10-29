
def makeBoard(elements):
    returnedBoard = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    count = 0
    for row in returnedBoard:
        for column in range(len(row)):
            row[column] = elements[count]
            count += 1

    return returnedBoard

def formatBoard(board):
    verticalBorderLength = 25
    output = "     A    B    C    D    E\n"
    output += "   " + "_" * verticalBorderLength + "\n"
    for idx, row in enumerate(board, 1):
        row_str = " | ".join(f"{item:2}" for item in row)
        output += f"{idx} | {row_str} |\n"
    output += "   " + "_" * verticalBorderLength
    return output

def findLocation(board, key, value):

    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            for dictionary in elements:
                if key in dictionary and dictionary[key] == value and dictionary[key] == cell:
                    return f"{toIdxConverter('col', col_idx)}{toIdxConverter('row', row_idx)}"
    return None

def findElement(board, column, row):
    return board[row][column]

def findSpecificElementInfo(key, value, info):
    for element in elements:
        if element.get(key) == value:
            return element.get(info)

def findElementInfo(element):
    return f"""
Your Card is {findSpecificElementInfo('symbol', element, 'name')}.
The Atomic Number is {findSpecificElementInfo('symbol', element, 'atomic_number')}.
The Symbol of the Card is {element}.
Your card is {findSpecificElementInfo('symbol', element, 'state')} at room temperature.
Your card's melting point in Celsius is {findSpecificElementInfo('symbol', element, 'melting_point')}.
Your card is naturally {findSpecificElementInfo('symbol', element, 'color')}.
Your card {findSpecificElementInfo('symbol', element, 'lustre')} lustrous.
Your card {findSpecificElementInfo('symbol', element, 'malleability')} malleable.
Your card {findSpecificElementInfo('symbol', element, 'ductility')} ductile.
Your card {findSpecificElementInfo('symbol', element, 'magnetism')} magnetic.
Your card {findSpecificElementInfo('symbol', element, 'sonority')} sonorous.
Your card is considered {findSpecificElementInfo('symbol', element, 'status')}.
Your card has {findSpecificElementInfo('symbol', element, 'shells')} shells."""

def toIdxConverter(row_column, value):
    colIdxConverter = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E"
    }
    rowIdxConverter = {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5
    }

    if row_column == 'row':
        return rowIdxConverter[value]
    elif row_column == 'col':
        return colIdxConverter[value]


def fromIdxConverter(row_column, value):
    colIdxConverter = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4
    }
    rowIdxConverter = {
        '1' : 0,
        '2' : 1,
        '3' : 2,
        '4' : 3,
        '5' : 4
    }

    if row_column == 'row':
        return rowIdxConverter.get(value)
    elif row_column == 'col':
        return colIdxConverter.get(value)
    else: return None


elements = [
    {"atomic_number": 1, "name": "Hydrogen", "symbol": "H", "state": "gas", "melting_point": -259.1, "color": "colorless", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 1},
    {"atomic_number": 2, "name": "Helium", "symbol": "He", "state": "gas", "melting_point": -272.2, "color": "colorless", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 1},
    {"atomic_number": 3, "name": "Lithium", "symbol": "Li", "state": "solid", "melting_point": 180.5, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 2},
    {"atomic_number": 4, "name": "Beryllium", "symbol": "Be", "state": "solid", "melting_point": 1287, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 2},
    {"atomic_number": 5, "name": "Boron", "symbol": "B", "state": "solid", "melting_point": 2076, "color": "black", "lustre": 'is', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 2},
    {"atomic_number": 6, "name": "Carbon", "symbol": "C", "state": "solid", "melting_point": 3550, "color": "black", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 2},
    {"atomic_number": 7, "name": "Nitrogen", "symbol": "N", "state": "gas", "melting_point": -210.0, "color": "colorless", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 2},
    {"atomic_number": 8, "name": "Oxygen", "symbol": "O", "state": "gas", "melting_point": -218.8, "color": "colorless", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 2},
    {"atomic_number": 9, "name": "Fluorine", "symbol": "F", "state": "gas", "melting_point": -219.6, "color": "yellow", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 2},
    {"atomic_number": 10, "name": "Neon", "symbol": "Ne", "state": "gas", "melting_point": -248.6, "color": "orange", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 2},
    {"atomic_number": 11, "name": "Sodium", "symbol": "Na", "state": "solid", "melting_point": 97.8, "color": "white", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 3},
    {"atomic_number": 12, "name": "Magnesium", "symbol": "Mg", "state": "solid", "melting_point": 650, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 3},
    {"atomic_number": 13, "name": "Aluminum", "symbol": "Al", "state": "solid", "melting_point": 660.3, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 3},
    {"atomic_number": 14, "name": "Silicon", "symbol": "Si", "state": "solid", "melting_point": 1414, "color": "gray", "lustre": 'is', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 3},
    {"atomic_number": 15, "name": "Phosphorus", "symbol": "P", "state": "solid", "melting_point": 44.2, "color": "white", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 3},
    {"atomic_number": 16, "name": "Sulfur", "symbol": "S", "state": "solid", "melting_point": 115.2, "color": "yellow", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 3},
    {"atomic_number": 17, "name": "Chlorine", "symbol": "Cl", "state": "gas", "melting_point": -101.5, "color": "green", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 3},
    {"atomic_number": 18, "name": "Argon", "symbol": "Ar", "state": "gas", "melting_point": -189.3, "color": "colorless", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 3},
    {"atomic_number": 19, "name": "Potassium", "symbol": "K", "state": "solid", "melting_point": 63.5, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 20, "name": "Calcium", "symbol": "Ca", "state": "solid", "melting_point": 842, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 26, "name": "Iron", "symbol": "Fe", "state": "solid", "melting_point": 1538, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is', "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 27, "name": "Cobalt", "symbol": "Co", "state": "solid", "melting_point": 1495, "color": "gray", "lustre": "is", "malleability": "is", "ductility": "is", "magnetism": "is", "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 28, "name": "Nickel", "symbol": "Ni", "state": "solid", "melting_point": 1455, "color": "gray", "lustre": "is", "malleability": "is", "ductility": "is", "magnetism": "is", "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 29, "name": "Copper", "symbol": "Cu", "state": "solid", "melting_point": 1085, "color": "red", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 30, "name": "Zinc", "symbol": "Zn", "state": "solid", "melting_point": 419.5, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 4},
    {"atomic_number": 31, "name": "Gallium", "symbol": "Ga", "state": "solid", "melting_point": 29.8, "color": "silver", "lustre": "is", "malleability": "is", "ductility": "is", "magnetism": "is not", "sonority" : "is not", "status": "metallic", "shells": 4},
    {"atomic_number": 35, "name": "Bromine", "symbol": "Br", "state": "liquid", "melting_point": -7.2, "color": "red", "lustre": 'is not', "malleability": 'is not', "ductility": 'is not', "magnetism": 'is not', "sonority" : "is not", "status": "non metallic", "shells": 4},
    {"atomic_number": 47, "name": "Silver", "symbol": "Ag", "state": "solid", "melting_point": 961.8, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 5},
    {"atomic_number": 49, "name": "Indium", "symbol": "In", "state": "solid", "melting_point": 156.6, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 5},
    {"atomic_number": 79, "name": "Gold", "symbol": "Au", "state": "solid", "melting_point": 1064, "color": "yellow", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 6},
    {"atomic_number": 80, "name": "Mercury", "symbol": "Hg", "state": "liquid", "melting_point": -38.8, "color": "silver", "lustre": "is", "malleability": "is", "ductility": "is", "magnetism": "is not", "sonority" : "is not", "status": "metallic", "shells": 6},
    {"atomic_number": 82, "name": "Lead", "symbol": "Pb", "state": "solid", "melting_point": 327.5, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 6},
    {"atomic_number": 88, "name": "Radium", "symbol": "Ra", "state": "solid", "melting_point": 700, "color": "white", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 7},
    {"atomic_number": 92, "name": "Uranium", "symbol": "U", "state": "solid", "melting_point": 1132, "color": "gray", "lustre": 'is', "malleability": 'is', "ductility": 'is', "magnetism": 'is not', "sonority" : "is", "status": "metallic", "shells": 7}
]
