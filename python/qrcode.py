#pip install qrcode
import qrcode

img = qrcode.make("https://stren.com.br/")
img.save('qrcode-stren.jpg')