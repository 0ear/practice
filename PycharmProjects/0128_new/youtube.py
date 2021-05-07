url = 'https://www.youtube.com/watch?v=fR9HCMxCZqk'
import pafy,cv2
vpafy = pafy.new(url)
play = vpafy.getbest(preftype = 'mp4')
cap = cv2.VideoCapture(play.url)
while(cap.isOpened()):
    ret, frame = cap.read()
    print('ret:', ret)
    print('frame:', frame)
    cv2.imshow('frame:', frame)
    cv2.imwrite('./mp4/' + str(a)+'.png',frame)
    a+=1
    k = cv2.waitKey(20)
    if k ==27:
        break
cap.release()
cv2.destroyWindow(())