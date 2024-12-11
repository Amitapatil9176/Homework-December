#1 calculator program
n=int(input("enter any number"))
print("************")
print("menu")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
a=int(input())
b=int (input())
print("**********")
for i in range(1,n):
    if (i ==1):
     print(a+b)
    elif(i==2):
       if(a>b):
        print(a-b)
       else:
         print(" substraction is in neagative")
    elif(i==3):
      print(a*b)
    elif(i==4):
      print(a/b)
    else:
      print("out of order")
#2 to find reverse of number
print("**********")
n1=int(input("enter any number"))
r=n1 
rev=0
for i in range(len(str(n1))):
  m=r%10
  rev=rev*10+m
  r=r//10
print(rev)
# 3 to find addition of even and odd digits of a number
print("******")
no=int(input("enter any number"))
e=0
o=0
for i in (str(no)) :
    if int(i)%2==0:
      e=e+int(i)
    else:
        o=o+int(i)
print("sum of evendigits =",e)
print (" sum of odd=",o) 
#4 to calculate fibonaccis series 
print("*******")
nt=int(input("enter any number"))
x=0
y=1
print(x)
print(y)
for i in range(nt):
  sum=x+y
  print(sum)
  x=y
  y=sum
# 5 to findhow many vowels in name and print
print("************")
a="amita"
s=0
list=['a','e','i','o','u']
for i in a:
    if (i in list):
        print(i)
        s=s+1
print(s)
# to output in line 0 1 2 3 4
print("************")
for i in range(5):
   print(i,end='')
#to print multiple of 3 
a=int(input("enter any number"))
b=int (input("enter another number"))
for i in range(b,0,-1):
    if i% 3==0:
        print(i)  

