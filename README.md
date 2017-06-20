# Discordlist Bans Python

## Installation: ##

### pip: ###

```bash
$ pip install dbans
```

### Manual Install: ###

```bash
$ git clone https://github.com/JustMaffie/dbanspy && cd dbanspy
$ pip install .
```

### Examples: ###

```py
from dbans import DBans

dBans = DBans(token="token here")
print(dBans.lookup("user id here"))
```