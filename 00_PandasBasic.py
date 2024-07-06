import pandas as pd 
import lxml
import logging
logging.basicConfig(filename="01_logging.log",level=logging.INFO, format='')

#reading a csv file.
df=pd.read_csv("04_services.csv") #reads the csv file 
#df=dataframe : its just data stored in tabular format


logging.info(df.head()) #reads first five records.
logging.info(df.tail()) #reads last five records , to read x last records use df.tail(x).
logging.info(type(df))  #finds the data type of df.
logging.info(df.columns)#reads all columns. 
logging.info(type(df['status'])) #reads the data type of desired column.
logging.info(df['status']) #reads the selected column.

#pandas returns every single column as a series which is equivalent to a list.
 
logging.info(list(df['status'])) #convert a series into a list.
#if we convert series into list then it will not show index.

logging.info(df[['status','email']]) #to read multiple columns put column names in list.
logging.info(df.dtypes) #reads data types of elements in columns.


#reading an excel file
df1 = pd.read_excel("03_MyExcel.xlsx")
logging.info(type(df1))
logging.info((df1.columns))
logging.info(df1[['Unnamed: 0','Unnamed: 6']])


#reading a csv file from url
df2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
logging.info(df2.head(2))
logging.info(df2.columns)
logging.info(df2['Survived'])
#rest operations are same as before.

#reading a html file 
url_data=pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")
logging.info("number of tables : {}".format(len(url_data)))
df3=url_data[0]

logging.info(df3.head()) #reads first five records.
logging.info(df3.tail()) #reads last five records , to read x last records use df3.tail(x).
logging.info(type(df3)) #finds the data type of df3.
logging.info(df3.columns) #reads all columns. 
logging.info(type(df3['Age'])) #reads the data type of desired column.
logging.info(df3['Rk']) #reads the selected column.

df3.to_csv("02_basketball.csv",index=False) #saving the data from html file(without index)to local pc in a file.
