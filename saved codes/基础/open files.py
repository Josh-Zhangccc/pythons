text='jj\ngg'
print(text)

my_file=open('pythontxt.txt','a')#write可改动，打开形式
#'a',appecd,追加,即是在文件末尾添加内容
#'w',write,写入，即是覆盖原有内容
#'r',read,只读，即是不能改动原有内容
#'r+',read and write,读写，即是可以改动原有内容
#'w+',write and read,写入和读，即是覆盖原有内容
#'a+',append and read,追加和读，即是在文件末尾添加内容
#'x+',create and read,创建和读，即是创建一个新文件并读取
#'x',create,创建，即是创建一个新文件
#'wb',write binary,写二进制
#'xb',create binary,创建二进制
#'b',binary,二进制
#'t',text,文本，即是文本文件
#'at',append text,追加文本
#'rt',read text,读文本
my_file.write(text)

#read 只读
append_text=','
my_file.write(append_text)#加
my_file.close()
f=open('pythontxt.txt','r')
content=f.read()#read全部读取
f.close()
print(content)
#file.readline只读第一行，随后2，3，···
#read.readlines全部读取,但是列表
