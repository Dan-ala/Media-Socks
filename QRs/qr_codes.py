import qrcode
#Generate the QR code
img = qrcode.make("http://190.9.217.44:7000/auth/login")

#Save the imng as an image file like (.jpg)
img.save('Media-Socks.jpg')