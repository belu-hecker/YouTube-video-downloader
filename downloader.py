
from pytube import YouTube, Playlist

print ("***** You Tube video & playlist Downloader *****")
b = int(input("\nPress 1 for Single video and 2 for Playlist Download : "))

# for Video 

if b == 1:
  link = input("\n Enter The link : ")
  youtube_1 = YouTube(link)

  print(f" \n The title of the video is - {youtube_1.title} \n")

  # video = youtube_1.streams.all() for ALL FORMATS
  a = int(input(" Press 1 for Video and 2 for Audio! : "))

  if a == 1 :
    video = youtube_1.streams.filter(only_video=True, progressive= False)
    vid = list(enumerate(video))

    for i in vid:
      print (i)

    print()

    strm = int(input("Enter the Resolution tag  : "))
    print("\n Downloading ...... \n")
    video[strm].download()
    print("Done!")

  else:
    video = youtube_1.streams.filter(only_audio=True, progressive= False)
    vid = list(enumerate(video))

    for i in vid:
      print (i)

    print()

    strm = int(input("Enter the quality tag : "))
    print("\n Downloading ...... \n")
    video[strm].download()
    print("Done!")


#  For Playlist 
else: 
  c= input("Enter the playlist link : ")
  py = Playlist(c)
  o = int(input("Press 1 for Video and 2 for Audio : "))
  if o ==1:
    print(f"Downloading : {py.title}")
    for video in py.videos:
      video.streams.filter(only_video=True).first().download()
    
  else:
    print(f"Downloading : {py.title}")
    for video in py.videos:
      video.streams.filter(only_audio=True).first().download()



