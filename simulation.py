import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected

        self.newly_infected_list = []
        self.dead_people_list = []

        self.time_step_counter = 0
        self.current_infected = 0
        self.total_infected = 0
        self.vaccinated_counter = 0
        self.total_vaccinated = 0
        self.total_dead = 0
        self.total_interactions = 0
        self.total_lives_saved_with_vaccine = 0

        self.logger = Logger(f"{virus.name}-logger.txt")
        self.population = self._create_population()


    def _create_population(self):
        """
        creates population based on population data
        """
        population_list = []

        poplulation_vaccinated = self.pop_size * self.vacc_percentage
        poplulation_vaccinated = int(poplulation_vaccinated)
        self.current_vaccinated = poplulation_vaccinated

        population_unvaccinated = self.pop_size - self.initial_infected - poplulation_vaccinated

        population_infected = self.initial_infected

        id_count = 0

        # creates vaccinated population
        for _ in range(poplulation_vaccinated):
            id_count += 1
            self.vaccinated_counter += 1
            person = Person(id_count, True, None)
            population_list.append(person)

        # creates unvaccinated population
        for _ in range(population_unvaccinated):
            id_count += 1
            person = Person(id_count, False, None)
            population_list.append(person)

        # creates infected population
        for _ in range(population_infected):
            id_count += 1
            self.current_infected += 1
            self.total_infected += 1
            person = Person(id_count, False, self.virus)
            population_list.append(person)

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus, self.initial_infected)
        return population_list


    def _simulation_should_continue(self):
        """
        checks to see if the simulation should continue or not
        """
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False
            

    def run(self, virus):
        """
        starts the simulation and contains the main while loop
        """
        
        should_continue = True

        while should_continue:
            self.time_step()
            should_continue = self._simulation_should_continue()
            self.time_step_counter += 1
            self.logger.log_interactions(self.time_step_counter, self.total_interactions, self.total_dead, self.total_vaccinated, self.current_infected)

            if not should_continue:
                self.logger.answers_log(self.time_step_counter, self.total_interactions, self.total_dead, self.total_vaccinated, self.total_infected, virus, self.pop_size, self.initial_infected, self.vacc_percentage, self.total_lives_saved_with_vaccine)

        print(f"Time steps: {self.time_step_counter}")
        print(self.time_step_counter, self.total_interactions, self.total_dead, self.total_vaccinated, self.current_infected)    


    def random_person_grabber(self):
        """
        grabs random person from population and returns them if they're still alive
        """
        random_person_grab = random.choice(self.population)
        while not random_person_grab.is_alive and not random_person_grab.is_vaccinated and random_person_grab is None:
            random_person_grab = random.choice(self.population)
        return random_person_grab


    def time_step(self):
        """
        one infected person interacts with 100 random alive people
        """
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):
                    self.interaction(person, self.random_person_grabber())

                if person.did_survive_infection() == True:
                    self.current_infected -= 1
                    person.is_vaccinated = True
                    self.total_vaccinated += 1

                else:
                    person.is_alive = False
                    self.total_dead += 1
                    self.current_infected -= 1

        self._infect_newly_infected()


    def interaction(self, infected_person, random_person):
        """
        one infected person interacts with 100 random alive people
        """
        self.total_interactions += 1

        if random_person.is_vaccinated == True:
            self.total_lives_saved_with_vaccine += 1
        elif random_person.is_vaccinated == False and random_person.infection == None and random_person.is_alive == True:
            if random.random() < self.virus.repro_rate: # random num is chance of infection
                self.newly_infected_list.append(random_person)
                self.population.remove(random_person)

    def _infect_newly_infected(self):
        """
        infects everyone in list then clears list
        """
        for person in self.newly_infected_list:
            person.infection = self.virus
            self.current_infected += 1
            self.total_infected += 1
            self.population.append(person)

        self.newly_infected_list = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.4
    mortality_rate = 0.3

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.2
    initial_infected = 10

    # Make a new instance of the simulation
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run(virus)
    
