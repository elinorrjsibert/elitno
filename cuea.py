import pandas as pd
import numpy as np

def return_2DF():
    date = pd.date_range('today', periods=20)
    DF1 = pd.DataFrame(np.random.rand(20, 2), index=date, columns=list('xyz'))
    DF2 = pd.DataFrame(np.random.rand(20, 4), index=date, columns='A B C D'.split())
    return DF1, DF2

df1, df2 = return_2DF()
