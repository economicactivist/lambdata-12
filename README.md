# lambdata-mountain

Install from test PyPI:

```sh
pip install -i https://test.pypi.org/simple/ Mountain-Scott-ds12
```


Using the package from PyPI Example instructions:
```py
from lambdata_mountain.my_mod import SplitAddColumn

my_splitter = SplitAddColumn(df)
#SplitAddColumn(df).df_split(test_size, random_state) the_list, col_name
x, y = my_splitter.df_split(test_size=.2, random_state=99)
print(x)
print(y)
#SplitAddColumn(df).list_to_new_column(the_list, col_name="new_column")

alphabet_list = ['a','b','c','d','e','f','g']

my_splitter.list_to_new_column(alphabet_list, col_name="Alphabet")

```
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