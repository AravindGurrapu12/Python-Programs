# # b=19
# # c=0
# # for i in range(1,b+1):
# #     if b%i ==0:
# #         c=c+1
# # if c==2:
# #     print("prime number")
# # else:
# #     print("not prime")
# # a=[1,2,12,22]
# # b=[22,34,23]
# # a.extend(b)
# # # print(a)
# # def add(num1,*num2):
# #     return num1 + sum(num2)
# # result=add(11,22,22,22)
# # print(result)
# # def info(**kwargs):
# #     for n,b in kwargs.items():
# #         print(n ," : ",b)
# #
# # info(name="arvind",age=22,location ="hyd",sex ="M")
# # def greet(name,msg="hey what's up"):
# #     print("Hello",name,msg)
# #
# # greet("manohar")
# # greet("manohar","why again")
#
# class E:
#     def __init__(self, a):
#         self.a = a
#     def __gt__(self, other):
#         return self.a > other.a
# e1=E(25)
# e2=E(30)
# print(e1.a>e2.a)
# print(e1.a<e2.a)
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def td(self):
#         return (self.x**2 + self.y**2)**0.5
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#     def __gt__(self, other):
#         return self.td > other.td
#     def __lt__(self, other):
#         return self.td < other.td
#     def __eq__(self, other):
#         return self.td== other.td
#     def __ge__(self,other):
#         return self.td >= other.td
#     def __le__(self,other):
#         return self.td <= other.td
#     def __str__(self):
#         print(f"vector ({self.x}, {self.y})")
#         return f"total_distance: {self.td()}"
# v1=Vector(10,20)
# v2=Vector(30,40)
# v3=Vector(50,60)
# print(v1-v2 +v3)

#
#
# class Books:
#     def _init__(self,title,author):
#         self.title =title
#         self.author=author
#         self.is_borowed =False
#

# a=199
# r=0
# s=0
# t=a
# dc=0
# while(a!=0):
#     r=a%10
#     dc=dc+1
#     a=a//10
#
#
# class Bank:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(amount,"deposited")
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-= amount
#             print(amount,"withdraw")
#         else:
#             print(amount,"insuficent balance")
#
#     def __st

#class A:
#     def m1(self):
#         print("A")
# class B(A):
#     def m1(self):
#         print("B")
# b1=B()
# b1.m1()

# class A:
#     def m1(self):
#         super().m1()
#         print("A")
# class B:
#     def m1(self):
#         super().m1()
#         print("B")
#
# class C:
#     def m1(self):
#         print("C")
# class D(A,B,C):
#     def m1(self):
#         super().m1()
#         print("D")
# d1=D()
# d1.m1()
# print()

# class Animal:
#     def sound(self):
#         print("Animal")
#
# class Dog(Animal):
#     def sound(self):
#         print("dog")
#
# obj1=Animal()
# obj2=Dog()
#
# obj1.sound()
# obj2.sound()


# class A:
#     def show(self):
#         print("Show A")
# class B(A):
#     def show(self):
#         super().show()
#         print("Shows B")
#
# obj=B()
# obj.show()

class A:
    def














