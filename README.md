# MusicLM-Api-wrapper
A simple and low resource reverse engineered api wrapper for google's music lm experiment

# Requirements:
- Python >=3.6.0 
- Requests_html
- Base64

# Usage:
using it is pretty simple, heres an example:
```
from GoogleMusicLM import GMusic
music = GMusicAsync("your token here")
music.ask("repetition heavy grindhouse electro cut copy",1,"output")
```
# Async
this project also supports async, pretty cool
```
from GoogleMusicLM import GMusicAsync
import asyncio

async def start():
    music = GMusicAsync("your token here")
    await music.ask_async("repetition heavy grindhouse electro cut copy",1,"output")
asyncio.run(start())
```
# some notes:
this project uses requests, so it is possible to run in cli mode, without having the need of setting up gui and stuff like that
this also means that your ram will thank you :]


thanks for checking it out :]
