from qrcode import QRCode
qr = QRCode(foreground_color="#424242")
qr.add_data("test")
img = qr.make_image()
img.save("test.png")
