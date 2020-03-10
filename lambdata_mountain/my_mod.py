
import pandas as pd
import numpy as np

class SplitAddColumn:

    def __init__(self, df):
        self.df = df
        

    def df_split(self, test_size, random_state=42):
        np.random.seed(random_state)
        shuffled_indices = np.random.permutation(len(self.df))
        test_set_size = int(len(self.df) * test_size)
        test_indices = shuffled_indices[:test_set_size]
        train_indices = shuffled_indices[test_set_size:]
        return self.df.iloc[train_indices], self.df.iloc[test_indices]

    def list_to_new_column(self, the_list, col_name="new_column"): 
        series = pd.Series(the_list)
        self.df[col_name] = series 
        return self.df

     