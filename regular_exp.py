#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 04:28:41 2020

@author: gimjiwon
"""

import re

f = open("Twitter_UTF8.txt","r",encoding = 'utf-8')#encoding..
lines = f.read()
f.close()

pat = re.compile(r'\(?(\d{2,3})(\)|-)\s?(\d{3,4})-(\d{3,4})')
lines=pat.sub("<TEL>"+"\g<1>"+"-"+"\g<3>"+"-"+"\g<4>"+"</TEL>",lines)

f = open("twitter_result.txt","w")
f.write(lines)
f.close()