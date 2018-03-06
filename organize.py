#########

# written by Rohan Gupta

########

import sys
import os
import json
import argparse


class ClutterManager:

    """Manages home directory, destination directory and file extensions.

    Public mathods:
    __init__ -- constructor
    updateHome -- update home directory
    updateDestination -- update destination directory
    addExtensions -- adds extension to extension list
    delExtensions -- removes extension from extension list
    clutterRemover - organizes files based on their extension 

    """

    def __init__(self, home, destination, extensions):
        """Constructor. Assigns default values to object attributes."""
        
        self.home = dictionary['home']
        self.destination = dictionary['destination']
        self.extensions = dictionary['extensions']

    def updateHome(self, path):
        """Updates home directory."""
        
        dictionary['home'] = path
        return

    def updateDestination(self, path):
        """Updates destination directory."""

        dictionary['destination'] = path
        return

    def addExtensions(self, extension):
        """Adds an extension to the extension list."""
        
        if extension not in dictionary['extensions']:
            dictionary['extensions'].append(extension)
        else:
            print('error: argument already exists')
        return

    def delExtensions(self, extension):
        """Removes an extension from the extension list."""
        
        if extension not in dictionary['extensions']:
            print('error: argument does not exist')
        else:
            dictionary['extensions'].remove(extension)
        return

    def clutterRemover(self):
        """Organizes files based on their extension."""
        
        self.home = dictionary['home']
        self.destination = dictionary['destination']
        self.extensions = dictionary['extensions']

        for file in os.listdir(self.home):
            oldpath = self.home + '/' + file
            for ext in self.extensions:
                if file.endswith(ext):
                    newpath = self.destination + '/' + ext[1:].upper()
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    os.rename(oldpath, newpath + '/' + file)
        return


"""Loads the config file."""

try:
    with open('config_for_organize.txt') as input_file:
        dictionary = json.load(input_file)
except IOError:
    print('An error occured trying to read the config file')
    exit()

"""Creates an instance of class ClutterManager."""

clutter_manager_obj = ClutterManager(
    dictionary['home'], 
    dictionary['destination'], 
    dictionary['extensions'],
)

"""Command Line Interface."""

parser = argparse.ArgumentParser()

parser.add_argument(
    "--updateHome",
    help="updates home directory", 
    dest="home_path",
)
parser.add_argument(
    "--updateDest",
    dest="destination_path", 
    help="updates destination directory",
)
parser.add_argument(
    "--addExtension",
    dest="ext_add", 
    help="Adds extension",
)
parser.add_argument(
    "--delExtension",
    dest="ext_rem", 
    help="Removes extension",
)
parser.add_argument(
    "--removeClutter", 
    help="Removes clutter",
    action="store_true", 
    dest="remove_clutter",
)

args = parser.parse_args()

if args.home_path:
    clutter_manager_obj.updateHome(args.home_path)
if args.destination_path:
    clutter_manager_obj.updateDestination(args.destination_path)
if args.ext_add:
    clutter_manager_obj.addExtensions(args.ext_add)
if args.ext_rem:
    clutter_manager_obj.delExtensions(args.ext_rem)
if args.remove_clutter:
    clutter_manager_obj.clutterRemover()

"""No argument encountered."""

if len(sys.argv) == 1:
    print('Type "-h" for help')

"""Reflect the changes in config file."""

try:
    with open('config_for_organize.txt', 'w') as output_file:
        json.dump(dictionary, output_file)
except IOError:
    print('An error occured trying to read the config file')
    exit()
