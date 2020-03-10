# lambdata-mountain

Using the package from PiPy Example instructions:
```py
from lambdata_mountain.my_mod import SplitAddColumn

my_splitter = SplitAddColumn(df)
#SplitAddColumn(df).df_split(test_size, random_state) the_list, col_name
x, y = my_splitter.df_split(test_size=.2, random_state=99)

#SplitAddColumn(df).list_to_new_column(the_list, col_name)

alphabet_list = ['a','b','c','d','e','f','g']
print(x)
print(y)
````
<hr>

Install dependencies:
```sh
pipenv install pandas 
pipenv install numpy
```



An example script:
```sh
python my_lambdata/my_script.py
```