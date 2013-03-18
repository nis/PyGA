class pyga():
	"""docstring for PyGA"""

	def __init__(self, populations, individuals, genes, mutation_rate, crossover_rate):
		self.number_populations = populations
		self.number_individuals = individuals
		self.number_genes = genes
		self.mutation_rate = mutation_rate
		self.crossover_rate = crossover_rate

		self.initialize_population()
		
	def initialize_population(self):
		# Initialize the population with random values from -1 to 1
		import random
		self.population = []

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

	def mutate(self):
		# Mutate genomes
		import random

		for i in range(0,self.number_populations):
			for ii in range(0, self.number_individuals):
				for iii in range(0, self.number_genes):
					if random.random() < self.mutation_rate: # Should we mutate this gene?
						self.population[i][ii][iii] = float(random.uniform(-1, 1))

	def crossover(self):
		import random

		for i in range(0,self.number_populations):
			if random.random() < self.crossover_rate: # Should we do crossover in this population?
				# Pick two individuals:
				individual_1 = random.randrange(0, len(self.population[i]))
				individual_2 = individual_1
				while individual_1 == individual_2:
					individual_2 = random.randrange(0, len(self.population[i]))

				# Pick the crossover points (2-point crossover)
				crossover_point_1 = random.randrange(0, self.number_genes)
				while crossover_point_1 < (self.number_genes - 2):
					crossover_point_1 = random.randrange(0, self.number_genes)

				crossover_point_2 = crossover_point_1
				while crossover_point_2 < crossover_point_1:
					crossover_point_2 = random.randrange(0, self.number_genes)

				# Do the cross over
				for ii in range(self.number_genes):
					if ii >= crossover_point_1 and ii <= crossover_point_2:
						tempvalue = self.population[i][individual_1][ii]

						self.population[i][individual_1][ii] = self.population[i][individual_2][ii]
						self.population[i][individual_2][ii] = tempvalue






		
		