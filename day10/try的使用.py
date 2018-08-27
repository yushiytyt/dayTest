# coding=utf-8
import time
# import xlrd
try:
    f = open("tt1.txt")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                print("文件读取完毕")
                break
            time.sleep(1)
            print(content)

    except Exception as e:
        print(e)
        pass
    finally:
        f.close()
        time.sleep(1)
        print("关闭文件")
except Exception as e:
    print(e)
    print("没有这个文件")
