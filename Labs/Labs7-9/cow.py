class Cow:
    """
    Class Cow - Sets up instances with cow name and default image set to None

    """

    def __init__(self,name):
        self.name = name
        self.image = None


    def get_name(self):
        #getter - returns the name attribute of the instance
        return self.name


    def get_image(self):
        #getter - returns the image attribute of the instance
        return self.image


    def set_image(self,image):
        #setter - update the image attribute of the instance
        self.image = image