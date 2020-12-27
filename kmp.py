#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 01:56:32 2020

@author: gimjiwon
"""


def kmp_search(pattern, border, text):
    m = 0
    i = 0
    t_len = len(text)
    p_len = len(pattern)
    
    while m+1 < t_len:
        
        if pattern[i] == text[m+i]:
            if i == p_len-1:
                return m
            i += 1
        else:
            if border[i] > -1:
                m = m + i - border[i]
                i = border[i]
            else:
                i = 0
                m += 1
    return -1

def make_kmp_table(pattern, border):
    
    m = len(pattern)
    border[0] = -1
    border[1] = 0
    
    i = 2
    cnd = 0
    
    while i < m:
        if pattern[i-1] == pattern[cnd]:
            cnd += 1
            border[i] = cnd
            i += 1
        
        elif cnd > 0 :
            cnd = border[cnd]
            
        else:
            border[i] = 0
            i += 1

if __name__ == '__main__':
    #raw_input 은 파이썬3 에서 지원안하므로 str으로 무조건 형변환하는것으로 대체.
    pattern = str(input("Please input the patter : "))
    len_p = len(pattern)
    border = [0] * len(pattern)
    
    broder = make_kmp_table(pattern,border)
    f = open("source.txt","r", encoding = 'cp1252')#encoding..
    lines = f.readlines()
    f.close()
    
    
    finded_poses = []
    
    for idx,line in enumerate(lines):
        tmp = line
        perior =  0 
        while True:
            pos = kmp_search(pattern, border, tmp)
            if pos != -1:
                pos2 = pos
                pos += perior
                finded_poses.append(pos)
                perior+= pos2+len(pattern)
                tmp = line[perior:]
            else:
                break
        offset = 0
        if len(finded_poses) !=0:
            for i in finded_poses:
                line = line[:offset+i] +"["*len(finded_poses)+" " + line[offset+i:offset+i+len(pattern)] + " "+"]"*len(finded_poses) + line[offset+i+len(pattern):]
                offset+=1*len(finded_poses) * 2 + 2
            print(idx+1,finded_poses,"------------------")
            print(line)
        finded_poses =[]


