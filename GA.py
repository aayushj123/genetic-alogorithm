from numpy.random import randint
from numpy.random import rand

# define variables

# number of iterations
iterations = 10
# number of bits
no_of_bits = 20
# population size
population_size = 10
# crossover rate
crossover_rate = 0.4
# utation rate
mutation_rate = 1.0 / float(no_of_bits)



def objective(x):
	return -sum(x)

def tournament_selection(pop, scores, k=3):
	selection = randint(len(pop))
	for i in randint(0, len(pop), k-1):
		if scores[i] < scores[selection]:
			selection = i
	return pop[selection]
 
def crossover(p1, p2, crossover_rate):
	c1, c2 = p1.copy(), p2.copy()
	if rand() < crossover_rate:
		pt = randint(1, len(p1)-2)
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]
 
def mutation(bitstring, mutation_rate):
	for i in range(len(bitstring)):
		if rand() < mutation_rate:
			#flipping the bit
			bitstring[i] = 1 - bitstring[i]
 
def genetic_algorithm(objective, no_of_bits, iterations, population_size, crossover_rate, mutation_rate):
	pop = [randint(0, 2, no_of_bits).tolist() for _ in range(population_size)]
	best, best_eval = 0, objective(pop[0])
	for gen in range(iterations):
		scores = [objective(c) for c in pop]
		#checking for new best solution
		for i in range(population_size):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print("generation %d: new best solution f(%s) = %.3f" % (gen,  pop[i], scores[i]))
		#parent selection
		selected = [tournament_selection(pop, scores) for _ in range(population_size)]
		#next generation
		children = list()
		for i in range(0, population_size, 2):
			p1, p2 = selected[i], selected[i+1]	
			for c in crossover(p1, p2, crossover_rate):
				mutation(c, mutation_rate)
				children.append(c)
		pop = children
	return [best, best_eval]
 


best, score = genetic_algorithm(objective, no_of_bits, iterations, population_size, crossover_rate, mutation_rate)