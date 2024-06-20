import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=3)
url=input('please paste your link here :')
qr.add_data(url)
qr.make(fit=True)
#here you can customize color.
img=qr.make_image(fill_color='#E2BBE9',back_color='#5A639C')
img.save('qrcode.png')
print('your qrcode is ready.')