#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os

os.system('clear')
ga = pyga.pyga(1, 3, 5, 0, 0.50)
ga.print_populations()
ga.mutate()
ga.crossover()
ga.print_populations()