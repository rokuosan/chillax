# Chillax

Provides chill and relax musics to your discord server!

## Getting Started

### Requirements

- Python3.x
- FFmpeg
- Discord Bot API Token

### Installation

> **NOTE**
> 
> You must have a discord bot api token. 
> If you don't have it, you can get from [Discord Developer Portal](https://discord.com/developers/applications).
> 

Install Python3 and FFmpeg using apt.

```shell
$ sudo apt update -y
$ sudo apt install -y python3 python3-pip python3-venv ffmpeg
```

Create and activate Python virtual environment.

```shell
$ python -m venv venv
$ source ./venv/bin/activate
```

Install some libraries.

```shell
$ pip install -r requirements.txt
```

Download and concat music.

Executing this script, ``music.mp3`` will appear in ``./sounds`` directory.

```shell
$ ./prepare.sh
```

Create .env file.

```shell
$ echo PUT_YOUR_API_TOKEN_HERE > .env
```

Start discord bot.

```shell
$ python main.py 
```


## Contribution

(Optional) To enable python virtual environment is good for your development experience.

Just run!

```shell
$ source ./venv/bin/activate
```

## Thanks

Composer: zukisuzuki 

- [YouTube](https://www.youtube.com/@zukisuzukiBGM)
- [https://zukisuzukibgm.com/](https://zukisuzukibgm.com/)
