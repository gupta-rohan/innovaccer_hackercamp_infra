# Innovaccer Summer Hackercamp - Infrastructure

## Assignment objectives:
1. Finds out n largest files in a directory.
2. Organizes files in a directory according to their file extensions.

 ## Getting started:
 1. Install Python 2.7 from - (https://www.python.org/downloads/)
 
 2. Download repository:
 
    ```
    cd path_to_repository
    git clone git://github.com/ 
    ```
 3. To find out n largest files in a directory:
 
    ```
    cd path_to_repository/innovaccer_hackercamp_infra/python nlargestfiles.py --help
   
    Usage Example:
    Typing nlargestfiles.py --help will list all the available commands.
   
    usage: nlargestfiles.py [-h] [--updateNumber NUMBER] [--updateHome HOME_PATH]
                        [--addPre ADD_PREFIX] [--delPre DEL_PREFIX]
                        [--nlargest]

    optional arguments:
    -h, --help            show this help message and exit
    --updateNumber NUMBER
                        Updates number of files
    --updateHome HOME_PATH
                        Updates home directory
    --addPre ADD_PREFIX   Adds a prefix to be omitted
    --delPre DEL_PREFIX   Deletes a prefix to be omitted
    --nlargest            Finds n largest files
    ```
 4. To organize files in a directory based on their extension:
 
    ```
    cd path_to_repository/innovaccer_hackercamp_infra/python organize.py --help
    
    Usage Example:
    Typing organize.py --help will list all the available commands.
    
    usage: organize.py [-h] [--updateHome HOME_PATH]
                   [--updateDest DESTINATION_PATH] [--addExtension EXT_ADD]
                   [--delExtension EXT_REM] [--removeClutter]

    optional arguments:
    -h, --help            show this help message and exit
    --updateHome HOME_PATH
                        updates home directory
    --updateDest DESTINATION_PATH
                        updates destination directory
    --addExtension EXT_ADD
                        Adds extension
    --delExtension EXT_REM
                        Removes extension
    --removeClutter       Removes clutter
  
## Features:
### nlargestfiles.py
1. The home directory, number of files to be listed and list of exclude prefixes can be changed.
2. The corresponding effects can be seen in the associated config file.
 
### organize.py
1. The home directory, destination directory and list of extension can be changed.
2. The corresponding effects can be seen in the associated config file.
