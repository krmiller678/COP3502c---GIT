from pakuri import Pakuri

class Pakudex:
    """
    Contains all of the pakuri instances and sets capacity limits. This program is Class in pakuri_program
    """
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.pakuris = [] #stores a list of pakuri objects
        self.size = 0 #keeps track of the concrete pakuri objects in the list

    def get_size(self):
        return self.size
    
    def get_capacity(self):
        return self.capacity
    
    def get_species_array(self):
        species_list = []
        for species in self.pakuris:
            species_list.append(species.species)            
        if species_list == []:
            return None
        return species_list
    
    def get_stats(self, species):
        for names in self.pakuris:
            if names.species == species:
                return [names.attack, names.defense, names.speed]
        return None
    
    def sort_pakuri(self):
        sorted_list = self.get_species_array()
        if sorted_list == None:
            pass
        else:
            sorted_list.sort()
            copy_of_pakuris = self.pakuris[:]
            counter = 0
            for names in sorted_list:
                for species in copy_of_pakuris:
                    if species.species == names:
                        self.pakuris[counter] = species
                        counter += 1
                        break
        

    #species vs. pakuri object
    def add_pakuri(self,species):
        # 1. Check duplicates => Return False if exists in list
        # loop through self.pakuris to see if pakuri.species == species
        if self.get_species_array() == None:
            pass
        elif species in self.get_species_array():
            return False
        # 2. If self.size = self.capacity, list is full False
        if self.size >= self.capacity:
            return False
        
        self.pakuris.append(Pakuri(species))
        #increment self.size
        self.size += 1
        #Return true
        return True

    def evolve_species(self,species):
        for names in self.pakuris:
            if names.species == species:
                names.evolve()
                return True
        return False