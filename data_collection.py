import os
import cv2
import time
import uuid

image_path = "raw_data"

labels = ["Hello","IloveYou" ,"No", "Please","Thank you", "Yes"]

number_of_images = 30


for label in labels:
    image_dir = os.path.join(image_path, label)
    os.makedirs(image_dir)

    cap = cv2.VideoCapture(0)

    print(f"Collecting images for {label}")
    time.sleep(2)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        imagename=os.path.join(image_path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(5)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()