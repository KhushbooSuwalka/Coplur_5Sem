#------------------QRCode----------------------
import os
import qrcode
data="https://www.coplur.com/home"
img=qrcode.make(data)
img.save("Qr1.png")
# data1={
#     "qr2":"https://www.coplur.com/home",
#     "name":"Coplur"
# }
# img1=qrcode.make(data1)
# img1.save("Qr2.png")


#---------------Qrcode image read----------------------------
# To import cv2 first install opencv-python using pip install opencv-python
# import cv2
# image=cv2.imread("Qr1.png")
# detector=cv2.QRCodeDetector()
# data,vertices_array,binary_qrcode=detector.detectAndDecode(image)
# if vertices_array is not None and data:
#     print("Decoded data:", data)
# else:
#     print("No data found in the QR code.")