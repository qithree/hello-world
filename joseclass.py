#!/usr/bin/env Python
# coding=utf-8
__metaclass__ = type
class Person:
    def __init__(self,name,sex="male",age="1"):
       self.name = name
       self.age = age
       self.sex = sex

def people_list():
    fpath = r'E:\game.txt'               #打开文本文件的内容
    with open(fpath,'r') as f:
       s = f.readlines()
       f.close()
       gameGroup = []
    for i in s:
         i = list(i.strip().split(' '))
         gameGroup.append(i)
    return(gameGroup)
    
def josePhus(begin_number, step):
    total_num = len(gameGroup)
    for i in range(0,total_num-1):
        begin_number = (begin_number + step) % len(gameGroup) 
        begin_number -= 1
        print ('the outMan is:',gameGroup[begin_number])
        del gameGroup[begin_number]
    if begin_number == -1: 
         begin_number = 0
    return(gameGroup[0])
    
if __name__ == '__main__':
    gameGroup = people_list()                                    #将txt的内容赋给gameGroup
try:
    begin_number = int(input('the begin number is:'))
    step = int(input('the step is:'))
    assert (begin_number <= 10)                         #测试开始号码是否小于10
    luckyMan =  josePhus(begin_number,step) 
    a = gameGroup[0]
    luckyMan = Person(a[0],sex=a[1],age=a[2])          #实例化                                     
    print ("the luckyMan's name is %s, sex is %s, age is %s"%(luckyMan.name,luckyMan.sex,luckyMan.age))
except Exception as e:
    print("发现错误:",e)



