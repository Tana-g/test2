from pytube import YouTube
link = "https://youtu.be/lXz-Ypc7b9g"
yt = YouTube(link)
yt1 = yt.streams.get_highest_resolution()
yt1.download()
print('success')

