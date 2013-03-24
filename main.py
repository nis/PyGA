#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import pyga
import os
import time
import sys
import getopt

def java_semaphor(path):
	if os.path.exists(path):
		os.remove(path)
		return True
	else:
		return False

def set_ga_semaphor(path):
	open(path, 'w').close() 

def start_ga(populations, individuals, genes, mutationrate, datafolder, generations_path, semaphor_path, result_path, ga_semaphor_file):

	# setup the folders
	if not os.path.exists(datafolder):
		os.makedirs(datafolder)
	else:
		print 'Directory exists:', datafolder
		print 'Are you sure you want to initialize a GA here?'
		sys.exit()

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

def main2(argv):
	datafolder = 'data/'
	
	max_generations = 100000
	populations = 1
	individuals = 5
	genes = 3
	mutation_rate = 0.02
	
	initialize_ga = False

	try:
		opts, args = getopt.getopt(argv,"hid:p:u:g:m:", [])
	except getopt.GetoptError:
		print 'main.py -i <true/false> -d <datadir> -p <populations> -u <individuals> -g <genes> -m <mutationrate>'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-i':
			initialize_ga = True
		elif opt == '-d':
			datafolder = arg
		elif opt == '-p':
			populations = int(arg)
		elif opt == '-u':
			individuals = int(arg)
		elif opt == '-g':
			genes = int(arg)
		elif opt == '-m':
			mutation_rate = float(arg)

	generations_path = datafolder + 'generations/'
	semaphor_path = datafolder + 'semaphors/'
	result_path = datafolder + 'results/'
	java_semaphor_file = semaphor_path + 'JAVAKlar.sem'
	ga_semaphor_file = semaphor_path + 'GAKlar.sem'
	setup_file = datafolder + 'setup.txt'

	os.system('clear')
	
	if initialize_ga:
		ga = start_ga(populations, individuals, genes, mutation_rate, datafolder, generations_path, semaphor_path, result_path, ga_semaphor_file)
		print 'GA initialized.'
		sys.exit()
	
	
	for i in range(max_generations):
		while not java_semaphor(java_semaphor_file):
			time.sleep(0.1)
	
		print 'Generation', i
		ga = pyga.pyga()
		ga.import_folder(setup_file, result_path)
		ga.run(1)
		ga.export_to_file(datafolder)
		set_ga_semaphor(ga_semaphor_file)

if __name__ == "__main__":
	main2(sys.argv[1:])
	