import csv
import matplotlib.pyplot as plt
import pandas as pd


with open('../product_output/11232021/Artworks_clean_prod.csv', encoding="utf8") as csvfile:

    data_list=list(csv.reader(csvfile))
    totalSubs = {}
    Subjects = []
    Scores = []

    datesdictionary = {}
    dates = []
    title_per_date = []
    for row in data_list[1:]:
        if row[5] in totalSubs:
            totalSubs[row[5]]+=1
        else:
            totalSubs[row[5]] =1

        if row[7]!='':
         date=(int(float(row[7])))
         if date!="":
            date=date-int(date%10)
            if date in datesdictionary:
                datesdictionary[date]+=1
            else:
                datesdictionary[date]=1

    for elem in totalSubs:
        Subjects.append(elem)
        Scores.append(totalSubs[elem])

    for elem in sorted(datesdictionary):
        currdate=str(elem)+"-"+str(int(elem)+9)
        dates.append(currdate)
        title_per_date.append(datesdictionary[elem])



    frequencies=title_per_date

    freq_series=pd.Series(frequencies)

    y_labels=dates

    #plot the figure
    plt.figure(figsize=(12,8))
    ax=freq_series.plot(kind='barh')
    ax.set_title('Artworks distribution')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Date')
    ax.set_yticklabels(y_labels)

    rects=ax.patches

    #for each bar: place a label
    for rect in rects:
        #get x and y placement of label from rect
        x_value=rect.get_width()
        y_value=rect.get_y()+rect.get_height()/2

        #number of points between bar and label
        space=5
        #vertical alignment for positive values
        ha='left'

        #if value of bar is negative: place label left of bar
        if x_value<0:
            #invert space to place label to the left
            space*=-1
            #horizontaly align label at right
            ha='right'

        #use x value as label and format number with 0 decimal place
        label="{:.0f}".format(x_value)

        #create annotation
        plt.annotate(
            label,
            (x_value,y_value),
            xytext=(space,0),
            textcoords="offset points",
            va='center',
            ha=ha
        )
    plt.show()
    #plt.savefig('image.png')