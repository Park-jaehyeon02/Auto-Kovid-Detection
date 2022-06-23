import os
import shutil

propath = "./img_pro"
rawpath = "./img_raw"

li = os.listdir(propath)
li2 = os.listdir(rawpath)
for i in range(len(li)):
    li[i] = li[i].split('.')
    li[i] = li[i][0]
li2_n = []
for i in range(len(li2)):
    li2[i]=li2[i].split('.')
    li2_n.append(li2[i][0])
    
print(li,"\n",'='*200)
print(li2,"\n",'='*200)

for i  in range(len(li)):
    if li[i] in li2_n:
        idx = li2_n .index(li[i])
        shutil.copyfile(rawpath+'/'+li2[idx][0]+'.'+li2[idx][1],propath+'/'+li2[idx][0]+'.'+li2[idx][1])
