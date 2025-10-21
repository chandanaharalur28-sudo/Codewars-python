def valid_parentheses(strng):
    while 0<=len(strng)<=100:
        count=0
        i=0
        for i in range(0,len(strng)):
            if strng[i] == ")":
                count=count-1
                if count<0:
                    break
            else:
                count=count+1

        if count==0:
            return(True)
        else:
            return(False)
                
