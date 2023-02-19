from instagrapi import Client
import os
import platform
from PIL import Image, ImageDraw, ImageFont
from instagrapi.types import Usertag, Location
import requests
import textwrap
import time
cl = Client()
cl.login("thenewssage", "u4njF!kAt4Di7SF")
key = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8127727ffc49478ab6685dd16fadc301"
NewsList = []
News = requests.get(key).json()
if platform.system() == "Windows":
    style = ImageFont.truetype("arialbd.ttf", 34)
else:
    style = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf:", 31)
Heading = News['articles']
description = News['articles']
i = 0
while True:
    Heading = News['articles'][i]["title"]
    if Heading not in NewsList:
        NewsList.append(Heading)
        description = News['articles'][i]["description"]
        Url = "Read the complete news from here:- ",News['articles'][i]["url"]
        textx = textwrap.fill(text=Heading, width=27.5)
        scnd = time.localtime().tm_sec
        Eimg = Image.open('Main.jpg') 
        d = ImageDraw.Draw(Eimg)
        d.text((50, 225), textx, font=style, fill="black")
        pathName = f"{scnd}img.jpg"
        Eimg.save(pathName)
        cl.photo_upload(path=pathName, caption=description, location=Location(name="India, Kerala"))
        print("In Sleep will post again in 45 seconds.. Please be patient")
        if platform.system() == "Windows":
            os.system(f"del {pathName}")
        else:
            os.system(f"rm -rf {pathName}")
        print(f"Value of i is {i}")
        print("In sleep mode will wake in 45 seconds...!")
        time.sleep(45)
        i = i+1    
        if len(NewsList) == 20:
            NewsList.clear()
        if i == 9:
            i = 0
    else:
        print("Checking For Latest News")
        print("No Latest News Found")
        i = 0
        time.sleep(3.5)