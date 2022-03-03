from pytube import YouTube
from moviepy.editor import *
from mutagen.id3 import ID3, TIT2

import os

# Função que realiza o download do vídeo do youtube em MP3 e salva na pasta
def ytDownload():
    
    # Abre o arquivo que realiza download do vídeo
    ytUrlLote = open("YT_URL_List.txt","r")
    
    # Pega o conteúdo do arquivo e separa em uma lista
    fileContent = ytUrlLote.read();
    UrlList = fileContent.split("\n")
    
    # Loop para cada url
    for url in UrlList:
        # valida se recebeu uma url
        if url != "":
            
            # instancia a url do youtube
            yt = YouTube(str(url))
            video = yt.streams.filter(only_audio=True).first()
            
            # diretorio onde será salvo
            dir_musicas = "musicas"
            
            # local de download
            out_files = video.download(output_path=dir_musicas)
            
            print("Musica baixada: " + yt.title)
                        
    converteMP4toMP3()
    
    
def converteMP4toMP3():
    
    path = "musicas"
    
    dirList = os.listdir(path)
    
    for musicName in dirList:
        
        filename, file_extension = os.path.splitext(musicName)
        
        filename = filename.replace("/","")
        
        if file_extension == ".mp4":
    
            mp4_without_frames = AudioFileClip(os.path.join("musicas",filename + file_extension))
            mp4_without_frames.write_audiofile(os.path.join("musicas",filename + ".mp3"))
            mp4_without_frames.close()
            
            os.remove(os.path.join("musicas", filename + file_extension));
        
            print("Música convertida para MP3 com sucesso")
            
            setMetaData(filename, filename + ".mp3")

def setMetaData(filename, musicName):
    
    path_file = os.path.join("musicas",musicName)
    
    tags = ID3(path_file)
    
    tags["TIT2"] = TIT2(encoding = 3, text=filename)
    
    tags.save()
    

ytDownload()
