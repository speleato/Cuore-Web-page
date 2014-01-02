__author__ = 'Kirby'
class Department(object):
    def __init__(self, name=None):
        self.name=name

    def __str__(self):
        return self.name
