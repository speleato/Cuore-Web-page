__author__ = 'Kirby'
class Title(object):
    def __init__(self, name=None):
        self.name=name
        #self.permissions=permissions

    def __str__(self):
        return self.name
