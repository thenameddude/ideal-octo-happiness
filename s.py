import itertools
import time
import io
import cProfile

def userinput(k = None): 
    
    if isinstance(k,int):
        return input_validation(k)
    
    while True:
        try:
            k = int(input())
            return input_validation(k)
        except ValueError:
            print("Enter a valid integer.")
                  
def input_validation(k):
    if k%4 == 2 or k%4 == 3 or k < 1:
        return
    return k

def permutation_gen(k):    
    for perm in itertools.permutations(range(1,k+1)):
        if not perm[0]-1 == perm[1]:
            yield list(perm)

def s_gen(perm, k):
    pos = 0
    s = [False] * 2 * k

    for perm_num in perm:
        try:            
            if s[pos+perm_num]:
                return False
             
            s[pos] = perm_num
            s[pos+perm_num] = perm_num
            
            while pos < 2*k and s[pos]:
                pos += 1
                
        except:
            return False
    return True

def recursive_s_gen(perm, k, pos = 0, s = None):
    
    if not s:
        s = [False] * 2 * k

    if perm:

        try:
            perm_num = perm[0]            
            
            if s[pos+perm_num]:
                return False

            s[pos] = perm_num
            s[pos+perm_num] = perm_num
            
            del perm[0]

            if not perm:
                return False
            
            while s[pos]:
                pos += 1
            
            recursive_s_gen(perm, k, pos, s) 
        except:
            return False
    if not perm:
        return all(s)

def everything(k, arg = 0):
    
    k = userinput(k)
    
    if not k:
         return 0
    if k == 1:
        return 1

    x = 0
    if arg == 0:
        for perm in itertools.permutations(range(1,k+1)):
            if not perm[0]-1 == perm[1]:
                if s_gen(perm, k):
                    x += 1
        return(x)


    if arg == 1:
        for perm in permutation_gen(k):
            if recursive_s_gen(perm, k):
                x += 1
        return(x)


cProfile.run('everything(9,0)')
cProfile.run('everything(9,1)')

for i in range(1,13):
    for arg in range(2):
        time_start = time.time()
        x = everything(i,arg)
        time_elapsed = time.time()-time_start
        file_name = "fasts.txt"
        file = open(file_name,"a+")
        if arg == 0:
            print("non recursive: ", end = " ")
            file.write("non recursive:  , ")
        elif arg == 1:
            print("recursive: ", end = "     ")
            file.write("recursive:      , ")
        file.write(str(x) + ", ")
        file.write(str(time_elapsed) + "\n")
        print(x, end = " ")
        print(time_elapsed)
