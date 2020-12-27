import os
import re
from timeit import itertools
def process_file(f):
    fp = open(f)
    all_str = fp.read()
    fp.close()
    result = []
    for w in all_str.split():
        if re.search(r'(.+)/[A-Z]+', w):
            result.append(w)
    return result


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(data):
    if len(data)<=1: return data
   
    mid=int(len(data)/2)
    
    left=merge_sort(data[ :mid])
    right=merge_sort(data[mid: ])
    
    return merge(left,right)
    

if __name__ == "__main__":
    START_DIRECTORY = "/Users/gimjiwon/Desktop/dev-3/Algo/homework/brown/"
    
    All = []
    
    merged_file=open('brown_dic.txt','w')
    for root, dirs, files in os.walk(START_DIRECTORY) :
        full_files = (os.path.join(root, f) for f in files)
        for f in full_files:
            if f.find('.pos') > 0:
                fList  = process_file(f)
                All = All + fList
    
    #All=[1,6,7,9,8,4,5,3,2]
    
    #start_idx = 0
    #end_idx = len(All)-1
    dest = merge_sort(All)

    #print(dest)
    #https://python.flowdas.com/library/itertools.html

    for word,k in itertools.groupby(dest):
        #print(word,len(list(k)))
        freq_num=len(list(k))
        merged_file.writelines(word+"\t"+str(freq_num)+'\n')

