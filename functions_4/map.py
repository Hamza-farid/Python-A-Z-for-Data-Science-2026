listt = [1,2,3,4,5]

def sqq(x):
    
    ret_list = [i*i for i in x]
    return ret_list

def sq(x):
    return x*x

res= list(map(sq, listt))  # returns a map object
print(res)