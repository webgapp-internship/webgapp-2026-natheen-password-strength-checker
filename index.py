# a=int(input("enter the number :"))
# b=int(input("enter the number"))
# c=a+b
# print(c)
# a=int(input("enter a number"))
# if a>50:
#    print("i am pass")
# elif a<50:
#     print("i am fail")
# else:
#     print("not valid")
# password="ns200"
# x=input("enter the password")
# if(x==password):
#     print("logoin successfully")
# else:
# #     print("error")
# x=int(input("enter a number"))
# if(x%2==0):
#     print("even")
# else:
#     print("odd")
# x=input("enter your")
# if(len(x)>7):
#     print("name is too longer")
# elif(len(x)<7):
#     print("name is too shorter")
# else:
#     print("name is correct")
# name=input("enter your name")
#  count=0
# for i in name:
    #  print(i)
#     count=count+1
# print(count)
#  monthlysal=int(input("enter the montly salary:"))
#  yearlysal=int(input("enter the yearly salary:"))
#  if monthlysal>=30000 and yearlysal>=40000:
#      print("eligible for loan")
#  else:
#       print("not eligible for loan")
# check grade
# mark=int(input("enter the mark:"))
# if mark>90:
#     print("grade s")
# elif mark>80 and mark<90:
#     print("grade a")
# elif mark>65 and mark<80:
#     print("grade b")
# elif mark>40 and mark<65:
#     print("grade c") 
# else:
#  print("fail")
# vowels="aeiou"
# username=input("enter your name:")
# count=0
# for i in username:
#     if i in vowels:
#         count=count+1
# print(count)
# email="natheen2000@gmail.com"
# if '@gmail.com' in email:
#     print("Your email is valid")
# else:
#     print("Enter correct email")
# s1="ac30bc40"
# letter=""
# digits=""
# for i in s1:
#     if i.isalpha():
#         letter=letter+i
#     elif i.isdigit():
#         digits=digits+i
# print(letter)
# print(digits)
# sumdigits=0
# for k in digits:
#     sumdigits=int(k)+sumdigits
# newchar=letter+str(sumdigits)
# print(newchar)
# num=int(input("enter a number"))
# count=0
# for i in range(num,0,-1):
#     count=count+i
# print(count)

# def add(a,b):
#     c=a+b
#     print(c)
# add(10,30)

# def check_password_strength(pwd):
#     import re
#     if (len(pwd) >= 8 and
#         re.search(r"[A-Z]", pwd) and
#         re.search(r"[a-z]", pwd) and
#         re.search(r"[0-9]", pwd) and
#         re.search(r"[!@#$%^&*()_+]", pwd)):
#         return "Strong"
#     return "Weak"

# print(check_password_strength("Hello123"))  # Strong


# correct_user = "admin"
# correct_pass = "1234"

# while True:
#     user = input("Enter username: ")
#     pwd = input("Enter password: ")

#     if user == correct_user and pwd == correct_pass:
#         print("Login Successful")
#         break
#     else:
#         print("Wrong credentials, try again!")


# rows = 5
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()
