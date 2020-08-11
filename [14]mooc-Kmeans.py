import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans

def loadData(path):
    f = open(path,'rb')
    data = []
    img = image.open(f)
    m,n = img.size
    for i in range(m):
        for j in range(n):
            # 获取像素RGB
            x,y,z = img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
    return np.mat(data),m,n

imgData,row,col = loadData(r'lib\picture\62549331_p0.jpg')

# 对相近的像素进行聚类
label = KMeans(n_clusters=8).fit_predict(imgData)

# 将label由一维转换为二维
label = label.reshape([row,col])
pic_new = image.new('L',(row,col))
for i in range(row):
    for j in range(col):
        # 填充像素亮度,不同类的像素亮度不同
        pic_new.putpixel((i,j), int(256/(label[i][j]+1)))

pic_new.save('result-bull-4.jpg','JPEG')
print('完毕')