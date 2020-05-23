f = open("file.txt",'rb+')
# f.write("Hello world"+"\n")
# f.flush()
# list1=[]
# count=0
# for line in f:
#     head = line.split(' ')[0]
#     list1.append(head)
#     if len(list1)==0:
#         count=1
#     else:
#         count=max(list1)
# print(count)

# print("======")
# print("文件偏移量位置:",f.tell())
# f.seek(5,0)
# data = f.read()
# print("读出来:",data)
# #
# # f.close()
# import time
# file01=open("my.log","a")
# conten= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# file01.write("1")
# file01.write(" ")
# file01.write(conten+"\n")
# time.sleep(2)
for line in f:
    head = max(line.split(' ')[0])
    print(head)