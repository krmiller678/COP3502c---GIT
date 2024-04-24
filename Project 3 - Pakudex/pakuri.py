class Pakuri:
    def __init__(self, species):
        """attack, defense and speed attributes are defined based on the species attribute retrieved from call"""
        self.species = species
        self.attack = (len(species)*7) + 9
        self.defense = (len(species)*5) + 17
        self.speed = (len(species)*6) + 13

    #getters and setters
    #getters: retrieve the value of a species, return something

    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed
    
    #setters: set the value of a specific attribute, do not return anything, simply update
    def set_attack(self, new_attack):
        self.attack = new_attack

    #updates variables
    def evolve(self):
        self.attack = self.attack*2
        self.defense = self.defense*4
        self.speed = self.speed*3

    # Might be a good option to sort with a less than function using the operator overload method
    def __lt__(self,other):
        """When looking at left operand, if it is of class Pakuri implement less than based on species name"""
        if self.species.upper() < other.species.upper():
            return True
        else:
            return False
