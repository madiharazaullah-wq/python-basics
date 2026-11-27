# a=int(input("Enter a number "))
# if(a%2==0):
#     print("Number is even") 
# else:
#     print("Number is odd")

# if(a%5==0):
#      print("divisible by five") 
# else:
#      print("not divisible by five") 
# a=int(input("Enter a year "))
# if((a%4==0 and a%100!=0 ) or (a%400==0) ):
#     print("Leap year")
# else:
#       print(" not leap year")

# password="1234"
# username="admin"
# correct_password=(input("Enter a password: "))
# correct_username=(input("Enter a username: "))
# if(password==correct_password and username==correct_username ):
#     print("Login Successfully!")
# else:
#     print("Invalid credentials")

# print("-------Student Grading System-------")
# a=int(input("Enter a programming Marks: "))
# if(a<0 or  a>60):
#     print("invalid number")
# elif(a>=48 and a<=60):
#     print("A Grade")
# elif(a>=39 and a<=47):
#     print("B Grade")
# elif(a>=32 and a<=38):
#     print("C Grade")
# elif(a>=25 and a<=31):
#     print("D Grade")
# else:
#     print("F Grade")
# for i in range(1,101):
#     print(i)
# a=int(input("Enter a  number: "))
# sum=0
# for i in range(1,a):
#     sum=sum+i
# print(sum)
# a=int(input("Enter a number: "))
# i=1
# while a>0 and i<=10:
#     print(a,"*",i,"=",a*i)
#     i+=1
# print("----Calculator------")
# a=float(input("Enter a  number one: "))
# b=float(input("Enter a  number two: "))
# c=input("Enter a operator +,-,*,/,%: ")
# if(c=="+"):
#     print("The result is: ",a+b)
# elif(c=="-"):
#     print("The result is: ",a-b)
# elif(c=="*"):
#     print("The result is: ",a*b)
# elif(c=="/"):
#     if(b==0):
#         print("Cannot divide by zero")
#     else:
#         print("The result is: ",a/b)
# elif(c=="%"):
#     if(b==0):
#         print("Cannot divide by zero")
#     else: 
#         print("The result is: ",a%b)
# else:
#     print("Invalid Operator")
# a=int(input("Enter a number one: "))
# b=int(input("Enter a number two: "))
# c=int(input("Enter a number three: "))
# if(a<b+c and b<a+c and c<a+b):
#     print("Valid triangle")    
# else:
#      print(" Not Valid triangle")
# age=int(input("Enter your age: "))
# day=input("Enter a day in which you watch movie!!")
# if(age<5):
#     price=0
# elif(age>=5 and age<=17):
#     price=300  
# elif(age>=18 and age<=59):
#     price=500  
# else:
#     price=250

# if(day.lower()=="tuesday"):
#     discount=(price * 20/100)
#     actual_price=price-discount
#     print("Movie Price: ",actual_price)
# else:
#     print("Movie Price: ",price)
# balance=10000
# amount=int(input("Enter a amount: "))
# if(amount<=0):
#     print("Invalid amount")
# elif(amount>balance):
#     print("Insufficient Balance")
# elif(amount%500!=0):
#     print("Amount must be a multiple of 500")
# elif(amount<=balance):
#     balance-=amount
#     print("Amount is ",balance)
# else:
#     print("Try again")
# unit=int(input("Enter your bill units: "))
# if(unit<=0):
#     print("Invalid unit")
# elif(unit<=100):
#     bill=unit*10
# elif(unit<=200):
#     bill=1000 + (unit-100)*15
# else:
#     bill=2500 + (unit-200)*20

# print("Bill: ",bill)

# age=int(input("Enter your age: "))
# salary=float(input("Enter your salary: "))
# credit_score=int(input("Enter your credit score: "))
# if(salary>100000 and  age>=21 and age<=60 and credit_score>=600 and credit_score<650):
#     print("you are eligible for loan")
# elif((age>=21 and age<=60) and (salary>=50000) and (credit_score>=650)):
#     print("you are eligible for loan")
# else:
#     print("you are  not eligible for loan")

# num=int(input("Enter a number: "))
# if(num%3==0 and num%5==0):
#     print("FizzBuzz")
# elif(num%3==0):
#     print("Fizz")
# elif(num%5==0):
#     print("Buzz")
# else:
#     print(num)