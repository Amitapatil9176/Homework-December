#1. To find year is leap or not
year=2022
if year%4==0:
    print("it is a leap year")
elif year%400==0:
 print("it is a leap year")
else:
   print("it is not a leap year")
#2.find larger number
n1=20
n2=5
n3=180
if(n1>n2):
   if(n1>n3):
      print("n1 is larger")
   else:
      print("n3 is larger")
elif(n2>n3):
   print(" n2 is larger")
else:
   print(" n3 is larger")
#3.find smaller number
no=15
no1=33
if(no>no1):
   print("number2 is smaller")
else:
   print(" number 1 is smaller")
           
#4.find temperature
temp=30
if(temp>30):
   print(" hot temperature")
elif(30>=temp>=15):
   print("warm temperature")
else:
   print("cold temperature")
#5. find letter is vowel or not
list =['a','e','i','o','u','A','E','I','O','U']
l='b'
if(l in list):
      print(" letter is vowel")
else:
      print("letter is consonant")
#6. find number is odd or even
nu = 52
if(nu % 2 == 0):
         print("number is even")
else:
         print("number is odd")
#7.find Driving eligibility
age=25
if(age>=18):
     print(" age is valid for driving")     
else:
     print("age must be greater than 18")
#8.To check grade of student
score=89
if(90<=score<=100):
   print("grade A")
elif(70<=score<=89):
    print("grade B")
elif(50<=score<=69):
    print("grade C")
else:
    print("grade F")
#9.to find divisibility of number by 3 and 5 or both
nm=14
if(nm%3==0):
   if(nm%5==0):  
    print("number is divisible by both 3 and 5")
   else:
       print(" number is divisible by 3")
elif(nm%5==0):
   print(" number is divisible by 5") 
else :
   print(" number is not divisible by 3 and 5")
#10. check number is positive or negative
num=-20
if(num<0):
    print("number is negative")
elif(num==0):
         print("number is zero")
else:
    print("number is positive")
#11.Traingle validation
s1=15
s2=20
s3=40
if(s1+s2>s3)and(s1+s3>s2)and(s2+s3>s1):
     print("these sides makes an triangle")
else:
     print("these sides doesn't make any traingle")    
#12.calculate tax based in salary
salary=2500000
if(salary<=500000):
    print("tax is 5% ")
elif(500000<salary<=1000000):
    print("tax is 10%")
else:
    print("tax is 20%")
#13. check number is greater than 10 and divisible by 2
p=25
if (p>10):
    if (p%2==0):
        print("number is greater than 10 and divisible by 2")
    else :
        print("number is greater than 10 but not divisible by 2")
else :
    print("number is not greater than 10")
#14. logical OR check
p1=23
if (p1<5)or(p1>20):
    print("done")
else:
    print("not done")
#15.Elecrticity bill
use=250
if(use<=100):
    print("bill=",use*5)
elif(100<use<200):
    print("bill",use*10)
else:
    print("bill",use*20)
#16.  categorize age
ag=65
if(0<=ag<=12):
  print("child")
elif(12<ag<=19):
    print("Teen")
elif(19<ag<=59):
    print("Adult")
else:
    print("Senior citizen")
#17. season finder
mo="november"
if(mo=="December")or(mo=="january")or(mo=="february"):
    print("Winter")
elif(mo=="march")or(mo=="april")or(mo=="may"):
    print("Spring")
elif(mo=="August")or(mo=="july")or(mo=="june"):
    print("Rainy")
elif(mo=="september")or(mo=="octomber")or(mo=="November"):
    print("Autumn")
else:
    print("invalid option")  
#18. Categorize BMI
wt=20
if(wt<18.5):
    print("underweight")
elif(18.5<=wt<=24.9):
    print("Normal")
elif(24.5<wt<=29.9):
    print("Overweight")
else:
    print("Obesity") 
#19. check given character is alphabet or digit or special character
ch='100'
if('a'<=ch<='z') or ('A'<ch<='Z'):
  print("letter is alphbet")
elif('0'<ch<'9'):
    print(" letter is digit")
else:
    print("it is special character")
#20. password validation
pas='amitapa'
if(len(pas)==8):
    if('@'in pas):
        print("vaild password")
    else:
        print(" please add @ sign in yoyr password")
else:
    print(" password contains 8 letters")





 







