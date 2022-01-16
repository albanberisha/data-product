import sys
from os import path
import pathlib
from os import walk
from Validation import Validation
import os
import pandas as pd
import utils
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import cufflinks as cf
import plotly.offline

import os
import sys
from os.path import join

import pandas as pd
import numpy as np
import seaborn as sns
import time
import datetime
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.getcwd(), "src"))



def showGenderPlot(data):
    gender=data.groupby(['Gender']).size().reset_index(name='counts')
    print(gender.head(10))
    scores=gender['counts']
    subjects = gender['Gender']

    plt.pie(scores,labels=subjects,autopct='%.2f%%')
    plt.title("Gender of artists",fontsize=20)
    plt.show()
    #
    # data2=data.sample(n=10)
    # data2["Gender"].iplot(kind="histogram", bins=20, theme="white", title="Passenger's Ages", xTitle='Ages', yTitle='Count')


def vizualizeFile(sourceToVizualize,path,currentDir):
    data_artworks = pd.read_csv(f'{path}/{sourceToVizualize}')
    #showGenderPlot(data_artworks)




def thirdPhase(currentDir):
    sourceToVizualize=["Artworks_clean_prod.csv"]
    print(f"-- Listing files inside {pathlib.Path(__file__).parent.resolve()}\\product_output\\{currentDir} directory")
    path = f"{pathlib.Path(__file__).parent.resolve()}\product_output\{currentDir}"
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        if (dirpath == path):
            f.extend(filenames)
    if len(f) != 0:
        validation = True
        count = 0
        vizualize_files = []
        # check if excepted files are inside source
        for file in f:
            if file in sourceToVizualize and validation:
                count += 1
                vizualize_files.append(file)

        # if files inside arent the one we expected
        if count != 1:
            print(
                f"ERROR: Files  inside: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/product_output/{currentDir} \n {2 * ' '} does correspond with excepted file names.\n {2 * ' '} Missing: {sourceToVizualize} files")
        else:
            print(
                f"-- File {sourceToVizualize} inside {pathlib.Path(__file__).parent.resolve()}\product_output\\{currentDir} found")
            vizualizeFile(sourceToVizualize[0],path,currentDir)
    else:
        print(
            f"-- Directory: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/product_output/{currentDir} \n is empty. \nProcess terminated with status error {error}. ")


# Count the arguments
arguments = len(sys.argv) - 1
error=0
if arguments==0:
    print("Starting Third phase.")
    lastdir=utils.getLastDir(mainDir="product_output")
    if lastdir==-1:
        print("No directory found.")
    else:
        print(f"-- Directory {lastdir} found in path: \n{4 * ' '}{pathlib.Path(__file__).parent.resolve()}\\product_output \n")
        thirdPhase(lastdir)
elif arguments>2 or arguments<2:
    print("Required arguments 2.")
    print("Options.\n --third-phase [date]")
else:
    # Output argument-wise
    first_arg = sys.argv[1]
    if first_arg == '--third-phase':
        date = sys.argv[2]
        print(f"-- Checking if directory {date} exists in path {pathlib.Path(__file__).parent.resolve()}\\product_output")
        if (path.isdir(f'product_output/{date}')):
            print(f"-- Directory {date} found in path \n{4 * ' '}{pathlib.Path(__file__).parent.resolve()}\\product_output \n")
            thirdPhase(date)
        else:
            print(
                f"ERROR: Given directory: \n {4 * ' '}{pathlib.Path(__file__).parent.resolve()}/product_output/{date} \n {2 * ' '}could not be found. \nProcess terminated with status error {error}. ")
    else:
        print("Options.\n --third-phase [date]")



