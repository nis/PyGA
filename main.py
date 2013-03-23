#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os

datafolder = 'data/'

os.system('clear')
ga = pyga.pyga()
ga.import_folder(datafolder)
ga.print_populations()
ga.run(1)
ga.print_populations()
# ga.export_to_file(datafolder)
# ga = pyga.pyga(1, 5, 3, 0.02)
# ga.export_setup(datafolder)
# for i in range(5):
# 	ga.export_to_file(datafolder)
# 	ga.run(1)

# ga.export_setup(datafolder)