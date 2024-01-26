import pandas as pd

maceio_2003 = pd.read_csv('P007/dataset/maceio_2003.CSV' , encoding='latin-1', sep=';', header=None, skiprows=8)
maceio_2013 = pd.read_csv('P007/dataset/maceio_2013.CSV' , encoding='latin-1', sep=';', header=None, skiprows=8)
maceio_2023 = pd.read_csv('P007/dataset/maceio_2023.CSV' , encoding='latin-1', sep=';', header=None, skiprows=8)


print(maceio_2003.head())
print(maceio_2013.head())
print(maceio_2023.head())


