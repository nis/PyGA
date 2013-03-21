#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os

os.system('clear')
ga = pyga.pyga(1, 100, 5, 0.02, 10000)
ga.run()