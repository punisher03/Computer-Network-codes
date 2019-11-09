import random
#for error correction
#lab2
k=1
a=input("enter the binary string:")
while(2**k<k+len(a)+1):
       k=k+1       
s=len(a)+k
v=[]
for i in range (s):
   v.append(i+1)
b=[]
i=0 
w=0
for i in range(s):
   b.append(i+1)
for i in range(len(b)):
   if (2**i<len(b)):
       w=w+1
       b.remove(b[2**i-1])
       b.insert(2**i-1,"r")
for i in range(len(b)):
   if(b[i]!="r"):
       q=str(bin(b[i]))
       q=q[2:]
       b[i]=(k-len(q))*"0"+q 
p=0
o={}
u=1
for i in range(len(b)):
   if(b[i]!="r"):     
#        print(a[u])
       o[b[i]]=a[-u]
       u=u+1
#print(o)
red=[] 
f=1            
for i in range(len(b)):
   if (b[i]=="r"):
       p=p+1
       u=[]
       for keys in o.keys():
           if (keys[len(keys)-p]==str(1)):
               u.append(o[keys])
       #print(u)
       r=u[0]
       for j in range (1,len(u)):
           if(r==u[j]):
               r="0"
           elif (r!=u[j]):
               r="1"
#            print(r)
             
       red.append(r)
#print(o)
#print(b)
#print(red)   

final=[]
j=0
for i in range(len(b)):
   if(b[i]=="r"):
       final.append(red[j])
       j=j+1             
   else:
       final.append(o[b[i]])
final=final[::-1]
#print(final)         
bfinalt="".join(final)
print("The binary string that is going to transfer is:",bfinalt)  
a= random.randint(1,len(final))
#print("a is:",a)
if(final[len(final)-a]=="1"):
   final[len(final)-a]="0"
else:
   final[len(final)-a]="1"
finalt="".join(final)
print("The transferred bits is:",finalt)
o={}
for i in range (1,len(finalt)+1):
   q=str(bin(i))
   q=q[2:]
   q=(k-len(q))*"0"+q 
   o[q]=finalt[len(finalt)-i]
   
#print(o)
q=1
s=[]
pos=[]
while q<=k:
   s=[]
   for keys in o.keys():
       if(keys[len(keys)-q]=="1"):
           s.append(o[keys])
       
   q=q+1
   h=s[0]
   for i in range(1,len(s)):
       if(h==s[i]):
           h="0"
       else:
           h="1"
   pos.insert(0,h)

#print(pos)  
q="".join(pos)
position=int(q,2)
print("the error is at:",position)
if(final[len(final)-position]=="1"):
   final[len(final)-position]="0"
else:
   final[len(final)-position]="1"

print("the error is corrected:","".join(final))
