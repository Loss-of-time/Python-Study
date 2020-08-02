from PIL import Image

im = Image.open('lib\\picture\\62549331_p0.jpg')
r,g,b = im.split()
r.show()
g.show()
b.show()