import os
import zipfile

path='C:/Users/Yijun Ma/Desktop/tiger'
f=os.listdir(path)

for i in f:
    with zipfile.ZipFile(path+'/'+i,"r") as z:
        z.extractall(path)