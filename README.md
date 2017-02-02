# compare-sqlalchemy-speed

Compare the speed of sqlalchemy ORM vs core.

## Requirements

- Python
  - 3.5.1 or greater

## Setup

To install requirements

```shell
pip install -r requirements.txt
```

To setup DB

```shell
sh ./db/setup.sh
```

## Usage

### Prepare configuration files

Prepare configuration files in according to `resources/config/*.example` files.

- `database.json`

### Test Data Structure

sqlalcyemy_test db has two tables, user and team.

##### user table

| id  | name  |  age  | team_id |created_at|updated_at|
|:---:|:-----:|:-----:|:-------:|:--------:|:--------:|
|  1  | John1 |  12   |    4    |1486030539|1486030539|
|  2  |Kevin2 |  54   |    12   |1486030539|1486030539|


##### team table

| id  | name  |created_at|updated_at|
|:---:|:-----:|:--------:|:--------:|
|  1  | John1 |1486030539|1486030539|
|  2  |Kevin2 |1486030539|1486030539|
  
### Insert data to DB

To insert dummy data

```shell
sqlalchemy-test insert -i ****
```

You can set options for insertion with `-i/--insert_option`.

See

```
sqlalchemy-test -h
```

This option has three types:

- single: single insert with sqlalchemy ORM (default)
- multi:  multi insert with sqlalchemy ORM
- core:   multi insert with sqlalchemy core

### Select data from DB

After insertion, you can try select data with various ways.

```shell
sqlalchemy-test select -s ****
```

You can set options for insertion with `-s/--select_option`.

This option has three types:

- orm:   select with sqlalchemy ORM (default)
- core:  select with sqlalchemy core
- multi: parallelized selection using multiprocessing

You can also test three selection types using `--select_type` option.

- user:  select 100 users in deceingin order of age.

```python
[{'id': 1, 'name': 'John1', 'age': 10, 'team': 'J'},{...}, ...]
```

- team:  select 100 users in decenging order of age in each team.

```python
[{'id': 1, 'name': 'A', 'users': [{'id': 500, 'name': 'Shun', 'age': 23}, {...}, ...]},
 {...}, ...]
```

- count: count users　whose age is under 50 in each team.

```python
{'A': 3245, 'B': 23245, ....}
```