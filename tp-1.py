from random import *
from statistics import mean
import matplotlib.pyplot as plt

#funcion objetivo = x/(2**30-1)
cromosomas = []
BinaryCromosomas = []

#parámetros
prob_crossover = 0.75
prob_mutacion = 0.005
tam_poblacion = 10
ciclos = 20
tam_torneo = 4
metodo_selec = 'R' # R: ruleta / T: torneo
usa_elitismo = True 


def poblacion_inicial(n: int) -> None:
    for _ in range(n):
        cromosoma = ''.join(choice(['0', '1']) for _ in range(30))
        BinaryCromosomas.append(cromosoma)
        s = int(cromosoma, 2)
        cromosomas.append(s)
    return BinaryCromosomas, cromosomas


def ruleta(funciones_fitness: list, n_padres: int) -> list:
    padres_elegidos = []

    for _ in range(n_padres):
        list = [j for j in range(len(funciones_fitness))]
        padres_elegidos.append(choices(list, funciones_fitness)[0])

    return padres_elegidos


def torneo(funciones_fitness : list, n_padres: int, torneo_size: int) ->list:
    padres_elegidos = [] 

    for _ in range(n_padres): 
        list = [j for j in range(len(funciones_fitness))]
        torneo = sample(list, torneo_size) #elige participantes del torneo
        funciones_fitness_torneo = [funciones_fitness[i] for i in torneo]
        padres_elegidos.append(choices(torneo, funciones_fitness_torneo)) #elige ganador del torneo con probabilidad basada en su fitness
    
    flat_elegidos = []
    
    for padre in padres_elegidos:
        flat_elegidos.extend(padre)
    
    return flat_elegidos
        
       
def mutacion(cromosoma : str, prob: float) -> list:
    genes = list(cromosoma)
    if random() < prob: #determina si se aplica la mutación o no basado en la probabilidad de mutación
        punto = randint(1, len(genes) - 1) #determina el gen que se va a mutar
        #Método de mutación: Invertida. Si es 1 pone 0 y si es 0 pone 1
        if genes[punto] == '0':
            genes[punto] = '1'
        else: 
            genes[punto] = '0'
        cromosoma = ''.join(genes)
    return cromosoma 


def crossover(padre1: str, padre2: str) -> tuple[str, str]:
    # Escoger un punto de cruzamiento aleatorio
    punto_crossover = randint(1, len(padre1) - 1)

    # Combinar los genes de los padres
    hijo1 = padre1[:punto_crossover] + padre2[punto_crossover:]
    hijo2 = padre2[:punto_crossover] + padre1[punto_crossover:]

    # Devolver los dos nuevos hijos generados
    return hijo1, hijo2

def funcion_fitness(funciones_objetivo: list) -> list:
    funciones = []
    sumatoria_funciones = sum(funciones_objetivo)
    for funcion in funciones_objetivo:
        funciones.append(funcion / sumatoria_funciones)
    return funciones

def funcion_objetivo(x: int) -> float:
    return (x/(2**(30) - 1))


def graficar(ciclos: int, maximos: list, promedios: list, minimos: list) -> None:
    plt.plot(maximos, color='red' ) 
    plt.xlim([0,ciclos])
    plt.ylim([0,1])
    plt.ylabel('valor') 
    plt.xlabel('población') 
    plt.title("Valores máximos") 
    plt.show()

    plt.plot(promedios, color='green' ) 
    plt.xlim([0,ciclos])
    plt.ylim([0,1])
    plt.ylabel('valor') 
    plt.xlabel('población') 
    plt.title("Valores promedio") 
    plt.show()


    plt.plot(minimos, color='blue' ) 
    plt.xlim([0,ciclos])
    plt.ylim([0,1])
    plt.ylabel('valor') 
    plt.xlabel('población') 
    plt.title("Valores mínimos") 
    plt.show()


def main():

    maximos = []
    promedios = []
    minimos = []
    funciones_objetivo = []
    
    binary_cromosomas, cromosomas = poblacion_inicial(tam_poblacion)
    
    for ciclo in range(ciclos):
        #calcula la función objetivo de cada elemento
        funciones_objetivo = []
        for cromosoma in cromosomas:
            funciones_objetivo.append(funcion_objetivo(cromosoma))
        funciones_fitness = funcion_fitness(funciones_objetivo)

        #extraer valores obtenidos
        print("")
        print("===================================")
        print("Generación: " + str(ciclo))
        print("Cromosoma Mayor valor: "+ str(binary_cromosomas[funciones_objetivo.index(max(funciones_objetivo))]))
        print("Mayor:" + str(max(funciones_objetivo)))
        print("Promedio:" + str(mean(funciones_objetivo)))
        print("Menor:" + str(min(funciones_objetivo)))
        maximos.append(max(funciones_objetivo))
        promedios.append(mean(funciones_objetivo))
        minimos.append(min(funciones_objetivo))

        #inicializa la siguiente generación
        next_binary_cromosomas = [] 
        n = int(tam_poblacion/2)
        
        if usa_elitismo:
            int((tam_poblacion-2)/2) #corre una vez menos porque con elitismo los dos mejores padres pasan directamente
            next_binary_cromosomas.append(binary_cromosomas[funciones_fitness.index(max(funciones_fitness))])
            next_binary_cromosomas.append(binary_cromosomas[funciones_fitness.index(sorted(funciones_fitness)[-2])])

        for i in range(n): 
            #selecciona par de padres según el método seteado
            padres = []
            if metodo_selec == 'R':
                padres = ruleta(funciones_fitness, 2)
            else:
                padres = torneo(funciones_fitness,2, tam_torneo)

            if random() < prob_crossover: #verifica si hay crossover
                hijo1, hijo2 = crossover(binary_cromosomas[padres[0]], binary_cromosomas[padres[1]]) #aplica operador de crossover
            else: #no hay corossover y los padres pasan a ser hijos
                hijo1 = binary_cromosomas[padres[0]]
                hijo2 = binary_cromosomas[padres[1]]
            
            next_binary_cromosomas.extend([hijo1, hijo2]) #se agregan los hijos a la siguiente generación

        for i in range(len(next_binary_cromosomas)): #verifica si se aplica mutación para cada cromosoma
            next_binary_cromosomas[i] = mutacion(next_binary_cromosomas[i], prob_mutacion) 

        binary_cromosomas = next_binary_cromosomas #la siguiente generación pasa a ser la actual
        cromosomas = []

        #se calculan los valores en decimal
        for b_cromosoma in binary_cromosomas:
            cromosoma = int(b_cromosoma, 2)
            cromosomas.append(cromosoma)
    
    graficar(ciclos, maximos, promedios, minimos)


if __name__ == '__main__':
    main()
