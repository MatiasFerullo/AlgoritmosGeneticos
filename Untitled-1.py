from random import *

cant = 10
zeroCount = 30

inputsBinary = []
inputs = []

def getPoblacionInicial(cant, zeroCount):
    for _ in range(cant):
        numero = ''.join([choice(['0', '1']) for _ in range(zeroCount)])
        inputsBinary.append(numero)

        num = int(numero, 2)
        inputs.append(num)

def fitnessFunct():
    pass



print(inputsBinary)
print(inputs)
