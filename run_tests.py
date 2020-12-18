import json
import os
import subprocess
from subprocess import run

import argparse

global args

def get_arguments():
    parser = argparse.ArgumentParser(description='Script to run tests of a salesforce app code')

    parser.add_argument("-cn", "--classes-names", dest = "classes_names", default = "", help="A list, separated with commas, of the test classes names")
    parser.add_argument("-wf", "--workspace-folder", dest = "workspace_folder", default = "", required=True, help="The workspace path to the folder of the project")
    parser.add_argument("-s", "--synchronous", dest = "synchronous", type = bool, default = False, help="If the test 'll be run in synchronous mode")
    
    global args
    args = parser.parse_args()

def run_command(command, shell=False):
    try:
        result_command = run(command, universal_newlines=True, shell=shell)
        print(result_command)
    except KeyboardInterrupt as err:
        print('\nCOMANDO CANCELADO')
    except:
        print('ERRO AO EXECUTAR COMANDO')

def run_all_tests():
    command = ['sfdx','force:apex:test:run', '--codecoverage', '--resultformat', 'human', '--wait', '2']
    if args.synchronous:
        command.append('--synchronous')

    print(command)

def run_classes_tests():
    command = ['sfdx', 'force:apex:test:run', '--codecoverage', '--resultformat', 'human']
    
    if args.synchronous:
        command.append('--synchronous')
    
    command.append('--classnames')

    classes_names = args.classes_names.split(',')

    for class_name in classes_names:
        command.append(class_name)
    
    print(command)

def main():
    get_arguments()

    if not args.classes_names:
        run_all_tests()
    else:
        run_classes_tests()
   
    print('SCRIPT EXECUTADO')

if __name__ == "__main__":
    main()