#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:50:12 2020

@author: gimjiwon
"""
#Node클래스 생성, value, left, right, parent
class Node():
    def __init__(self, data, left = None, right = None, parent = None):
        self.value = data
        self.left = left
        self.right = right
        self.parent= parent
        
    def __str__(self):
        return self.value.__str__()
    
#BST 클래스 초기화 None
class BST:
    def __init__(self):
        self.root = None

    def _print_tree(self):
        def print_tree(root):

            if root == None:
                pass
            else:
                print_tree(root.left)
                print(str(root.value),end=' ')
                print_tree(root.right)
                
        return print_tree(self.root)

    def __str__(self):
        print("Tree: [ ",end='')
        self._print_tree()
        print("]",end='')
        return "\n"
    
    #검색.. 크기비교에따라 좌우로 서칭
    def search(self,target,tree):
        if tree == None: return None
        
        if tree.value == target:
            return tree
        
        if tree.value < target:
            return self.search(target, tree.right)
        else:
            return self.search(target, tree.left)

    #value, tree받아서 insert
    def insert(self,value,tree):
        #tree is empty
        if tree == None and self.root == None:
            self.root = Node(value)
            return
        #현재 노드 값 보다 넣어야할 값이 큰 경우
        if tree.value < value:
            #오른쪽이 비어있으면 삽입
            if tree.right == None:
                node = Node(value)
                tree.right = node
                node.parent = tree
            #비어있지 않으면 value와 오른쪽 tree값으로 재귀함수 호출.. 거기서 다시 비교후 후 삽입
            else:
                self.insert(value, tree.right)
        #현재 노드 값 보다 넣어야할 값이 작은 경우
        else:
            if tree.left == None:
                node = Node(value)
                tree.left = node
                node.parent = tree
            else:
                self.insert(value, tree.left)
                
    def remove(self, target, node):
        
        if node == None:
            return None

        
        #타깃 서칭...
        if node.value < target:
            self.remove(target,node.right)
        elif node.value > target:
            self.remove(target,node.left)
        #목표물을 찾은 경우
        else:
            
            #마지막 노드의 경우
            if node.left == None and node.right == None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            #child가 두개인 경우
            elif node.left != None and node.right != None:
                #우측트리에서 최소값 찾기
                Min_node = self.search_min(node.right)
                #value값 저장
                tmp = Min_node.value
                #최솟값 노드 삭제
                Min_node = self.remove(Min_node.value, node)
                #삭제하려던 노드에 최솟값 넣어주기
                node.value = tmp
            #child가 하나인 경우
            else:
                
                tmp = Node(None)
                if node.left != None:
                    tmp = node.left
                    del node.left
                else:
                    tmp = node.right
                    del node.right
                #skewd된 경우 try ~ except로 임시방편으로 처리함..
                try:
                    if node.parent.left == node:
                        node.parent.left = tmp
                        
                    else:
                        node.parent.right = tmp
                # skewed 된  root 노드 제거
                except:
                    if node.right != None:
                        self.root = node.right
                        del node
                    else:
                        self.root = node.left
                        del node
                        
    def search_min(self,tree):
        while True:
            if tree.left == None:
                break
            tree = tree.left
        return tree


if __name__ == '__main__':
   
    items = [4, 2, 3, 1, 6, 5, 7]
    #items = [4, 27]
    #items = [5,4,3,2,1]
    mytree = BST()
    
    for x in items:
        mytree.insert(x,mytree.root)
    print(mytree)
    print(mytree.root)
    mytree.remove(1, mytree.root)
    print(mytree)
    print(mytree.root)

    
    
    
    items = [3,5,1,7,4,8,9,2]
    
    mytree = BST()
    
    for x in items:
        mytree.insert(x, mytree.root)
    
    print(mytree)
    
    found = mytree.search(100,mytree.root)
    print('100 Found? -->',found)
    
    found = mytree.search(4,mytree.root)
    print('100 Found? -->', found)
    
    print(mytree)

    mytree.remove(8, mytree.root)
    mytree.remove(1, mytree.root)
    mytree.remove(3, mytree.root)
    print("Deleted 1,3,8..")
    print(mytree)
    