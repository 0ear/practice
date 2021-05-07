import cv2
im = cv2.imread('../img/cat.jpg')
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(im)
ss.switchToSelectiveSearchFast()
rects = ss.process()
print('候選區域總數量:', len(rects))
numShowRects = 100
increment = 50
while True:
    imOut = im.copy()
    for i, rect in enumerate(rects):
        if(i<numShowRects):
            x, y, w, h = rect
            cv2.rectangle(imOut, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
            print('rect:', rect)
            print('a:', a)
            print('準備進行裁切圖片')
            crop1 = imOut[y:y+h, x:x+w]
            cv2.imwrite('./crop/'+str(a)+'.png', crop1)
            a+=1
        else:
            break
    cv2.imshow('output', imOut)
    print('進行鍵盤狀態偵測')
    k = cv2.waitKey(0)
    if k == 109:  #只ASCII碼的109 為m
        numShowRects+=increment
    elif k == 108 and numShowRects>increment: #為l
        numShowRects-= increment
    elif k == 113: #為q
        break
    #cv2.imwrite('output1.png', imOut)