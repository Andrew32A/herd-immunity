from person import Person

class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, virus_name, pop_size, vacc_percentage, mortality_rate,
                       basic_repro_num):
        log = open(self.file_name, "w")

        log.write("Welcome to herd immunity simulator!\n")
        log.write(f"Initial population size: {pop_size}\n")
        log.write(f"Percentage vaccinated {vacc_percentage}\n")
        # log.write(f"Initially infected: {basic_repro_num}\n")
        log.write(f"Virus name: {virus_name}\n")
        log.write(f"Reproduction rate {basic_repro_num}\n")
        log.write(f"Virus mortality rate: {mortality_rate}\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        pass

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):
        # 
        pass