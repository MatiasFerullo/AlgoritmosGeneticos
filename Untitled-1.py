from random import *

inputs = []

for _ in range(10):
    numero = [choice(['0', '1']) for _ in range(30)]
    s = int(''.join(numero), 2)
    inputs.append(s)
print(inputs)
