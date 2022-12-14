from binascii import crc32
from prettytable import PrettyTable as PT

"""
Color   First    Second    Third
Black   0        0         x1
Brown   1        1         x10
Red     2        2         x100
Orange  3        3         x1000
Yellow  4        4         x10000
Green   5        5         x100000
Blue    6        6         x1000000
Violet  7        7         --
Gray    8        8         --
White   9        9         --
"""

"""
Color   Tolerance
None    20%
Silver  10%
Gold    5%
Red     2%
Brown   1%
"""

def getColors(col1, col2, col3, col4 = None):

    #Store values for each color for columns 1 and 2
    colorDict = {
        'Black': '0',
        'Brown': '1',
        'Red': '2',
        'Orange': '3',
        'Yellow': '4',
        'Green': '5',
        'Blue': '6',
        'Violet': '7',
        'Gray': '8',
        'White': '9'
    }

    #Store the multiplying values on the colors
    multiplyColor = {
        'Black': 1,
        'Brown': 10,
        'Red': 100,
        'Orange': 1000,
        'Yellow': 10000,
        'Green': 100000,
        'Blue': 1000000,
        'Violet': None,
        'Gray': None,
        'White': None
    }

    #Store the color associated with each number
    referenceNums = {
        0:'Black',
        1:'Brown',
        2:'Red',
        3:'Orange',
        4:'Yellow',
        5:'Green',
        6:'Blue',
        7:'Violet',
        8:'Gray',
        9:'White'
    }

    tolerances = {
        0:'10%',
        1:'5%',
        2:'2%',
        3:'1%'
    }

    #Check user input
    inputs = [col1, col2, col3]

    for inp in inputs:
        if type(inp) != int:
            raise TypeError('Not a valid input type')
    
    #First integer for first color
    color1 = referenceNums.get(col1)
    color2 = referenceNums.get(col2)

    #Second integer for second color
    num1 = colorDict.get(color1)
    num2 = colorDict.get(color2)
    finalNum = num1+num2
    finalNum = int(finalNum)

    #Multiply operation for fourth color
    color3 = referenceNums.get(col3)
    num3 = multiplyColor.get(color3)
    total = num3 * finalNum

    #Get the tolerance percentage 
    #tolerancePercentage = '20%'
    if col4 != None:
        tolerancePercentage = tolerances.get(col4)
    else:
        tolerancePercentage = '20%'

    print('Your result is %d with a tolerance of %s\n' % (total, tolerancePercentage))
    return finalNum * num3
    
def main():

    #Create table for displaying colors 
    table = PT()
    table.border = True

    table.field_names = ['Color', 'number']
    table.add_rows([['Black', '0'], 
        ['Brown', '1'], 
        ['Red','2'], 
        ['Orange', '3'], 
        ['Yellow', '4'],
        ['Green', '5'], 
        ['Blue', '6'], 
        ['Violet', '7'], 
        ['Gray', '8'], 
        ['White', '9']])

    #Print first tabel and then proceed to take input from the user
    print('Color table by number')
    print(table)
    print()

    print('Column 1: ')
    c1 = int(input())
    print()

    print('Column 2: ')
    c2 = int(input())
    print()

    print('Column 3: ')
    c3 = int(input())
    print()

    #table displaying colors for tolerances. Print this table and then get last user input
    tolerancesTable = PT()
    tolerancesTable.field_names = ['Color', 'number']
    tolerancesTable.add_rows([['None', 'NULL'], 
    ['Silver', '0'],
    ['Gold', '1'],
    ['Red', '2'],
    ['Brown', '3']])
    print(tolerancesTable)
    print()

    print('Column 4: ')
    c4 = input()

    #If we pass nothing to c4 then it will just equal None
    if c4 != 'NULL':
        c4 = int(c4)
    else:
        c4 = None
    print()

    getColors(c1, c2, c3, c4)

    
if __name__ == '__main__':
    main()