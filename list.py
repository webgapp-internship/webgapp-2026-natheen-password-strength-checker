# nums = [10, 20, 30, 40]

# for i in nums:
#     print(i)

# nums = [1, 2, 3, 4]
# rev = []

# for i in nums:
#     rev = [i] + rev

# print("Reversed:", rev)

# nums = [1, 2, 2, 3, 4, 4]
# unique = []

# for i in nums:
#     if i not in unique:
#         unique.append(i)

# print(unique)

# students = {}

# while True:
#     print("\n1. Add Student")
#     print("2. View Students")
#     print("3. Search Student")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         roll = input("Enter Roll No: ")
#         name = input("Enter Name: ")
#         mark = input("Enter Marks: ")

#         students[roll] = {
#             "name": name,
#             "mark": mark
#         }

#         print("Student Added!")

    
#     elif choice == "2":
#         if len(students) == 0:
#             print("No records found")
#         else:
#             for roll in students:
#                 print("Roll:", roll,
#                       "Name:", students[roll]["name"],
#                       "Marks:", students[roll]["mark"])

#     elif choice == "3":
#         roll = input("Enter Roll No: ")

#         if roll in students:
#             print("Found:", students[roll])
#         else:
#             print("Student not found")

   
#     elif choice == "4":
#         roll = input("Enter Roll No: ")

#         if roll in students:
#             del students[roll]
#             print("Deleted successfully")
#         else:
#             print("Student not found")

  
#     elif choice == "5":
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice")


# f = open("file.txt", "r")
# print(f.read())   # read full file
# f.close()
# f = open("file.txt", "w")
# f.write("Hello Natheen!!")
# f=open("file.txt","a")
# f.write("\nwelcome to python file handling")
# f.close()


# text="CodEkaTa"
# print(text.swapcase())

# name=input()
# result=""
# for i in name:
#     if i.islower():
#         result=result+i.upper()
#     elif i.isupper():
#         result=result+i.lower()
#     else:
#         result=result+i
# print(result)

# name="prakash raj"
# count=0
# for i in name:
#     count=count+1
# print(count)

# a=input("enter a day to tell holiday or not : ")
# x=a.lower()
# if x=="sunday" or x=="saturday":
#     print("it is holiday")
# else:    
#     print("it is not holiday")


# name="subash"
# unique=[]
# for i in name:
#     if i not in unique:
#         unique.append(i)
# print(unique)



# a=input("enter a word to check whether it is a palindrome : ")
# if a==a[::-1]:
#      print("yes it is a palindrome")
# else:    
#      print("no it is not a palindrome")


# import qrcode
# from PIL import Image
# data = "https://in.linkedin.com/"
# qr = qrcode.make(data)
# qr.show()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student("Ishwarya", 20)
# s2 = Student("Natheen",19)
# s1.display()
# s2.display()

# class Student:
#     college_name = "American"   # class variable

#     def __init__(self):
#         self.name = input ("enter your name")        # instance variable

#     def display(self):
#         print("Name:", self.name)
#         print("College:", Student.college_name)


# s1 = Student()
# s2 = Student()


# s1.display()
# print("-----")
# s2.display()     




# def is_strong_password(password):
#     # Conditions
#     if (len(password) >= 8 and
#         (c.isupper() for c in password) and
#         (c.islower() for c in password) and
#         (c.isdigit() for c in password) and
#         (c in "@#$%&!" for c in password)):
#         return True
#     return False


# # User input
# pwd = input("Enter your password: ")

# # Check password
# if is_strong_password(pwd):
#     print(" Strong password")
# else:
#     print(" Weak password - Please create a strong password")