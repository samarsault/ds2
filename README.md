# ds2 (Distributed, Secure Storage Database)

A simple encrypted database for files.

## Need
Sometimes, instead of entire folders, which are visibly encrypted, we need to store only files

## Installation

```sh
$ git clone https://github.com/thelehhman/ds2
$ cd ds2
$ pip install .
```

## Usage

We need to first define the environment variable DS2_DIR, the path to the database root directory.

```sh
export DS2_DIR="$HOME/ds2" 
```

ds2 can then be invoked as

```sh
$ ds2

Usage: ds2 [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  access   Launch database shell
  create   Create new database
  destroy  Destroy database
  ls       List all databases
```

Accessing a database will launch a shell to perform operations in the database.

```sh
$ ds2 access test
Enter Password:
Initialized Database test

> help

Documented commands (type help <topic>):
========================================
add  extract  help  ls  quit  rm

```