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

        self.logger = Logger("test-logger.txt")
        self.population = self._create_population()
        self.newly_infected_list = []
        self.dead_people_list = []

        self.total_vaccinated = 0
        self.total_infected = 0
        self.total_dead = 0
        self.total_interactions = 0
        self.total_lives_saved_with_vaccine = 0

    def _create_population(self):
        """
        creates population based on population data
        """
        population_list = []

        for i in range(self.pop_size):
            population_list.append(Person(i, False))

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, virus.name, mortality_rate, repro_num)
        return population_list

    def _simulation_should_continue(self):
        """
        checks to see if the simulation should continue or not
        """
        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False:
                return True
            else:
                return False
            

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        time_step_counter = 0
        should_continue = True

        while should_continue:
            self.time_step()
            should_continue = self._simulation_should_continue()
            time_step_counter += 1

            # TODO: Increment the time_step_counter
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
        print(f"Time steps: {time_step_counter}")

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def random_person_grabber(self):
        random_person_grab = random.choice(self.population)
        while random_person_grab.is_alive == False:
            random_person_grab = random.choice(self.population)
        return random_person_grab


    def time_step(self):
        for person in self.population:
            if person.infection is not None and person.is_alive == True:
                for _ in range(100):
                    self.interaction(person, self.random_person_grabber())

                if person.did_survive_infection() == True:
                    person.is_vaccinated = True
                    person.infection = None
                    self.total_infected -= 1
                    self.total_vaccinated += 1

                    self.logger.log_infection_survival(person, True)
                else:
                    person.is_alive = False
                    self.total_dead += 1
                    self.total_vaccinated += 1
                    self.total_dead -= 1

                    self.logger.log_infection_survival(person, False)

        self.logger.log_time_step() # finish later
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        self.total_interactions += 1

        if random_person.is_vaccinated == True:
            self.total_lives_saved_with_vaccine += 1
        elif random_person.is_vaccinated == False and random_person.infection == None:
            if random.random() < virus.repro_rate: # random num is chance of infection
                self.newly_infected_list.append(random_person)

    def _infect_newly_infected(self):
        """
        infects everyone in list then clears list
        """
        for person in self.newly_infected_list:
            person.infection = self.virus
            self.total_infected += 1

        self.newly_infected_list = []


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    # sim.run()
