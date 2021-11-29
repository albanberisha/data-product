from csv import  reader
import pandas as pd
import statistics
import numpy as np
from datetime import datetime
class Validation:

    #Checks if filepath has expected columns inside
    def validateArtists(self,filepath,path,currentDir):
        validation=True
        data = pd.read_csv(f'{path}/{filepath}')
        data.rename(columns=lambda x: x.strip().capitalize().replace(' ', '_'), inplace=True)
        data.rename(columns={'Constituentid':'ConstituentId','Begindate': 'BeginDate', 'Enddate': 'EndDate'},
                    inplace=True)
        #getting dataset header
        data_columns = list(data.columns)
        header=list(data.columns)
        print(f"{4*' '} Validating header columns of dataSet {filepath}")
        header_columns=self.checkHeader(header)
        #if header columns are not as excepted
        if(not header_columns):
            validation=header_columns
            print(f"ERROR: Validation of file {filepath} failed.\n")
        else:
            print(f"{4 * ' '} Column names in file {filepath} validated successfully.\n")
            validation=True

        return validation


    # Checks if filepath has expected columns inside
    def validateArtworks(self,filepath,path,currentDir):
        validation = True
        data = pd.read_csv(f'{path}/{filepath}')

        data.rename(columns=lambda x: x.strip().capitalize().replace(' ', '_'), inplace=True)
        data.rename(columns={'Constituentid': 'ConstituentId','Dateacquired': 'DateAcquired'},
                    inplace=True)
        # getting dataset header
        data_columns = list(data.columns)
        header = list(data.columns)
        print(f"{4 * ' '} Validating header columns of dataSet {filepath}")
        header_columns = self.checkHeader2(header)
        # if header columns are not as excepted
        if (not header_columns):
            validation = header_columns
            print(f"ERROR: Validation of file {filepath} failed.")
        else:
            print(f"{4 * ' '} Column names in file {filepath} validated .successfully.\n")
            validation = True

        return validation


     #validates header columns
    def checkHeader(self,found_columns):
        result=True
        excepted_columns = ['ConstituentId', 'Displayname', 'Artistbio', 'Nationality', 'Gender', 'BeginDate', 'EndDate', 'Wiki_qid', 'Ulan']
        print(f"{5*' '}|  -Expecting columns: {excepted_columns}")
        print(f"{5*' '}|  -Found columns:     {found_columns}")
        #columns that are excepted and havn't founded
        couldNotFound=set(excepted_columns)-set(found_columns)

        if(len(couldNotFound)!=0):
            for col in couldNotFound:
                print(f"{4*' '}ERROR: Missing column: {col}.")
                result=False
        return result

    # validates header columns
    def checkHeader2(self,found_columns):
        result=True
        expected_columns= ['Title', 'ConstituentId', 'Date',
         'Medium', 'Dimensions', 'Creditline', 'Accessionnumber', 'Classification', 'Department', 'DateAcquired',
         'Cataloged', 'Objectid', 'Url', 'Thumbnailurl', 'Circumference_(cm)', 'Depth_(cm)', 'Diameter_(cm)',
         'Height_(cm)', 'Length_(cm)', 'Weight_(kg)', 'Width_(cm)', 'Seat_height_(cm)', 'Duration_(sec.)']
        print(f"{5*' '}|  -Expecting columns: {expected_columns}")
        print(f"{5*' '}|  -Found columns:     {found_columns}")
        #columns that are excepted and havn't founded
        couldNotFound=[]
        for col in expected_columns:
            if col not in found_columns:
                couldNotFound.append(col)

        if(len(couldNotFound)!=0):
            for col in couldNotFound:
                print(f"{4*' '}ERROR: Missing column: {col}.")
                result=False

        return result

    #clean data inside dataFrame
    def cleanArtworks(self,data):
        # fill missing data
        print(f"{4 * ' '} | Handling missing values.")
        data["ConstituentID"].fillna('0,0', inplace=True)
        data["Medium"].fillna('Unknown', inplace=True)
        data["Dimensions"].fillna('', inplace=True)
        data["CreditLine"].fillna('Unknown', inplace=True)
        data["AccessionNumber"].fillna('0,0', inplace=True)
        data["Classification"].fillna('Unknown', inplace=True)
        data["Department"].fillna('Unknown', inplace=True)
        data["DateAcquired"].fillna('(0)', inplace=True)
        data["Cataloged"].fillna('', inplace=True)

        #drop rows that have more than one ConstituentID
        print(f"{4 * ' '} | Dropping unwanted rows.")
        unwanted_rows=data[data['ConstituentID'].str.contains(',')].index
        data=data.drop(unwanted_rows)
        # fill missing data and transforming data
        data['Date'] = data['DateAcquired'].apply(lambda x: np.nan if x == "(0)" else int(datetime.strptime(str(x), '%Y-%m-%d').year))
        data['DateAcquired'] = data['DateAcquired'].apply(lambda x: '' if x == "(0)" else datetime.strptime(str(x), '%Y-%m-%d').date())
        data['DateAcquired'] = data['DateAcquired'].apply(lambda x: '' if x == 0 else x)
        data['Cataloged'] = data['Cataloged'].apply(lambda x: 1 if x == 'Y' else 0 if x == 'N' else np.nan)

        # defining column types
        data['Title'] = data['Title'].astype("string")
        data['ConstituentID'] = data['ConstituentID'].astype(int)
        data['DateAcquired'] = data['DateAcquired'].astype("string")
        data['Classification'] = data['Classification'].astype("string")
        data['Department'] = data['Department'].astype("string")
        data['Cataloged'] = pd.to_numeric(data['Cataloged'])
        print(f"{3 * ' '} Dataset has undergone the process of Data Cleaning with success.\n")

        return data

    # clean data inside dataFrame
    def cleanArtists(self,data):
        # fill missing data
        print(f"{4 * ' '} | Handling missing values.")
        data["ConstituentID"].fillna('0,0', inplace=True)
        data["Nationality"].fillna('()', inplace=True)
        data["Gender"].fillna('()', inplace=True)
        data["BeginDate"].fillna('(0)', inplace=True)
        data["EndDate"].fillna('(0)', inplace=True)

        # fill missing data and transforming data
        data['Nationality'] = data['Nationality'].apply(
            lambda x: "Nationality Unknown" if '()' in str(x) else str(x).replace('(', ' ').replace(')', ' '))
        data['Nationality'] = data['Nationality'].apply(lambda x: "Nationality Unknown" if "   " in str(x) else str(x))
        data['BeginDate'] = data['BeginDate'].apply(
            lambda x: '' if '(0)' in str(x) or str(x)=="0" else str(x).replace(' ', '-').replace('(', '').replace(')', '').split(
                "-")).apply(
            lambda x: '' if x is None else int(statistics.mean(list(map(float, x)))) if isinstance(x, list) else x)
        data['EndDate'] = data['EndDate'].apply(
            lambda x: '' if '(0)' in str(x) or str(x)=="0" else str(x).replace(' ', '-').replace('(', '').replace(')', '').split("-")) \
            .apply(
            lambda x: '' if x is None else int(statistics.mean(list(map(float, x)))) if isinstance(x, list) else x)
        data['Gender'] = data['Gender'].apply(
            lambda x: "Gender Unknown/Other" if "()" in str(x) else str(x).replace('(', ' ').replace(')', ' ').title())
        data['Gender'] = data['Gender'].apply(
            lambda x: "Male" if "Male" in str(x) else "Female" if "Female" in str(x) else "Gender Unknown/Other")

        # defining column types
        data['ConstituentID'] = data['ConstituentID'].astype(int)
        data['DisplayName']=data['DisplayName'].astype("string")
        data['Nationality']=data['Nationality'].astype("string")
        data['Gender']=data['Gender'].astype("string")
        print(f"{3 * ' '} Dataset has undergone the process of Data Cleaning with success.\n")

        return data


    def completeValidationProcess(self,path,currentDir,listOfFiles):
        data_artists = pd.read_csv(f'{path}/{listOfFiles[0]}')
        data_artworks= pd.read_csv(f'{path}/{listOfFiles[1]}')
        data_artworks_wanted_columns=['Title', 'ConstituentID', 'Date', 'Medium', 'Dimensions',
                                      'CreditLine', 'AccessionNumber', 'Classification', 'Department',
                                      'DateAcquired', 'Cataloged', 'ObjectID', 'URL', 'ThumbnailURL',
                                      'Circumference (cm)', 'Depth (cm)', 'Diameter (cm)', 'Height (cm)',
                                      'Length (cm)', 'Weight (kg)', 'Width (cm)', 'Seat Height (cm)',
                                      'Duration (sec.)']
        data_artworks = data_artworks[list(data_artworks_wanted_columns)]
        print(f"-- Data cleaning started for file {listOfFiles[0]} inside path : {path}")
        data_artists = self.cleanArtists(data_artists)
        print(f"-- Data cleaning started for file {listOfFiles[1]} inside path : {path}")
        data_artworks=self.cleanArtworks(data_artworks)

        print(f"-- Data Integration and Transformation started for file/s {listOfFiles} inside path : {path}")
        print(f"{4 * ' '} | Merging files {listOfFiles}.")
        data_artworks=data_artworks.merge(data_artists, on='ConstituentID', how='left')
        print(f"{4 * ' '} | Detecting and resolving data value concepts files.")
        data_artworks['DateAcquired'] = pd.to_datetime(data_artworks['DateAcquired'])
        data_artworks['DateAcquired']=pd.to_datetime(data_artworks['DateAcquired'].dt.strftime('%m/%d/%Y'))
        print(f"{3 * ' '} Dataset has undergone the process of Data Integration and Transformation with success. Main Data Set has been created.\n")

        print(f"-- Data Reduction started for Main Data Set.")
        wanted_data_volume = ['Title', 'DisplayName','ConstituentID','Nationality', 'BeginDate', 'EndDate', 'Gender', 'Date','Classification', 'Department',
                              'DateAcquired', 'Cataloged']
        print(f"{4 * ' '} | Dimensionality reduction.")
        print(f"{4 * ' '} | Wanted columns:\n {6 * ' '}{wanted_data_volume}")
        print(f"{3 * ' '} Main Data Set  has undergone the process of Data Reduction with success.\n")
        data_artworks = data_artworks[list(wanted_data_volume)]
        #print(f"{4 * ' '} | Removing duplicates.")
        data_artworks = data_artworks.drop_duplicates(subset=wanted_data_volume,keep=False)
        data_artworks.rename(columns={'DisplayName': 'Artist'},
                    inplace=True)
        return data_artworks
