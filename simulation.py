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

        self.total_infected = 0
        self.total_dead = 0

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

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for people in self.people_list():
            people.interaction()
            people._infect_newly_infected()

        # RUN LOGGER HERE

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        if random_person.is_vaccinated == True:
            ...
        elif random_person.infection == True:
            ...
        elif random_person.is_vaccinated == False:
            # todo later
            ...
            

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
