# +--------------------------------------------------------------+
# | Size         | 1.63 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 602 bytes                                     |
# |--------------------------------------------------------------|
# | Created      | July 21st 2020, 13:45:14                      |
# |--------------------------------------------------------------|
# | Changed      | July 22nd 2020, 13:25:51                      |
# +--------------------------------------------------------------+
import threading
import os


def creatFolder(dir):
    try:
        os.mkdir(dir)
        print('文件夹已创建。')
    except:
        print('文件夹已存在。')


def getSourceLi(dir):
    fileLi = os.listdir(dir)
    return fileLi


def copyWork(sourceDir, destDir, fileName):
    sourcePath = sourceDir + '/'+fileName
    destPath = destDir + '/'+fileName
    with open(sourcePath, 'rb') as sf:
        with open(destPath, 'wb') as df:
            while True:
                data = sf.read(4096)
                if data:
                    df.write(data)
                else:
                    break


def filesCopy():
    sourceDir = r'C:\Users\86156\OneDrive\图片\Saved Pictures'
    destDir = r'C:\Users\86156\OneDrive\桌面\aim'
    creatFolder(destDir)
    fileLI = getSourceLi(sourceDir)
    print(fileLI)
    for fileName in fileLI:
        td = threading.Thread(
            target=copyWork, args=(sourceDir, destDir, fileName))
        td.start()


if __name__ == "__main__":
    filesCopy()
