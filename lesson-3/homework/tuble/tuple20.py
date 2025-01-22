#Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
from collections import namedtuple
Adam = ('Dad', 42, 'tall', 'asian')
Eyla = ('Mom', 36, 'tall', 'iranian')
Family = namedtuple("Family", ['x', 'y'])