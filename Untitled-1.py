from random import *

#funcion bjetivo = x/(2**30-1)
inputs = []
inputsBin = []

#Chance esta entre (0, 1)
def roll(chance: float) -> bool:
    pass

def poblacion_inicial(n: int) -> None:
    for _ in range(n):
        numero = ''.join(choice(['0', '1']) for _ in range(30))
        inputsBin.append(numero)
        s = int(numero, 2)
        inputs.append(s)

def ruleta(listFitness: list, popSelected: int) -> list:
    elegidos = []
    for _ in range(popSelected):
        list = [j for j in range(len(listFitness))]
        elegidos.append(choices(list, listFitness)[0])
    return elegidos

def mutacion():
    pass

def crossover(parent1: str, parent2: str) -> Tuple[str, str]:
    # Escoger un punto de cruzamiento aleatorio
    crossover_point = randint(1, len(parent1) - 1)

    # Combinar los genes de los padres
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    # Devolver los dos nuevos individuos generados
    return child1, child2

def fitness(funciones_obj: list) -> list:
    func = []
    sum_func = sum(funciones_obj)
    for fun in funciones_obj:
        func.append(fun / sum_func)
    return func

def objetiveFunc(x: int) -> float:
    return (x/(2**(30) - 1))

def main():
    objFuncs = []
    poblacion_inicial(10)
    for ints in inputs:
        objFuncs.append(objetiveFunc(ints))
    funcs = fitness(objFuncs)
    print(funcs)
    print(sum(funcs))
    print(ruleta(funcs, 2))


if __name__ == '__main__':
    main()
