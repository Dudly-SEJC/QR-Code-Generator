import qrcode
from PIL import Image

Logo_link = 'csumb.png' #convert file to PNG file type
logo = Image.open(Logo_link).convert('RGBA') #converted to RGBA, to set alpha

basewidth = 100

wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))

logo = logo.resize((basewidth, hsize), Image.LANCZOS)

# Manipulating pixel colors in logo background to create transparency
logo_data = logo.getdata()
new_logo_data = []
for item in logo_data: #sets condition
    if item[:3] == (255, 255, 255):  # Sets white pixels to be manipulated
        new_logo_data.append((0, 0, 0, 255)) #manipulates white pixels to be transparent
    else:
        new_logo_data.append(item)  #if pixels are not white in logo, then don't change

logo.putdata(new_logo_data)

QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
url = 'https://csumb.edu/business/about/'

QRcode.add_data(url)

QRimg = QRcode.make_image(fill_color='black', back_color='papayawhip').convert('RGBA') #converted to RGBA

diff = (QRimg.size[0]-logo.size[0])//2, (QRimg.size[1]-logo.size[1])//2
QRimg.paste(logo, diff)
QRimg.save("mynewQRcodeTransparent.png")
img = Image.open("mynewQRcodeTransparent.png")
img.show()
