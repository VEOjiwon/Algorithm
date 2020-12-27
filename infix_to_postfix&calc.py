#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:14:01 2020

@author: gimjiwon
"""

import re


def infix2postfix(expr):
    expression = re.sub('([\+\-\*\/\(\)])', '\g<1> ', expr)

    OP_CODE = ('+', '-', '*', '/', '^')
    OP_ORD = {'*': 2, '/': 2, '+': 1, '-': 1, '^': 3, '(': 0}

    stack, postfix = list(), list()
    for a in expression.split():
        # 계산식 일 경우에
        if a in OP_CODE:
            # 우선순위가 더 높은동안 출력
            while stack and OP_ORD[stack[-1]] >= OP_ORD[a]:
                postfix.append(stack.pop())
            # 우선순위 낮은게 들어오면 스택에 추가
            stack.append(a)
        # 닫는괄호 만났을 때
        elif a == ')':
            # '(' 만날 때 까지  pop
            while stack:
                x = stack.pop()
                if x == '(':
                    break
                postfix.append(x)
        elif a == '(':
            stack.append(a)
        # 숫자일 경우 그냥 append
        else:
            postfix.append(float(a))
    # 남은거 마저 pop & append
    while stack:
        postfix.append(stack.pop())

    return postfix


def post_calc(a):
    stack = list()
    for i in a:
        if i == "+":
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1 + x2)
        elif i == "-":
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1 - x2)
        elif i == "*":
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1 * x2)
        elif i == "/":
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1 / x2)
        elif i == "^":
            x2 = stack.pop()
            x1 = stack.pop()
            stack.append(x1 ** x2)
        else:
            stack.append(i)
    return stack.pop()


expression = "( ( 5.12 - 2.74 + 0.24 ) * ( 3.15 - 2.0 ) + 1.12 * 4.09 )"
postfix = infix2postfix(expression)
# print(postfix)
print(expression, " - >  ", end="")
for i in postfix:
    print(i, end=" ")

print()
print("answer = ", post_calc(postfix))