import pygad
import numpy

inputs = [0.4,1,0,7,8]
desired_output = 32


def fitness_func(self,solution, solution_idx):
    output = numpy.sum(solution*inputs)
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)
    
    return fitness

ga_instance = pygad.GA(num_generations=100,
                       sol_per_pop=10,
                       num_genes=len(inputs),
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       mutation_type="random",
                       mutation_probability=0.6)

ga_instance.run()

ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

