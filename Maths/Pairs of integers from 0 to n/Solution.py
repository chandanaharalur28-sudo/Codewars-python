def generate_pairs(n):
    s=[]
    for i in range(0,n+1):
        for j in range(i,n+1):
            s.append([i,j])
            j+=1
        i+=1
    return s
        
