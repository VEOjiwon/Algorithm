#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:52:29 2020

@author: gimjiwon
"""

def BuildGST(pattern, suffix, GST):
    
    m = len(pattern)
    g = m - 1
    
    for i in range(m-2, -1, -1):
        if i>g and suffix[i+m-1-f] < i-g:
            suffix[i] = suffix[i+m-1-f]
        else:
            if i<g: g= i
            f = i
            while (g>=0 and pattern[g] == pattern[g+m-1-f]): g-=1
            suffix[i] = f-g
    for i in range(0,m,1):
        GST[i] = m
        
    j=0
    for i in range(m-1, -1, -1):
        if suffix[i] == i+1:
            while j < m-1-i :
                if GST[j] == m:
                    GST[j] = m-1-i
                j+=1
    for i in range(0,m-1,1):
        GST[m-1-suffix[i]] = m-1-i


def BuildBCT (BCT,pattern):
    for idx in range(len(pattern)-1,-1,-1):
        if pattern[idx] not in BCT:
            BCT[pattern[idx]] = idx

def search(pattern,line):
    i = 0
    p_len = len(pattern)
    l_len = len(line)
    j = p_len -1
    idx = []
    while i+j < l_len:
        if pattern[j] == line[i+j]:
            if j ==0:
                idx.append(i)
                j = p_len -1
                i += 1
            j-=1
        else:
            if line[i+j] in BCT:
                i+=max(GST[j], j - BCT[line[i+j]])
            else:
                i+=max(GST[j],j+1)
            j = p_len -1
    return idx
    

if __name__ == "__main__":
    #pattern = "Three"
    pattern = str(input("Please input the patter : "))
    BCT = {}
    suffix = [0] * len(pattern)
    GST = [0] * len(pattern)
    
    BuildBCT(BCT,pattern)
    BuildGST(pattern, suffix, GST)
    

    f = open("source.txt","r",encoding = 'cp1252')#encoding..
    lines = f.readlines()
    f.close()
    answer=[]
    
    #line = lines[0]
    #print(search(pattern,line))
    line=[]
    for idx,line in enumerate(lines):
        finded_poses = search(pattern,line)
        offset = 0
        if len(finded_poses) !=0:
            for i in finded_poses:
                line = line[:offset+i] +"["*len(finded_poses)+" " + line[offset+i:offset+i+len(pattern)] + " "+"]"*len(finded_poses) + line[offset+i+len(pattern):]
                offset+=1*len(finded_poses) * 2 + 2
            print(idx+1,finded_poses,"------------------")
            print(line)
        finded_poses =[]
            
