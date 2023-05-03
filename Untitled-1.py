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


def torneo(listFitness : list, popSelected: int, torneo_size: int) ->list:
    elegidos = [] 
    for _ in range(popSelected): 
        list = [j for j in range(len(listFitness))]
        torneo = sample(list, torneo_size) #elige participantes del torneo
        listFitness_torneo = [listFitness[i] for i in torneo]
        elegidos.append(choices(torneo, listFitness_torneo)) #elige ganador del torneo con probabilidad basada en su fitness
    flat_elegidos = []
    for e in elegidos:
        flat_elegidos.extend(e)
    return flat_elegidos
        
       

def mutacion(cromosoma : str, prob: float) -> list:
    lista = list(cromosoma)
    if random() < prob: #determina si se aplica la mutación o no basado en la probabilidad de mutación
        punto = randint(1, len(lista) - 1) #determina el gen que se va a mutar
        #Método de mutación: Invertida. Si es 1 pone 0 y si es 0 pone 1
        if lista[punto] == 0:
            lista[punto] = 1
        else: 
            lista[punto] = 0
        cromosoma = str(lista)
    return cromosoma 


def crossover():
    pass

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
    print("Ruleta:")
    print(ruleta(funcs, 2))
    print("Torneo:")
    print(torneo(funcs, 2, 4))
    mutacion(inputsBin[0], 0.99)




if __name__ == '__main__':
    main()