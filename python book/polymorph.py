from duck import * 
from mouse import *

def describe(object):
    object.talk()
    object.talk()

donald = Duck()
mickey = Mouse()

describe(donald)
describe(mickey)