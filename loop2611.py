animals=['dog','cat','bird']
for index,animals in enumerate(animals):
    print(f"{index}:{animals}")
# to print range
print("******")
for i in range(5,2,-1):
     print(i)
#1.to print even numbers to n
print("******")
n=15
for i in range(n):
    if i%2==0:
        print(i)
#2 to print odd numbers
print("******")
for i in range(1,25):
    if i % 2!=0:
        print(i)
#3 to print palindrome number
print("******")
n=1002001
b=n
r=0
for i in range(len(str(n))):
 a=n%10
 r=r*10+a
 n=n//10
print(r)
print(b)
if b!=r:
    print("number is  not palindrome")
else :
    print("number is  palindrome")
#4 to print number series divisible by 5 
print("******")
for i in range(50,1,-1):
    if i % 5==0:
        print(i)
#5 to print pattern
print("******")
for i in range(10):
    if i%2==0:
     print("E*")
    else:
        print("O*")
#6 to check number contain how many even and odd numbers
print("******")
no="2222"
e=0
o=0
for i in no :
    if int(i)%2==0:
      e=e+1
    else:
        o=o+1
print("even=",e)
print ("odd=",o) 
#7 print elements of number
print("**********")
n="513689"
for i in n:
    print(i)
#8 to check sum of digits of number is divisible by 2
num="5684"
su=0
print("**********")
for i in num:
    su=su+int(i)
print(su)
if (su%2==0):
    print("sum is divisible")
else:
    print("sum is not divisible")
# 9 find table of given number
print("**********")
b=int(input("enter number to form table"))
for i in range(1,11):
    print(b*i)
# 10 to find cube of number series
print("**********")
t=int(input("enter number to form cube series"))
for i in range(1,t+1):
    s=i*i*i
    print("cube of",i,s)

