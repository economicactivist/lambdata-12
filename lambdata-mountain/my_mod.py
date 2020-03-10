


def df_split(data, test_size, random_state):
    np.random.seed(random_state)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_size)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def list_to_new_column(df, the_list, col_name): 
    series = pd.Series(the_list)
    df[col_name] = series
    return df