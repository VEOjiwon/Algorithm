#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 06:20:51 2020

@author: gimjiwon
"""

class Node():
    
    def __init__(self,data):
        self.data = data
        self.children = list()
        
    def __str__(self):
        return self.data.__str__()
    
    def add_child(self,node):
        self.children.append(node)
        
class Tree():
    
    def __init__(self, data='ROOT'):
        self.root = Node(data)
        
    def _print_tree(self,tree):
        
        ret_str =''
        if tree.children != []:
            ret_str = tree.data.__str__() + '--> ['
            tmp = []

            for x in tree.children:
                tmp.append(x.data.__str__())
            ret_str += ','.join(tmp)+ ']\n'
        
        gchild = []
        for x in tree.children:
            gchild.append(self._print_tree(x))
        else:
            return ret_str + '\n'.join(gchild)
        
    def __str__(self):
        return self._print_tree(self.root)
    

    def build_tree_stack(self,parent,treeSLst):
        stack = []
        for x in treeSLst:
            if x == "(":
                stack.append("(")
            elif x == ")":
                if len(stack) == 2 :
                    self.root.add_child(stack.pop())
                    return
                tmp = []
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        for k in tmp:
                            stack[-1].add_child(k)
                        break
                    else:
                        tmp.append(stack.pop())
                                        
            else:
                stack.append(Node(x))
                            
        return
    
    def build_tree(self,parent,treeSLst):
        
        rest = treeSLst

        while(rest):
            first = rest[0]
            rest = rest[1:]
    
            if first =='(':
                child = Node(rest[0])
                parent.add_child(child)
                rest = self.build_tree(child,rest[1:])

                    
            if first == ')':
                return rest
    

class Node2():
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return self.data.__str__()
    
class BTree():
    
    def __init__(self, data='ROOT'):
        self.root = Node2(data)
    
    def _print_tree(self,tree):
        
        if tree != None: ret_str = tree.__str__()
        else: return ''
        
        if tree.left != None:
            ret_str += '-->' + tree.left.__str__()
        else:
            ret_str += '--> None'
        if tree.right != None:
            ret_str += ',' + tree.right.__str__()
        else:
            ret_str += ', None'
            
        left_s = self._print_tree(tree.left)
        right_s = self._print_tree(tree.right)
        
        return ret_str + '\n' + left_s + '\n' + right_s
    
    def __str__(self):
        return self._print_tree(self.root)
    
    
    def to_lchild_rsibling(self,parent,old_child):
        
        new_children = []
        for c in old_child:
            new_children.append(Node2(c.data))

        if new_children == []: return
        parent.left = new_children[0]
        for c_idx in range(len(new_children)-1):
            new_children[c_idx].right = new_children[c_idx+1]

        for c, d in zip(new_children, old_child):
            self.to_lchild_rsibling(c, d.children)
        
            
            
if __name__ =='__main__':
    
    tree_s = '(A(B(C)(D(E)(F)))(G(H))(I(J(K))))'
    #tree_s = '(A(B)(C))'
    treeSLst = [x for x in tree_s if x!= '']
    
    p = Tree()
    p.build_tree_stack(p.root,treeSLst)
    print(p)
    
    z = Tree()
    z.build_tree(z.root,treeSLst)
    print(z)

    
    print('----------------------------------------')
    q=BTree()
    q.to_lchild_rsibling(q.root,p.root.children)
    
    print(q)
    

    