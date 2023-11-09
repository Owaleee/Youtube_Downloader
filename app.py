from pytube import YouTube

link = input("Qual o link do video que você quer baixar? ")
YouTube = YouTube(link)

video = YouTube.streams.get_highest_resolution()
video.download()
print('Done!!')

