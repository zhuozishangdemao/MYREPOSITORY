from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
map((lambda x : x.upper()),countries)
filter((lambda coun : 'land' in coun),countries)
reduce((lambda x , y:x+y),countries)
import json
from . import countries_data