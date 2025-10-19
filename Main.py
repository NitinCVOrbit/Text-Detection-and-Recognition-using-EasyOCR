import cv2 
import easyocr
import random
import matplotlib.pyplot as plt
import os

thresold = 0.25

img_paths = os.listdir('Image')

## Read Image ##
input = f'Image/{random.choice(img_paths)}'

img = cv2.imread(input)

## Instance of Detector ##
reader = easyocr.Reader(['en'],gpu=False)

## Extract Text from Image ##
text = reader.readtext(img)

## Draw bbox on Text ##
# print(text)
for t in text:
    # print(t)
    bbox,txt,score = t
    if score > thresold :
        # print(bbox[0])
        x1,y1 = int(bbox[0][0]), int(bbox[0][1])
        x2,y2 = int(bbox[2][0]), int(bbox[2][1])
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)    
        cv2.putText(img,txt,(int(bbox[0][0]),int(bbox[0][1])-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)     
        print(txt)     

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()