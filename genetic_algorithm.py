import random
from population import Population
from fitness import Fitness
from chromosome import Chromosome


class GA:
    uniform_rate = 0.5
    mutation_rate = 0.001
    tournament_size = 5
    elitism = True
    stagnant_generations_limit = 50

    @staticmethod
    def evolve_population(pop):
        new_population = Population(pop.size(), initialise=False)

        elitism_offset = 1 if GA.elitism else 0
        if GA.elitism:
            new_population.save_chromosome(0, pop.get_fittest())

        for i in range(elitism_offset, pop.size()):
            indiv1 = GA.tournament_selection(pop)
            indiv2 = GA.tournament_selection(pop)
            new_indiv = GA.crossover(indiv1, indiv2)
            new_population.save_chromosome(i, new_indiv)

        for i in range(elitism_offset, new_population.size()):
            GA.mutate(new_population.get_chromosome(i))

        return new_population

    @staticmethod
    def crossover(indiv1, indiv2):
        new_sol = Chromosome()
        for i in range(indiv1.size()):
            if random.random() <= GA.uniform_rate:
                new_sol.set_gene(i, indiv1.get_gene(i))
            else:
                new_sol.set_gene(i, indiv2.get_gene(i))
        return new_sol

    @staticmethod
    def mutate(indiv):
        for i in range(indiv.size()):
            if random.random() <= GA.mutation_rate:
                gene = random.randint(0, 1)
                indiv.set_gene(i, gene)

    @staticmethod
    def tournament_selection(pop):
        tournament = Population(GA.tournament_size, initialise=False)
        for i in range(GA.tournament_size):
            random_id = random.randint(0, pop.size() - 1)
            tournament.save_chromosome(i, pop.get_chromosome(random_id))
        return tournament.get_fittest()


if __name__ == "__main__":
    target_number = 7
    Fitness.set_solution(target_number)

    my_pop = Population(100, True)
    generation_count = 0
    previous_fittest = my_pop.get_fittest().get_fitness()
    stagnant_generations = 0

    while my_pop.get_fittest().get_fitness() < Fitness.get_max_fitness():
        generation_count += 1
        fittest_value = Fitness.chromosome_to_float(my_pop.get_fittest())
        current_fittest = my_pop.get_fittest().get_fitness()

        print(f"Generation: {generation_count} Fittest value: {
              fittest_value} Fitness: {current_fittest}")

        if abs(current_fittest - previous_fittest) < 1e-6:
            stagnant_generations += 1
        else:
            stagnant_generations = 0
        previous_fittest = current_fittest

        if stagnant_generations >= GA.stagnant_generations_limit:
            print("No significant improvement, stopping early due to stagnation.")
            break

        if my_pop.get_fittest().get_fitness() >= 0.999999:
            break

        my_pop = GA.evolve_population(my_pop)

    print("Solution found!")
    print(f"Generation: {generation_count}")
    print("Approximate square root:")
    print(Fitness.chromosome_to_float(my_pop.get_fittest()))
