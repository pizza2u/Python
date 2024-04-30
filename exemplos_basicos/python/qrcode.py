import pyqrcode
import png

from pyqrcode import QRCode

QRString = 'https://www.linkedin.com/in/sara-n%C3%B3brega-4a08a6265/'

url = pyqrcode.create(QRString)

url.png('qr.png',scale=8)
