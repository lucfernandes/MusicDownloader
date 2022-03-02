from logging.config import fileConfig
from mutagen.id3 import ID3, TIT2, ID3NoHeaderError
from mutagen.easyid3 import EasyID3
from pytube import YouTube
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
            
            # altera para o formato mp3
            filename, file_extension = os.path.splitext(out_files)
            new_file_name = filename + ".mp3"
            os.rename(out_files, new_file_name)
            
            print("Musica baixada: " + yt.title)
    
    # Inicia o tratamento das meta tags do arquivo baixado
    atualizaMetaTags()
    
    
# Função que realiza uma correção no metadados do mp3
def atualizaMetaTags():
    path = "musicas"

    # pega todos arquivos da pasta das musicas
    dirList = os.listdir(path)

    # loop para cada musica
    for musicName in dirList:
        
        filename, file_extension = os.path.splitext(musicName)
        
        # valida se é um mp3
        if(file_extension == ".mp3"):
            
            # diretorio até a musica
            dirMusic = path + "/" + musicName
                    
            try:
                
                # pega as tags do arquivo
                tags = ID3(dirMusic)
            
                # define as tags
                tags["TIT2"] = TIT2(encoding=3, text=filename)
                
                # salva as tags editadas
                tags.save()
                
            except ID3NoHeaderError:
                
                # TODO: Fazer a criação de um header para mp3 quando não tiver
                print(filename + " - Não foi processado")
                # mp3 = mutagenMp3import.MP3(dirMusic)
                
                
            
    print("Processamento finalizado")

ytDownload()
