class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    covid = Virus("Covid", 0.6, 0.2)
    assert covid.name == "Covid"
    assert covid.repro_rate == 0.6
    assert covid.mortality_rate == 0.2

    ebola = Virus("Ebola", 0.4, 0.9)
    assert ebola.name == "Ebola"
    assert ebola.repro_rate == 0.4
    assert ebola.mortality_rate == 0.9