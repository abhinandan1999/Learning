## Pandas
#### Pandas settings

* Display all columns
```
pd.set_option('display.max_columns', None)
```

* Show complete columns
```
pd.set_option('display.max_colwidth', None)
```

* Set Max rows to display
```
pd.set_option('display.max_rows', n)
```

* Set Min rows to display
```
pd.set_option('display.min_rows', n)
```

* Set the display of decimal places
```
pd.set_option('display.float_format', lambda x: '%.2f' % x)
```

* Resets any pandas settings
```
pd.reset_option(args: str)
    args:
        "max_columns"
```