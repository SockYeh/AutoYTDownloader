import requests, threading
from bs4 import BeautifulSoup

with open("urls.txt", "r") as f:
    ytids = f.read().splitlines()


def download(ytid):
    r = requests.get(f"https://www.yt-download.org/api/button/videos/{ytid}")
    soup = BeautifulSoup(r.text, "html.parser")

    link = soup.find("a")
    link = link.get("href")
    r = requests.get(link, allow_redirects=True)
    with open(f"{ytid}.mp4", "wb") as f:
        f.write(r.content)
    print(f"{ytid} downloaded")


for ytid in ytids:

    threading.Thread(target=download, args=(ytid,)).start()
