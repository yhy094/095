# import json
# with open("json1.json","r",encoding="utf-8") as f:
#     data = json.load(f)
# print(data)
# data2={
#     "name":"张三",
#     "age":18,
#     "sex":"男",
#     "hobby":["篮球","足球","乒乓球"]
# }
# with open("json1.json","a",encoding="utf-8")as f1:
#     json.dump(data2,f1,ensure_ascii=False)
#     f1.write("\n")
# with open("./a1.json", "w", encoding='utf-8') as f:
#     json.dump(data2, f)  # 直接将列表保存为文本（自动转化格式）

# print(0.8//0.5)


# def test(x):
#     return x if (x%2==0) else None
# list1=[5,10,15,20,25,30]
# obj=filter(test,list1)
# print(type(obj))
# print(obj)

# def run(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return n*run(n-1)
# n=int(input())
# print(f'Total:{run(n)}')


# def hanoi(n, a, b, c):  
#     if n > 0:  
#         # 将前n-1个盘子从source移动到auxiliary  
#         hanoi(n-1, a, c, b)  
#         # 将最后一个盘子从source移动到target  
#         print(f"Move disk {n} from {a} to {b}")  
#         # 将n-1个盘子从auxiliary移动到target  
#         hanoi(n-1, c, b, a)  
# # 调用函数，开始移动64个盘子  
# hanoi(64, 'A', 'C', 'B')


# class G():
#     def atio1(self):
#         print("atio1")
# class F(G):
#     def atio2(self):
#         print("atio23")
# class U(G):
#     def atio2(self):
#         print("atio24")
# class I(F,U):
#     """
#     继承F和U，F优先级高，U优先级低
#     """
#     def __int__(self,name):
#         self.name=name
#     def atio4(self):
#         """
#         继承F和U，F优先级高，U优先级低234
#         """
#         print("atio4")
#     def atio5(self):
#         return '%s' % self.name


# ivan=I()
# a=input()
# print(a)
# ivan.atio1()
# ivan.atio2()
# ivan.atio4()



# class Name:
#     def __init__(self,name) :
#         self.name=name
#     def __str__(self) :
#         return self.name
#     # __repr__=__str__
# a=Name('Yang')
# print(a)


# class Fib:
#     def __init__(self,max) :
#         self.max=max
#     def __iter__(self):
#         self.a=1
#         self.b=1
#         return self
#     def __next__(self):
#         fib=self.a
#         if fib>self.max:
#             raise StopIteration
#         self.a,self.b=self.b,self.a+self.b
#         return fib
# for i in Fib(100):
#     print(i)


# import time 
# print(time.asctime())   #输出目前的系统时间
# lotime=time.localtime()   #放回当前的系统时间
# print(lotime[0])
# print(lotime[1])
# print(lotime[2])
# print(lotime[3])
# print(lotime[4])
# print(lotime[5])
# print(lotime[6])
# print(lotime[7])
# print(lotime[8])







