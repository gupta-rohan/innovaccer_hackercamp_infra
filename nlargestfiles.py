#########

# written by Rohan Gupta

########

import heapq
import os
import sys
import operator
import json
import argparse

class Nlargest:
    """Finds out the largest n numbers.

    Public methods:
    __init__ -- constructor
    updateNfiles -- updates number of files
    updateHome -- updates home directory
    addPrefix -- adds a prefix to be omitted
    delPrefix -- removes a prefix to be omitted
    fileTraversal -- recursive traversal of directory
    printFunction -- prints the largest n files
    largestFiles -- finds out the n largest files

    """

    def __init__(self, nfiles, home, _exclude_prefix):
        """Constructor. Assigns default values to nlargest_object attributes."""

        self.nfiles = dictionary['nfiles']
        self.home = dictionary['home']
        self._exclude_prefix = dictionary['_exclude_prefix']

    def updateNfiles(self, n):
        """Updates number of files to be list."""

        if n <= 0:
            print('error: insufficient number: largest cannot be found')
        else:
            dictionary['nfiles'] = n
        return

    def updateHome(self, path):
        """Updates home directory."""

        dictionary['home'] = path
        return

    def addPrefix(self, prefix):
        """Adds a prefix to be omitted."""
        
        if prefix not in dictionary['_exclude_prefix']:
            dictionary['_exclude_prefix'].append(prefix)
        else:
            print('error: prefix already exists')
        return

    def delPrefix(self, prefix):
        """Removes a prefix to be omitted."""

        if prefix not in dictionary['_exclude_prefix']:
            print('error: prefix does not exist')
        else:
            dictionary['_exclude_prefix'].remove(prefix)
        return

    def fileTraversal(self, path):
        """Recursive traveral of directory."""
        """Return : Path of file, size of file in MB."""

        for dirpath, dirname, filename in os.walk(path):
            #Remove files starting with _exclude_prefixes
            dirname[:] = [d for d in dirname if not d[0]
                          in dictionary['_exclude_prefix']]
            filename[:] = [f for f in filename if not f[0]
                           in dictionary['_exclude_prefix']]
            for name in filename:
                full_path = os.path.join(dirpath, name)
                yield full_path, (os.path.getsize(full_path) 
                    / (1024.0*1024.0)
                )

    def printFunction(self, largest_files):
        """Prints the largest n files."""

        print('The {L} largest files are :'.format(L=len(largest_files)))
        for ii in range(len(largest_files)):
            print('{index}. {path} -> {size:.2f} MB'.format(
                index=ii + 1, 
                path=largest_files[ii][0].encode('utf-8'), 
                size=largest_files[ii][1],
            )
        )
        return

    def largestFiles(self):
        """Evaluates largest n files."""

        self.nfiles = dictionary['nfiles']
        self.home = dictionary['home']
        self._exclude_prefix = dictionary['_exclude_prefix']

        largest_files = heapq.nlargest(
            self.nfiles, 
            self.fileTraversal(self.home), 
            key=operator.itemgetter(1),
        )
        self.printFunction(largest_files)
        return


"""Loading the config file."""

try:
    with open('config_for_nlargestfiles.txt') as input_file:
        dictionary = json.load(input_file)
except IOError:
    print('An error occured trying to read the config file')
    exit()

"""Creates an instance of class Nlargest."""

nlargest_obj = Nlargest(
    dictionary['nfiles'],
    dictionary['home'],
    dictionary['_exclude_prefix'],
)

"""Command Line Interface."""

parser = argparse.ArgumentParser()

parser.add_argument(
    "--updateNumber",
    dest="number",
    help="Updates number of files",
)
parser.add_argument(
    "--updateHome",
    dest="home_path",
    help="Updates home directory",
)
parser.add_argument(
    "--addPre", 
    dest="add_prefix",
    help="Adds a prefix to be omitted",
)
parser.add_argument( 
    "--delPre", 
    dest="del_prefix",
    help="Deletes a prefix to be omitted",
)
parser.add_argument( 
    "--nlargest", 
    action="store_true",
    dest="nlargest", 
    help="Finds n largest files",
)

args = parser.parse_args()

if args.number:
    nlargest_obj.updateNfiles((int)(args.number))
if args.home_path:
    nlargest_obj.updateHome(args.home_path)
if args.add_prefix:
    nlargest_obj.addPrefix(args.add_prefix)
if args.del_prefix:
    nlargest_obj.delPrefix(args.del_prefix)
if args.nlargest:
    nlargest_obj.largestFiles()

"""No argument encountered."""

if len(sys.argv) == 1:
    print('Type "-h" for help')

"""Reflect the changes in corresponding config file."""
try:
    with open('config_for_nlargestfiles.txt', 'w') as output_file:
        json.dump(dictionary, output_file)
except:
    print('An error occured trying to read the config file')
    exit()
