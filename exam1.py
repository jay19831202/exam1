# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:29:11 2024

@author: USER
"""

# -*- coding: utf-8 -*-
class Geometric():
    def __init__(self):     #1.__init__初始化
        self.color = "Green"
class Circle(Geometric):    #5.Geometric可刪除
    def __init__(self,radius):
        super().__init__()  #2.直接使用初始化設定
        self.PI = 3.14159
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius = radius
    def getDiameter(self):
        return self.radius * 2
    def getPerimeter(self):
        return self.radius * 2 * self.PI
    def getArea(self):
        return self.PI * (self.radius ** 2)
#3.self變成全域變數,4.沒有設定self為區域變數。

半徑 = Circle(5)

print("圓形的半徑 : ", 半徑.getRadius())
print("圓形的直徑 : ", 半徑.getDiameter())
print("圓形的圓周 : ", 半徑.getPerimeter())
print("圓形的面積 : ", 半徑.getArea())
半徑.setRadius(10)
print("圓形的直徑 : ", 半徑.getDiameter())
