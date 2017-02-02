# sqlalchemy-test

Compare the speed of sqlalchemy.

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

- single: single insert with sqlalchemy ORM
- multi:  multi insert with sqlalchemy ORM
- core:   multi insert with sqlalchemy core

### Select data from DB

After insertion, you can try select data with various ways.

```shell
sqlalchemy-test select -s ****
```

You can set options for insertion with `-s/--select_option`.

This option has three types:

- orm: select with sqlalchemy ORM
- core:  select with sqlalchemy core
- multi: parallelized selection using multiprocessing