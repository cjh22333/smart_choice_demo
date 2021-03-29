
import datetime
import tushare as ts
import pandas as pd
import numpy as np
from jqdatasdk import *
auth('15989211288', 'As82701800')

df = get_bars('600000.XSHG',count=1)
print(df)


pro = ts.pro_api()
df = pro.daily(ts_code="600000.SH", start_date='20180701')
name = pro.stock_basic(ts_code = "600008.SH")
print(df,name)

data = df.iloc[-1]
data = [i for i in data]
print(data)

today = datetime.datetime.today().strftime(format="%Y%m%d")
print(today)