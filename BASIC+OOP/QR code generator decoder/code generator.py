import qrcode
data='https://futurevisioncomputers.com/'
QrCode="FVQR.png"
QrImage=qrcode.make(data)
QrImage.save(QrCode)
