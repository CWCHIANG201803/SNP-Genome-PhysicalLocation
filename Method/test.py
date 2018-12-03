import pathlib
import os
import re
import pathlib
import os.path

# 這個程式的目的是用來建立輸入檔案

rootPath='D:/workFolder/pgx/uniRsNum'

exp = r".*_(.*).txt"

fileList=os.listdir(rootPath)
print(fileList[0])

outputPath=os.path.join(rootPath,'result.txt')
outFile = open(outputPath,'w')
# 從檔案中擷取出來gene name
for file in fileList:
    # 透過regular expression擷取基因名字
    geneName=re.findall(exp,file)[0]
    # 串接檔案路徑
    filePath=os.path.join(rootPath,file)
    # 開啟檔案
    inFile = open(filePath,'r')
    # 迴圈用來讀取每個檔案
    while True:
        # 讀取一行
        line = inFile.readline()
        # 當line 為 true
        if not line:
            # 跳出
            break
        else:
            # 印出資料
            print("{0}\t{1}".format(geneName,line.split()[0]))
            outFile.writelines("{0}\t{1}\n".format(geneName,line.split()[0]))
    inFile.close()
outFile.close()