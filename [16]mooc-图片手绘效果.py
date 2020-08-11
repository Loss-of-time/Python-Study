# 照着做的数学部分完全不懂
import numpy as np
from PIL import Image


def draw(inPath='', outPath=''):
    a = np.asarray(Image.open(inPath).convert('L')).astype('float')

    depth = 36
    grad = np.gradient(a)
    gradX, gradY = grad
    gradX = gradX*depth/100.0
    gradY = gradY % depth/100.0
    A = np.sqrt(gradX**2+gradY**2+1.0)
    uniX = gradX/A
    uniY = gradY/A
    uniZ = 1.0/A

    vecEl = np.pi/2.2
    vecAz = np.pi/4.0
    dx = np.cos(vecEl)*np.cos(vecAz)
    dy = np.cos(vecEl)*np.sin(vecAz)
    dz = np.sin(vecEl)

    b = 255*(dx*uniX+dy*uniY+dz*uniZ)
    b = b.clip(0, 255)

    im = Image.fromarray(b.astype('uint8'))
    im.save(f'{outPath}')


draw(r"C:\[User]Quick\QQ图片20200809181830.jpg", './out/draw.jpg')
