import sys
from os import path
import pathlib
from os import walk

# Count the arguments
arguments = len(sys.argv) - 1
error=0
if arguments>2 or arguments<2:
    print("Required arguments 2.")
    print("Options.\n --first-phase [date]")
else:
    # Output argument-wise
    first_arg=sys.argv[1]
    if first_arg=='--first-phase':
        date = sys.argv[2]
        print(f"-- Checking if directory {date} exists in path {pathlib.Path(__file__).parent.resolve()}\sources")
        if(path.isdir(f'sources/{date}')):
            print(f"-- Directory {date} found in path \n{4*' '}{pathlib.Path(__file__).parent.resolve()}\sources \n")
            print(f"-- Listing files inside {pathlib.Path(__file__).parent.resolve()}\sources\{date} directory")
            path=f"{pathlib.Path(__file__).parent.resolve()}\sources\{date}"
            f = []
            for (dirpath, dirnames, filenames) in walk(path):
                if(dirpath==path):
                    f.extend(filenames)
            if len(f)>=0:
                   print(f"--Directory: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/sources/{date} \n is empty. \nProcess terminated with status error {error}. ")

        else:
            print(f"ERROR: Given directory: \n {4*' '}{pathlib.Path(__file__).parent.resolve()}/sources/{date} \n {2*' '}could not be found. \nProcess terminated with status error {error}. ")
    else:
        print("Options.\n --first-phase [date]")