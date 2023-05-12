class Person:
    '''A base class to define Person properties.'''
    def __init__(self, name):
        self.name = name

    def sepak(self, msg = '(Calling the Base Class)'):
        print(self.name, msg)