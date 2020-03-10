import pandas as pd
import numpy as np


df = pd.DataFrame({'A': "1 2 3 4".split()})
from my_lambdata.my_mod import df_split

x, y = df_split(df, .2, 3)
print(x,y)
