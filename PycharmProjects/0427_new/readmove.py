import  cv2
cap = cv2.VideoCapture('0612.mp4')
check, vid = cap.read()
counter = 0
check = True
frame_list = []
while check == True:
    cv2.imwrite('./face0/'+str(counter)+'.jpg', vid)
    check, vid = cap.read()
    frame_list.append(vid)
    counter+=1
frame_list.pop()
for frame in frame_list:
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) and 0xff == ord('q'):
        break
cap.release()
frame_list.reverse()
for frame in frame_list:
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) and 0xff == ord('q'):
        break