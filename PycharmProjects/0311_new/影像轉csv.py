from PIL import Image
import os, sys, csv
import numpy as np
def createFilelist(myDir, format = '.jpg'):
    filelist = []
    #print(myDir)
    for root, dir, files in os.walk(myDir, topdown = False):
        print('root:', root)
        print('dir:', dir)
        print('files:', files)
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                filelist.append(fullName)
    return filelist
myFileList = createFilelist('./directory/')

for file in myFileList:
    #print(file)
    img_file = Image.open(file)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode
    #print(format)
    #print(mode)
    img_gray = img_file.convert('L')
    print('img_gray.size[0]:', img_gray.size[0])
    print('img_gray.size[1]:', img_gray.size[1])
    print(format)
    print(img_gray.mode)
    value = np.array(img_gray.getdata(), dtype = np.int).reshape(
        (img_gray.size[1], img_gray.size[0])
    )
    print(value)
    print()
    value = value.flatten()
    print(value)
    with open('img_pixels.csv', 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(value)