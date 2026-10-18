#------------------QRCode----------------------
import os
import qrcode
# install qrcode using python -m pip install qrcode[pil]

# data="https://www.coplur.com/home"
# img=qrcode.make(data)
# img.save("Qr1.png")

data1={
    "qr2":"https://www.coplur.com/home",
    "name":"Coplur"
}
img1=qrcode.make(data1)
img1.save("Qr2.png")
