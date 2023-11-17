#Change delimiter 
import pandas as pd
input_delimiter = ','
output_delimiter = ';'


df = pd.read_csv('listings.csv',delimiter=input_delimiter)
df.to_csv('listings_changed.csv',sep=output_delimiter,index=False)
