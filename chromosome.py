import random
from fitness import Fitness


class Chromosome:
    default_gene_length = 256

    def __init__(self):
        self.genes = [0] * Chromosome.default_gene_length
        self.fitness = 0

    def generate_chromosome(self):
        for i in range(self.size()):
            gene = random.randint(0, 1)
            self.genes[i] = gene

    def get_gene(self, index):
        return self.genes[index]

    def set_gene(self, index, value):
        self.genes[index] = value
        self.fitness = 0

    def size(self):
        return len(self.genes)

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = Fitness.get_fitness(self)
        return self.fitness

    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)
