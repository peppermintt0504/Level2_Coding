def solution(s):
    temp = []
    ans = []
    
    for i in range(int(len(s)/2)) :
        
        n = 0
        while 1 :
            
            if s[(n * (i + 1)) : (n * (i + 1)) + i + 1] == '' : break
            temp.append(s[(n * (i + 1)) : (n * (i + 1)) + i + 1])     
            n += 1
        
        ans.append(0)
        conti = 0 
        for n in range(len(temp)) :
            if n == len(temp) - 1 : 
                ans[i] += len(temp[n])
                break
            
            if temp[n] == temp[n + 1] :
                if conti != 1 :
                    conti = 1 
                    ans[i] += 1
            else :
                ans[i] += (i + 1)
                conti = 0
            
        temp.clear()  
    
    return min(ans)
