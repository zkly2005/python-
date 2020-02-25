name=input("输入要转换的字符串:")
name_list=[]
for i in name:
    name_list.append(i)
for i in range(len(name_list)):
    if ord(name_list[i]) in range(65,91):
        name_list[i]=chr(ord(name_list[i])+32)
    elif ord(name_list[i]) in range(97,123):
        name_list[i]=chr(ord(name_list[i])-32)
sep=""
print(sep.join(name_list))
