#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:39:42 2020

@author: gimjiwon
"""

def MySort(item,alg,reverse=False):
    if alg =='Bubble':
        if reverse == True:
            flag = True #이미 정렬되어 있을 경우 최소 수행을 위한 플래그
            for i in range(len(item)-1):
                for j in range(len(item)-i-1):
                    if item[j] < item[j+1]:
                        item[j], item[j+1] = item[j+1], item[j]
                        flag = False
                if flag :
                    print("Already Sorted..")
                    return
                
        elif reverse == False:
            flag = True
            for i in range(len(item)-1):
                for j in range(len(item)-i-1):
                    if item[j] > item[j+1]:
                        item[j], item[j+1] = item[j+1], item[j]
                        flag = False
                    if flag:
                        print("Already Sorted..")
                        return
        return
    
    elif alg == 'Insertion':
        if reverse == False:
            for i in range(1,len(item)):
                if item[i-1] <= item[i] : continue
                value = item[i]
                for j in range(i):
                    if item[j] > value:
                        item[j:i+1] = item[i:i+1]+item[j:i]
                        break
        elif reverse == True:
            for i in range(1,len(item)):
                if item[i-1] >= item[i] : continue
                value = item[i]
                for j in range(i):
                    if item[j] < value:
                        item[j:i+1] = item[i:i+1]+item[j:i]
                        break
            
        return
    
    elif alg == 'Quick':
        def quick_sort_re(item):
            def sort(left,right):    
                if right <=left:
                        return
                
                idx = Partition(left,right)
                sort(left, idx-1)
                sort(idx, right)
                
            def Partition(left,right):
                pivot = item[(left + right) // 2]
                while left <= right:
                    while item[left] > pivot:
                        left+=1
                    while item[right] < pivot:
                        right -= 1
                    if left <= right:
                        item[left],item[right] = item[right], item[left]
                        left, right = left+1, right -1
                return left
            
            return sort(0,len(item)-1)
        
        def quick_sort(item):
            def sort(left,right):    
                if right <=left:
                        return
                
                idx = Partition(left,right)
                sort(left, idx-1)
                sort(idx, right)
                
            def Partition(left,right):
                pivot = item[(left + right) // 2]
                while left <= right:
                    while item[left] < pivot:
                        left+=1
                    while item[right] > pivot:
                        right -= 1
                    if left <= right:
                        item[left],item[right] = item[right], item[left]
                        left, right = left+1, right -1
    
                return left
            
            return sort(0,len(item)-1)
    
        
        if reverse == False:
            quick_sort(item)
        
        elif reverse == True:
            quick_sort_re(item)
            
        return


if __name__ == "__main__" :
    
    

    print("buble sorting..")
    #이미 정렬된 경우 수행 1
    item1 = [8,7,6,5,4,3,2,1]
    MySort(item1, alg='Bubble', reverse=True) # 정렬이 되어 있는 경우
    print (item1)
                                         # 최소로 수행할 수 있도록
    #이미 정렬된 경우 수행 2
    item1 = [1,2,3,4,5,6,7,8]
    MySort(item1, alg='Bubble') # 정렬이 되어 있는 경우
    print (item1)

    #정렬되지 않은 경우 정렬시키기
    item1 = [8,7,6,5,3,4,10,11]
    MySort(item1, alg='Bubble', reverse=True) # 정렬이 되어 있는 경우
    print (item1)
    
    print()
    
    print('Insertion Sorting..')
    #item2 = [5, 61, 89, 910, 123, 895, 2, 4, 77, 13, 5567, 83, 44]
    item2 = [40,20,100]
    MySort(item2, alg='Insertion')  # default는 오름차순
    print (item2)
    item2 = [5, 61, 89, 910, 123, 895, 2, 4, 77, 13, 5567, 83, 44]
    MySort(item2, alg='Insertion',reverse=True)
    print (item2)

    print()
    
    print("Quick Sroting..")
    item3 = [5, 61, 89, 910, 123, 895, 2, 4, 77, 13, 5567, 83, 44]
    
    MySort(item3, alg='Quick', reverse=False)
    print (item3)
    item3 = [5, 61, 89, 910, 123, 895, 2, 4, 77, 13, 5567, 83, 44]
   
    MySort(item3, alg='Quick', reverse=True)
    print (item3)
