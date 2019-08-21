

s="this is great day"
def swap(src, des, array):
    temp = array[src]
    array[src]= array[des]
    array[des]= temp

    return array      
            
            
def reverse_string(s):
    
    string= list(s)
    length= len(string)-1
    position = 0
    
    for char in range(0, length):
        if char <= length-char:
            string =swap(char, length-char, string)
    print ''.join(string)  
    
    for ptr in range(0, length):
        
        if (string[ptr]==" ") or ptr==(length-1):
            
            if ptr==(length-1):
                end = ptr+1
            else: 
                end = ptr-1
            for position in range(position, ptr): 
                
                if position<end:
                    string = swap(position, end, string)
                    end = end-1
            position = ptr+1
        else:
            continue
    return ''.join(string)  
