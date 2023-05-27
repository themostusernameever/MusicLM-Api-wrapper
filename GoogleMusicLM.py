from requests_html import HTMLSession, AsyncHTMLSession
import base64
import os
class GMusic:
    def __init__(self, token):
        self.token = token
        self.session = HTMLSession()
    def ask(self, prompt: str, generation_count = 2, path = ""):
        json = {
            "generationCount": generation_count,
            "input":{
                "textInput": prompt
            },
            "soundLengthSeconds": 30 # changing it wont affect anything, it will stay at 20 no matter what.
        }
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
        }
        r = self.session.post("https://content-aisandbox-pa.googleapis.com/v1:soundDemo?alt=json", headers=headers, json=json)
        file_paths = []
        for index, file in enumerate(r.json()["sounds"]):
            binary_data = base64.b64decode(file["data"])
            newpath = path
            if(path[-1] != "/" and path != ""):
                newpath+="/"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
            with open(f"{newpath}output{index}.mp3", "wb") as f:
                f.write(binary_data)
            file_paths.append(f"output{index}.mp3")
        return file_paths

class GMusicAsync:
    def __init__(self, token):
        self.token = token
        self.asession = AsyncHTMLSession()
    async def ask_async(self, prompt: str, generation_count = 2, path = ""):
        json = {
            "generationCount": generation_count,
            "input":{
                "textInput": prompt
            },
            "soundLengthSeconds": 30 # changing it wont affect anything, it will stay at 20 no matter what.
        }
        headers = {
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
        }
        r = await self.asession.post("https://content-aisandbox-pa.googleapis.com/v1:soundDemo?alt=json", headers=headers, json=json)
        file_paths = []
        for index, file in enumerate(r.json()["sounds"]):
            binary_data = base64.b64decode(file["data"])
            newpath = path
            if(path[-1] != "/" and path != ""):
                newpath+="/"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
            with open(f"{newpath}output{index}.mp3", "wb") as f:
                f.write(binary_data)
            file_paths.append(f"output{index}.mp3")
        return file_paths