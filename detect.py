import sys, time, smtplib, os 
import cv2, PIL, numpy as np, matplotlib.pyplot as plt
from email.message import EmailMessage
from login_info import EMAIL, PASSWD


def capture_mailtruck():
    with open('model_files/obj.names', 'r') as f:
        classes = f.read().splitlines()

    net = cv2.dnn.readNetFromDarknet('model_files/yolo-obj.cfg', 'model_files/yolo-obj_final.weights')
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    cam = cv2.VideoCapture(0)

    while True:
        cam.set(cv2.CAP_PROP_BUFFERSIZE,1)
        img = cam.read()[1]
        result = model.detect(img)  #If detects USPS logo, returns tuple of 3 numpy arrays, else returns 3 empty tuples
        if type(result[0]) != tuple:
            send_email(img)
            return
        time.sleep(3)


def send_email(img):
    message = EmailMessage()
    message['Subject'] = 'YOUR MAIL IS HERE'
    message['From'] = EMAIL
    message['To'] = EMAIL

    cv2.imwrite('USPS_image.png',img)
    with open ('USPS_image.png', 'rb') as f:
        file_data = f.read()
        file_name = f.name
        message.add_attachment(file_data,maintype='image',subtype='png',filename='USPS_image.png')
        os.remove('USPS_image.png')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL, PASSWD)
        smtp.send_message(message)

capture_mailtruck()

