def initialize_KyleStats():    

    class KyleStats:
        """A class with info on Kyle"""
        age = 18
        def __init__(self, weight = 140, height = 180):
            self.bday = "April 18th, 1996"
            self.height = height
            self.weight = weight

        def functionjunction(self):
            KyleStats.age = 27

        def create_contact_dict(self):
            self.contactinfo = {
                "Number" : "123-456-7890",
                "Email" : "krmiller678@gmail.com",
            }

    Kyle = KyleStats(180)
    print(Kyle.bday)
    print(Kyle.age)
    print(KyleStats.age)
    Kyle.functionjunction()
    print(Kyle.age)
    print(KyleStats.age)
    Kyle2 = KyleStats()
    print(Kyle2.age)
    print(Kyle.weight)
    print(Kyle2.weight)
    Kyle.create_contact_dict()
    print(Kyle.contactinfo)
    number = int(Kyle.contactinfo["Number"].replace("-",""))
    print(number)

    KyleStats.new = 123
    print(KyleStats.new)
    print(Kyle.new)

    Kyle3 = KyleStats(height = 6, weight = 40)
    print(Kyle3.weight, Kyle3.height)

if __name__ == "__main__":
    initialize_KyleStats()
    