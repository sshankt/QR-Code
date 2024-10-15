#import qrcode as qr

#image = qr.make("https://www.youtube.com/@user-ShashankTiwari123")

#image.save("shashank.youtube.png")

import qrcode

from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1 , error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10, border  = 4)
qr.make("https://erp.kcnitgroup.in/")

qr.make(fit = True)  

img = qr.make_image(fill_color = "red", back_color = "yellow" )  
img.save("Kcnit_web.png") 