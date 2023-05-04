import pyqrcode
import png
from pyqrcode import QRCode
website="https://archive.org/"
myqrcode=pyqrcode.create(website)
myqrcode.svg("Random.svg",scale=8)
myqrcode.png("Random.png",scale=6)
