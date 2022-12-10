class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus, initial_infected):
        log = open(self.file_name, "w")

        log.write(f"""
Initial population size: {pop_size}.
Percentage vaccinated: {vacc_percentage}.
Virus name: {virus.name}.
Reproduction rate: {virus.repro_rate}.
Virus mortality rate: {virus.mortality_rate}.
Initial infected: {initial_infected}.
""")
        log.close()

    def log_interactions(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections):
        log = open(self.file_name, "a")
        to_file = f"""
Step: {step_number}
Total interactions: {number_of_interactions} 
Total people dead: {dead_people}
Total vaccinated: {total_vaccinated}
Current infections: {total_infections}
"""
        log.write(to_file)
        log.close()

    def final_log(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections, virus, pop_size, initial_infected, vacc_percentage, vaccine_saves):
        log = open("answers.txt", "w")
        log.write(f"""
The final report is:

What were the inputs you gave the simulation? (Population size, percent vaccinated, virus name, mortality rate, reproductive rate)
The initial population size was: {pop_size}.
Vaccinated percentage was: {round(vacc_percentage * 100)}%.
Name of the virus: {virus.name}.
The mortality rate was: {virus.mortality_rate}.
The reproductive rate of this virus was: {virus.repro_rate}.
Total initial infected: {initial_infected}.

What percentage of the population died from the virus?
{round(pop_size / dead_people)}%

What percentage of the population became infected at some point before the virus burned out?
{round(total_infections / pop_size * 100)}%

Out of all interactions sick individuals had during the entire simulation, how many times, in total, did a vaccination save someone from potentially becoming infected?
Total times someone was saved: {vaccine_saves}

Total steps: {step_number}
Total interactions: {number_of_interactions} 
Total people dead: {dead_people}
Total vaccinated: {total_vaccinated}
Total infections: {total_infections}
""")
        log.close()