#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 03:00:22 2020

@author: gimjiwon
"""

class node():
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data.__str__() 
    

class LinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def __str__(self): #[1,2,3]
        q = self.head
        ret_str = '['
        while q != None:
            ret_str += q.__str__()
            #ret_str += q.data.__str__()
            if q.next != None: ret_str += ', '
            q = q.next
        
        return ret_str + ']'
    
    def append_node(self, data):
        
        new_node = node(data)
        
        if self.head == None : # 첫번째 node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count+=1
        return 
   
    def extend_list(self, aList): 
        #추가하려는 링크드 리스트가 비었을 때 그냥 리턴
        if aList.head == None: return
        
        #추가하려는 링크드 리스트 복사
        new_l = LinkedList()
        q = aList.head
        while q != None:
            new_l.append_node(q.data)
            q = q.next
        
        #기존의 링크드리스트가 비었을 경우 헤드로...
        if self.head == None :
            self.head = new_l.head
        
        #기존의 링크드 리스트의 테일노드가 있을경우
        if self.tail != None:
            #tail 뒤에 추가해준다
            self.tail.next = new_l.head
        
        #기존 tail값 변경
        self.tail = new_l.tail
        
        #새로 추가된 만큼 더해준다.
        self.count+= new_l.count
        return
    
    #노드 개수 리턴해주는 함수
    def get_count(self):
        return self.count
    
    def remove_first(self,data):
        item = self.head
        if item == None: 
            print("no item")
            return
        else:
            prev= None
            while item:
                if item.data == data:
                    if item == self.tail:
                        temp3 = self.tail
                        self.tail = prev
                        self.tail.next = None
                        self.count-=1
                        del temp3
                        return
                        #break
                    
                    if item == self.head:
                        temp2 = self.head
                        self.head = self.head.next
                        self.count-=1
                        del temp2
                        return
                        #break
                    else:
                        temp = item
                        prev.next = item.next
                        self.count-=1
                        del temp
                        return
                        #break
                else:
                    prev = item
                    item = item.next
            else:
                print("no data")
                return
            
    
    def remove(self, item):
        
        if self.head == None:
            return
        
        #head가 내가 지워야 하는 item인 경우...
        while self.head and self.head.data == item:
            self.head = self.head.next
            self.count-=1
            #print(self.get_count())

        if self.head == None:
            self.tail = None
            return
        p = self.head.next # 앞서서 지울 노드를 검사
        q = self.head #next연결을 위해서 p의 바로 앞노드를 pointing
        while p:
            if p.data == item:
                #여기는 여러분들이 채워주세요
                # p는 앞쪽으로 한칸 이동
                # q의 next는 p의 next로 
                self.count-=1 
                if p == self.tail : # 대상이 마지막 노드일 경우 tail을 바꾸어주고 break..
                    del p
                    q.next = None
                    self.tail = q
                    break
                    
                else:
                    p=p.next
                    q.next=p
                    

            else:
                p = p.next
                q = q.next
        
            
            
if __name__ == '__main__':
    
    a = LinkedList()
    a.append_node(1)
    a.append_node(1)
    a.append_node(1)
    a.append_node(2)
    a.append_node(3)
    print("a :", a)
    print("the number of a is ", a.get_count())
    print()
    b = LinkedList()
    b.append_node('a')
    b.append_node('b')
    print("b : ",b)
    a.extend_list(b)
    print("a+b : ",a)
    print("the number of b is ", b.get_count())
    print("the number of a = a+b is ", a.get_count())
    print()
    b.append_node('c')

    print("c appended b : ", b)
    print("the number of b is ", b.get_count())
    print("check extended a :", a)
    print("the number of a is ", a.get_count())
    print()
    a.remove_first(1)
    print("first 1 removed a : ", a)
    print("the number of a is ", a.get_count())
    print()
    a.append_node(1)
    a.append_node(2)
    a.append_node(3)
    a.append_node(1)
    
    print("1,2,3,1 appended a : ", a)
    print("the number of a is ", a.get_count())
    a.remove(1)
    print()
    
    print("all 1 removed a : ", a)
    print("the number of a is ", a.get_count())
    print()

    
    
    a.append_node(1)
    print("1 appended a : ", a)
    print("the number of a is ", a.get_count())