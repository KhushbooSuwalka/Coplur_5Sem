#---------------Qrcode image read----------------------------
# To import cv2 first install opencv-python using pip install opencv-python
import cv2
image=cv2.imread("Qr1.png")
detector=cv2.QRCodeDetector()
data,vertices_array,binary_qrcode=detector.detectAndDecode(image)
if vertices_array is not None and data:
    print("Decoded data:", data)
else:
    print("No data found in the QR code.")