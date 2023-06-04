#Import YouTube library from pytube
from pytube import YouTube
#Access link from CLI
import sys  

link = sys.argv [1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()  #Customeize Option 2: get_audio_only 

yd.download(r'C:\Users\TowfNguyenx\Desktop\Media\YT Download')