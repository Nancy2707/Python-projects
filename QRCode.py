#Installing package qrcode
pip install qrcode
#importing qrcode into our code
import qrcode as qr 
#qrcode package is aliased as qr
#importing required packages
from PIL import image
import qrcode as qr
from PIL import Image
#using QRCode feature of qrcode package to give specifications to our QRcode
QR=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=15,border=4)
#adding the data or the link which will be generated in the form of QRCode
QR.add_data("www.linkedin.com/in/nancy-sharma2707")
QR.make(fit=True)
img=QR.make_image(fill_color="green")
#giving the name of the image with extension which we want our qrcode to store as
img.save("linkedin.jpg")
