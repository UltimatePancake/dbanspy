# Discordlist Bans Python

DBans is a simple API wrapper for [DiscordList Bans](https://bans.discordlist.net), more info about DBans you can find there.

## Installation: ##

### pip: ###

```bash
$ pip install git+git@github.com:UltimatePancake/dbanspy.git@async
```

### Manual Install: ###

```bash
$ git clone https://github.com/UltimatePancake/dbanspy && cd dbanspy
$ pip install .
```

# Examples: #

```py
from dbans import DBans

dBans = DBans(token="token here")
print(dBans.lookup("user id here"))
```
