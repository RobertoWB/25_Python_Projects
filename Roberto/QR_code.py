import qrcode

data = "Don't forget to keep fighting"

#img = qrcode.make(data)
#When working with urls always change the backslash for the frontslash
#img.save('C:/Users/Roberto W/Documents/save/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'cyan')
img.save('C:/Users/Roberto W/Documents/save/myqrcode2.png')