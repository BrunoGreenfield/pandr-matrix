# Here we import the 'randint' function from the 'random' library. Libraries are files that contain
# functions written by other people. In this case, writing a function that returns a random integer
# between two values could be hard and time consuming to code. In such a case, we can use somebody 
# else's code (the 'randint' function) to serve our purpose. Examples on when we might do this is 
# for generating random things and handling time.
from random import randint
from utils.bin_dec_hex_conv import hexChars

# This is where we declare our function -> 'def' is a python keyword, telling it that the next bit
# of code will be the function name
def randBin():
    # Here we declare an output variable, which we will return. We want to return a string, and so
    # we set the output to initially be an empty string
    output = '' # we have this outside the loop because we don't want to set it to empty every time the loop is run

    # Now we want to create an 8 character long binary number, so we loop 8 times (add 8 random characters to 'output')
    for _ in range(8):
        # Here we use the 'randint' function that we imported at the top of our file. This will
        # generate a random integer from 0 to 1 (i.e. a random binary digit)
        randomDigit = randint(0, 1) # We assign this to a variable, to keep track of it

        # As we want to output a string, we must convert our randomDigit into a string format (otherwise
        # python will try to mathematically add our integer to a string which is not possible (words can't be used in addition))
        randomDigit = str(randomDigit)

        # We can now add this digit onto the end of our output string. This is called concatination
        # Because we have both data types as strings, python will interpret this '+' to do this
        output = output + randomDigit
    
    # Here we simple return our 'output' variable once the loop has finished.
    return output

def randDec():
    return randint(0, 255)

def randHex():
    output = ''

    for _ in range(2):
        randomHex = hexChars[randint(0,15)]
        output = output + randomHex

    return output
