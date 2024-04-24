from dragon import Dragon

class IceDragon(Dragon):

    """
    class IceDragon is derived from Dragon(Cow). Returns false through 
    static method can_breathe_fire
    """
    def __init__(self,name,image):
        self.name = name
        self.image = image

    @staticmethod
    def can_breathe_fire():
        return False