import random
from virus import Virus

class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection


    def did_survive_infection(self):
        if self.infection:
            random_survival_rate = random.random()
            if random_survival_rate > self.infection.mortality_rate:
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
                return True
            else:
                self.is_alive = False
                return False
            
        return self.is_alive


if __name__ == "__main__":
    virus = Virus("Dysentery", 0.7, 0.2)

    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    infected_person = Person(3, False, infection = virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    people = []
    for i in range(1, 101):
        people.append(Person(i, False, infection = virus))

    for person in people:
        if person.did_survive_infection():
            assert person.is_alive
            assert person.is_vaccinated
            assert not person.infection
        else:
            assert not person.is_alive
            assert not person.is_vaccinated
            assert person.infection