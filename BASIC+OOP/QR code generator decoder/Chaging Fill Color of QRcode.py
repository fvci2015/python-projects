import qrcode
data="https://www.google.com/"
QrCodeFile="QR code generator decoder/Changing Fill Color QrCode.png"
qrObject=qrcode.QRCode()

qrObject.add_data(data)

qrObject.make()
image=qrObject.make_image(fill_color='red')
image.save(QrCodeFile)