#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 06:06:47 2020

@author: gimjiwon
"""

import re

OP = ('+', '*', '-', '/') 

class Node():
    def __init__(self,data,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.data.__str__()


def infix2postfix(expr):
    
    expression = re.sub( '([\+\-\*\/\(\)])', '\g<1> ', expr)
    
    OP_CODE = ('+', '-', '*', '/', '^')
    OP_ORD = {'*':2, '/':2, '+':1, '-':1, '^':3, '(': 0}
    
    stack, postfix = list(), list()
    
    for a in expression.split():
        if a in OP_CODE:
            while stack and OP_ORD[stack[-1]] >= OP_ORD[a]:
                postfix.append(stack.pop())
            stack.append(a)
        elif a == ')':
            while stack:
                x = stack.pop()
                if x == '(':
                    break
                postfix.append(x)
        elif a == '(':
            stack.append(a)
        else:
            postfix.append(float(a))
    while stack:
        postfix.append(stack.pop())

    return postfix

def eval_tree(tree):
    if tree != None:
        eval_tree(tree.left)
        eval_tree(tree.right)
        if tree.data =="+":
            x2 = float(tree.right.data)
            x1 = float(tree.left.data)
            tree.data = x1+x2
        elif tree.data =="-":
            x2 = float(tree.right.data)
            x1 = float(tree.left.data)
            tree.data = x1-x2
        elif tree.data =="*":
            x2 = float(tree.right.data)
            x1 = float(tree.left.data)
            tree.data = x1*x2
        elif tree.data =="/":
            x2 = float(tree.right.data)
            x1 = float(tree.left.data)
            tree.data = x1/x2
        elif tree.data =="^":
            x2 = float(tree.right.data)
            x1 = float(tree.left.data)
            tree.data = x1**x2
    return node.data

if __name__ == "__main__":
    infix = '( 5.12 - 2.74 + 0.24 ) * ( 3.15 - 2.0 ) + 1.12 * 4.09'
    #infix = '1 + 2 * 5'
    #postfix = '5.12 2.74 - 0.24 + 3.15 2.0 - * 1.12 4.09 * +'
    post = infix2postfix(infix)
    post_str = ''
    for x in post:
        post_str+=str(x)+" "
    print(infix)
    print(post_str)
    #print(postfix)
    stack=[]
    
    for c in post_str.split():
        if c in OP:
            node = Node(c)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            node = Node(c)
            stack.append(node)
    
    print(eval_tree(stack[-1]))