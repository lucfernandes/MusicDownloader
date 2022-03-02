import os
from mutagen.id3 import ID3, TIT2


path = "musicas"

dirList = os.listdir(path)

for musicName in dirList:
    
    dirMusic = path + "/" + musicName
    musicWhitoutExt = musicName.split(".")
        
    tags = ID3(dirMusic)
    
    tags["TIT2"] = TIT2(encoding=3, text=(musicWhitoutExt[0]))
    
    tags.save()
    
    print(musicName)
