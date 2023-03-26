from pandas_datareader import data

df = data.DataReader('7203.JP', 'stooq')
df.head()

import pandas_datareader.data as web
from datetime import datetime

start = datetime(2000, 1, 1)
end = datetime(2018, 7, 18)
df = web.DataReader('WILLREITIND', 'fred', start, end)