import json
import os
import subprocess
from subprocess import run

import argparse

global args

def get_arguments():
    parser = argparse.ArgumentParser(description='Script to config a scratch org of salesforce')

    parser.add_argument("-sa", "--scratch-alias", dest = "scratch_alias", required=True, help="The scratch org's alias")
    parser.add_argument("-dd", "----duration-days", dest = "duration_days", type=int, default=7, help="The days duratation of scratch org")
    parser.add_argument("-wf", "--workspace-folder", dest = "workspace_folder", default = "", required=True, help="The workspace path to the folder of the project")
    
    global args
    args = parser.parse_args()

def run_command(command, shell=False):
    try:
        print('Executing command: ' + ' '.join(command))
        result_command = run(command, universal_newlines=True, shell=shell)
        return result_command
    except KeyboardInterrupt as err:
        print('COMMAND ERROR! EXITING SCRIPT')
        quit()

def connect_to_devhub():
    command = ['sfdx', 'force:auth:web:login', '--setdefaultdevhubusername', '--setalias', 'DevHub']
    
    run_command(command)
    

def create_scratch_org():
    command = ['sfdx', 'force:org:create', '-f', args.workspace_folder + '/config/project-scratch-def.json', '--setalias',
                args.scratch_alias, '--durationdays', str(args.duration_days), '--setdefaultusername', '--json', '--loglevel', 'fatal']
    
    run_command(command)

def install_dependencies():
    dependencies = get_dependencies()
    
    command = ['sfdx', 'force:package:install', '-u', args.scratch_alias]

    for dependency in dependencies:
        command.append('--package')
        command.append(dependency)
    
    run_command(command)
    

def get_dependencies():
    json_file = read_file(args.workspace_folder + '/environments.json')  
    json_object = json.loads(json_file)

    dependencies = []

    for dependency in json_object["development"]["dependencies"]:
        dependencies.append(dependency["id"])
    
    return dependencies

def read_file(dir_path):
    try:
        f = open(dir_path)
        file = f.read()
        f.close()
        return file
    except:
        print('Erro ao abrir arquivo ' + dir_path)
        return None

def push_code():
    command = ['sfdx', 'force:source:push', '-u', args.scratch_alias]

    run_command(command)

def open_scratch_org():
    command = ['sfdx', 'force:org:open', '-u', args.scratch_alias]

    run_command(command)

def main():
    get_arguments()

    connect_to_devhub()

    create_scratch_org()

    install_dependencies()

    push_code()

    open_scratch_org()
    
    print('END OF SCRIPT')

if __name__ == "__main__":
    main()