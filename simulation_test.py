from simulation import Simulation
from virus import Virus

# virus properties
virus_name = "test-virus"
repro_num = 0.6
mortality_rate = 0.2

# sim properties
pop_size = 1000
vacc_percentage = 0.2
initial_infected = 10

# object instantiation
virus = Virus(virus_name, repro_num, mortality_rate)
sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

# test what we expect
assert sim.pop_size == 1000
assert sim.total_dead == 0
assert sim.total_infected == 10
assert sim.initial_infected == 10

sim.run(virus)

# test that the sim changes our values
assert sim.pop_size == 1000
assert sim.total_dead != 0
assert sim.total_infected != 10
assert sim.initial_infected == 10

sim.run(virus)
    

