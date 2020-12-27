#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:06:41 2020

@author: gimjiwon
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:50:12 2020

@author: gimjiwon
"""
#Node클래스 생성, value, left, right, parent, color
class Node():
    def __init__(self, data, color='B', left = None, right = None, parent = None):
        self.value = data
        self.left = left
        self.right = right
        self.parent= parent
        self.color = color
        
    def __str__(self):
        return self.value.__str__()
    
#BST 클래스 초기화 None
#Red-Black Tree
class RBT:
    def __init__(self):
        self.root = None

    def _print_tree(self):
        def print_tree(root):

            if root == None:
                pass
            else:
                print_tree(root.left)
                print(str(root.value)+"("+root.color+")",end=' ')
                print_tree(root.right)
                
        return print_tree(self.root)

    def __str__(self):
        print("Tree: [ ",end='')
        self._print_tree()
        print("]",end='')
        return "\n"

    def rotate_right(self, parent):
        #left child 저장
        leftchild = parent.left
        #부모의 왼쪽 자식(rotate right이기 때문에) -> leftchild의 오른쪽자식과 연결
        parent.left = leftchild.right
        #오른쪽 자식이 있을 경우 연결.. 없으면 연결필요 없음
        if leftchild.right !=None:
            leftchild.right.parent = parent
            
        leftchild.parent = parent.parent
        #root rotate하는 경우..
        if parent.parent == None:
            self.root = leftchild
        else:
            if parent == parent.parent.left:
                parent.parent.left = leftchild
            else:
                parent.parent.right = leftchild
        
        leftchild.right = parent
        parent.parent = leftchild
    
    #왼쪽으로 회전
    def rotate_left(self,parent):
        rightchild = parent.right
        
        parent.right = rightchild.left
        if rightchild.left !=None:
            rightchild.left.parent = parent
        
        rightchild.parent = parent.parent
        if parent.parent == None:
            self.root = rightchild
        else:
            if parent == parent.parent.left:
                parent.parent.left  =rightchild
            else:
                parent.parent.right = rightchild
        rightchild.left = parent
        parent.parent = rightchild

    #형제 얻어오기
    def get_sibling(self, node):
        #왼쪽 자식의 경우
        if node.parent.left == node:
            if node.parent.right == None:
                return Node('NIL','B')
            else:
                return node.parent.right
        #오른쪽 자식의 경우
        else:
            if node.parent.left == None:
                return Node('NIL','B')
            else:
                return node.parent.left
    #왼쪽 자식인지 오른쪽 자식인지 return
    def which_child(self, node):
        if node.parent.left == node:
            return 'L'
        else:
            return 'R'
    
    #트리 리빌딩
    def rebuild(self,node):
        
        while node.parent != None and node.parent.color == 'R':
            parent_sibling = self.get_sibling(node.parent)
            
            #case-1
            if parent_sibling.color == 'R':
                node.parent.color = 'B'
                parent_sibling.color = 'B'
                node.parent.parent.color = 'R'
                node = node.parent.parent
            #부모형제의 색이 B인 경우 (case 2-1 ~ 4)
            else:
                if self.which_child(node.parent) == 'L':
                    # case-2-1
                    if self.which_child(node) =='R' and self.which_child(node.paret) == 'L':
                        self.rotate_left(node.parent)
                        node = node.left
                    
                    # case-2-2
                    if self.which_child(node) == 'L' and self.which_child(node.parent) == 'L':
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        self.rotate_right(node.parent.parent)
                else:
                    # case-2-3
                    if self.which_child(node) == 'L' and self.which_child(node.parent) == 'R':
                        self.rotate_right(node.parent)
                        node = node.right
                    
                    # case-2-4
                    if self.which_child(node) == 'R' and self.which_child(node.parent) == 'R':
                        node.parent.color = 'B'
                        node.parent.parent.color = 'R'
                        self.rotate_left(node.parent.parent)
        self.root.color = 'B'
        
    #insert
    def insert(self, value, tree):
        
        if tree == None and self.root == None:
            self.root = Node(value, 'B')
            return
        
        if tree.value < value:
            if tree.right == None or tree.right.value == 'NIL':
                node = Node(value, 'R')
                tree.right = node
                node.parent = tree
                
                self.rebuild(node)
            
            else:
                self.insert(value,tree.right)
            
        else:
            if tree.left == None or tree.left.value == 'NIL':
                node = Node(value,'R')
                tree.left = node
                node.parent = tree
                self.rebuild(node)
            else:
                self.insert(value,tree.left)
                
        
    #검색.. 크기비교에따라 좌우로 서칭
    def search(self,target,tree):
        if tree == None: return None
        
        if tree.value == target:
            return tree
        
        if tree.value < target:
            return self.search(target, tree.right)
        else:
            return self.search(target, tree.left)

if __name__ == '__main__':
    
    items = [3,5,1,7,8,4,9]
    
    mytree = RBT()

    for x in items:
        mytree.insert(x,mytree.root)

    print(mytree) # number(color)..inorder searching

