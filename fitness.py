class Fitness:
    target_value = 0.0

    @staticmethod
    def set_solution(target):
        Fitness.target_value = target

    @staticmethod
    def get_fitness(chromosome):
        value = Fitness.chromosome_to_float(chromosome)
        return 1 / (abs(value**2 - Fitness.target_value) + 1)

    @staticmethod
    def chromosome_to_float(chromosome):
        binary_str = ''.join(map(str, chromosome.genes))
        max_value = 100.0
        int_value = int(binary_str, 2)
        return (int_value / (2**len(chromosome.genes) - 1)) * max_value

    @staticmethod
    def get_max_fitness():
        return 1.0
