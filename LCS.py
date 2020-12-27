def LCS(m,n):
    
    for i in range(0,m+1):
        c[i][0] = 0
    for j in range(0,n+1):
        c[0][j] = 0
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1] :
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
    return c[m][n]
            
            
import re

f = open("brown_dic.txt","r",encoding = 'utf-8')#encoding..
lines = f.readlines()
f.close()
pat = re.compile(r"/\w*\s*\w*")
word_dict = []

for line in lines:
    line=pat.sub("",line)
    word_dict.append(line)

x = 'apple'
m = len(x)
max_list = [(-1,"")]
max_num = -1
cnt=0
for word in word_dict:
    y = word
    n = len(y)
    c = [[0]*(n+1) for _ in range(m+1)]
    if len(word) <= m-2 or len(word) >= m:
        tmp = LCS(m,n)
        if max(max_list)[0] < tmp:
            max_list = []
            max_list.append((tmp,y,int(lines[cnt][-2])))
        elif max(max_list)[0] == tmp:
            max_list.append((tmp,y,int(lines[cnt][-2])))
    cnt+=1

max_list = sorted(max_list, key = lambda max_list:max_list[2], reverse = True)
max_num = max_list[0][2]
result = []
for i,j,k in max_list:
    if k == max_num:
        result.append(j)

print("target : ",x)
print("result...")
print("".join(result))