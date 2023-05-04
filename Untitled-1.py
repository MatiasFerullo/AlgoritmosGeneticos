from random import *
from statistics import mean

#funcion objetivo = x/(2**30-1)
inputs = []
inputsBin = []

#parámetros
prob_crossover = 0.75
prob_mutacion = 0.005
tam_poblacion = 10
ciclos = 20
tam_torneo = 4
metodo_selec = 'R' # R: ruleta / T: torneo


#Chance esta entre (0, 1)
def roll(chance: float) -> bool:
    pass

def poblacion_inicial(n: int) -> None:
    for _ in range(n):
        numero = ''.join(choice(['0', '1']) for _ in range(30))
        inputsBin.append(numero)
        s = int(numero, 2)
        inputs.append(s)
    return inputsBin, inputs

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
        if lista[punto] == '0':
            lista[punto] = '1'
        else: 
            lista[punto] = '0'
        cromosoma = ''.join(lista)
    return cromosoma 


def crossover(parent1: str, parent2: str) -> tuple[str, str]:
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
    inputsBin, inputs = poblacion_inicial(tam_poblacion)
    for ciclo in range(ciclos):
        objFuncs=[]
        #calcula la función objetivo de cada elemento
        for ints in inputs:
            objFuncs.append(objetiveFunc(ints))
        funcs = fitness(objFuncs)

        #extraer valores obtenidos
        print("generación: " + str(ciclo))
        print("Cromosoma Mayor valor: "+ str(inputsBin[objFuncs.index(max(objFuncs))]))
        print("Mayor:" + str(max(objFuncs)))
        print("Promedio:" + str(mean(objFuncs)))
        print("Menor:" + str(min(objFuncs)))

        next_inputsBin = [] #inicializa la siguiente generación
        for i in range(int(tam_poblacion/2)): 
            padres=[]
            #selecciona par de padres según el método seteado
            if metodo_selec == 'R':
                padres = ruleta(funcs, 2)
            else:
                padres = torneo(funcs,2, tam_torneo)

            if random() < prob_crossover: #verifica si hay crossover
                hijo1, hijo2 = crossover(inputsBin[padres[0]], inputsBin[padres[1]]) #aplica operador de crossover
            else: #no hay corossover y los padres pasan a ser hijos
                hijo1 = inputsBin[padres[0]]
                hijo2 = inputsBin[padres[1]]
            next_inputsBin.extend([hijo1, hijo2]) #se agregan los hijos a la siguiente generación

        for i in range(len(next_inputsBin)): #verifica si se aplica mutación para cada cromosoma
            next_inputsBin[i] = mutacion(next_inputsBin[i], prob_mutacion) 
            #print(mutacion(next_inputsBin[i], prob_mutacion))

        inputsBin = next_inputsBin #la siguiente generación pasa a ser la actual
        inputs = []
        #se calculan los valores en decimal
        for i in inputsBin:
            s = int(i, 2)
            inputs.append(s)



if __name__ == '__main__':
    main()