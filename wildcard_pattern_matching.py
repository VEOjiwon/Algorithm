# Function that matches input with given wildcard pattern
def isMatching(string, pattern):
    n = len(string)
    m = len(pattern)
    
    #initialize
    table = [[False for _ in range(m+1)] for _ in range(n+1)]
    table[0][0] = True
    print("Initialized table")
    print_table(table,n,m)
    
    # handle empty case (i == 0)
    j = 1
    while j <= m:
        if pattern[j-1] == '*':
            table[0][j] = table[0][j-1]
        j+=1
    print("After handle empty case (i == 0)")
    print_table(table,n,m)
    
    #dynamic programming
    i=j=1
    while i <= n:
        j =1
        while j <= m :
            if pattern[j-1] == '*':
                table[i][j] = table[i-1][j] or table[i][j-1]
            elif pattern[j-1] =='?' or string[i-1] == pattern[j-1]:
                table[i][j] = table[i-1][j-1]
            j+=1
        i+=1
    
    print("Completed table")
    print_table(table,n,m)
    return table[n][m]
 
def print_table(table,n,m):
    for i in range(0,n+1):
        for j in range(0,m+1):
            print(table[i][j], end = ' ')
        print()
    print()
            
    
# Wildcard Pattern Matching
if __name__ == '__main__':
 
    str = "xyxzzxy"
    pattern = "x***x?"
 
    if isMatching(str, pattern):
        print("Match")
    else:
        print("No Match")