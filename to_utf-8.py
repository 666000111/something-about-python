import argparse
import chardet
parser = argparse.ArgumentParser(description ="Name of the file")
parser.add_argument('-f','--file',required=True,type = str)
parser.add_argument('-k','--kind',default ='non',type = str)
args = parser.parse_args()
name = args.file
kind = args.kind
f = open(name,"rb")
str1 = f.read()
if kind == 'non':
    kind = chardet.detect(str1)['encoding']
    if kind == None :
        print("抱歉，无法解码该文件")
    else :
        if kind != 'utf-8':
            print("猜测该文件编码方式为"+kind)
            str1.decode(kind).encode("utf-8")
            fp = open("new_"+name,"wb")
            fp.write(str1)
            fp.close()
            print("转换完成")
        else :
            print("本文件已经是utf-8编码无需转化")
else :
    if kind == "utf-8":
        print("已经是utf-8编码方式的了")
    else :
        str1.decode(kind).encode("utf-8")
        fp = open("new_"+name,"wb")
        fp.write(str1)
        fp.close()
        print("完成转化")
f.close()

