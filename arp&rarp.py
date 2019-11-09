import os
cmd = 'arp -a > out_file.txt'
os.system(cmd)
ip=input("Enter ip address to get mac= ")
filey=open("out_file.txt","r")
for i in filey.readlines():
    i=i.split()
    if len(i)>=2:        
        if ip==i[0]:
            print(i[1])
            break
filey.close()
mac=input("Enter mac address to get ip= ")
filey=open("out_file.txt","r")
for i in filey.readlines():
    i=i.split()
    if len(i)>=2:   
        if mac==i[1]:
            print(i[0])
            break
filey.close()



