from mutagen.id3 import ID3, TIT2
import os

def setMetaData():

    path = "musicas"
    
    dirList = os.listdir(path)
    
    for musicName in dirList:
    
        path_file = os.path.join("musicas",musicName)

        filename, file_extension = os.path.splitext(path_file)

        if file_extension == '.mp3':
    
            tags = ID3(path_file)
        
            tags["TIT2"] = TIT2(encoding = 3, text=musicName)
        
            tags.save()

setMetaData()
