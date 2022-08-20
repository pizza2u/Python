from tkinter import X
import pandas as pd

x = pd.read_csv('C:\\Users\\bialn\\Downloads\\ArquivoCSV\\data2.csv')

x['Date']= pd.to_datetime(x['Date'])

print(x.to_string())