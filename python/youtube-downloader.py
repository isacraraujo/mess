#pip install pytube
from pytube import YouTube

link   = input("Input YouTube URL: ")
yt     = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))

for i in video:
    print(i)
print("Enter the Desired Option to Download the Format: ")

dn_option = int(input("Enter the Option: "))
dn_video  = videos[dn_option]
dn_option.download()
print("Download Successfully")