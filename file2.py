'''a,b=0,1
while b<=10:
    print(b,end=',')
    a,b=b,a+b


no=int(input("Enter no= "))
if no>0:
    print("+ve")
elif no<0:
    print("-ve")
else:
    print("0")

'''
'''
w=['KIshan','Jay','Swaminarayan',"1234567"]
for i in w:
    print(i,"COUNT= "+str(len(i))+".")
for i in w[:]:
    if len(i)>6:
        w.insert(0,i)    
        print(i)
'''
'''
no=int(input("Enter no= "))
i,j=0,0
for i in range(2,no):
    for j in range(2,i):
        if i%j==0:
           break
    else:
        print(i)
'''
#class myenptyclass(int):print("class")
'''
def sqr(num):
    print(num*num)
sqr(4.444)
sqr(4.444)
sqr(645545647)
'''
'''
def fibo(number):
    result=[]
    a,b=0,1
    for i in range(0,number):
        result.append(a)
        #print(a, end=' ')
        a,b=b,a+b
    return result
no=int(input("Enter no= "))
print(fibo(no))
'''
