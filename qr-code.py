import qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)
qr.add_data('https://www.youtube.com/watch?v=l4ugfcj7qrI&list=PL7yh-TELLS1EgOLIPo1sVuf_rDPEp33S8&index=5&t=2s')
qr.make(fit=True)

img = qr.make_image()
img.save('qr-code.png')