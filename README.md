# The Museum of Modern Art (MoMA) Collection

Taken from **[github](https://github.com/MuseumofModernArt/collection)**

The Museum of Modern Art (MoMA) acquired its first artworks in 1929, the year it was established. Today, the Museum’s evolving collection contains almost 200,000 works from around the world spanning the last 150 years. The collection includes an ever-expanding range of visual expression, including painting, sculpture, printmaking, drawing, photography, architecture, design, film, and media and performance art.
## Installation

This module requires the following modules:
```bash
pip install matplotlib
pip install numpy
pip install pandas
pip install pandera
pip install pip
```
Create new project, download the source files from  **[github project](https://github.com/albanberisha/data-product)** and unzip inside your project.
This project uses folder 'sources' as source folder and inside are date formats as folders (ex 11/22/2021 as 11232021). To run the project u need to create new folder with upload date of files downloaded from **[github](https://github.com/MuseumofModernArt/collection)** (this link contains data sets). 

Keep in mind that the data sets need to be exactly inside date folder(ex 11232021), any directory inside those folders will be ignored. Also data sets need to have this exact name convention: "Artists.csv" and "Artworks.csv".

## Usage for FIRST PHASE

After you have:
 
 * Downloaded this project
 * Created new folder inside **sources** folder with name: yourdate (ex 11232021)
 * Downloaded the data set (**[github](https://github.com/MuseumofModernArt/collection)**) files and moved inside folder
      * **sources/yourdate**
 
Now you are all set.

To run the **First Phase** run the following command inside terminal:

```python
>>  python bootstrap.py
```

This command will run the last uploaded date inside **sources** folder.

If you want to run specific **uploaded date** folder inside **sources** folder use command:

```python
>>  python bootstrap.py --first-phase yourdate
#where yourdate is like: 11232021
```

After running the command inside your terminal,if there is not any error in the console, after some minutes you will find new folder created inside **first_phase_output** folder. There is your folder and inside it will be the result of this execution. The file will be named **Artworks_clean.csv** and it will be ready for next PHASE.
## Contributing
This project has been created by:
 * Alban Berisha 
   * Visit https://github.com/albanberisha.
 * Arti Sadikaj 
   * Visit https://github.com/ArtiSadikaj.