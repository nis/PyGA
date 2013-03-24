#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os
import time

datafolder = 'data2/'
generations_path = datafolder + 'generations/'
semaphor_path = datafolder + 'semaphors/'
result_path = datafolder + 'results/'
java_semaphor_file = semaphor_path + 'JAVAKlar.sem'
ga_semaphor_file = semaphor_path + 'GAKlar.sem'
setup_file = datafolder + 'setup.txt'

max_generations = 100000
populations = 1
individuals = 5
genes = 3

initialize_ga = True

def java_semaphor(path):
	if os.path.exists(path):
		os.remove(path)
		return True
	else:
		return False

def set_ga_semaphor(path):
	open(path, 'w').close() 

def start_ga(populations, individuals, genes, mutationrate):
	global datafolder
	global generations_path
	global semaphor_path
	global ga_semaphor_file
	global result_path

	# setup the folders
	if not os.path.exists(datafolder):
		os.makedirs(datafolder)

	if not os.path.exists(generations_path):
		os.makedirs(generations_path)

	if not os.path.exists(semaphor_path):
		os.makedirs(semaphor_path)

	if not os.path.exists(result_path):
		os.makedirs(result_path)

	ga = pyga.pyga(populations, individuals, genes, mutationrate)
	ga.export_setup(datafolder)
	ga.export_to_file(datafolder)
	set_ga_semaphor(ga_semaphor_file)
	return ga



os.system('clear')

if initialize_ga:
	ga = start_ga(1, 5, 3, 0.02)
	print 'GA initialized.'


for i in range(max_generations):
	while not java_semaphor(java_semaphor_file):
		time.sleep(0.1)

	print 'Generation', i
	ga = pyga.pyga()
	ga.import_folder(setup_file, result_path)
	ga.run(1)
	ga.export_to_file(datafolder)
	set_ga_semaphor(ga_semaphor_file)
	