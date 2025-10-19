import cv2
import easyocr
import os
import random

input = 'Image'
thresold = 0.25

# img_path = "Image/OIP (1).jpg"


# img = cv2.imread(img_path)
# image_copy = img.copy()

# reader = easyocr.Reader(['en'])

# text = reader.readtext(img)


# for t in text:
#     bbox,txt,score = t
#     # print(bbox)
#     # print(txt)
#     # print(score)
#     # break
#     if score > thresold :
#         x1,y1 = int(bbox[0][0]), int(bbox[0][1])
#         x2,y2 = int(bbox[2][0]), int(bbox[2][1])
#         cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)    
#         cv2.putText(img, txt, (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)     


# img = cv2.resize(img,(640,480))
# image_copy = cv2.resize(image_copy,(640,480))
# cv2.imshow("image",img)
# cv2.imshow("image_01",image_copy)
# cv2.waitKey(0)




for file in sorted(os.listdir(input)):

    img = cv2.imread(os.path.join(input,file))
    reader = easyocr.Reader(['en'])
    img = cv2.resize(img,(640,480))
    text = reader.readtext(img)

    for t in text:
        bbox,txt,score = t
        if score > thresold :
            x1,y1 = int(bbox[0][0]), int(bbox[0][1])
            x2,y2 = int(bbox[2][0]), int(bbox[2][1])
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)    
            cv2.putText(img,txt,(int(bbox[0][0]),int(bbox[0][1])-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)     
    
    cv2.imwrite(f"test/{file}.png",img)