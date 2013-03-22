#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os

datafolder = '/Users/tamen/Documents/Archive/Skole/SDU/8. Semester/AI2/Code/Ludo/data/'

os.system('clear')
ga = pyga.pyga(10, 100, 5, 0.02)
generation, data = ga.export()
print generation
ga.run(1)
generation, data = ga.export()
print generation