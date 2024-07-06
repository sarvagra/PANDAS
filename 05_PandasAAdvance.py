import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

import logging 
logging.basicConfig(filename="06_logging.log",level=logging.INFO,format='')
logging.info(df.describe()) 