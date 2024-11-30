#importing the cv2 library
import cv2

#name of the QRcode image file
filename="FVQR.png"

#read the QRcode image
image=cv2.imread(filename)

#initialize the qr code detector
detector=cv2.QRCodeDetector()

#detect and decode
data,vertices_array,binary_qrcode=detector.detectAndDecode(image)

if vertices_array is not None:
    print("Qrcode Data: ")
    print(data)
else:
    print("There was some error")