import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

import logging 
logging.basicConfig(filename="06_logging.log",level=logging.INFO,format='')
logging.info(df.describe()) #shows data in a statistical manner
logging.info(df[['name','sex','age']])    #prints selected columns


logging.info(df[df.dtypes[df.dtypes =='object'].index].describe()) #prints all data of type OBJECT
logging.info(df[df.dtypes=='float64'].index) #prints all numerical data.
 
# to print data from a particular interval , use [<upper bound>:<lower bound>:<jump>]
logging.info(df[['Ticket']][4:11])

# creating a new column
df['new_column']=0
df["new_column_one"]=df['PassengerId']+df['Pclass']
pd.Categorical(df['Pclass'])
df['Cabin'].unique()

logging.info(df.head())

#filter the data  by age >18.
if df['Age']>18 :
    logging.info(df['Age'])

#to get the names of all passangers who payed greater fair than average.
if df[df['Fare']>32.204308 ] :
    logging.info(df['Fare'])

# to get the name of passangers who didnt pay any fare
if(df['Fare']==0):
    logging.info(df['Fare'])

if(df['Sex']=='male'):
    logging.info(df['sex'])
    git pus 