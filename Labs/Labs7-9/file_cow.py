"""
This class is derived from the cow class - it takes a file from the cows folder and
assigns it to a cow class
"""
from cow import Cow

class FileCow(Cow):

    def __init__(self, name, filename):
        self.name = name
        try:
            file = open(filename)
            lines = file.readlines()
            self.image = ''.join(line for line in lines)
        except RuntimeError:
            print('MOOOOO!!!!!!')
        finally:
            file.close

    def set_image(self,image):
        raise RuntimeError('Cannot reset FileCow Image')