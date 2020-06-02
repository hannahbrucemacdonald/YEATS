import yaml 
import sys
import itertools
import os

def run_relative_perturbation(ligA, ligB,tidy=True):
    print('Starting relative calcluation of ligand {} to {}'.format(ligA,ligB))
    trajectory_directory = 'lig{}to{}'.format(ligA,ligB) 
    new_yaml = 'vanilla_{}to{}.yaml'.format(ligA,ligB) 
    
    # rewrite yaml file
    with open('setup.yaml', "r") as yaml_file:
        options = yaml.load(yaml_file)
    options['old_ligand_index'] = ligA
    options['new_ligand_index'] = ligB
    options['trajectory_directory'] = trajectory_directory
    with open(new_yaml, 'w') as outfile:
        yaml.dump(options, outfile)
    
    # run the simulation
    os.system('python ~/software/perses/perses/app/setup_relative_calculation.py {}'.format(new_yaml))

    print('Relative calcluation of ligand {} to {} complete'.format(ligA,ligB))

    if tidy:
        os.remove(new_yaml)

    return

# work out which ligand pair to run
ligand_pairs = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
ligand1, ligand2 = ligand_pairs[int(sys.argv[1])-1] # jobarray starts at 1 

#running forwards
run_relative_perturbation(ligand2, ligand1)
