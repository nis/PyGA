class pyga():
	"""docstring for PyGA"""

	def __init__(self, populations, individuals, genes, mutation_rate):
		self.number_populations = populations
		self.number_individuals = individuals
		self.number_genes = genes
		self.mutation_rate = mutation_rate

		self.initialize_population()

	def run(self, generations, output = 0):
		# Run the GA

		for i in range(0, generations):
			self.generation = self.generation + 1

			if output:
				if i == 0 or i == (generations - 1):
					print 'Generation', i+1
			# Do a generation
			for ii in range(0, self.number_populations):
				# Find the two best individuals, and the two worst
				best_index, next_best_index, worst_index, next_worst_index = self.find_best_and_worst(self.population[ii])
				
				if output:
					if i == 0 or i == (generations - 1):
						print "\tPopulation", ii+1
						print "\t\tBest fitness:", self.fitness(self.population[ii][best_index])
						print "\t\tWorst fitness:", self.fitness(self.population[ii][worst_index])

				# Do crossover
				kid_1, kid_2 = self.crossover(self.population[ii][best_index], self.population[ii][next_best_index])

				# Replace the two worst with the new children
				self.population[ii][worst_index] = self.mutate(kid_1)
				self.population[ii][next_worst_index] = self.mutate(kid_2)

	def export(self):

		data = ''

		for i in range(0, self.number_populations):
			for ii in range(0, self.number_individuals):
				data = data + '['
				for iii in range(0, self.number_genes):
					data = data + str(self.population[i][ii][iii])
					if iii < self.number_genes - 1:
						data = data + ','

				data = data + ']' + '\n'
		return self.generation, data


	def find_best_and_worst(self, population):
		best_index = 0
		best_value = 0
		next_best_index = 0
		next_best_value = 0

		worst_index = 0
		worst_value = 99999999999999
		next_worst_index = 0
		next_worst_value = 99999999999999

		for i in range(0, self.number_individuals):
			fitness = self.fitness(population[i])
			if fitness > best_value:
				next_best_value = best_value
				next_best_index = best_index
				best_index = i
				best_value = fitness
			elif fitness > next_best_value:
				next_best_index = i
				next_best_value = fitness

			if fitness < worst_value:
				next_worst_value = worst_value
				next_worst_index = worst_index
				worst_value = fitness
				worst_index = i
			elif fitness < next_worst_value:
				next_worst_value = fitness
				next_worst_index = i

		return (best_index, next_best_index, worst_index, next_worst_index)

	def fitness(self, individual):
		return sum(individual) / self.number_genes

	def initialize_population(self):
		# Initialize the population with random values from -1 to 1
		import random
		self.population = []
		self.generation = 0

		for i in range(0,self.number_populations):
			pop = []
			for ii in range(0, self.number_individuals):
				individual = []
				for iii in range(0, self.number_genes):
					individual.append(float(random.uniform(-1, 1)))
				pop.append(individual)
			self.population.append(pop)

	def print_populations(self):
		for i in range(len(self.population)):
			print 'Population', i+1
			for ii in range(len(self.population[i])):
				print '\tIndividual', ii+1, self.population[i][ii]

	def mutate(self, individual):
		# Mutate genomes
		import random

		for i in range(self.number_genes):
			if random.random() < self.mutation_rate: # Should we mutate this gene?
				individual[i] = float(random.uniform(-1, 1))

		return individual

	def crossover(self, individual_1, individual_2):
		import random

		new_individual_1 = list(individual_1)
		new_individual_2 = list(individual_2)

		crossover_point_1 = random.randrange(0, self.number_genes)
		while crossover_point_1 > (self.number_genes - 1):
			crossover_point_1 = random.randrange(0, self.number_genes)

		crossover_point_2 = crossover_point_1
		while crossover_point_2 < crossover_point_1:
			crossover_point_2 = random.randrange(0, self.number_genes)

		# Do the cross over
		for i in range(self.number_genes):
			if i >= crossover_point_1 and i <= crossover_point_2:
				tempvalue = new_individual_1[i]

				new_individual_1[i] = new_individual_2[i]
				new_individual_2[i] = tempvalue

		return new_individual_1, new_individual_2

	def mean(self, individual):
		return sum(individual) / self.number_genes