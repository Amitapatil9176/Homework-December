#1. sum of numbers upto n number
n=11
i=1
j=1
sum=0
sum1=0
while j<20:
    sum1=sum1+j
    j+=1
print(sum1)
# to print number from 1 to n
k=1
n1=int(input("enter any number"))
while k<=n1:
    print(k)
    k+=1
# t0 print table of any giveb number
g=1
g1=int(input("enter any number"))
while g<=10:
  print(g*g1)
  g+=1
# print number with skip of given number
o=0
o1=0
d=int(input("enter any number to skip by"))
d1=int(input("enter number for series"))
while o<d1:
   o1=o1+d
   print(o1)
   o+=1
# to print countdown of number
nt=int(input("enter any number"))
while nt>=1:
   print(nt)
   nt=nt-1
   # To reverse the number 
n=int(input("enter any number"))
rev=0
i=0
while n>0:
    i=n%10
    rev=rev*10+i
    n=n//10
print(rev)
#  to print even numbers upto n 
no=int(input("enter any number"))
i=1
while i<=no:
   if (i%2==0):
      print(i)
   i=i+1
# to print odd number upto n 
nm=int(input("enter number to series"))
i=1
while i<=nm:
   if (i%2!=0):
      print(i)
   i=i+1
# find factorial of given number
nm1=int(input("enter any number"))
fact=1
i=1
while i<=nm1:
    fact=fact*i
    i=i+1
print("factorial =",fact)
# to find number is palinndrome 
nu=int(input("enter any number"))
pal=nu
rev=0
re=0
while nu>0:
   re=nu%10
   rev=rev*10+re
   nu=nu//10
print(rev)
if (pal==rev):
   print("number is palindrome")
else:
   print(" number is not palindrome")
# to check number is armstrong or not
arm=int(input("enter any number"))
rm=1
sum=0
armo=arm
while arm>0:
    rm=arm%10
    sum=sum+(rm*rm*rm)
    arm=arm//10
print(sum)
if (armo==sum):
    print("armstrong number")
else:
    print("not armstrong")
# to count digits of given number
nc=int(input("enter any number"))
s=0
co=0
while nc>0:
  s=nc%10
  co=co+1
  nc=nc//10
print(co)
# to print fibonacci series upto n
a=0
b=1
sum=0
fb=int(input("enter value of n"))
print(a)
print(b)
i=1
while i<=fb:
   sum=a+b
   a=b
   b=sum
   i=i+1
   print(sum)
# to find sum of all numbers divisible by 3 or 5 upto n
nt=int(input("enter value of n "))
i=1
sum=0
while i<=nt:
    if(i%3==0)or(i%5==0):
        sum=sum+i
    i=i+1
print(sum)
# to find number is prime or not
pm=int(input("enter value of n "))
i=2
cnt=0
while i<pm:
   if(pm%i==0):
      cnt=cnt+1
   i=i+1    
if (cnt==0):
   print("prime number")
else:
   print("not prime") 
# to print pattern
i = 1
while i <= 4:  # Outer loop for rows
    j = 1
    while j <= 4 - i:  # Loop for leading spaces
        print('-', end='')
        j += 1
    
    k = 1
    while k <= 2 * i - 1:  # Loop for stars and trailing spaces
        print('*', end='')
        k += 1
    
    print()  # Move to the next line
    i += 1
# To print prime number series upto n
num=int(input("enter value of n "))
i=1
cot=0
while i<=num:
    j=2
    while j<i:
       
        if(i%j==0):
            cot+=1
            break
        j+=1
    if(cot==0):
      print(i,end=' ')
    else:
      cot=0
    i+=1
# to print prime number series
print("\n***************************")
n=int(input("enter valu of n"))
print(f"Prime numbers up to {n}:")
num = 1
while num <= n:
        is_prime = True
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            print(num, end=" ")
        num += 1
# to print sum of even numbers upto n
np=int(input("enter any number"))
i=0
sum_even=0
sum_odd=0
while i<=np:
    if(i%2==0):
        sum_even+=i
    else:
        sum_odd+=i
    i+=1      
print(f"sum of even numbers=",sum_even)
print(f"sum of odd numbers =",sum_odd)
# to print armstrong numbers upto n
na=int(input(" enter value of n "))
i=1
while i<=na:
    sum=0
    arm=i
    am=0
    while arm>0:
        am=arm%10
        sum+=am*am*am
        arm=arm//10
    
    if(sum==i):
        print(i,end=" ")
    i+=1
# to find minimum number
listo=[45,1,25,6,8,78,32,6,0.5]
min=listo[0]
le=len(listo)
i=1
while i<le:
    if(min>listo[i]):
        min=listo[i]
    i+=1
print("Minimum number of list is",min)
# to ascend number in the list
print("******************")
listo=[9,6,3,5,4,78,99,100,789,456]
m=0
let=len(listo)-1
i=0
while i<=let:
     j=0
     while j<=let:
          if(listo[i]<listo[j]):
               m=listo[j]
               
               listo[j]=listo[i]
               listo[i]=m
          j+=1
     i+=1
print(listo)
# To descend the list
listo=[11,2,45,100,1,99,55,24]
m=0
let=len(listo)-1
i=0
while i<=let:
     j=0
     while j<=let:
          if(listo[i]>listo[j]):
               m=listo[j]
               listo[j]=listo[i]
               listo[i]=m
          j+=1
     i+=1
print(listo)
