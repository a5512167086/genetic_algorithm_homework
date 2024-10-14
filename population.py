from chromosome import Chromosome


class Population:
    def __init__(self, population_size, initialise=True):
        self.chromosomes = [None] * population_size

        if initialise:
            for i in range(self.size()):
                new_chromosome = Chromosome()
                new_chromosome.generate_chromosome()
                self.save_chromosome(i, new_chromosome)

    def get_chromosome(self, index):
        return self.chromosomes[index]

    def get_fittest(self):
        fittest = self.chromosomes[0]
        for i in range(self.size()):
            if fittest.get_fitness() <= self.get_chromosome(i).get_fitness():
                fittest = self.get_chromosome(i)
        return fittest

    def size(self):
        return len(self.chromosomes)

    def save_chromosome(self, index, chrom):
        self.chromosomes[index] = chrom
