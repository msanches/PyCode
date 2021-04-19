#pip install pytube3

#importa biblioteca
import pytube

url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download() # mesma pasta
# ou em outra pasta
#video.download('/Downloads')