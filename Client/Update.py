import os
import requests
from zipfile import ZipFile



def DownloadFile(URL):

    Request = requests.get(URL, allow_redirects=True)

    open('Update.zip', 'wb').write(Request.content)

def UpdateApp():
    DownloadFile("https://archive.org/download/update_20230223/Update.zip")

    with ZipFile('Update.zip', 'r') as f:
        f.extractall()
        
    exit()