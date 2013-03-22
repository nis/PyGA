#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os

datafolder = '/Users/tamen/Documents/Archive/Skole/SDU/8. Semester/AI2/Code/Ludo/data/'

os.system('clear')
ga = pyga.pyga()
ga.import_setup(datafolder)
# ga = pyga.pyga(10, 100, 5, 0.02)
# ga.export_setup(datafolder)
# for i in range(5):
# 	ga.export_to_file(datafolder)
# 	ga.run(1)