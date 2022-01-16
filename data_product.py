import sys
from os import path
import pathlib
from os import walk
from Validation import Validation
import os
import pandas as pd
import utils

#save dataset on specified folder
def savedataSet(data_set,currentDir,summary):
    filename='Artworks_clean_prod.csv'
    pathToCreate = f"{pathlib.Path(__file__).parent.resolve()}/product_output"
    pathToCreate = os.path.join(pathToCreate, currentDir)
    #Create the directory for output
    os.mkdir(pathToCreate)
    print(f"-- Directory {currentDir} created inside path:\n {4*' '} {pathlib.Path(__file__).parent.resolve()}\product_output\ ")
    df = pd.DataFrame(data_set)
    df.to_csv(f"{pathToCreate}\{filename}", header=True, sep=',',index=False)
    print(
        f"-- Dataset {filename} has been saved inside path:\n {4 * ' '} {pathlib.Path(__file__).parent.resolve()}\product_output\ {pathToCreate}")
    summary_filename= 'Summary_Artworks_clean_prod.csv'
    df = pd.DataFrame(summary)
    df.to_csv(f"{pathToCreate}\{summary_filename}", header=True, sep=',', index=True)
    print(
        f"-- Summary {summary_filename} has been saved inside path:\n {4 * ' '} {pathlib.Path(__file__).parent.resolve()}\product_output\ {pathToCreate}")

    print(f"SECOND PHASE HAS BEEN FINISHED SUCCESSFULLY. ")



def validateFile(file,path,currentDir):
    dataset,summary,raport=utils.secondphaseRun(file,path,currentDir)
    savedataSet(dataset,currentDir,summary)

def secondPhase(currentDir):
    firstphasesource=["Artworks_clean.csv"]
    print(f"-- Listing files inside {pathlib.Path(__file__).parent.resolve()}\\first_phase_output\{currentDir} directory")
    path = f"{pathlib.Path(__file__).parent.resolve()}\\first_phase_output\\{currentDir}"
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        if (dirpath == path):
            f.extend(filenames)
    if len(f) != 0:
        if utils.secondPhaseIsRunned(currentDir):
            print(f"ERROR: Given directory: \n {4*' '}{pathlib.Path(__file__).parent.resolve()}//first_phase_output//{currentDir} \n {2*' '} is already found in output path. \nSecond phase cannot run more than once in same source. ")
        else:
            validation = True
            count = 0
            validation_files = []
            # check if excepted file is inside source
            for file in f:
                if file in firstphasesource and validation:
                    count += 1
                    validation_files.append(file)

            # if files inside arent the one we expected
            result=False
            if count == 0:
                print(f"ERROR: Files  inside: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}//first_phase_output//{currentDir} \n {2 * ' '} does correspond with excepted file names.\n {2 * ' '} Missing: {firstphasesource} file")
            elif count == 1:
                print(f"-- Files {firstphasesource} inside {pathlib.Path(__file__).parent.resolve()}\ first_phase_output\{currentDir} found")
                validateFile(file,path,currentDir)


    else:
        print(f"-- Directory: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/first_phase_output/{currentDir} \n is empty. \nProcess terminated with status error {error}. ")





# Count the arguments
arguments = len(sys.argv) - 1
error=0
if arguments==0:
    print("Starting Product phase.")
    lastdir=utils.getLastDir(mainDir="first_phase_output")
    if lastdir==-1:
        print("No directory found.")
    else:
        print(f"-- Directory {lastdir} found in path: \n{4 * ' '}{pathlib.Path(__file__).parent.resolve()}\\first_phase_output \n")
        secondPhase(lastdir)
elif arguments>2 or arguments<2:
    print("Required arguments 2.")
    print("Options.\n --second-phase [date]")
else:
    # Output argument-wise
    first_arg = sys.argv[1]
    if first_arg == '--second-phase':
        date = sys.argv[2]
        print(f"-- Checking if directory {date} exists in path {pathlib.Path(__file__).parent.resolve()}\\first_phase_output")
        if (path.isdir(f'sources/{date}')):
            print(f"-- Directory {date} found in path \n{4 * ' '}{pathlib.Path(__file__).parent.resolve()}\\first_phase_output \n")
            secondPhase(date)
        else:
            print(
                f"ERROR: Given directory: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/first_phase_output/{date} \n {2 * ' '}could not be found. \nProcess terminated with status error {error}. ")
    else:
        print("Options.\n --second-phase [date]")