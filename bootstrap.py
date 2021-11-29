import sys
from os import path
import pathlib
from os import walk
from Validation import Validation
import os
import pandas as pd
#getting the last dir inside the mainDir
def getLastDir(mainDir):

    source_dirs=[]
    path = f"{pathlib.Path(__file__).parent.resolve()}\{mainDir}"
    print(f"Getting the last directory inside {path}")
    #walk through all dirs inside path
    for (dirpath, dirnames, filenames) in walk(path):
        if (dirpath == path):
            #get all dirs inside path
            source_dirs.extend(dirnames)
    #return last dir
    lastdir=-1
    if(len(source_dirs)!=0):
        lastdir=source_dirs[len(source_dirs)-1]
    return lastdir

#checking if first phase has been runned
def firstPhaseIsRunned(pathDir):
    exists=False
    if (path.isdir(f'first_phase_output/{pathDir}')):
        exists=True
    return exists

#Validate header of dataset given in fileame
def validateFileHeader(filename,path,currentDir):
    v = Validation()
    result=True
    print(f"-- Validation started for file {filename} inside path : {path}")
    if filename == "Artists.csv":
        result=v.validateArtists(filename,path,currentDir)
    elif filename == "Artworks.csv":
        result=v.validateArtworks(filename,path,currentDir)
    #print(f"ERROR: Validation filed. Contents inside {filename} could not validate. ")
    return result

def mergeAndValidateFiles(path,currentDir,listOfFiles):
    v = Validation()
    data_set=v.completeValidationProcess(path,currentDir,listOfFiles)
    savedataSet(data_set,currentDir)

#save dataset on specified folder
def savedataSet(data_set,currentDir):
    filename='Artworks_clean.csv'
    pathToCreate = f"{pathlib.Path(__file__).parent.resolve()}/first_phase_output"
    pathToCreate = os.path.join(pathToCreate, currentDir)
    #Create the directory for output
    os.mkdir(pathToCreate)
    print(f"-- Directory {currentDir} created inside path:\n {4*' '} {pathlib.Path(__file__).parent.resolve()}\first_phase_output\ ")
    df = pd.DataFrame(data_set)
    df.to_csv(f"{pathToCreate}\{filename}", header=True, sep=',',index=False)
    print(
        f"-- Dataset {filename} has been saved inside path:\n {4 * ' '} {pathlib.Path(__file__).parent.resolve()}\first_phase_output\ {pathToCreate}")

    print(f"FIRST PHASE HAS BEEN FINISHED SUCCESSFULLY. ")


def firstPhase(currentDir):
    firstphasesource=["Artists.csv","Artworks.csv"]
    print(f"-- Listing files inside {pathlib.Path(__file__).parent.resolve()}\sources\{currentDir} directory")
    path = f"{pathlib.Path(__file__).parent.resolve()}\sources\{currentDir}"
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        if (dirpath == path):
            f.extend(filenames)
    if len(f) != 0:
        #print(f"-- Files inside {pathlib.Path(__file__).parent.resolve()}\sources\{currentDir} found")
        if firstPhaseIsRunned(currentDir):
            print(f"ERROR: Given directory: \n {4*' '}{pathlib.Path(__file__).parent.resolve()}/sources/{currentDir} \n {2*' '} is already found in output path. \nFirst phase cannot run more than once in same source. ")
        else:
            validation=True
            count=0
            validation_files=[]
            #check if excepted files are inside source
            for file in f:
                if file in firstphasesource and validation:
                    count += 1
                    validation_files.append(file)

            #if files inside arent the one we expected
            if count == 0:
                print(f"ERROR: Files  inside: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/sources/{currentDir} \n {2 * ' '} does correspond with excepted file names.\n {2 * ' '} Missing: {firstphasesource} files")
            elif count==1:
                #missing one file that is excepted
                couldNotFound=str(set(firstphasesource)^set(validation_files))
                print(f"ERROR: Excepting files: \n {4 * ' '} {firstphasesource} inside:{pathlib.Path(__file__).parent.resolve()}/sources/{currentDir}  \n {1 * ' '} Missing: {couldNotFound} file")
            else:
                print(f"-- Files {firstphasesource} inside {pathlib.Path(__file__).parent.resolve()}\sources\{currentDir} found")
                validation=True
                for file in f:
                    if file in firstphasesource:
                        validation=validateFileHeader(file,path,currentDir)
                    if not validation:
                      print(f"ERROR: File {file} inside {pathlib.Path(__file__).parent.resolve()}\sources\{currentDir} could not be validated")
                      break

                if validation:
                    mergeAndValidateFiles(path,currentDir,firstphasesource)

    else:
        print(f"-- Directory: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/sources/{currentDir} \n is empty. \nProcess terminated with status error {error}. ")


# Count the arguments
arguments = len(sys.argv) - 1
error=0
if arguments==0:
    print("Starting first phase.")
    lastdir=getLastDir(mainDir="sources")
    if lastdir==-1:
        print("No directory found.")
    else:
        print(f"-- Directory {lastdir} found in path: \n{4 * ' '}{pathlib.Path(__file__).parent.resolve()}\sources \n")
        firstPhase(lastdir)
elif arguments>2 or arguments<2:
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
            firstPhase(date)
        else:
            print(f"ERROR: Given directory: \n {4*' '}{pathlib.Path(__file__).parent.resolve()}/sources/{date} \n {2*' '}could not be found. \nProcess terminated with status error {error}. ")
    else:
        print("Options.\n --first-phase [date]")