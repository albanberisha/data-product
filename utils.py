import sys
from os import path
import pathlib
from os import walk
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
import pandas as pd
warnings.simplefilter(action="ignore", category=FutureWarning)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 13)
from Validation import Validation
import os
import pandas as pd
#getting the last dir inside the mainDir
def getLastDir(mainDir):
    source_dirs=[]
    path = f"{pathlib.Path(__file__).parent.resolve()}\\{mainDir}"
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


def secondPhaseIsRunned(pathDir):
    exists=False
    if (path.isdir(f'product_output/{pathDir}')):
        exists=True
    return exists


#Removing innacurate findings where data of artwork created is not in author birth/death date
def inaccurate_findings(data):
    data_accurate=data
    data_accurate['EndDate'] = data_accurate['EndDate'].fillna(0)
    data_accurate['EndDate'].astype(int)
    data_accurate["Innacurate"]=np.where(((data['BeginDate']>=data['Date']) | (data['EndDate']<=data['Date'])) & (data['EndDate']!=0) ,0, 1)
    inacurate_count=data_accurate.loc[data_accurate['Innacurate'] == 0].shape[0]
    data_accurate.drop(data_accurate.loc[data_accurate['Innacurate']==0].index, inplace=True)
    print(f"{4 * ' '} | Successfully {inacurate_count} inaccurate records were removed from dataset.\n")
    data_accurate['EndDate'] = data_accurate['EndDate'].apply(
        lambda x: '' if "0.0" in str(x) else x)
    data_accurate = data_accurate.drop('Innacurate', 1)
    return data_accurate

def removeOutliners(data):
    startshape = data.shape[0]
    sns.boxplot(data['EndDate'])
    plt.show()
    print(f"{4 * ' '} | Graph showed with outliners.")
    data.drop(data.loc[data['EndDate'] < 1900].index, inplace=True)
    print(f"{4 * ' '} | Removed {startshape - data.shape[0]} outliners.")
    sns.boxplot(data['EndDate'])
    plt.show()
    # print(data.head(20))
    print(f"{4 * ' '} | Graph showed after outliners were removed.\n")
    return data

def secondphaseRun(file,path,currentDir):
    data_artworks=pd.read_csv(f'{path}/{file}')

    # Showing outliners then removing them from data set
    print(f"-- Detecting outliners for {file} inside path : {path}")
    data_artworks=removeOutliners(data_artworks)

    #Finding inacurate findings then removing them
    print(f"-- Avoiding inaccurate findings started for file {file} inside path : {path}")
    data_artworks_filtered=inaccurate_findings(data_artworks)

    print(f"-- Displaying summary statistics for output dataframe.")
    summarystatistics=data_artworks_filtered.describe()
    print(summarystatistics)
    print(f"-- Displaying multivariant statistics for output dataframe.")
    pd.plotting.scatter_matrix(data_artworks_filtered.loc[:, "BeginDate":"Date"], diagonal="kde")
    plt.tight_layout()
    plt.show()

    return data_artworks_filtered,summarystatistics,True




