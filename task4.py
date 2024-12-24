#To print datatype of variables
b=55.5
print(b,type(b))
a=12
print(a,type(a))
c=55+3j
print(c,type(c))
d='amita'
print(d,type(d))
bol=True
print(bol,type(bol))
li=[22,55,88,33,66,'amita',3.14]
print(li,type(li))
se={1,5,8,9,7,3,4,6,3,3,44,3.3,5.6,'a'}
print(se,type(se))
dict={'Name':'Amita','Age':33,'City':'Kolhapur'}
print(dict,type(dict))
tu=(99,88,77,66,55,55.6,8.8,'a')
print(tu,type(tu))
# program for to do simple arithmatic operation
n=int(input("enter any number"))
n1=int(input("enter second number"))
print("Addition=",n+n1)
print("Substraction=",n-n1 if n>n1 else n1-n)
print("Multiplication=",n*n1)
print("Division=",n/n1 if n>n1 else n1/n)
# Write a program to convert temperature from fahrenheit to celcius and vice versa
T=float(input("Enter temperature in celcius"))
F=float(input("Enter temperaturein farhenite"))
t=((F-32)*5)/9
f=(9*T+160)/5
print("Temperature in celcius=",t)
print("Temperature in fahrenite=",f)
#Condition flow
#Check number is even or odd
num=int(input("Enter any number"))
print(num,"is Even" if num%2==0 else "is Odd")
#To check given character is vowel or consonant
vo={'a','e','i','o','u','A','E','I','O','U'}
l=input("enter a character  ")
if(l in vo ):
            print("Vowel")
elif(l==' '):
            print("enter character")
else:
    print("Consonant")
#find what grade estudent got
marks=int(input("Enter marks of student"))
if(90<=marks<=100):
    print("Grade A")
elif(80<=marks<=89):
    print("Grade B")
elif(70<=marks<=79):
    print("Grade C")
elif(60<=marks<=69):
    print("Grade D")
else:
    print("Fail")
# Lists
# program to calculate sum of all elements of lists
lit={11,22,33,44,55,66,77,88,100}
sum=0
for i in lit:
    sum+=i
print("Sum of all elements=",sum)
# Find largest number from list
lis=[55,98,75,63,35,23,41,151]
m=lis[0]
temp=0
l=len(lis)-1
while(l>=1):
    if(m<lis[l]):
        temp=lis[l]
        lis[l]=m
        m=temp
    l=l-1
print("Largest number is ",m)       
# write a program to reverse elements of list
lt=[25,29,52,88,55]
i=0
temp=0
ln=len(lt)-1
while(i<ln):
    if(i<(ln-i)):
       temp=lt[i]
       lt[i]=lt[ln-i]
       lt[ln-i]=temp
    i+=1
print(lt)
lt1=[98,78,45,63,37,21]
print(lt1[::-1])

# for Loop
# write a program to calculate factorial of number
f=int(input("enter number"))
fact=1
i=1
while(i<=f):
    fact=fact*i
    i+=1
print("Factorial=",fact)
fac=1
for i in range(1,f+1):
    fac=fac*i
print("Factorial of number is",fac)
# Write a program to create multiplication table of given number
mp=int(input("Enter number"))
k=1
while(k<=10):
    print(k*mp)
    k+=1
for k in range(1,11):
    print(k*mp)
# Write a program to find sum of squares of n natural numbers
no=int(input("Enter number"))
su=0
for i in range(1,(no+1)):
    su=su+i*i
print(f"Sum of squares of {no} natural numbers is=",su)
adi=0
i=1
while(i<=no):
    adi+=i*i
    i+=1
print("Sum of squeares=",adi)
# Write program to reverse number
n=int(input("Enter number to reverse"))
ny=n
st=str(n)
lg=len(st)
i=lg
rem=0
while (i>0):
    nr=n%10
    rem=rem*10+nr
    n=n//10
    i=i-1
print("Reverse of number",rem)
rm=0
for j in range (0,lg):
     g=ny%10
     rm=rm*10+g
     ny=ny//10
print("Reverse=",rm)
# Generate the fibonacci series
x=0
y=1
fb=0
z=int(input("Enter number to series "))
print(x,y,end=' ')
i=0
while(i<z):
     fb=x+y
     print(fb,end=' ')
     x=y
     y=fb
     i+=1
x1=0
y1=1
bf=0
print("\n",x1,y1,end=' ')
for j in range(z):
      bf=x1+y1
      print(bf,end=' ')
      x1=y1
      y1=bf
#dictionaries
#To merge dictionaries 
dic={'name':'Amita','Age':33}  
dic1={'City':'Warana','Degree':'BCS'} 
dic.update(dic1)
print(dic)
print(dic1)
sti=input("Enter any word ")
nl=len(sti)
listi=[]
for i in sti(nl):
    listi[i]=i
print(listi)
