from csv import  reader
import pandas as pd
class Validation:

    def validateArtists(self,filepath,path,currentDir):
        validation=True



        artists_df = pd.read_csv(f'{path}/{filepath}')
        #print(filepath + " Validated")
        #opened_file=open(f'{path}/{filepath}',encoding="utf8")
        #read_file=reader(opened_file)
        #artist_data=list(read_file)
        header=list(artists_df.columns)
        print(f"{4*' '} Validating header columns of dataSet {filepath}")
        header_columns=self.checkHeader(header)
        #if header columns are not as excepted
        if(not header_columns):
            validation=header_columns
            print(f"ERROR: Validation of file {filepath} failed.")
        else:
            print(f"{4 * ' '} Column names in file {filepath} validated successfully.")
            validation=True

        if validation:
            print(f"  File {filepath} was validated successfully.")

        return validation

    def validateArtworks(self,filepath,path,currentDir):
        validation = True
        filepath=f'sources\{currentDir}\{filepath}'
        opened_file=open(filepath,encoding="utf8")
        read_file=reader(opened_file)
        artworks=list(read_file)
        header=sum(artworks[:1], [])
        header_columns = self.checkHeader2(header)
        # if header columns are not as excepted
        if (not header_columns):
            validation = header_columns
            print(f"ERROR: Validation of file {filepath} failed.")
        else:
            print(f"{4 * ' '} Column names in file {filepath} validated successfully.")
            # Hapat per ti validuar dhe pastruar rreshtat
            for row in artworks:
                nationality=row[4]
                nationality=nationality.replace("(","")
                nationality = nationality.replace(")","")
                row[4]=nationality
            print(artworks[300][4])
        '''
        artworks_df = pd.read_csv(f'{path}/{filepath}')
        # print(filepath + " Validated")
        #opened_file=open(f'{path}/{filepath}',encoding="utf8")
        #read_file=reader(opened_file)
        #artworks_data=list(read_file)
        #header = artworks_data[0:1]
        #artworks_data=artworks_data[1:]
        print(f"{4 * ' '} Validating header columns of dataSet {filepath}")
        header_columns = self.checkHeader2(artworks_df.columns)
        # if header columns are not as excepted
        if (not header_columns):
            validation = header_columns
            print(f"ERROR: Validation of file {filepath} failed.")
        else:
            print(f"{4 * ' '} Column names in file {filepath} validated successfully.")
            #Hapat per ti validuar dhe pastruar rreshtat
            artworks_df=artworks_df[1:]
            for row in artworks_df:
                print(row)

        if validation:
            print(f"  File {filepath} was validated successfully.")
        '''
        return validation

#validates header columns
    def checkHeader(self,found_columns):
        result=True
        expected_columns=['ConstituentID', 'DisplayName', 'ArtistBio', 'Nationality', 'Gender', 'BeginDate', 'EndDate', 'Wiki QID', 'ULAN']
        print(f"{5*' '}|  -Expecting columns: {expected_columns}")
        print(f"{5*' '}|  -Found columns:     {found_columns}")

        #columns that are excepted and havn't founded
        couldNotFound=set(expected_columns)-set(found_columns)

        if(len(couldNotFound)!=0):
            for col in couldNotFound:
                print(f"{4*' '}ERROR: Missing column: {col}.")
                result=False
        return result

    def checkHeader2(self,found_columns):
        result=True
        expected_columns= ['\ufeffTitle', 'Artist', 'ConstituentID', 'ArtistBio', 'Nationality', 'BeginDate', 'EndDate', 'Gender', 'Date', 'Medium', 'Dimensions', 'CreditLine', 'AccessionNumber', 'Classification', 'Department', 'DateAcquired', 'Cataloged', 'ObjectID', 'URL', 'ThumbnailURL', 'Circumference (cm)', 'Depth (cm)', 'Diameter (cm)', 'Height (cm)', 'Length (cm)', 'Weight (kg)', 'Width (cm)', 'Seat Height (cm)', 'Duration (sec.)']
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