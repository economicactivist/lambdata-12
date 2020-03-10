import pandas as pd
import numpy as np


df = pd.DataFrame({'A': "1 2 3 4 5 6 7 8 9 10".split()})
from lambdata_mountain.my_mod import SplitAddColumn

a = "e b e r g y u i s f".split()

my_splitter = SplitAddColumn(df)
# df, test_size, random_state, the_list, col_name
x, y = my_splitter.df_split(.2, 99)
print(x)
print(y)





