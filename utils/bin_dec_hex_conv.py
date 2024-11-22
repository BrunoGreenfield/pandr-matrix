# A collection of functions that allow us to convert between Binary, Hexadecimal and Decimal 8-bit integers

# hexChars is a list of all the hex characters in order
hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Converts any hex integers to binary equivlents intuitively
def hexToBin(hexStr):
    hexList = [i for i in hexStr] # This is a list comprehension. It saves me from having to run a 'for' loop in order to get each element from our string to put into a list

    result = ''
    for nibble in hexList:
        result += decToBin(hexChars.index(nibble), True) # The index will be the decimal equivlent as the list is ordered

    return result

# Can convert 4 or 8 bit decimal integers to binary intuitively. Defaults to 8 bit mode unless fourBitMode is specified as true
def decToBin(dec, fourBitMode=False): # We assume 8 bit mode unless explicitly stated
    if fourBitMode:
        comparisonNum = 8
    else:
        comparisonNum = 128

    result = ''
    while True:
        if comparisonNum <= dec:
            result += '1'
            dec -= comparisonNum
        else:
            result += '0'

        comparisonNum /= 2
        if comparisonNum < 1:
            break

    return result

def binToDec(binStr):
    comparisonNum = 128
    total = 0
    for char in binStr:
        if char == "1":
            total += comparisonNum
        else:
            total += 0
        comparisonNum /= 2
        if comparisonNum < 1:
            break
    return total
