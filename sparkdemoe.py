import pandas as pd
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
import pyspark

spark_conf = SparkConf().setAppName("test")
spark = SparkContext(conf = spark_conf)
df=spark.read.csv('sources/appleStore_description.csv')
df.show()
df = pd.read_csv ('sources/11232021/appleStore_description.csv')
df = pd.DataFrame(df, columns= ['id','track_name','size_bytes','app_desc'])
print(df.take(3))
