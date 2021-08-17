import numpy as np
import cv2
import winsound

classes = []
f=open('coco_names.txt','r')
classes=[line.strip() for line in f.readlines()]      #80개의 부류 이름을 파일에서 읽고,
colors=np.random.uniform(0,255,size=(len(classes),3)) #각 부류의 구분을 위해 난수로 각기 다르 색상을 지정

yolo_model=cv2.dnn.readNet('yolov3.weights','yolov3.cfg') #YOLOv3 모델 로딩. 여기서 자꾸 error 발생
layer_names=yolo_model.getLayerNames()     #네트워크의 모든 레이어 이름을 가져옴
out_layers=[layer_names[i[0]-1] for i in yolo_model.getUnconnectedOutLayers()] # 출력 레이어의 인덱스를 가져옴

def process_video():
    video=cv2.VideoCapture(0) # 웹캠 연결
    while video.isOpened():   # 웹캠이 연결된 동안 계속 구간 반복
        success,img=video.read() #웹캠 영상 획득 시도
        if success:              #웹캠 영상 획득 성공 시
            height,width,channels=img.shape
            blob=cv2.dnn.blobFromImage(img,1.0/256,(448,448),(0,0,0),swapRB=True,crop=False) #입력 영상을 Blob ObJ로 생성

            yolo_model.setInput(blob)    # 생성된 Blob Obj를 yolo에 입력.
            output3=yolo_model.forward(out_layers) #출력을 받아 저장

            class_ids,confidences,boxes=[],[],[]
            for output in output3: #바운딩 박스 정보 수집
                for vec85 in output:
                    scores=vec85[5:]
                    class_id=np.argmax(scores)
                    confidence=scores[class_id]
                    if confidence>0.5: #신뢰도가 50%이상인 경우만 취합
                        centerx,centery=int(vec85[0]*width),int(vec85[1]*height) 
                        w,h=int(vec85[2]*width),int(vec85[3]*height)
                        x,y=int(centerx-w/2),int(centery-h/2)
                        boxes.append([x,y,w,h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
                    
            indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)#NMS 알고리즘을 적용하여 주위 바운딩 박스에비해
                                                               # 최대를 유지 중인 것만 남김
                    
            for i in range(len(boxes)):#NMS 알고리즘을 통과한 바운딩 박스를 영상에 출력. 부류 이름과 확률 정보 포함
                if i in indexes:
                    x,y,w,h=boxes[i]
                    text=str(classes[class_ids[i]])+'%.3f'%confidences[i]
                    cv2.rectangle(img,(x,y),(x+w,y+h),colors[class_ids[i]],2)
                    cv2.putText(img,text,(x,y+30),cv2.FONT_HERSHEY_PLAIN,2,colors[class_ids[i]],2)

            cv2.imshow('Object detection',img)

            if 0 in class_ids:  #coco_names.txt에 사람(person)이 0번. 바운딩 박스 정보에 0이 있으면 영상에 사람이 포함되어 있음
                print('사람이 나타났다!!!')
                winsound.Beep(frequency=2000,duration=500)

        key=cv2.waitKey(1) & 0xFF
        if key==27: break  #[ESC] 입력시 루프 종료

    video.release()
    cv2.destroyAllWindows()

process_video()