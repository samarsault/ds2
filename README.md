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

We need to first define the environment variable DS2_DIR, the path to the datastore.

```sh
export DS2_DIR="/usr/local/ds2" # may require sudo if using this path
```

Ds2 can then be invokes as

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