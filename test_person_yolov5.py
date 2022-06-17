import torch
import cv2
import time

print('start load model!!!')
model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)
model.conf = 0.5
model.iou = 0.4
print('load yolov5 successfully!!!')

st = None
cap = cv2.VideoCapture('rtsp://admin:888888@192.168.7.50:10554/tcp/av0_0')

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,360))
    if st == None:
        st = time.time()
    et = time.time()

    if et-st > 1:

        results = model(frame, size=640)
        out2 = results.pandas().xyxy[0]

        if len(out2) != 0:
            for i in range(len(out2)):
                output_landmark = []
                obj_name = out2.iat[i, 6]
                if obj_name == 'person' or obj_name == '0':
                    xmin = int(out2.iat[i, 0])
                    ymin = int(out2.iat[i, 1])
                    xmax = int(out2.iat[i, 2])
                    ymax = int(out2.iat[i, 3])

                    cv2.rectangle(frame,(xmin,ymin),(xmax,ymax),(0,255,0),2)
        st = time.time()
        cv2.imshow('f',frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()