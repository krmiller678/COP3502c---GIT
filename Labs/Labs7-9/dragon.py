from cow import Cow

class Dragon(Cow):
    """
    Class dragon is derived from class cow and extends the program
    to include function for breathe_fire
    """
    def __init__(self, name, image):
        self.name = name
        self.image = image

    @staticmethod
    def can_breathe_fire():
        return True