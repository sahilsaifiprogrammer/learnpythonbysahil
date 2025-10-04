                    # python start

# print("Sahil")
# age=20
# if(age==20):
#     print("sahil")





                # if-else in python


# a=int(input("enter your age"))
# print("your age is",a)
# if(a>18 ):
#     print("you can drive")
#     if(a>60):
#      print("soory you are old because you are",a,"of age so you are old")
#     elif(a==60):
#         print("you are",a)
# elif(a==18):
#     print("you can also drive")


# else:
#     print("you can not drive")
# print("i am happy now")






            # strings in python


# a="saifi sahil saifi"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("sahil","harry"))
# print(a.split(" "))
# print(a.capitalize())
# print(a.count("saifi"))
# print(len(a.center(50)))
# str="my name is sahil"
# print(str.endswith("sahil",2,25))
# str1="he's name is dan.he is an honest man"
# print(str.find("is"))
# # print(str.index("ishh"))
# str3="welcome to the console"
# print(str3.isalnum())    # if alphabet h to hi true dega varna false dega
# str4="welcome00"
# print(str4.isalpha())   #if alpha bet h to hi false dega varna true--->alphabet jaise 1,2,78,
# str5="hello world"
# print(str5.islower())   #if sare lower case me honge to hi true return karega varna false return karega
# str6="we wish you a merry christmas"
# print(str6.isprintable()) # if \n ya \t ya esa kuch ni hoga to hi true return karega varna false
# str7='''      '''
# print(str7.isspace())   # if space hogi to hi true return hoga
# str8="we wish you a merry christmas"
# print(str8.istitle())  # sare word capitalize hoge to true varna false return
# str9="python wish you a merry christmas"
# print(str9.startswith("python"))
# str10="python wish you a merry christmas"
# print(str10.swapcase())
# str11="python wish you a merry christmas"
#  # sare first number capitle kar dega 
# print(str11.title())






        


        #match case

# x=int(input("enter te value of x"))
# match x:
#     case 0:
#         print("case is 0")
#     case 1:
#         print("case is 1")
#     case _ if x!=18:
#             print(x,"sorry is not equal 18")
#     case _:
#           print("wrong number")



                            #for loops in python


# name="sahilsaifi"
# for i in name:
#     print(i,",")
#     if(i=="l"):
#         print("this is something special")






# colors=["red","blue","purple","pink"]
# for color in colors:
#     print(color)
#     if(color=="red"):
#         print("this is a special color")
#     elif(color=="blue"):
#         print("this is very bad color")




# for k in range(1,5):
#     print(k)



# for k in range(6,10,20):
#     print(k)
    


# for k in range(5):
#     print("sahil")
        



                                        # while loops





# i=0
# while(i<3):
#     print(i)
#     i=i+1
#print("done with a loop")


# i=int(input("enter any number"))
# print("if you dial under 38 so you are wrong")
# while(i<=38):
#     i=int(input("enter any number"))
#     print(i)
# print("you chose write")    




        # import time in python

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# a=(input("enter your name"))
# print("hii",a)









                    # oops in python


                        # simple class in python

# class sahil:
#     name="harry"
#     networth=10
#     def display(self):
#         print(f"{self.name} have networth {self.networth} rupee")
# a=sahil()
# a.display()



                     # constructor in python

# class sahil:
#     def __init__(self,name,id,salary):         //define cons
#         self.name=name
#         self.id=id
#         self.salary=salary

#     # def display(self):
#     #     print(self.name)
#     #     print(self.id)    ya to ye ya fir niche wala
#     #     print(self.salary)   
#     def display(self):
#         print(f" the name is {self.name} and thi id {self.id} and the salary is {self.salary}")
# a=sahil("sahilsaifi",1,20000)
# a.display()




                # decoraters is python

# def greet(fx):
#     def mfx():                            //define decorators
#         print("good morning")
#         fx()
#         print("thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("hello world")

# def add(a,b):
#     print(a+b)

# add(12,13)
# a=hello()



                 # getter and setter in python 

# class myclass:
#     def __init__(self,value):
#         self.value=value
    
#     def show(self):
#         print(f"the value is {self.value}")
    
#     @property
#     def ten_value(self):            //getter
#         return 10 *self.value

#     @ten_value.setter
#     def ten_value(self,new_value):          //setter
#         self.value=new_value/10
# obj=myclass(50)
# obj.ten_value=100
# print(obj.ten_value)
# obj.show()




                # inheritence in python


# class worker:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def show(self):
#         print(f"the id is {self.id} and the name is {self.name}")

# class programmer(worker):         //inherit properties of worker
#     def print(self):
#         print("i am a programmer not a worker")


# a=programmer("sahil",12)
# a.show()
# b=programmer("suhel",13)
# b.show()
# b.print()





            # access modifier in python




# class student:
#     def __init__(self):
#         self.__name="sahilsaifi"    //now this is private using __
# a=student()
# print(a.name)        //cannot be accesed error throw
# print(a._student__name)  //can be accessed sure




                        # snake water gun game i python



# import random
# def check(comp,user):
#     if comp==user:
#         return 0
#     if(comp==0 and user==1):
#         return -1
#     if(comp==1 and user==2):
#         return -1
#     if(comp==2 and user==0):
#         return -1
#     return 1
    
# comp=print(random.randint(0,2))
# user=int(input("0 for snake ,1 for water and 2 for gun"))
# score=check(comp,user)
# print("you",user)
# print(comp,comp)
# if(score==0):
#     print("its a draw ")
# elif(score==-1):
#     print("you loss")
# else:
#     print("you won")




                        # static method in python



# class Math:
#         def __init__(self,num):
#                 self.num=num
#         def addtonum(self,n):
#                 self.num=self.num+n
# @staticmethod
# def  add(a,b):
#         return a+b
# # result =Math.add(1,2)
# # print(result)

# a=Math(5)
# print(a.num)

# a.addtonum(6)
# print(a.num)





                # instance variable v/s class variable


# class Employee:
#     companyname="apple"     //class variable
#     def __init__(self,name):
#         self.name=name
#         self.raise_amount=0.02  //instance variable
#     def showdetails(self):
#             print(f"the name of the employee is {self.name} and the raise amount is{self.raise_amount} and company name is {self.companyname}")
# emp1=Employee("harry")
# emp1.raise_amount=0.3
# emp1.showdetails()
# emp2=Employee("Rohan")
# emp2.showdetails()



                        # class method in python


# class Employye:
#     company="apple"
#     def show(self):
#         print(f"the name is {self.name} and company is {self.company}")
#     @classmethod
#     def changeCompany(cls,newCompany):
#         cls.company=newCompany

# e1=Employye()
# e1.name="harry"
# e1.show()
# e1.changeCompany("tesla")
# e1.show()
# print(Employye.company)

 

                        # class method as alternative constructor

# class Employye:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def  fromStr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
# e1=Employye("harry",12000)
# print(e1.name)
# print(e1.salary)


# string="harry-12000"
# e2=Employye.fromStr(string)
# print(e2.name)
# print(e2.salary)





                           # dir ,dict and help method in python


# x=[1,2,3]
# print(dir(x))
# print(x.__add__)




                        # super keword in python


# class ParentClass:
    
#     def parent_method(self):
#         print("this is a parent method")
# class childclass(ParentClass):
#     def parent_method(self):
#         print("harry")
#         super().parent_method()
#     def child_method(self):
#         print("this is a child class method")

# child_object=childclass()
# child_object.child_method()
# child_object.parent_method()



                # invoke super class constructor in python


# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# class Programmer(Employee):
#     def __init__(self,name,id,lang):
#         super().__init__(name,id)
#         self.lang=lang
# sahil=Programmer("sahil saifi",12,"java")
# print(sahil.name)
# print(sahil.id)
# print(sahil.lang)





                                # dunder method in python


# class Employye:
#     name="sahil saifi"
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i=i+1
#         return i
    
# e=Employye()
# print(e.name)
# print(len(e))






                                # method ovverriding in python


# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y


# class circle(shape):
#     def __init__(self,radius):
#         super().__init__(radius,radius)
     
#     def area(self):
#         return 3.14 * super().area()
    

# c=circle(5)
# print(c.area())






                        # operator overloading in python

# class vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
    
#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"
    
#     def __add__(self,x):
#        print("this is add of both vector")
#        return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k" 


# v=vector(1,2,3)
# print(v)
# v2=vector(3,4,5)
# print(v+v2)




                        # single inheritance in python



# class Dog:
#     def __init__(self,name,breed,spicefies):
#         self.name=name
#         self.breed=breed
#         self.spicefies=spicefies
#     def make_sonud(self):
#         print("sound made by the animal")

# class Cat(Dog):
#     def __init__(self,name,breed,spicefies,house):
#         super().__init__(name,breed,spicefies)
        
#         self.house=house
   

# c=Cat("billi","burgur","kuch nhi",12)
# print(c.name)
# print(c.breed)
# print(c.spicefies)
# print(c.house)




                # multiple inheritance in python


# class Employye:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"the name is {self.name}")
# class Dancer:
#     def __init__(self,dance):
#         self.dance=dance
#     def show(self):
#         print(f"the dance is {self.dance}")

# class Both (Employye,Dancer):
#     def __init__(self,name,dance):
#         self.name=name
#         self.dance=dance

# o=Both("sivani","khathak")
# print(o.name)
# print(o.dance)
# o.show()




                        # multilevel inheritance in python


# class Employye:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"the name is {self.name}")
# class Dancer(Employye):
#     def __init__(self,dance,name):
#         self.dance=dance
#         self.name=name
#     def show(self):
#         print(f"the dance is {self.dance}")
#         super().show()

# class Both (Dancer):
#   def __init__(self,name,dance,id):
#       self.name=name
#       self.dance=dance
#       self.id=id
  
#   def show(self):
#       print(f"the name is {self.name} and the dance is {self.dance} and the id is {self.id}")
#       super().show()
# o=Both("sivani","khathak",12)
# print(o.name)
# print(o.dance)
# print(o.id)
# o.show()





                        # hybrid and hierarchical inheritance




                                # time modeule is python

# import time
# def usinghile():
#     i=0
#     while i<=5000:
#         i=i+1
#         print(i)
# def usingfor():
#     i=0
#     for i in range(5000):
#         print(i)

# init=time.time()
# usingfor()
# t1=print(time.time() - init)


# init=time.time()
# usinghile()
# t2=print(time.time() - init)
# print(t2)
# print(t1)



# import time
# for i in range(10):
#     time.sleep(3)
#     print(i)





                                # command line utility in python






# import argparse
# import requests

# def download_file(url, local_filename): 
#   if local_filename is None:
#     local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#   with requests.get(url, stream=True) as r:
#       r.raise_for_status()
#       with open(local_filename, 'wb') as f:
#           for chunk in r.iter_content(chunk_size=8192): 
#               # If you have chunk encoded response uncomment if
#               # and set chunk_size parameter to None.
#               #if chunk: 
#               f.write(chunk)
#   return local_filename
  
# parser = argparse.ArgumentParser()

# # Add command line arguments
# parser.add_argument("url", help="Url of the file to download")
# # parser.add_argument("output", help="by which name do you want to save your file")
# parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# # Parse the arguments
# args = parser.parse_args()

# # Use the arguments in your code
# print(args.url)
# print(args.output, type(args.output))
# download_file(args.url, args.output)





                        # warlus operator in python


# a=True
# print(a:=False)



# numbers=[1,2,3,4,5]
# while(n:=len(numbers)) >0:
#     print(numbers.pop())





# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression




# happy = False
# print(happy)

# print(happy := True)






# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)





# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)




                # shutil module in python


# import shutil
# shutil.copy("sahil.py","ss.py")     //ek file ko dusri file me copy karne ke liye



# import shutil
# shutil.copytree("myfolder","anotherfolder")      //folder copy karne ke 





# import os
# os.remove("ss.py")     
# file delete karne ke liye




                        # request module in python

# import requests
# response=requests.get("https://www.google.com")
# print(response.text)





# import requests 
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)






                                # generators in python




# def my_generator():
#     for i in range(5):
#         yield i

# gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for j in gen:
#     print(j)






                                # function catching in python




# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def fx(n):
#   time.sleep(5)
#   return n*5
    

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")
# print(fx(61))
# print("done for 61")
# # Output: 6765





                                # regular expression in python

