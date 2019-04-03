import requests
import bs4
import urllib.parse
import youtube_dl

res=requests.get('https://www.youtube.com/results?search_query=machine+learning+vs+artificial+intelligence')
data=bs4.BeautifulSoup(res.text,'lxml')
final_links=[]
for link in data.find_all('a',href=True):
    if link['href'][0:7]=='/watch?':
        final_links.append(link['href'])
print(final_links)      

download_link=urllib.parse.urljoin('https://www.youtube.com/', final_links[0])
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([download_link])
https://www.dotnetcurry.com/nodejs/1422/store-binary-using-mongodb-gridfs
        